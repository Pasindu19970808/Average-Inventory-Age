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

dailychange = list() 
for i in range(len(dates)):
    curs.execute('''SELECT Trans,Quantity FROM Inventory WHERE Date = ?''',(dates[i],))
    temp = list()
    for row in curs:
        if row[0] == 'P':
            temp.append(1*row[1])
        if row[0] == 'S':
            temp.append(-1*row[1])
    datecomp = dates[i].split('-')
    date = datetime.date(int(datecomp[2]),int(datecomp[1]),int(datecomp[0]))
    #dailychange[date] = sum(temp)
    dates[i] = date
    dailychange.append(sum(temp))


positions = list()
for i in range(len(dailychange)):
    if (dailychange[i] > 0):
        positions.append(i)

inventorydate = dict()
for i in range(len(positions)):
    if positions[-1] == positions[i]:
        inventorydate[dates[positions[i]]] = sum(dailychange[positions[i]:])
    else:
        inventorydate[dates[positions[i]]] = sum(dailychange[positions[i]:positions[i+1]])
    
referenceday  = datetime.date(2020,3,4)

tempsum = 0
total = 0
for (date,value) in inventorydate.items():
    tempsum += ((referenceday - date).days)*value
    total += value

averageage = tempsum/total

print(averageage)

    
    
