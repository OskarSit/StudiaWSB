#Utworzenie klasy Flight

class Flight:
    def __init__(self, flight_number, origin, destination, departure_time, capacity):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.capacity = capacity
        self.seats_booked = 0

    def display_flight_details(self):
        print("Flight Number:", self.flight_number)
        print("Origin:", self.origin)
        print("Destination:", self.destination)
        print("Departure Time:", self.departure_time)
        print("Capacity:", self.capacity)
        print("Seats Booked:", self.seats_booked)

    def book_seat(self, num_seats):
        if self.seats_booked + num_seats <= self.capacity:
            self.seats_booked += num_seats
            print(f"Successfully booked {num_seats} seat(s).")
        else:
            print("Sorry, there are not enough available seats.")

    def cancel_seat(self, num_seats):
        if self.seats_booked >= num_seats:
            self.seats_booked -= num_seats
            print(f"Successfully cancelled {num_seats} seat(s).")
        else:
            print("Sorry, invalid cancellation request.")


# Tworzenie lotów
flight1 = Flight("FL3131", "Warsaw", "Sosnowiec", "2023-05-25 10:00", 174)
flight2 = Flight("FL5435", "Chile", "Tokyo", "2023-06-01 14:30", 200)

# Wyświetlanie szczegółów lotów
flight1.display_flight_details()
print()
flight2.display_flight_details()
print()

# Rezerwacja miejsc
num_seats = int(input("Enter the number of seats to book for Flight 1: "))
flight1.book_seat(num_seats)
print()

num_seats = int(input("Enter the number of seats to book for Flight 2: "))
flight2.book_seat(num_seats)
print()

# Anulowanie rezerwacji miejsc
num_seats = int(input("Enter the number of seats to cancel for Flight 1: "))
flight1.cancel_seat(num_seats)
print()

num_seats = int(input("Enter the number of seats to cancel for Flight 2: "))
flight2.cancel_seat(num_seats)
print()

# Wyświetlanie zaktualizowanych szczegółów lotów
flight1.display_flight_details()
print()
flight2.display_flight_details()
print()
