import psycopg2
from datetime import datetime

from .todo_controller import TodoController

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
            repeat = int(input("Repeat: "))
            tag = input("Tag: ")
            ticket_title = input("Ticket title: ")
            ticket_note = input("Ticket note: ")
            ticket_diff = input("Ticket diff: ")
            goal_type = "repeat"
            dt = datetime.now()

            insert_ticket = (f"INSERT INTO {self.list} (TITLE, NOTE," +
                             f"TICKETS, COUNTS, COUNTS_DONE, TAG, COMPLETED," +
                             f"START_DATE, TYPE) VALUES (%s, %s, %s, %s, 0," + 
                             f"%s, FALSE, %s, %s)")

            cursor.execute(insert_ticket, [title, note, ticket_title, repeat, tag, dt, goal_type])
            self.connection.commit()

            for i in range(repeat):
                if i == 0:
                    insert_ticket = (f"INSERT INTO todo (TITLE, NOTE, DIFFICULTY," +
                                f"TAG, COMPLETED, START_DATE, VISIBLE, GOAL) VALUES (%s, %s, %s," + 
                                f"%s, FALSE, %s, TRUE, %s)")
                else:
                    insert_ticket = (f"INSERT INTO todo (TITLE, NOTE, DIFFICULTY," +
                                    f"TAG, COMPLETED, START_DATE, VISIBLE, GOAL) VALUES (%s, %s, %s," + 
                                    f"%s, FALSE, %s, FALSE, %s)")

                cursor.execute(insert_ticket, [ticket_title, ticket_note, ticket_diff, tag, dt, title])
                self.connection.commit()

            return True

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

            return False

    def del_ticket(self, id):
        try: 
            cursor = self.connection.cursor()

            del_ticket = (f"SELECT TICKETS FROM goal WHERE id = %s;")

            cursor.execute(del_ticket, [id])

            ticket_name = cursor.fetchall()[0][0]

            del_ticket = (f"DELETE FROM todo WHERE title = %s;")

            cursor.execute(del_ticket, [ticket_name])
            self.connection.commit()

            dt = datetime.now()

            del_ticket = (f"DELETE FROM {self.list} WHERE id = %s;")

            cursor.execute(del_ticket, [id])
            self.connection.commit()



            return True

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

            return False
            
    def done_ticket(self, id):
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

    def pretty_print_goals(self, results):
        if(results):
            print("\n Here are your tickets: \n")

            repeat = epic = list()

            for i in range(len(results)):
                if(results[i][7] == "repeat"):
                    repeat.append(results[i])
                elif(results[i][7] == "epic"):
                    epic.append(results[i])

            for goal in repeat:
                id = goal[0]
                title = goal[1]
                notes = goal[2]
                count = goal[4]
                counts_done = goal[5]
                tag = goal[6] 
                goal_type = goal[7] 

                print("* Ticket:")
                print("    {} | ID: {} | Tag: {} | Goal Type: {}".format(title, id, tag, goal_type))
                print("  Notes: \n    {}".format(notes))

                progress_bar = "["

                for i in range(counts_done):
                    progress_bar += "*"

                for i in range(count - counts_done):
                    progress_bar += "-"
                
                progress_bar += "]"

                print("  Progress: \n    {}".format(progress_bar))

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

            self.pretty_print_goals(result)

            return True

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

            return False