import sqlite3

DB = 'my_bd.db'
FILE_PATH = r'C:\Users\tio\Downloads\part_data_1 (1).txt'

connection = sqlite3.connect(DB)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS contracts (
    contract_code INTEGER PRIMARY KEY,
    client_code TEXT,
    credit_code INTEGER,
    issue_date TEXT,
    amount INTEGER
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS contracts_unique (
    contract_code INTEGER PRIMARY KEY,
    client_code TEXT UNIQUE,
    credit_code INTEGER,
    issue_date TEXT,
    amount INTEGER
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS contracts_non_null (
    contract_code INTEGER PRIMARY KEY,
    client_code TEXT,
    credit_code INTEGER NOT NULL,
    issue_date TEXT,
    amount INTEGER
);
""")

data = []
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()
    for line in lines[1:]:
        parts = line.strip().split('\t')
        data.append((parts[0], parts[1], parts[2], parts[3], parts[4]))

cursor.executemany("""
INSERT OR IGNORE INTO contracts (contract_code, client_code, credit_code, issue_date, amount)
VALUES (?, ?, ?, ?, ?);
""", data)

cursor.executemany("""
INSERT OR IGNORE INTO contracts_unique (contract_code, client_code, credit_code, issue_date, amount)
VALUES (?, ?, ?, ?, ?);
""", data)

cursor.executemany("""
INSERT OR IGNORE INTO contracts_non_null (contract_code, client_code, credit_code, issue_date, amount)
VALUES (?, ?, ?, ?, ?);
""", data)

connection.commit()

connection.close()

cursor.executemany("""
INSERT OR IGNORE INTO contracts_unique (contract_code, client_code, credit_code, issue_date, amount)
VALUES (?, ?, ?, ?, ?);
""", data)

cursor.executemany("""
INSERT OR IGNORE INTO contracts_non_null (contract_code, client_code, credit_code, issue_date, amount)
VALUES (?, ?, ?, ?, ?);
""", data)

connection.commit()
connection.close()

connection.commit()
connection.close()


