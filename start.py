import psycopg2

from controllers.todo_controller import TodoController
from controllers.goal_controller import GoalController

# from controllers.todo_controller import TodoController
# from controllers.goal_controller import GoalController

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

    command = input("Select a list: Todo \n")

    while(True):
        if command == "Todo":
            return "todo"
        else:
            print("list does not exist")

def todo(connection):
    todo_list = select_list()

    controller = TodoController(connection, todo_list)

    while(True):
        controller.show()

        command = input("Take a step: add ticket(add) | done ticket(done) | switch (sw) \n" + 
                        "             delete (del) | show (show) | exit (exit) \n")

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

            query = controller.done_ticket(id)

            if query:
                print("Completed 1 ticket.")
            else:
                print("Failed to complete ticket ):")
        
        elif command == "del":
            id = input("ID: ")

            query = controller.del_ticket(id)

            if query: 
                print("Deleted 1 ticket.")
            else: 
                print("Failed to deleted ticket ):")

        elif command == "sw":
            print(f"Options: {controller.show_tags()} or 'all'")                
            tag = input("Pick a tag: ")

            controller.switch_tag(tag)

            print(f"Switched to {tag} tag (:")

        elif command == "exit":
            print("Solo Leveling system closed. See you soon (:")
            break

        elif command == "show":
            continue

        else:
            print("Invalid command")


def goal(connection):
    todo_list = select_list()

    controller = GoalController(connection, "goal", todo_list)

    while(True):
        controller.show()

        command = input("Take a step: add repeat(adr) | add epic(ade) | switch (sw) \n" + 
                        "             delete (del) | show (show) | exit (exit) \n")

        if command == "adr":

            query = controller.add_repeat_goal()

            if query:
                print("Added 1 repeat goal.")
            else:
                print("Failed to add repeat goal ):")

        elif command == "done":
            id = input("ID: ")

            query = controller.done_ticket(id)

            if query:
                print("Completed 1 ticket.")
            else:
                print("Failed to complete ticket ):")
        
        elif command == "del":
            id = input("ID: ")

            query = controller.del_ticket(id)

            if query: 
                print("Deleted 1 ticket.")
            else: 
                print("Failed to deleted ticket ):")

        elif command == "sw":
            print(f"Options: {controller.show_tags()} or 'all'")                
            tag = input("Pick a tag: ")

            controller.switch_tag(tag)

            print(f"Switched to {tag} tag (:")

        elif command == "exit":
            print("Solo Leveling system closed. See you soon (:")
            break

        elif command == "show":
            continue

        else:
            print("Invalid command")

    
    

def select_mode():
    mode = input("Select mode: todo | goal\n")
    
    return mode

def start():
    print("Welcome to Solo Leveling, let the grinding begin C:")

    connection = connect_db()

    if(connection):

        mode = select_mode()

        print(mode)

        if mode == "goal":
            goal(connection)
        elif mode == "todo":
            todo(connection)

    else:
        print("Failed to connect to solo database")

start()