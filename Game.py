import time
import sys
import random

def cls():
    print("                                                "*100)
r = random.randint

class Dogs:
    def __init__(self,name):
        self.name = name
        self.excercise = r(1,5)
        self.intelligence = r(1,100)
        self.friendliness = r(1,10)
        self.drool = r(1,10)
    def __repr__(self):
        return "\n{}: \n (1)DROOL = {} \n (2)INT = {} \n (3)FRIEND = {} \n (4)EX = {} \n".format(self.name.upper(),self.drool,self.friendliness, self.intelligence, self.excercise)
    def __str__(self):
        return self.__repr__()
    def compare_drool(self,other):
        if self.drool <= other.drool:
            return True
        else:
            return False
    def compare_intelligence(self,other):
        if self.intelligence >= other.intelligence:
            return True
        else:
            return False
    def compare_friendliness(self,other):
        if self.intelligence >= other.intelligence:
            return True
        else:
            return False
    def compare_excercise(self,other):
        if self.excercise >= other.excercise:
            return True
        else:
            return False


print("***************************\n*WELCOME TO CELEBRITY DOGS*\n***************************")

while True:
    print("START GAME (_1_)")
    print("QUIT GAME  (_2_)")
    start_game = input("")
    if start_game == "1":
        cls()
        print("GAME START")
        break
    elif start_game == "2":
        print("Exiting")
        time.sleep(1)
        cls()
        print("Good Bye")
        sys.exit()

    else:
        pass

cls()

print ("ENTER THE AMOUNT OF CARDS YOU WOULD LIKE TO USE\nYOU CAN NOT HAVE LESS THAN 4 CARDS\nYOU CAN NOT HAVE MORE THAN 30 CARDS\nYOU CAN NOT HAVE AN ODD NUMBER OF CARDS")

while True:
    cards_num = int(input(""))
    if not (4 <= cards_num <= 30):
        print("PlEASE INPUT A NUMBER IN THE SPECIFIED RANGE")
        continue
    elif cards_num%2 == 1:
        print("PLEASE INPUT A NUMBER IN THE SPECIFIED RANGE")
        continue
    elif cards_num == "":
        print("PLEASE INPUT A VALID NUMBER")
        continue

    else:
        break



dog_names = open("dogs.txt", "r")
a = dog_names.read()
names = a.split("\n")
random.shuffle(names)
dog_names.close()

converter = []
cardsUsed = []
cardsC = []
cardsP = []
for i in range(cards_num):
    converter.append(names[i])
for i in range(int(len(converter))):
    atconvert = Dogs(converter[i])
    cardsUsed.append(atconvert)
halfCards = int(cards_num/2)

for i in range(halfCards):
    cardsC.append(cardsUsed.pop(0))
for i in range(halfCards):
    cardsP.append(cardsUsed.pop(0))

print(cardsC)
print(cardsP)

cls()

while True:
    if len(cardsC) < 1:
        cls()
        print("YOU WON!")
        break
    elif len(cardsP) < 1:
        cls()
        print("YOU LOOSE!")
        break
    else:
        pass
    print("CURRENT TOP CARD :")
    print(cardsP[0])
    print("CARDS REMAINING : ",len(cardsP))
    while True:
        print("SELECT AN ATTRIBUTE (1/2/3/4)")
        selectAttr = input()
        if selectAttr == "1" or selectAttr == "2" or selectAttr ==  "3" or selectAttr == "4":
            break
        else:
            pass
    if selectAttr == "1":
        cls()
        compareTool = Dogs.compare_drool(cardsP[0],cardsC[0])
        if compareTool == True:
            cardsP.append(cardsC.pop(0))
            cardsP.append(cardsP.pop(0))
            print("ENEMY LAST CARD : ")
            try:
                print(cardsC[0])
            except IndexError:
                cls()
                print("$$$$$$$$$$$$$$$$$$$$")
                print("$ YOU WIN THE GAME $")
                print("$$$$$$$$$$$$$$$$$$$$")
                break
            print("$$$$$$$$$$$")
            print("$ YOU WON $")
            print("$$$$$$$$$$$")
        else:
            cardsC.append(cardsP.pop(0))
            cardsC.append(cardsC.pop(0))
            print("ENEMY LAST CARD : ")
            try:
                print(cardsC[0])
            except IndexError:
                cls()
                print("$$$$$$$$$$$$$$$$$$$$")
                print("$ YOU WIN THE GAME $")
                print("$$$$$$$$$$$$$$$$$$$$")
                break
            print("YOU LOST")
    elif selectAttr == "2":
        cls()
        compareTool = Dogs.compare_intelligence(cardsP[0],cardsC[0])
        if compareTool == True:

            cardsP.append(cardsC.pop(0))
            cardsP.append(cardsP.pop(0))
            print("ENEMY LAST CARD : ")
            try:
                print(cardsC[0])
            except IndexError:
                cls()
                print("$$$$$$$$$$$$$$$$$$$$")
                print("$ YOU WIN THE GAME $")
                print("$$$$$$$$$$$$$$$$$$$$")
                break
            print("$$$$$$$$$$$")
            print("$ YOU WON $")
            print("$$$$$$$$$$$")
        else:

            cardsC.append(cardsP.pop(0))
            cardsC.append(cardsC.pop(0))
            print("ENEMY LAST CARD : ")
            try:
                print(cardsC[0])
            except IndexError:
                cls()
                print("$$$$$$$$$$$$$$$$$$$$")
                print("$ YOU WIN THE GAME $")
                print("$$$$$$$$$$$$$$$$$$$$")
                break
            print("YOU LOST")
    elif selectAttr == "3":
        cls()
        compareTool = Dogs.compare_friendliness(cardsP[0],cardsC[0])
        if compareTool == True:

            cardsP.append(cardsC.pop(0))
            cardsP.append(cardsP.pop(0))
            print("ENEMY LAST CARD : ")            
            try:
                print(cardsC[0])
            except IndexError:
                cls()
                print("$$$$$$$$$$$$$$$$$$$$")
                print("$ YOU WIN THE GAME $")
                print("$$$$$$$$$$$$$$$$$$$$")
                break
            print("$$$$$$$$$$$")
            print("$ YOU WON $")
            print("$$$$$$$$$$$")
        else:

            cardsC.append(cardsP.pop(0))
            cardsC.append(cardsC.pop(0))
            print("ENEMY LAST CARD : ")
            try:
                print(cardsC[0])
            except IndexError:
                cls()
                print("$$$$$$$$$$$$$$$$$$$$")
                print("$ YOU WIN THE GAME $")
                print("$$$$$$$$$$$$$$$$$$$$")
                break
            print("YOU LOST")
    elif selectAttr == "4":
        cls()
        compareTool = Dogs.compare_excercise(cardsP[0],cardsC[0])
        if compareTool == True:

            cardsP.append(cardsC.pop(0))
            cardsP.append(cardsP.pop(0))
            print("ENEMY LAST CARD : ")
            try:
                print(cardsC[0])
            except IndexError:
                cls()
                print("$$$$$$$$$$$$$$$$$$$$")
                print("$ YOU WIN THE GAME $")
                print("$$$$$$$$$$$$$$$$$$$$")
                break
            print("$$$$$$$$$$$")
            print("$ YOU WON $")
            print("$$$$$$$$$$$")
        else:

            cardsC.append(cardsP.pop(0))
            cardsC.append(cardsC.pop(0))
            print("ENEMY LAST CARD : ")
            try:
                print(cardsC[0])
            except IndexError:
                cls()
                print("$$$$$$$$$$$$$$$$$$$$")
                print("$ YOU WIN THE GAME $")
                print("$$$$$$$$$$$$$$$$$$$$")
                break
            print("YOU LOST")
    else:
        pass







