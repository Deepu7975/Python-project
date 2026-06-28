import random
import uuid
from datetime import datetime

otp = random.randint(1000, 9999)

with open("Otp-generator.txt", "w") as f:
    f.write(str(otp))


class Movie:
    def __init__(self, movie_name, category, language, duration):
        self.movie_name = movie_name
        self.category = category
        self.language = language
        self.duration = duration

    def display_movie(self):
        print("\n" + "=" * 50)
        print("MOVIE DETAILS")
        print("=" * 50)
        print(f"Movie Name : {self.movie_name}")
        print(f"Category   : {self.category}")
        print(f"Language   : {self.language}")
        print(f"Duration   : {self.duration}")
        print("=" * 50)


class Theater:
    def __init__(self, theater_name, location, seats, amount):
        self.theater_name = theater_name
        self.location = location
        self.seats = seats
        self.amount = amount

    def display_theater(self):
        print("\n" + "=" * 50)
        print("THEATER DETAILS")
        print("=" * 50)
        print(f"Theater : {self.theater_name}")
        print(f"Location : {self.location}")
        print(f"Available Seats : {self.seats}")
        print(f"Ticket Price : ₹{self.amount}")
        print("=" * 50)

    def book_ticket(self):
        self.display_theater()

        number = int(input("Enter Number of Tickets : "))

        if number <= 0 or number > self.seats:
            print("Invalid ticket count or seats unavailable.")
            return

        customer = input("Enter Customer Name : ")

        total = number * self.amount

        print(f"\nTotal Amount : ₹{total}")
        print("1. Online Payment")
        print("2. Cash Payment")

        payment = int(input("Select Payment Method : "))

        if payment == 1:
            input("Enter UPI ID : ")
            pin = int(input("Enter UPI PIN : "))
            if pin != 1234:
                print("Wrong PIN")
                return

            print(f"Generated OTP (Demo): {otp}")
            user_otp = int(input("Enter OTP : "))
            if user_otp != otp:
                print("Invalid OTP")
                return

        elif payment == 2:
            cash = int(input("Enter Cash Amount : "))
            if cash < total:
                print("Insufficient Cash")
                return
            print(f"Change Returned : ₹{cash-total}")
        else:
            print("Invalid Payment")
            return

        gst = total * 0.18
        grand_total = total + gst
        booking_id = str(uuid.uuid4())[:8]
        booking_time = datetime.now().strftime("%d-%m-%Y %I:%M %p")

        self.seats -= number

        print("\n" + "=" * 60)
        print("MOVIE TICKET")
        print("=" * 60)
        print(f"Booking ID : {booking_id}")
        print(f"Customer : {customer}")
        print(f"Theater : {self.theater_name}")
        print(f"Tickets : {number}")
        print(f"Subtotal : ₹{total}")
        print(f"GST : ₹{gst:.2f}")
        print(f"Grand Total : ₹{grand_total:.2f}")
        print(f"Remaining Seats : {self.seats}")
        print(f"Booking Time : {booking_time}")
        print("=" * 60)

        with open("Booking_History.txt", "a") as f:
            f.write(f"{booking_id},{customer},{self.theater_name},{number},{grand_total:.2f},{booking_time}\n")


movies = {
    1: (Movie("Karva", "Horror", "Kannada", "2h 28m"), Theater("PVR", "Bangalore", 100, 250)),
    2: (Movie("Kantara", "Action", "Kannada", "2h 30m"), Theater("INOX", "Mysore", 150, 220)),
    3: (Movie("777 Charlie", "Drama", "Kannada", "2h 44m"), Theater("Cinepolis", "Mangalore", 120, 200)),
    4: (Movie("Lucia", "Thriller", "Kannada", "2h 15m"), Theater("Carnival", "Hubli", 180, 180)),
    5: (Movie("U Turn", "Mystery", "Kannada", "2h 10m"), Theater("Rockline", "Belgaum", 140, 170)),
    6: (Movie("Arya", "Love Story", "Kannada", "2h 18m"), Theater("Ganesha", "Tiptur", 100, 190)),
    7: (Movie("Journey 2", "Adventure", "Kannada", "2h 20m"), Theater("Lakshmi", "Tumakuru", 130, 210)),
    8: (Movie("College Days", "Rom-Com", "Kannada", "2h 12m"), Theater("SRS", "Bangalore", 160, 230)),
    9: (Movie("Kirik Party", "Comedy", "Kannada", "2h 25m"), Theater("Lakshmi", "Tiptur", 110, 200)),
}

while True:
    print("\n===== KANNADA MOVIE BOOKING SYSTEM =====")
    for i, (m, _) in movies.items():
        print(f"{i}. {m.category} - {m.movie_name}")
    print("10. Exit")

    choice = int(input("Enter choice: "))

    if choice == 10:
        print("Thank you!")
        break

    if choice in movies:
        movie, theater = movies[choice]
        movie.display_movie()
        theater.book_ticket()
    else:
        print("Invalid Choice")
