from ast import Not
from os.path import exists
from datetime import date


def sub(num,take):

    x = int(num)
    return x - take

def add(num,take):

    x = int(num)
    return x + take


def main():

    Users = []
    Owe = []
    lines = []
    today = "--------------------" + str(date.today()) + "--------------------" + " \n"

    if exists("LatestLOG.txt"):

        with open('LatestLOG.txt','r') as file:

            lines = file.readlines()

            for i in range(len(lines)):
                Users.append(lines[i].split()[0])

            Users.pop(0)
            Users.pop(len(Users)-1)

            for i in range(len(lines)):
                x = [int(s) for s in lines[i].split() if s.isdigit()]

                if len(x) > 0:
                    y = x[0]
                    Owe.append(y) 

        for i in range(len(Users)):
            print("User\t{}\t\towes {}".format(Users[i],Owe[i]))

        for i in range(len(Users)):

            print("Change how much {} owes?\tThey owe {}".format(Users[i],Owe[i]))
            inp = input("y/n?\t").lower()
            if(inp == 'y'):

                inp = input("Subtract or add? y for add, n for subtract\t").lower()

                if(inp == 'y'):

                    Owe[i] = add(int(Owe[i]),int(input("How much?\t")))
                else:
                    Owe[i] = sub(int(Owe[i]),int(input("How much?\t")))


    else:
        print("No file exists, please enter some names, enter 'none' to end this process")
        x = input("Enter a name: ")
        y = input("\nHow much do they owe: ")

        while(x != 'none'):
            Users.append(x)
            Owe.append(y)
            x = input("Enter a name: ")
            if x == "none":
                break
            y = input("\nHow much do they owe: ")
            

    with open('LatestLOG.txt',"w") as file:
         file.write(today)

         for i in range(len(Users)):
             file.write(Users[i] + "\t | \t")
             file.write(str((int(float(Owe[i])))) + "\n")

         file.write("--------------------------------------------------")

    

main()