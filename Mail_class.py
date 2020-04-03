import time
import random
import string

user_list = ["Nylon", "Fresher guy", "Guro tiger", "God"]

user_password_chars = ["", "", "", "", "", "", ""]

def account_make():
    char = ""
    for i in range(0, 8):
        user_password_chars[i] = string.ascii_letters[random.randint(0, 51)]
        char = char + user_password_chars[i]
    print("'", char, "'", "is your password")
    g = input("What should your gmail be? ")
    time.sleep(0.420)
    print("So,", g, char, "is your ID")
    time.sleep(0.2785)
    username = input("Almost done! Enter your username: ")
    time.sleep(0.27)
    print("Welcome", username)
    time.sleep(2)
    print("\n" * 500)

class Gm:
    def __init__(self):
        self.msg_num = 0
        self.draft_num = 0
        self.draft = ""
        self.msg = ""
        self.user_spam = ""
        self.spam = ""
        self.responses = ""
    def user_spam(self):
        self.msg_num = 100
        self.user_spam = self.msg * self.msg_num
    def mail_receive(self, sender):
        print("You have received", self.msg_num, "msgs")
        if self.msg_num > 10:
            print("You have been spam")
            counter_q = input("Would you like to counter? (Y/N)").lower()
            if counter_q == "y":
                try:
                    self.draft = input("What would you like to send the spammer? ")
                    en = int(input("How many times"))
                    self.spam = self.draft * en
                    print("You have sent", self.draft, en, "amount of times to the", sender)
                except:
                    print("Something went wrong, sorry!")
            elif counter_q == "n":
                pass
            else:
                print("Invalid response, so, it will pass as a no.")
    def mail_sent(self, receiver):
        self.draft = input("What would you like to send to the {}?".format(receiver))
        opt = input("Would you like to spam? (Y/N)").lower()
        if opt == "y":
            sn = int(input("How many times?"))
            self.spam = self.draft * sn
            self.draft_num += sn
            print("You have sent", self.draft, self.draft_num, "amount of times")
            if sn > 10:
                random_var = random.randint(1, 6)
                if random_var == 1:
                    print("User has spammed you back!")
                    self.msg_num += random.randint(1, 15)
                    print("You have {} in your indbox".format(self.msg_num))
                else:
                    pass
            else:
                pass
        elif opt == "n":
            print("You only sent", self.draft)
    def nf(self, sender):
        self.msg_num += 1
        print(sender, "has sent something inappropritate!")
        self.responses = input("Would you like to: [A]send something more inappropriate or [B]tell {} not to send anything inappropriate".format(sender)).lower()
        if self.responses == "a":
            print("You sent a shirtless Homer simpson to", sender)
        elif self.responses == "b":
            print("You told the sender to stop with it ")
        else:
            print("Not a valid response, so redirected to a pass.")
