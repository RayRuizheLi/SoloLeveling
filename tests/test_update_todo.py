import psycopg2

try:
    connection = psycopg2.connect(user="solo",
                                  password="level99",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="solo")

    cursor = connection.cursor()
    # Executing a SQL query to insert data into  table
    insert_query = """ INSERT INTO todos (TITLE, NOTE, DIFFICULTY, COMPLETED) 
                            VALUES ('test1', 'Test insert ticket 1', 1, FALSE)"""
    cursor.execute(insert_query)
    connection.commit()
    print("1 Record inserted successfully")
    # Fetch result
    cursor.execute("SELECT * from todos")
    record = cursor.fetchall()
    print("Result ", record)

    # Executing a SQL query to update table
    update_query = """Update todos set completed = TRUE where title = 'test1'"""
    cursor.execute(update_query)
    connection.commit()
    count = cursor.rowcount
    print(count, "Record updated successfully ")
    # Fetch result
    cursor.execute("SELECT * from todos where title = 'test1'")
    print("Result ", cursor.fetchall())

    # Executing a SQL query to delete table
    delete_query = """Delete from todos where title = 'test1'"""
    cursor.execute(delete_query)
    connection.commit()
    count = cursor.rowcount
    print(count, "Record deleted successfully ")
    # Fetch result
    cursor.execute("SELECT * from todos")
    print("Result ", cursor.fetchall())


except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")