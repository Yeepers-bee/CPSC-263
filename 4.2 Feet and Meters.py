import conversions


def main():
    title()
    user_continue = 'y'
    while user_continue == 'y':
        user_input = menu()
        if user_input == 'a':
            feet = input("Enter feet: ")
            answer = conversions.feet_to_meters(float(feet))
            print(str(round(answer, 2)), " meters")
        elif user_input == 'b':
            meters = input("Enter meters: ")
            answer = conversions.meters_to_feet(float(meters))
            print(str(round(answer, 2)), " feet")
        user_continue = input("\nWould you like to perform another conversion? (y/n): ")
        if user_continue == 'n':
            print("\nThanks, bye!")
            break
def menu():
    print("\nConversions Menu: ")
    print("a.      Feet to Meters")
    print("b.      Meters to Feet")
    user_input = input("Select a conversion (a/b): ")
    return user_input
def title():
    print("Feet and Meters Converter")

if __name__ == "__main__":
    main()
