import sqlite3
import datetime

conn = sqlite3.connect('avginvagedb.sqlite')
curs = conn.cursor()

curs.execute('''DROP TABLE IF EXISTS Inventory''')

curs.execute('''CREATE TABLE IF NOT EXISTS Inventory (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        Date VARCHAR, 
        Trans TEXT,
        Quantity FLOAT)''')

conn.execute('''INSERT or IGNORE INTO Inventory (Date,Trans,Quantity) VALUES ('25-02-2020','P',5.0)''')
conn.execute('''INSERT or IGNORE INTO Inventory (Date,Trans,Quantity) VALUES ('25-02-2020','S',2.0)''')
conn.execute('''INSERT or IGNORE INTO Inventory (Date,Trans,Quantity) VALUES ('26-02-2020','P',7.0)''')
conn.execute('''INSERT or IGNORE INTO Inventory (Date,Trans,Quantity) VALUES ('27-02-2020','S',3.0)''')
conn.execute('''INSERT or IGNORE INTO Inventory (Date,Trans,Quantity) VALUES ('28-02-2020','S',2.0)''')
conn.execute('''INSERT or IGNORE INTO Inventory (Date,Trans,Quantity) VALUES ('01-03-2020','S',1.0)''')
conn.execute('''INSERT or IGNORE INTO Inventory (Date,Trans,Quantity) VALUES ('02-03-2020','P',2.0)''')
conn.execute('''INSERT or IGNORE INTO Inventory (Date,Trans,Quantity) VALUES ('03-03-2020','S',1.0)''')


curs.execute('''SELECT DISTINCT Date FROM Inventory''')
dates = list()
for row in curs:
    dates.append(row[0])

inventoryage = dict()  
for date in dates:
    curs.execute('''SELECT Trans,Quantity FROM Inventory WHERE Date = ?''',(date,))
    temp = list()
    for row in curs:
        if row[0] == 'P':
            temp.append(1*row[1])
        if row[0] == 'S':
            temp.append(-1*row[1])
    datecomp = date.split('-')
    date = datetime.date(int(datecomp[2]),int(datecomp[1]),int(datecomp[0]))
    inventoryage[date] = sum(temp)
    
    
conn.commit()