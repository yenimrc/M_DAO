import pyodbc

conn = pyodbc.connect(
    "DRIVER={MySQL ODBC 9.4 ANSI Driver};"
    "SERVER=localhost,3306;"
    "DATABASE=usuarios;"
    "UID=root;"
    "PWD=;"
    "TrustServerCertificate=yes;"
)
print("✅ Conexión exitosa a SQL Server")
conn.close()

