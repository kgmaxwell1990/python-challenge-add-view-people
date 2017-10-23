def show_menu():
    print("1. Add Person")
    print("2. View People")
    print("3. Stats")
    print("4. Exit")

    option = input("Enter option:\n> ")
    return option

def add_person():
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    age = input("Enter Age: ")
    team = input("Enter Team: ")
    
    line = first_name + "," + last_name + "," + age + "," + team + "\n"
    
    print(line)
    
    with open("options.txt", "a") as people_file:
        people_file.write(line)

def person_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_person()
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


