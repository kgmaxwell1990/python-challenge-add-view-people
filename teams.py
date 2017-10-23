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
   
        
def view_people():
    with open("options.txt", "r") as people_file:
        people = []
        
        lines = people_file.read().splitlines()
        
        for line in lines:
            fields = line.split(",")
            people.append(fields)
        
    print("List of People")
    
    for person in people:
        print("First Name: {0}, Last Name: {1}, Age: {2}, Team: {3}".format(person[0], person[1], person[2], person[3], ))


def person_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_person()
        elif option == "2":
            view_people()
        elif option == "3":
            print("You selected 'Stats'")
        elif option == "4":
            break
        else:
            print("Invalid Option")
        print("")

person_loop()


