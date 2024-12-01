import sqlite3
db_path = r'C:\Users\tio\Desktop\Chinook_Sqlite.sqlite'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT * FROM Customer LIMIT 3;")
first_three_customers = cursor.fetchall()
print("1. перші 3 записи з таблиці Customer:")
for customer in first_three_customers:
    print(customer)

cursor.execute("SELECT SUM(Total) AS TotalSum FROM Invoice;")
total_sum = cursor.fetchone()[0]
print("\n2.  загальну суму елементів поля Total таблиці Invoice:", total_sum)


cursor.execute("SELECT * FROM Invoice WHERE BillingCity = 'Paris';")
invoices_paris = cursor.fetchall()
print("\n3. тільки ті записи з таблиці Invoice у яких домашнє місто Paris:")
for invoice in invoices_paris[:5]:
    print(invoice)
print(f"... (total {len(invoices_paris)} )")


cursor.execute("""
    SELECT * 
    FROM Invoice 
    WHERE InvoiceDate = (SELECT MIN(InvoiceDate) FROM Invoice);
""")
oldest_invoice = cursor.fetchone()
print("\n4.  запис із найстарішою датою з таблиці Invoice:")
print(oldest_invoice)


cursor.execute("""
    SELECT * 
    FROM Invoice 
    WHERE InvoiceDate = (SELECT MAX(InvoiceDate) FROM Invoice);
""")
latest_invoice = cursor.fetchone()
print("\n5.  запис із найсвіжішою датою з таблиці Invoice:")
print(latest_invoice)


conn.close()


