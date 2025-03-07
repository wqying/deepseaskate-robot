# Plotting the hunger values and eggs values over trials

# importing libraries
import matplotlib.pyplot as plt

hunger_levels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 0, 1, 2, 3, 4, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
eggs_levels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 12, 13, 14, 0, 1, 2, 3, 4, 5, 6, 6, 7, 8, 0, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 21, 22, 23, 24, 0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 21, 22, 23, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

plt.plot(hunger_levels, color = '#15b01a', label = "Hunger Values")  # darker green line
plt.plot(eggs_levels, color = '#0343df', label = "Egg-laying Values")  #  darker blue line
# hunger threshold: lighter green line
plt.axhline(y = 5, color = '#96f97b', label = "Hunger Value Threshold", linestyle = '-.')
# eggs threshold: lighter blue line
plt.axhline(y = 3, color = '#95d0fc', label = "Egg-laying Value Threshold", linestyle = '-.')

plt.xlabel("Trials")
plt.ylabel("Values for Hunger and Egg-laying tendency")

plt.legend(title = "Values and Threshold")
plt.title("Hunger and Egg-laying Values over Trials")

plt.savefig("hunger_egg_values.jpg")