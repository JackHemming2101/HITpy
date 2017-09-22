import random
class Resistor:
    def __init__(self,x,y,resist,group_in,group_out):
        self.position_x = x
        self.position_y = y
        self.resist = resist
        self.group_in = group_in
        self.group_out = group_out

    def show_position(self):
        return([self.position_x,self.position_y,])
    def show_connection(self):
        return([self.group_in,self.group_out])

    def check_connect(self,intake):
        if int(self.group_out) == intake:
            return(True)
        else:
            return(False)

    def get_connect(self):
        return(self.group_in,self.group_out)

class Link:
    def __init__(self,x,y,x2,y2):
        self.position_start_x = x
        self.position_start_y = y
        self.position_end_x = x2
        self.position_end_y = y2

    def show_position(self):
        print(self.position_start_x,self.position_start_y,self.position_end_x,self.position_end_y)

def read_object(path):
    object = open(path, 'r')
    ObjectArray = object.read().splitlines()

    for index in range(len(ObjectArray)):
        ObjectArray[index] = ObjectArray[index].split()
    #print(ObjectArray[1])
    ObjectClassArray = []
    for index in range(len(ObjectArray)):
        if ObjectArray[index][0] == 'Resi' :
            ObjectClassArray.append(Resistor(ObjectArray[index][1],ObjectArray[index][2],ObjectArray[index][3],ObjectArray[index][4],ObjectArray[index][5]))

        if ObjectArray[index][0] == 'Link' :
            ObjectClassArray.append(Link(ObjectArray[index][1],ObjectArray[index][2],ObjectArray[index][3],ObjectArray[index][4]))

    return(ObjectClassArray)


def Generate_resistor(range_pos,renge_resist):
    Type = "Resi"
    x = random.randrange(0,range_pos,1)
    y = random.randrange(0,range_pos,1)
    group_in = random.randrange(0,5,1)
    group_out= random.randrange(0,5,1)
    resist = random.randrange(0,renge_resist,10)
    return([Type,x,y,resist,group_in,group_out])

def Generate_file(path):
    File = open(path,'w')
    FileText=[]

    for index in range(10):
        FileText.append(Generate_resistor(10,100))

    File.write(str(FileText))
