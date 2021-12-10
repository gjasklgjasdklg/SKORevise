#imports
import webbrowser
import random
import time 
def machineLearn():
    #subroutine for machine learning
    print("""Welcome to the Machine Learning revision section! What would you like to do?
A: Read information
B: Useful weblinks
C: Test
D: Games
X: Go back to main menu""")
    choice = input("Enter your choice: ").lower()
    if choice == "x":
        menu()
    elif choice == "a":
        print("Welcome to the information section!")
    elif choice == "b":
        print("Welcome to the list of useful webistes!")
    elif choice == "c":
        print("Welcome to the unit test. Good Luck!")
    elif choice == "d":
        print("Welcome to the games section!")

def compThink():
    #subroutine for computational thinking
    print("Under Construction 👷")

def algorithims():
    #subroutine for fundamentals of algorithms
    print("Under Construction 👷")

def programming():
    #subroutine for programming
    print("Under Construction 👷")

def dataRepresentation():
    #subroutine for fundamentals of data representation
    print("Under Construction 👷")

def compSystems():
    #subroutine for computer systems
    print("Under Construction 👷")

def compNetworks():
    #subroutine for funadmentals of computer networks
    print("Under Construction 👷")

def cyberSec():
    #subroutine for fundamentals of cyber security
    print("Under Construction 👷")

def databasesAndSQL():
    #subroutine for relational databases and SQL
    print("Under Construction 👷")

def impactsOfTechnology():
    #subroutine for impacts of digital technology on society
    print("Under Construction 👷")


def menu():
    #main menu for selecting revision topic
    print("""Welcome to the Computer Science Revision Guide. Topic list(just type the letter of the topic and press enter: 
A: Machine Learning
B: Computational Thinking
C: Fundamentals of Algorithms
D: Programming
E: Fundamentals of Data Representation
F: Computer Systems
G: Fundamentals of Computer Networks
H: Fundamentals of Cyber Security
I: Relational Databases and Structured Query Language (SQL)
J: Impacts of Digital Technology on Society
X: EXIT PROGRAM""")
    choice = input("Enter your choice: ").lower()
    if choice == "x":
        print("Goodbye, make sure to revise often!")
        time.sleep(10)
        exit()
    elif choice == "a":
        machineLearn()
    elif choice == "b":
        compThink()
    elif choice == "c":
        algorithims()
    elif choice == "d":
        programming()
    elif choice == "e":
        dataRepresentation()
    elif choice == "f":
        compSystems()
    elif choice == "g":
        compNetworks()
    elif choice == "h":
        cyberSec()
    elif choice == "i":
        databasesAndSQL()
    elif choice == "j":
        impactsOfTechnology()   
    
#run program
menu()
    