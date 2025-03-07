# Neurorobotics of the Deep: Deep Sea Skate #
## Overview ##
This repository contains code for the final project for my COGS 112R: Cognitive Robotics class. The goal of the final project is to build a biomimetic agent using Lego Spike Prime sets with implementation of cognitive robotics techniques. This is a group project. Group members: Qian Ying Wong, Ethan Masiclat, Ramiyah Dougherty.

## Directories ##
**Data**: Contains a csv file and a .py file for data handling. These data are taken from the robot's logs when running trials.

**FinalReport**: Contains a pdf report of the project as well as plots describing our Q-learning implementation. There is also an image of our robot in its environment.

**Plotting**: Contains Python code (using Matplotlib) for plotting the graphs in FinalReport.

**src**: Contains a .llsp3 file and a .py file that has the exact same contents. The .py file was created for readability purposes.

## Code ##
**src**: The main script runnning our robot. Python code was written in Lego Spike Prime's built in Python environment that contains the necessary Lego Robotics modules and packages, such as hub, color_sensor, motor_pair, light_matrix, and others. The .llsp3 file in src/ was downloaded from Lego Spike Prime's ofiicial Python environment, where most of the coding was done throughout the project.

**Other Directories**: Data and Plotting contain Python code written to handle data and generate graphs to complement our final report. They provide no functionality for the neurorobot.

## The Robot ##
The robot is built using Lego parts and Lego Spike Prime's hub, motor, color sensors, and other various parts from the robotics kit provided by the professor.
