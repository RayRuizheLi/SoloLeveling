import psycopg2
from datetime import datetime

class TodoController:
    def __init__(self, connection, list):
        self.connection = connection
        self.list = list
        self.tag = "all"

    def show_tags(self):
        try: 
            # query all the items with tag 
            cursor = self.connection.cursor()

            distinct_tag = (f"SELECT DISTINCT tag FROM {self.list} " +
                            f"WHERE visible = TRUE" )
            cursor.execute(distinct_tag)

            result = cursor.fetchall()

            return result

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

            return False
            
    def switch_tag(self, tag):
            self.tag = tag

    def add_ticket(self, title, note, diff, tag):
        try: 
            cursor = self.connection.cursor()

            dt = datetime.now()

            insert_ticket = (f"INSERT INTO {self.list} (TITLE, NOTE, DIFFICULTY," +
                             f"TAG, COMPLETED, START_DATE, VISIBLE) VALUES (%s, %s, %s," + 
                             f"%s, FALSE, %s, TRUE)")

            cursor.execute(insert_ticket, [title, note, diff, tag, dt])
            self.connection.commit()

            return True

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

            return False

    def update_goal(self, id):
        try: 
            cursor = self.connection.cursor()

            goal = (f"SELECT * FROM {self.list} WHERE" +
                    f" id = %s")

            cursor.execute(goal, [id])

            result = cursor.fetchall()

            goal = (f"SELECT goal FROM {self.list} WHERE" +
                    f" id = %s")

            cursor.execute(goal, [id])

            result = cursor.fetchall()
        
            if result[0][0] == None:
                return 

            # Get the goal ticket counts done
            goal = (f"SELECT counts_done FROM goal WHERE" +
                           f" title = %s")
            cursor.execute(goal, [result[0][0]])

            counts_done = cursor.fetchall()[0][0]

            counts_done += 1

            goal = (f"UPDATE goal SET counts_done = %s " +
                    f"WHERE title = %s")

            cursor.execute(goal, [counts_done, result[0][0]])
            self.connection.commit()

            id = int(id)
            id += 1
            
            ticket = (f"UPDATE {self.list} SET visible = TRUE " +
                      f"WHERE id = %s")

            cursor.execute(ticket, [id])
            self.connection.commit()

            print("update goal completed")

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

            return False
            
    def done_ticket(self, id):
        try: 
            cursor = self.connection.cursor()

            dt = datetime.now()

            print("call update goal")
            self.update_goal(id)
            

            done_ticket = (f"UPDATE {self.list} SET completed = TRUE," +
                           f"end_date = %s WHERE id = %s")

            cursor.execute(done_ticket, [dt, id])
            self.connection.commit()

            return True

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

            return False

    def del_ticket(self, id):
        try: 
            cursor = self.connection.cursor()

            dt = datetime.now()

            del_ticket = (f"DELETE FROM {self.list} WHERE id = %s;")

            cursor.execute(del_ticket, [id])
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
                tag = results[i][4]
                stars = ""
                
                for star in range(diff):
                    stars += "*"

                print("* Ticket:")
                print("    {} | Diff: {} | ID: {} | Tag: {}".format(title, stars, id, tag))
                print("  Notes: \n    {}".format(notes))
                print("")

    def show(self):
        try: 
            cursor = self.connection.cursor()

            incomplete = (f"SELECT * FROM {self.list} WHERE completed = FALSE AND visible = TRUE")

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