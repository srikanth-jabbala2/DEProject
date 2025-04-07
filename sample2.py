import pandas
from sqlalchemy import create_engine

# df = pandas.read_csv("sample1.csv")
# print(df)
# df2 = df.groupby("Department")["Salary"].mean()
# print(df2)

server = 'localhost'
database = 'sqlpractice'
driver = 'ODBC Driver 17 for SQL Server'
Trusted_Connection= 'yes'

connection_string = f"mssql+pyodbc://{server}/{database}?driver={driver.replace(' ', '+')}&Trusted_Connection={Trusted_Connection}"
engine = create_engine(connection_string)
print("Connection successful!")
try:
    with engine.connect() as conn:
        df = pandas.read_sql("select * from employee", conn)
        df2 = pandas.read_sql("SELECT avg(emp_salary) as avg, emp_department FROM employee group by emp_department", conn)
        print(df)
        print(df2)
        # df.to_sql('employee', conn, if_exists='replace', index=False)
except Exception as e:
    print(f"Error: {e}")