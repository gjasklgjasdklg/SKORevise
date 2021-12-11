# imports
import time


def machine_learn():
    # subroutine for machine learning
    print("""Welcome to the Machine Learning revision section! What would you like to do?
A: Read information
B: Useful weblinks
C: Test
D: Games
X: Go back to main menu""")
    option = input("Enter your choice: ").lower()
    if option == "x":
        menu()
    elif option == "a":
        print("Welcome to the information section!\n")
        print("What is Machine Learning? This is a system where - rather than a computer programmer deciding the best way to sort, organise, classify or use information - a computer program develops its own set of instructions based on information that users feed it.\nHow do computers learn? They learn from")
    elif option == "b":
        print("Welcome to the list of useful websites!")
    elif option == "c":
        print("Welcome to the unit test. Good Luck!")
    elif option == "d":
        print("Welcome to the games section!")


def comp_think():
    # subroutine for computational thinking
    print("""Welcome to the Computational Thinking revision section! What would you like to do?
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
        print("Welcome to the list of useful websites!")
    elif choice == "c":
        print("Welcome to the unit test. Good Luck!")
    elif choice == "d":
        print("Welcome to the games section!")


def algorithms():
    # subroutine for fundamentals of algorithms
    print("""Welcome to the Algorithms revision section! What would you like to do?
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
        print("Welcome to the list of useful websites!")
    elif choice == "c":
        print("Welcome to the unit test. Good Luck!")
    elif choice == "d":
        print("Welcome to the games section!")


def programming():
    # subroutine for programming
    print("""Welcome to the Programming revision section! What would you like to do?
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
        print("Welcome to the list of useful websites!")
    elif choice == "c":
        print("Welcome to the unit test. Good Luck!")
    elif choice == "d":
        print("Welcome to the games section!")


def data_representation():
    # subroutine for fundamentals of data representation
    print("""Welcome to the Data Representation revision section! What would you like to do?
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
        print("Welcome to the list of useful websites!")
    elif choice == "c":
        print("Welcome to the unit test. Good Luck!")
    elif choice == "d":
        print("Welcome to the games section!")


def comp_systems():
    # subroutine for computer systems
    print("""Welcome to the Computer Systems revision section! What would you like to do?
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
        print("Welcome to the list of useful websites!")
    elif choice == "c":
        print("Welcome to the unit test. Good Luck!")
    elif choice == "d":
        print("Welcome to the games section!")


def comp_networks():
    # subroutine for fundamentals of computer networks
    print("""Welcome to the Computer Networks revision section! What would you like to do?
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
        print("Welcome to the list of useful websites!")
    elif choice == "c":
        print("Welcome to the unit test. Good Luck!")
    elif choice == "d":
        print("Welcome to the games section!")


def cyber_sec():
    # subroutine for fundamentals of cyber security
    print("""Welcome to the Cyber Security revision section! What would you like to do?
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
        print("Welcome to the list of useful websites!")
    elif choice == "c":
        print("Welcome to the unit test. Good Luck!")
    elif choice == "d":
        print("Welcome to the games section!")


def databases_and_sql():
    # subroutine for relational databases and SQL
    print("""Welcome to the Relational Databases and SQL revision section! What would you like to do?
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
        print("Welcome to the list of useful websites!")
    elif choice == "c":
        print("Welcome to the unit test. Good Luck!")
    elif choice == "d":
        print("Welcome to the games section!")


def impacts_of_technology():
    # subroutine for impacts of digital technology on society
    print("""Welcome to the Impacts of Digital Technology on Society revision section! What would you like to do?
A: Read information
B: Useful weblinks
C: Test
D: Games
X: Go back to main menu""")

    option = input("Enter your choice: ").lower()
    if option == "x":
        menu()
    elif option == "a":
        print("Welcome to the information section!")
    elif option == "b":
        print("Welcome to the list of useful websites!")
    elif option == "c":
        print("Welcome to the unit test. Good Luck!")
    elif option == "d":
        print("Welcome to the games section!")


def menu():
    # main menu for selecting revision topic
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
    option = input("Enter your choice: ").lower()
    if option == "x":
        print("Goodbye, make sure to revise often!")
        time.sleep(10)
        exit()
    elif option == "a":
        machine_learn()
    elif option == "b":
        comp_think()
    elif option == "c":
        algorithms()
    elif option == "d":
        programming()
    elif option == "e":
        data_representation()
    elif option == "f":
        comp_systems()
    elif option == "g":
        comp_networks()
    elif option == "h":
        cyber_sec()
    elif option == "i":
        databases_and_sql()
    elif option == "j":
        impacts_of_technology()


# run program


menu()
