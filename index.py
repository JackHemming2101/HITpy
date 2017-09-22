from tkinter import *
from Modules.Math import *

def read_object(path):
    object = open(path, 'r')
    ObjectArray = object.read().splitlines()

    for index in range(len(ObjectArray)):
        ObjectArray[index] = ObjectArray[index].split()
    print(ObjectArray)
    ObjectClassArray = []
    for index in range(len(ObjectArray)):
        if ObjectArray[index][0] == 'Resi' :
            ObjectClassArray.append(Resistor(ObjectArray[index][1],ObjectArray[index][2]))


    print(ObjectClassArray[1].show_position())

        #if TimeObjectArray[0] = "Resi":
            #print()

read_object('Maps/Map1.txt')
