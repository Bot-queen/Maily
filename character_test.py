import time

def character_test():
    time.sleep(1)
    print("You are in a room with three other people..")
    time.sleep(1)
    choice = input("What would you do? [A]Keep the silence, [B]Crack a joke about the silence, [C]leave, [D]Start up a topic, trying to draw everyone in").lower()
    try:
        if choice == "a":
            time.sleep(1)
            print("You are the type of person who likes to go with the flow.")
        elif choice == "b":
            time.sleep(1)
            print("You make people smile often and you are unique (that is if your joke is funny)")
        elif choice == "c":
            time.sleep(1)
            print("You try to avoid situations you don't like. More like running away.")
        elif choice == "d":
            time.sleep(1)
            print("You are somewhat hypocritic and want to be 'the leader'.")
        else:
            time.sleep(1)
            print("Your choice is invalid so I don't know what you are talking about.")
    except:
        print("Something went wrong.")

character_test()
