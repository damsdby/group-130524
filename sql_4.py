import sqlite3

connection = sqlite3.connect('C:\\Users\\tio\\Desktop\\Chinook_Sqlite.sqlite')
cursor = connection.cursor()


cursor.execute('''
    SELECT *
    FROM Customer
    WHERE Company = (
        SELECT Company
        FROM Customer
        GROUP BY Company
        ORDER BY LENGTH(Company) DESC
        LIMIT 1
    );
''')
result_level_1 = cursor.fetchall()
print("Покупці з найдовшою назвою компанії:")
for row in result_level_1:
    print(row)


cursor.execute('''
    SELECT COUNT(*)
    FROM Customer
    WHERE Company IS NULL AND Fax IS NULL;
''')
result_level_2 = cursor.fetchone()
print("\nКількість покупців без компанії та факсу:", result_level_2[0])

cursor.execute('''
    SELECT Country AS "НАЗВА КОНТИНЕНТУ", COUNT(*) AS "Кількість покупців"
    FROM Customer
    GROUP BY Country
    ORDER BY COUNT(*) DESC;
''')
result_level_3 = cursor.fetchall()
print("\nІнформація про континенти та кількість покупців:")
for row in result_level_3:
    print(f"{row[0]}: {row[1]}")


connection.close()
