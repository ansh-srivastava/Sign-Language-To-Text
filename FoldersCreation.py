# Importing the Libraries Required
import os
import string

# Creating the directory Structure
if not os.path.exists("dataSet"):
    os.makedirs("dataSet")

if not os.path.exists("dataSet/trainingData"):
    os.makedirs("dataSet/trainingData")

if not os.path.exists("dataSet/testingData"):
    os.makedirs("dataSet/testingData")

# Making folders for each class (0 to 25 for A to Z)
for i in range(26):
    class_label = chr(ord('A') + i)  # Convert index to corresponding alphabet
    if not os.path.exists(f"dataSet/trainingData/{class_label}"):
        os.makedirs(f"dataSet/trainingData/{class_label}")

    if not os.path.exists(f"dataSet/testingData/{class_label}"):
        os.makedirs(f"dataSet/testingData/{class_label}")

# Making Folders for the blank class
if not os.path.exists("dataSet/trainingData/blank"):
    os.makedirs("dataSet/trainingData/blank")

if not os.path.exists("dataSet/testingData/blank"):
    os.makedirs("dataSet/testingData/blank")

print("Directory structure created successfully.")
