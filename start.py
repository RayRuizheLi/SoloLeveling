import psycopg2

from ticketingSystem.controller import Controller

def connect_db():
    try:
        connection = psycopg2.connect(user="solo",
                                    password="level99",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="solo")
        return connection 

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return False

def select_list():

    command = input("Select a list: Todo, Work \n")

    while(True):
        if command == "Todo":
            return "todo"
        elif command == "Work":
            return "work"
        else:
            print("list does not exist")

def start():
    print("Welcome to Solo Leveling, let the grinding begin C:")

    connection = connect_db()

    if(connection):
        
        controller = Controller(connection, select_list())

        while(True):
            controller.show()

            command = input("Take a step: add ticket(add) | done ticket(done) | switch (sw) | exit (exit)\n")

            if command == "add":
                title = input("Title: ")
                note = input("Note: ")
                diff = int(input("Difficulty: "))
                tag = input("Tag: ")

                query = controller.add_ticket(title, note, diff, tag)

                if query:
                    print("Added 1 ticket.")
                else:
                    print("Failed to insert ticket ):")

            elif command == "done":
                id = input("ID: ")

                query = controller.del_ticket(id)

                if query:
                    print("Deleted 1 ticket.")
                else:
                    print("Failed to delete ticket ):")

            elif command == "sw":
                print(f"Options: {controller.show_tags()} or 'all'")                
                tag = input("Pick a tag: ")

                if controller.switch_tag(tag):
                    print(f"Switched to {tag} tag (:")
                else:
                    print("Tag does not exist")

            elif command == "exit":
                print("Solo Leveling system closed. See you soon (:")
                break

            else:
                print("Invalid command")
    else:
        print("Failed to connect to solo database")

start()