import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="solo",
                                  password="level99",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="solo")

    cursor = connection.cursor()

    cursor.execute('''DROP TABLE IF EXISTS goal;''')


    # SQL query to create a new table
    create_table_query = '''CREATE TABLE goal
          (ID             SERIAL PRIMARY KEY,
          TITLE           VARCHAR    NOT NULL,
          NOTE            TEXT,
          TICKETS         TEXT       NOT NULL,
          COUNTS          INT        NOT NULL,
          COUNTS_DONE     INT        NOT NULL,
          TAG             VARCHAR    NOT NULL,
          COMPLETED       BOOLEAN    NOT NULL,
          START_DATE      TIMESTAMP  NOT NULL,
          END_DATE        TIMESTAMP,
          REWARD          VARCHAR); ''' 

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