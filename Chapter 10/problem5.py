# problem5.py
# Que: Write a class Train which has methods to book a ticket. get status (no. of seats) and get fare information of train running under railways.


class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")

    def getFareInfo(self):
        print(f"The price of the ticket is {self.fare}")

    def bookTicket(self):
        if self.seats > 0:
            print("Ticket is booked")
            self.seats = self.seats - 1
        else:
            print("Ticket is not available")

    def cancelTicket(self):
        print("Ticket is cancelled")
        self.seats = self.seats + 1

    def getSeats(self):
        return self.seats

    def getFare(self):
        return self.fare

    def getName(self):
        return self.name


train1 = Train("Rajdhani Express", 100, 10)
train1.getStatus()
train1.bookTicket()
train1.getStatus()
train1.cancelTicket()
train1.getStatus()
