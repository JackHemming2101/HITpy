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
            ObjectClassArray.append(Resistor(ObjectArray[index][1],ObjectArray[index][2],ObjectArray[index][3]))

        if ObjectArray[index][0] == 'Link' :
            ObjectClassArray.append(Link(ObjectArray[index][1],ObjectArray[index][2],ObjectArray[index][3],ObjectArray[index][4]))

    print(ObjectClassArray[3].show_position())


read_object('Maps/Map1.txt')
