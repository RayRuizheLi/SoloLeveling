import psycopg2

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

def add_ticket(connection, title, note, diff):
    try: 
        cursor = connection.cursor()

        insert_ticket = """ INSERT INTO todos (TITLE, NOTE, DIFFICULTY, COMPLETED) 
                            VALUES (%s, %s, %s, FALSE)"""

        cursor.execute(insert_ticket, [title, note, diff])
        connection.commit()

        return True

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

        return False
        
def del_ticket(connection, id):
    try: 
        cursor = connection.cursor()

        done_ticket = """ UPDATE todos SET completed = TRUE WHERE id = %s"""

        cursor.execute(done_ticket, [id])
        connection.commit()

        return True

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

        return False

def pretty_print_ticket(results):
    if(results):
        print("Here are your tickets: \n")

        for i in range(len(results)):
            id = results[i][0]
            title = results[i][1]
            notes = results[i][2]
            diff = results[i][3]
            stars = ""
            
            for star in range(diff):
                stars += "*"


            print("{} | Diff: {} | ID: {}".format(title, stars, id))
            print("Notes: \n    {}".format(notes))
            print("")

def show(connection):
    try: 
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM todos WHERE completed = FALSE")

        result = cursor.fetchall()

        pretty_print_ticket(result)

        return True

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

        return False

def start():
    print("Welcome to Solo Leveling, let the grinding begin C:")

    connection = connect_db()

    if(connection):
        while(True):
            show(connection)

            command = input("Take a step: add ticket(add) | delete ticket(del) | exit (exit)\n")

            if command == "add":
                title = input("Title: ")
                note = input("Note: ")
                diff = int(input("Difficulty: "))

                query = add_ticket(connection, title, note, diff)

                if query:
                    print("Added 1 ticket.")
                else:
                    print("Failed to insert ticket ):")

            elif command == "del":
                id = input("ID: ")

                query = del_ticket(connection, id)

                if query:
                    print("Deleted 1 ticket.")
                else:
                    print("Failed to delete ticket ):")

            elif command == "exit":
                print("Solo Leveling system closed. See you soon (:")
                break
            else:
                print("Invalid command")
    else:
        print("Failed to connect to solo database")

start()