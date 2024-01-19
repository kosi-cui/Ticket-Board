import pymysql

def InitializeDb():
    # Connect to the database
    connection = pymysql.connect(
        host='db',  # Name of the MySQL service
        user='root',  # As defined in docker-compose.yml
        password='root_password',  # As defined in docker-compose.yml
        db='my_database',  # As defined in docker-compose.yml
    )

    # Create a cursor
    cursor = connection.cursor()

    # Execute the SQL script
    with open('schema.sql', 'r') as file:
        sql_script = file.read()
        for statement in sql_script.split(';'):
            if statement.strip():  # Ensure the statement is not empty
                cursor.execute(statement)

    # Commit the transaction
    connection.commit()

    # Close the connection
    connection.close()