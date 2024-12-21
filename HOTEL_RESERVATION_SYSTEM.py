class Hotel:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms  
        self.reservations = {}  
        
    def show_available_rooms(self):
        available_rooms = [room for room, available in self.rooms.items() if available]
        total_rooms = len(self.rooms)
        available_count = len(available_rooms)
        reserved_count = total_rooms - available_count
        
        print(f"Total Rooms: {total_rooms}")
        print(f"Available Rooms: {available_count}")
        print(f"Reserved Rooms: {reserved_count}")

    def make_reservation(self, customer_name, room_number, days, nights):
        if room_number in self.rooms and self.rooms[room_number]:
            self.rooms[room_number] = False
            self.reservations[customer_name] = {'room': room_number, 'days': days, 'nights': nights}
            print(f"Reservation successful for {customer_name} in room {room_number} for {days} days and {nights} nights.")
        else:
            print(f"Room {room_number} is not available.")

    def cancel_reservation(self, customer_name):
        if customer_name in self.reservations:
            room_number = self.reservations[customer_name]['room']
            self.rooms[room_number] = True  # Make the room available again
            del self.reservations[customer_name]  # Remove only that customer's reservation
            print(f"Reservation for {customer_name} in room {room_number} has been canceled.")
        else:
            print(f"No reservation found for {customer_name}.")

    def show_reservations(self):
        if self.reservations:
            print("Current Reservations:")
            for customer_name, reservation in self.reservations.items():
                room_number = reservation['room']
                days = reservation['days']
                nights = reservation['nights']
                print(f"Customer: {customer_name}, Room: {room_number}, Days: {days}, Nights: {nights}")
        else:
            print("No current reservations.")

    def show_hotel_info(self):
        print(f"Hotel Name: {self.name}")
        print(f"Total Rooms: {len(self.rooms)}")

def print_hollow_square_pattern(choices):
    width = max(len(choice) for choice in choices) + 4   

    print('*' * width)
    
    for choice in choices:
        print(f"* {choice.ljust(width - 3)}*")
    
    print('*' * width)

hotel_name = input("Enter the hotel name: ")
total_rooms = int(input("Enter the number of rooms: "))
rooms_dict = {i: True for i in range(101, 101 + total_rooms)}  

hotel = Hotel(hotel_name, rooms_dict)
hotel.show_hotel_info()

while True:
    print("\nHotel Reservation System")

    choices = [
        "1. Room Reservation",
        "2. View Available Rooms",
        "3. View Room Reservations",
        "4. Cancel Reservation",
        "5. Exit"
    ]
    print_hollow_square_pattern(choices)
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        customer_name = input("Enter customer name: ")
        room_number = int(input("Enter room number: "))
        days = int(input("Enter the number of days: "))
        nights = int(input("Enter the number of nights: "))
        hotel.make_reservation(customer_name, room_number, days, nights)
    
    elif choice == '2':
        hotel.show_available_rooms()
    
    elif choice == '3':
        hotel.show_reservations()
    
    elif choice == '4':
        customer_name = input("Enter customer name to cancel reservation: ")
        hotel.cancel_reservation(customer_name)
    
    elif choice == '5':
        print("Thank you for using the Hotel Reservation System. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")
