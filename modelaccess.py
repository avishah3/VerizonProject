# necessary imports
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
import pandas as pd
import joblib
import random
def Phone_selector(appl, sams, goog, mot, wealth, phones):

    # Random num between 0 and 1

    # low income: -70         0.1 0.4 0.1 0.4
    # medium income:          0.3 0.4 0.2 0.1
    # high income: +110        0.65 0.1 0.2 0.05

    if wealth < 70:
        w_appl = 0.1
        w_sams = 0.4
        w_goog = 0.1
        w_mot = 0.4

    elif wealth < 110:
        w_appl = 0.3
        w_sams = 0.4
        w_goog = 0.2
        w_mot = 0.1

    else:
        w_appl = 0.65
        w_sams = 0.1
        w_goog = 0.2
        w_mot = 0.05

    appl = (appl + w_appl) / 2
    sams = (sams + w_sams) / 2
    goog = (goog + w_goog) / 2
    mot = (mot + w_mot) / 2

    rand_num = np.random.rand(1)

    if rand_num < appl:
        random_item = random.choice(phones[0])

    elif rand_num < appl + sams:
        random_item = random.choice(phones[1])

    elif rand_num < appl + sams + goog:
        random_item = random.choice(phones[2])

    else:
        random_item = random.choice(phones[3])

    return random_item

phones = [["iphone Pro 15 Max", "iphone 15 Pro","iphone 15", "iphone 14 pro max","iphone 14", "iphone 13"],
        ["Samsung Galaxy S23 Ultra", "Samsung Galaxy S23", "Samsung Galaxy S22", "Samsung Galaxy S21", "Samsung Galaxy Z Flip5"],
        ["Google Pixel 7a", "Google Pixel Fold", "Google Pixel 7", "Google Pixel 6a"],
        ["Motorola one 5G UW ace", "Motorola edge - 2022"]]
def Accessory_selector(basics, protect, audio, gaming, wealth, accessories):

    # Random num between 0 and 1

    # low income: -70         0.6 0.3 0.05 0.05
    # medium income:          0.4 0.2 0.2 0.2
    # high income: +110        0.3 0.2 0.2 0.3

    if wealth < 70:
        w_basics = 0.6
        w_protect = 0.3
        w_audio = 0.05
        w_gaming = 0.05

    elif wealth < 110:
        w_basics = 0.4
        w_protect = 0.2
        w_audio = 0.2
        w_gaming = 0.2

    else:
        w_basics = 0.3
        w_protect = 0.2
        w_audio = 0.2
        w_gaming = 0.3

    basics = (basics + w_basics) / 2
    protect = (protect + w_protect) / 2
    audio = (audio + w_audio) / 2
    gaming = (gaming + w_gaming) / 2


    rand_num = np.random.rand(1)

    if rand_num < basics:
        random_item = random.choice(accessories[0])
    elif rand_num < basics + protect:
        random_item = random.choice(accessories[1])
    elif rand_num < basics + protect + audio:
        random_item = random.choice(accessories[2])
    else:
        random_item = random.choice(accessories[3])

    return random_item
accessories = [["Charging Cable", "Charging Brick"],
        ["Cases", "Screen Protector"],
        ["Apple Airpods Pro (2nd gen)", "Apple Airpods Pro (3rd gen)", "Beats Studio Buds", "Beats Studio Pro", "Galaxy Buds2 Pro", "Galaxy Buds2 Pro", "JBL Flip 6", ],
        ["Meta Quest 3","Nintendo Switch", "Xbox Series X"]]

def returnPredictions(input_array):
    output_array = ["", "", "", "", ""]
    # import model from phone_model.h5
    phonemodel = keras.models.load_model('phone_model_72.h5')
    # import model from accessory_model.h5
    accessorymodel = keras.models.load_model('accessory_model_71.h5')
    # import model from phoneplan_model.h5
    phoneplanmodel = keras.models.load_model('phoneplan_model.h5')
    # import model from homeplan_model.h5
    homeplanmodel = keras.models.load_model('homeplan_model.h5')

    # read data from UI or create a sample set of 7 preferences
    # preferences = [100, 0.6, 21, 2, 6, 1, 3]
    preferences = input_array

    # convert preferences into appropriate format
    processed_input = np.array([preferences])  # Assuming preferences is a list like [1, 0.5, 0, 1]

    # predict the top product
    phoneprediction = phonemodel.predict(processed_input)
    accessoryprediction = accessorymodel.predict(processed_input)
    phoneplanprediction = phoneplanmodel.predict(processed_input)
    homeplanprediction = homeplanmodel.predict(processed_input)

    # print the top product
    #topphones = np.argsort(phoneprediction[0])[-1:][::-1]
    #print(phoneprediction)
    #print(topphones)
    #topaccessory = np.argsort(accessoryprediction[0])[-1:][::-1]
    #print(accessoryprediction)
    #print(topaccessory)
    #print(np.round(phoneplanprediction))
    #print(np.round(homeplanprediction))

    selectedphone = Phone_selector(phoneprediction[0][0], phoneprediction[0][1], phoneprediction[0][2], phoneprediction[0][3], preferences[0], phones)
    selectedphone1 = Phone_selector(phoneprediction[0][0], phoneprediction[0][1], phoneprediction[0][2], phoneprediction[0][3], preferences[0], phones)
    selectedphone2 = Phone_selector(phoneprediction[0][0], phoneprediction[0][1], phoneprediction[0][2], phoneprediction[0][3], preferences[0], phones)
    # print(selectedphone)
    selectedaccessory = Accessory_selector(accessoryprediction[0][0], accessoryprediction[0][1], accessoryprediction[0][2], accessoryprediction[0][3], preferences[0], accessories)
    selectedaccessory1 = Accessory_selector(accessoryprediction[0][0], accessoryprediction[0][1], accessoryprediction[0][2], accessoryprediction[0][3], preferences[0], accessories)
    if (phoneplanprediction[0][0] > 2 and homeplanprediction[0][0] > 2):
        output_array[0] = selectedphone
        output_array[1] = selectedphone1
        output_array[2] = selectedaccessory
        if (preferences[6] == 1):
            output_array[3] = "Internet Plan 2"
        else:
            output_array[3] = "Internet Plan 3 - Unlimited Ultimate" 
        output_array[4] = "Home Plan 2 - Plus"

    elif(phoneplanprediction[0][0] > 2):
        output_array[0] = selectedphone
        output_array[1] = selectedphone1
        output_array[2] = selectedaccessory
        output_array[3] = selectedaccessory1
        if (preferences[6] == 1):
            output_array[4] = "Internet Plan 2"
        else:
            output_array[4] = "Internet Plan 3 - Unlimited Ultimate"
    elif(homeplanprediction[0][0] > 2):
        output_array[0] = selectedphone
        output_array[1] = selectedphone1
        output_array[2] = selectedaccessory
        output_array[3] = selectedaccessory1
        output_array[4] = "Home Plan 2 - Plus"
    else:
        output_array[0] = selectedphone
        output_array[1] = selectedphone1
        output_array[2] = selectedphone2
        output_array[3] = selectedaccessory
        output_array[4] = selectedaccessory1

    return output_array
