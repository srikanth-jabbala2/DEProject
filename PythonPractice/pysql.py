import pyodbc
import pandas as pd

# Define connection parameters
server = 'localhost'  # e.g., 'localhost' or '192.168.1.100'
database = 'sqlpractice'  # e.g., 'sqlpractice'
driver = 'ODBC Driver 17 for SQL Server'  # Ensure this driver is installed
Trusted_Connection='yes'

# Establish the connection
try:
    connection = pyodbc.connect(
        f"DRIVER={{{driver}}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"Trusted_Connection={Trusted_Connection};"
    )
    print("Connection successful!")

    # Create a cursor object
    cursor = connection.cursor()

   
    # Execute a query
    df = pd.DataFrame(cursor.execute("SELECT * from employee"))
    print(df)
    cursor.close()
    connection.close()


    # # for row in cursor.fetchall():
    # #     print(row)

    # df2 = pd.DataFrame(cursor.execute("SELECT * from dept"))
    # df2.show()

    # # # Fetch and print results
    # # for row in cursor.fetchall():
    # #     print(row)

    # # Close the connection
    

except Exception as e:
    print("Error while connecting to SQL Server:", e)