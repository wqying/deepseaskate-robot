import color_sensor
import color
from hub import port
import time
import motor_pair
from hub import light_matrix
from math import exp
import random

# Ethan Masiclat, Qian Ying Wong, Ramiyah Dougherty
# Team 12
# 8-Dec-2024

# initializes the motor pair
motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

# VARIABLES:
# Values influencing what set of actions the robot takes
hungerValue = 0
eggsValue = 0
hungerThreshold = 5
eggsThreshold = 3

# Constants For Exploration Phase
NUM_STATES = 7
NUM_MOVES = 3

# Action indices
LEFT = 0
RIGHT = 1
FORWARD = 2

# Q learning variables for exploration
ALPHA = 0.5
BETA = 0.3 # can be increased to promote exploitation or decreased for exploration
GAMMA = 0.99
REWARD = 20
RIGHTTRACK = 10
PUNISH = -10

# Functions for the robot's behavior:
# Movement Functions
def turn_left():
    motor_pair.move_tank(motor_pair.PAIR_1, 50,100)
    time.sleep_ms(1000)

def turn_right():
    motor_pair.move_tank(motor_pair.PAIR_1, 100, 50)
    time.sleep_ms(1000)

def go_forward():
    motor_pair.move_tank(motor_pair.PAIR_1, 100, 100)
    time.sleep_ms(1000)

# Behavior functions
def eat():
    print("I am eating\n")
    motor_pair.stop(motor_pair.PAIR_1)
    time.sleep_ms(5000)
    #This is inlcluded here for quality of life. The robot will back up and turn around as to not get stuck
    motor_pair.move_tank_for_time(motor_pair.PAIR_1,-100,-100, 1000)
    time.sleep_ms(2000)
    motor_pair.move_tank_for_time(motor_pair.PAIR_1,-100, 100, 3000)
    time.sleep_ms(5000)

def layEggs():
    print("I am laying eggs\n")
    motor_pair.stop(motor_pair.PAIR_1)
    time.sleep_ms(5000)
    # need to stop for a bit after laying eggs
    motor_pair.move_tank_for_time(motor_pair.PAIR_1,-100,-100, 1000)
    time.sleep_ms(2000)
    motor_pair.move_tank_for_time(motor_pair.PAIR_1,-100, 100, 3000)
    time.sleep_ms(5000)

def explore():
    print("I'm just a chill guy looking around\n")

    # Run for a limited number of steps to avoid infinite loops
    for _ in range(1):# Limit exploration to 1 iteration so it doesn't get stuck
        detected_color = color_sensor.color(port.C)# Get the detected color

        # Interrupt exploration if a meaningful event is detected
        if detected_color == color.GREEN and hungerValue > hungerThreshold:
            print("I'm hungry and found food!\n")
            return 1  # Signal to eat
        elif detected_color == color.WHITE and eggsValue > eggsThreshold:
            print("Ready to lay eggs!\n")
            return 2  # Signal to lay eggs
        # Check if the robot is out of its environment
        elif detected_color in [color.RED, color.MAGENTA, color.BLUE]:
            print("Whoops! I'm going back to my habitat!\n")
            motor_pair.move_tank(motor_pair.PAIR_1, -100, -100)  # moves backward
            time.sleep_ms(5000)
            motor_pair.move_tank_for_time(motor_pair.PAIR_1,-100, 100, 3000)
            time.sleep_ms(5000)
            return 0  # Exit explore once this condition is met and returns to main loop

# Dies when the hunger value or egg value exceeds their respective thresholds
def die():
    global hungerValue, eggsValue
    if (hungerValue > hungerThreshold + 30) or (eggsValue > eggsThreshold + 30):
        print("\nOh no....xP...I died")
        light_matrix.show_image(light_matrix.IMAGE_GHOST)
        motor_pair.stop(motor_pair.PAIR_1) # stop movement
        return False
    else:
        return True

# Action selection and Q learning functions
def action_select (q, beta):
    """
    Calculate the Softmax function to choose an action. Converts the q array into a probability distribution
    - Parameters
        q - expected values
        beta - temperature for Softmax function
    - Returns the selected action
    """
    act = 0
    p = 0
    sumSoftMax = 0
    sumP = 0

    # calculate the denominator sum
    for i in range(len(q)):
        sumSoftMax += exp(beta*q[i])

    r = random.random() # get a random number between 0 and 1
    done = False

    # loop through the q values
    for i in range(len(q)):
        # add the softmax probability to the sum total.
        # if the sum is greater than the total, that action is chosen.
        if not done:
            p = exp(beta*q[i])/sumSoftMax
            sumP += p
            if sumP >= r:
                done = True
                act = i
    return act

def get_reward ():

    rwd = 0
    nextState = 0
    # receives a reward (or punishment) based on the internal state and what sector of the environment it is in
    if (color_sensor.color(port.C) == color.GREEN) and (hungerValue > hungerThreshold):# when detecting green, robot would eat in cold region
        light_matrix.show_image(light_matrix.IMAGE_HAPPY)
        rwd = REWARD
        nextState = 1
    elif (color_sensor.color(port.C) == color.BLACK) and (hungerValue > hungerThreshold):# when detecting black, robot would continue exploring in the cold region
        light_matrix.show_image(light_matrix.IMAGE_CONFUSED)
        rwd = RIGHTTRACK
        nextState = 2
    elif ((color_sensor.color(port.C) == color.YELLOW) or (color_sensor.color(port.C) == color.WHITE)) and (hungerValue>hungerThreshold):# when neither green nor black is detected and if it's hungry, it'll know it's in the wrong region
        light_matrix.show_image(light_matrix.IMAGE_SAD)
        rwd = PUNISH
        nextState = 3
    elif (color_sensor.color(port.C) == color.WHITE) and (eggsValue > eggsThreshold):# white: hot region, lays eggs
        light_matrix.show_image(light_matrix.IMAGE_HAPPY)
        rwd = REWARD
        nextState = 4
    elif (color_sensor.color(port.C) == color.YELLOW) and (eggsValue > eggsThreshold):# yellow: exploring in the hot region
        light_matrix.show_image(light_matrix.IMAGE_CONFUSED)
        rwd = RIGHTTRACK
        nextState = 5
    elif ((color_sensor.color(port.C) == color.BLACK) or (color_sensor.color(port.C) == color.GREEN)) and (eggsValue>eggsThreshold):  # if the robot is in the cold region but wants to lay eggs it'll get punished
        light_matrix.show_image(light_matrix.IMAGE_SAD)
        rwd = PUNISH
        nextState = 6
    else:
        light_matrix.show_image(light_matrix.IMAGE_MEH)
        rwd = 0
        nextState = 0

    time.sleep_ms(2000)
    light_matrix.clear()

    return rwd, nextState

def print_qtbl(Q, t):
    """
    Prints out the Q table and the corresponding probabilities
    - Parameters
        Q - expected values for each state
        t - the trial number
    """
    print('TState Q(left) Q(right) Q(forward)')
    for i in range(len(Q)):
        print("%d:%d    %3.2f    %3.2f    %3.2f" % (t, i, Q[i][0], Q[i][1], Q[i][2]))

 # Main loop
 # randomize the initial Q-table values slightly to encourage exploration
qTbl = [[0.0 for y in range(NUM_MOVES)] for x in range(NUM_STATES)]
trial = 0
act = 0
# By default the robot's current state is exploration
currentState = 0
nextState = 0

while True:
    if not die():  # if "die" conditions are not met, this doesn't run and the while loop proceeds as normal
        break

    # boundary color detection
    detected_color = color_sensor.color(port.C)
    if detected_color in [color.RED, color.MAGENTA, color.BLUE]:
        print("Whoops! I'm going back to my habitat!\n")
        motor_pair.move_tank(motor_pair.PAIR_1, -100, -100)# moves backward
        time.sleep_ms(5000)
        motor_pair.move_tank_for_time(motor_pair.PAIR_1,-100, 100, 4000)
        time.sleep_ms(5000)

        continue

    act = action_select(qTbl[currentState],BETA)
    if act == LEFT:
        turn_left()
    elif act == RIGHT:
        turn_right()
    elif act == FORWARD:
        go_forward()
    # give time for robot to move
    time.sleep_ms(2000)

    # Update the expected value based on Q learning model free reinforcement learning.
    # After performing the action, q values are calculated
    rwd, nextState = get_reward()

    # for debugging:
    print("Reward: ", rwd, ", Next State: ", nextState)

    maxQ = max(qTbl[nextState])
    qTbl[currentState][act] = qTbl[currentState][act] + ALPHA*(rwd + GAMMA*maxQ - qTbl[currentState][act])
    currentState = nextState

    # Updates the trial number and prints the q table
    trial += 1
    print_qtbl(qTbl, trial)

    # Behavior, since states are detected when rewards are given, current states are based off of the reward function
    if currentState == 1:
        eat()
        hungerValue = 0
    elif currentState == 4:
        layEggs()
        eggsValue = 0
    else:
        explore()
        hungerValue = hungerValue + 1
        eggsValue = eggsValue + 1

    # for debugging purposes
    print("Hunger level:", hungerValue)
    print("Tendency to lay eggs:", eggsValue)

