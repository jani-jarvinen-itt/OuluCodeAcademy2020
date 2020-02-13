import pyodbc

print("Avataan tietokantayhteys ODBC:llä...")
yhteys = "Driver={SQL Server Native Client 11.0};server=localhost\\SQLEXPRESS;Database=Northwind;Trusted_Connection=yes;"
conn = pyodbc.connect(yhteys)
print("Tietokantayhteys on avattu.")

c = conn.cursor()
sql = "SELECT * FROM Customers"
rivit = c.execute(sql)
print("Tulostetaan rivit...")

for rivi in rivit:
    print(rivi)

conn.close()
print("Demo päättyy.")
