import random
class Resistor:
    def __init__(self,x,y,resist,group):
        self.position_x = x
        self.position_y = y
        self.resist = resist
        self.group = str(group)

    def show_position(self):
        return([self.position_x,self.position_y,])

    def get_resist(self):
        return(int(self.resist))

    def get_connect(self):
        return(self.group_in,self.group_out)
    def get_group(self):
        return(self.group)
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
            ObjectClassArray.append(Resistor(ObjectArray[index][1],ObjectArray[index][2],ObjectArray[index][3],ObjectArray[index][4]))

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

def find_res_map(Objects):
    Resistor_map = []
    Resistor_paralel_map = []
    resist_posl_par = 0
    index_b = 0
    index = 0
    resist_paralel=0
    while index < len(Objects):
        #print(Objects[index].get_group())
        #print(Objects[index].get_resist())
        print(index)
        if Objects[index].get_group()[0] == 'Z':
            Resistor_map.append(Objects[index].get_resist())
            index+=1

        elif Objects[index].get_group()[0] == Objects[index+1].get_group()[0] and not Objects[index].get_group()[0] == 'Z':
            index_b = index
            print(index,'Paralel')
            group=Objects[index].get_group()[0]
            while Objects[index_b].get_group()[0] == group :
                print(Resistor_paralel_map)
                resist_posl_par = 0
                #print(index,'REDC')
                group_2=Objects[index].get_group()[1]
                #print(type(group_2),"C")
                while Objects[index_b].get_group()[1] == group_2 and not group_2 == '0' and not group == 'Z':
                    resist_posl_par += Objects[index_b].get_resist()
                    #print(resist_posl_par,index_b,'WHILE')
                    index_b+=1
                if resist_posl_par>0:
                    Resistor_paralel_map.append(resist_posl_par)
                    print(Resistor_paralel_map)
                    Resistor_paralel_map.append(Objects[index_b].get_resist())
                #print(Resistor_paralel_map,'LIST')
                index_b +=1
                index = index_b

            print(Resistor_paralel_map,'CT')
            for count in range(len(Resistor_paralel_map)):
                resist_paralel += 1 / Resistor_paralel_map[count]
                print(resist_paralel)
                #print(resist_paralel,"MOR")``
            resist_paralel = 1 / resist_paralel
            Resistor_map.append(resist_paralel)
            #print(Resistor_paralel_map,'LIST')

        #print(index)
    return(Resistor_map,"DER")
