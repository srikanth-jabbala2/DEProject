import pandas as pd
from sqlalchemy import create_engine

server = 'localhost'
database = 'sqlpractice'
driver = 'ODBC Driver 17 for SQL Server'
Trusted_Connection='yes'

connection_string = f"mssql+pyodbc://{server}/{database}?driver={driver.replace(' ', '+')}&Trusted_Connection={Trusted_Connection}"
engine = create_engine(connection_string)

print("Connection successful!")

csv_file_path = 'AdventureWorks_Products.csv'
df = pd.read_csv(csv_file_path)


# Clean the data (optional)
# Replace invalid numeric values with NaN
for col in df.select_dtypes(include=['float', 'int']).columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Optionally, fill NaN values with a default value (e.g., 0)
df = df.fillna(value={'ProductCost': 0})  # Replace 'ProductCost' with your column name
# Write the DataFrame to the SQL table
table_name = 'Products'

try:
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Data from {csv_file_path} successfully written to the '{table_name}' table.")
except Exception as e:
    print(f"Error writing to table '{table_name}': {e}")