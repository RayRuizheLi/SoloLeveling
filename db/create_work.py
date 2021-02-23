import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="solo",
                                  password="level99",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="solo")

    cursor = connection.cursor()
    # SQL query to create a new table
    create_table_query = '''CREATE TABLE todos
          (ID             SERIAL PRIMARY KEY,
          TITLE           VARCHAR    NOT NULL,
          NOTE            TEXT,
          DIFFICULTY      INT        NOT NULL,
          COMPLETED       BOOLEAN    NOT NULL); ''' 

    # Execute a command: this creates a new table
    cursor.execute(create_table_query)
    connection.commit()
    print("Todo table created successfully in PostgreSQL")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")