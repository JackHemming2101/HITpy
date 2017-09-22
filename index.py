from tkinter import *
from Modules.Math import *


Objects = read_object('Maps/Map1.txt')
print(Objects[0].check_connect(2))
#print(Generate_resistor(100,100))
Generate_file('Maps/MapGen.txt')
