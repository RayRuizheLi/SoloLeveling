import psycopg2
from datetime import datetime

from todo_controller import TodoController

class GoalController:
    def __init__(self, connection, list, todo_list):
        self.connection = connection
        self.list = list
        self.tag = "all"
        self.controller = TodoController(connection, todo_list)

    def show_tags(self):
        try: 
            # query all the items with tag 
            cursor = self.connection.cursor()

            distinct_tag = (f"SELECT DISTINCT tag FROM {self.list}")
            cursor.execute(distinct_tag)

            result = cursor.fetchall()

            return result

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

            return False
            
    def switch_tag(self, tag):
            self.tag = tag

    def add_repeat_goal(self):
        try: 
            cursor = self.connection.cursor()

            title = input("Title: ")
            note = input("Note: ")
            repeat = input("Repeat: ")
            tag = input("Tag: ")
            ticket_title = input("Ticket title: ")
            ticket_note = input("Ticket note: ")
            dt = datetime.now()

            insert_ticket = (f"INSERT INTO {self.list} (TITLE, NOTE," +
                             f"TICKETS, COUNT, COUNTS_DONE, TAG, COMPLETED," +
                             f"START_DATE) VALUES (%s, %s, %s, %s, 0" + 
                             f"%s, FALSE, %s)")

            cursor.execute(insert_ticket, [title, note, ticket_title, repeat, tag, dt])
            self.connection.commit()

            return True

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

            return False
            
    def del_ticket(self, id):
        try: 
            cursor = self.connection.cursor()

            dt = datetime.now()

            done_ticket = (f"UPDATE {self.list} SET completed = TRUE," +
                           f"end_date = %s WHERE id = %s")

            cursor.execute(done_ticket, [dt, id])
            self.connection.commit()

            return True

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

            return False

    def pretty_print_ticket(self, results):
        if(results):
            print("\n Here are your tickets: \n")

            for i in range(len(results)):
                id = results[i][0]
                title = results[i][1]
                notes = results[i][2]
                diff = results[i][3]
                stars = ""
                
                for star in range(diff):
                    stars += "*"

                print("* Ticket:")
                print("    {} | Diff: {} | ID: {}".format(title, stars, id))
                print("  Notes: \n    {}".format(notes))
                print("")

    def show(self):
        try: 
            cursor = self.connection.cursor()

            incomplete = (f"SELECT * FROM {self.list} WHERE completed = FALSE")

            if self.tag != "all":
                incomplete = (f"SELECT * FROM {self.list} WHERE completed = FALSE AND tag = %s")

            if self.tag != "all":
                cursor.execute(incomplete, [self.tag])
            else:
                cursor.execute(incomplete)

            result = cursor.fetchall()

            self.pretty_print_ticket(result)

            return True

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

            return False