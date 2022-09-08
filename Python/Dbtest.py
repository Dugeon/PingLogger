import pyodbc 

cnxn = pyodbc.connect("DRIVER={ODBC Driver 18 for SQL Server};SERVER=localhost;DATABASE=pinglog;UID=dugeon;PASSWORD=Aztx2390;")
cursor = cnxn.cursor()
