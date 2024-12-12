# Task 1 Flight Itineraries
def display_itineraries(Itins):
    '''Display flights in numerical order.'''
    for index, (person, trips) in enumerate(Itins, start=1):
        for depart, destin in trips:
            print(f"\n {index}. {person}'s Trip: From {depart} to {destin}")
        print()

def add_flight(Itins):
    '''Add a new flight to Itins (Itierary).'''
    name = input("Enter traveler's name: ").capitalize()
    departure = input("Enter departure destination: ").capitalize()
    destination = input("Enter arrival destination: ").capitalize()

    new_flight = (name, [(departure, destination)])
    Itins.append(new_flight)
    print("-" * 30)
    print(f"Your flight {name}, has been added to the list")

def main():
    '''The main program'''
    Itins = [
        ("Alice", [("New York", "London")]),
        ("Bob", [("Tokyo", "San Francisco")])
    ]

    while True:
        action = input("\nWhat would you like to do? (display/add/quit): ").lower()

        if action == 'quit':
            print("Exiting the program.")
            break
        elif action == 'display':
            display_itineraries(Itins)
        elif action == 'add':
            add_flight(Itins)
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()
        
