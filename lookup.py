# Author: Rohde
# Creaed: 12/12/19
# About: Learning how to open external files
#
# Open a text file in the root local folder and verifies it is readable
# data_lookup = open("lookup.txt", "r")
# print(data_lookup.readable())
# data_lookup.close()
#
# Open a text file and reads the lines and adds to a list
# data_lookup = open("lookup.txt", "r")
# print(data_lookup.readlines())
# data_lookup.close()
#
# Opens a text file and uses a for each loop to prase through each item and print
# data_lookup = open("lookup.txt", "r")
# for item in data_lookup.readlines():
#   print(item)
# data_lookup.close()

data_lookup = open("lookup.txt", "a")
data_lookup.write("\nHeadband - Hybrid - TBD")
data_lookup.close()