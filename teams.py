def show_menu():
    print("1. Add Person")
    print("2. View People")
    print("3. Stats")
    print("4. Exit")

    option = input("Enter option: ")
    return option


def person_loop():
    while True:
        option = show_menu()
        if option == "1":
            print("You selected 'Add Person'")
        elif option == "2":
            print("You selected 'View People'")
        elif option == "3":
            print("You selected 'Stats'")
        elif option == "4":
            break
        else:
            print("Invalid Option")
        print("")

person_loop()


