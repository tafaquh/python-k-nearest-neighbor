# Created by M Tafaquh Fiddin Al Islami
# 2110151035 | 3 D4 IT B 2017
# Politeknik Elektronika Negeri Surabaya

#Nearest Neighbor

from operator import attrgetter
import math
import struct
import matplotlib
import matplotlib.pyplot as plt

list_data = []

class Data(object):
    def __init__(self, acidendurance, strength, tissue, rank):
        self.__acidendurance = acidendurance
        self.__strength = strength
        self.__tissue = tissue
        self.__rank = rank
    
    def __init__(self, acidendurance, strength, tissue):
        self.__acidendurance = acidendurance
        self.__strength = strength
        self.__tissue = tissue
        self.__rank = ""
        
    def printValue(self):
        acidEnd = str(self.__acidendurance)
        strength = str(self.__strength)
        tissue = str(self.__tissue)
        rank = str(self.__rank)
        return(acidEnd+"\t\t"+strength+"\t\t"+tissue+"\t\t"+rank)

    def setAcidEndurance(self, acidendurance):
        self.__acidendurance = acidendurance
    def getAcidEndurance(self):
        return self.__acidendurance

    def setStrength(self, strength):
        self.__strength = strength
    def getStrength(self):
        return self.__strength

    def setTissue(self, tissue):
        self.__tissue = tissue
    def getTissue(self):
        return self.__tissue

    def setRank(self, rank):
        self.__rank = rank
    def getRank(self):
        return self.__rank

def showGraph(data_test):
    plt.title('Tissue Strength')
    
    for tissue in list_data:
        if(tissue.getTissue() == "Good"):
            plt.scatter(tissue.getAcidEndurance(), tissue.getStrength(),color='blue')
        else:
            plt.scatter(tissue.getAcidEndurance(), tissue.getStrength(),color='red')
    plt.scatter(data_test.getAcidEndurance(), data_test.getStrength(),color='yellow')
    plt.show()

def main():
    print("Welcome to K-Nearest Neighbor created by Tafaquh")
    print("Case Study inspired by Depandy Enda EEPIS\n\n")

    
    dimStr = []
    
    #Training
    list_data.append(Data(7, 7, "Bad"))
    list_data.append(Data(7, 4, "Bad"))
    list_data.append(Data(3, 4, "Good"))
    list_data.append(Data(1, 4, "Good"))
    list_data.append(Data(2, 3, "Good"))
    
    loop = True
    while loop:
        acidEnd = int(input("How long tissue can endure in acid <second>? "))
        strength = int(input("Kekuatan tissue <kg/m> \t\t= "))
        tissue = input("How about tissue's quality <Good/Bad>\t? ")

        data = Data(acidEnd, strength, tissue)
        list_data.append(data)

        if(input("\nWanna add more data training <y/n>? ") == 'y'): loop = True
        else: loop = False

    
    print("\nNo\t AcidEnd\t Strength\t TissueQuality")
    for i in range(0, len(list_data)):
        print("%d\t %s"% ((i+1), list_data[i].printValue()));

    
    #Testing
    k = int(input("Masukkan jumlah K = "))
        
    acidEnd_test = int(input("How long tissue can endure in acid <second>? "))
    strength_test = int(input("Kekuatan tissue <kg/m> = "))

    data_test = Data(acidEnd_test, strength_test, "")
    data_test.printValue()

    for i in range(0, len(list_data)):
        d1 = [list_data[i].getAcidEndurance(), list_data[i].getStrength()]
        d2 = [data_test.getAcidEndurance(), data_test.getStrength()]

        d = [(d1[0]-d2[0]), (d1[1]-d2[1])]
        space = (d[0]*d[0]) + (d[1]*d[1])
        space = math.sqrt(space)
        list_data[i].setRank(space)

   

    temp = list(list_data)
    labeled_data = []
    for i in range(0, k):
        minVal = min(temp, key=attrgetter('_Data__rank'))
        labeled_data.append(minVal)

        try:
            for i in range(0, len(temp)):
                if(minVal == temp[i]): del temp[i]
        except IndexError:
            continue

    for i in range(0, len(labeled_data)):
        print(labeled_data[i].printValue())

    #Get The Result
    countGood = sum(d.getTissue() == "Good" for d in labeled_data)
    countBad = sum(d.getTissue() == "Bad" for d in labeled_data)

    print("Good = %d, Bad = %d"%(countGood, countBad))
    if(countGood > countBad): print("Data Test is GOOD TISSUE")
    elif (countGood == countBad): print("Data Test is both GOOD and BAD TISSUE")
    else: print("Data Test is BAD TISSUE")

    showGraph(data_test);
    
            
        
        
    
            
if __name__ == '__main__':
    main()
