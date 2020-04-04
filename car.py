import time

class Car:
    def __init__(self):
        self.acceleration = 0
        self.speedmeter = 0
    def accelerate(self):
        self.acceleration += 10
        time.sleep(0.4)
        print("You are going {} m/s!".format(self.acceleration))
        for i in range(0, self.acceleration):
            self.speedmeter += i
    def deceleration(self):
        self.acceleration -= 10
        if self.acceleration < 0:
            time.sleep(0.4)
            print("You are going reverse at {} kmph".format(self.acceleration))
        elif self.acceleration <= -30:
            time.sleep(0.4)
            print("Your reverse limit has peaked! First gear has been automatically initialized.")
            self.acceleration += 30
    def show_speed(self):
        time.sleep(0.4)
        print("You have travelled {} meters!".format(self.speedmeter))

car = Car()

def drive():
    while True:
        try:
            time.sleep(1)
            choice = str(input("What would you like to do? [A]accelerate, [B]decelerate, [C]show speed meter")).lower()
            if choice == "a":
                car.accelerate()
            elif choice == "b":
                car.deceleration()
            elif choice == "c":
                car.show_speed()
            else:
                time.sleep(0.4)
                print("Not one of the options.")
        except:
            time.sleep(0.4)
            print("Something went wrong with the input.. Try again")

drive()
