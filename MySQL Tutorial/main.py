import mysql.connector
from datetime import datetime
from secret import password

# initializing connection
db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd=password,
    database='testdatabase'
    )

# creating cursor variable
mycursor = db.cursor()


#mycursor.execute("CREATE TABLE Test (name varchar(50) NOT NULL, created datetime NOT NULL, "
#                 "gender ENUM('M', 'F', 'O') NOT NULL, id int PRIMARY KEY AUTO_INCREMENT)")
#mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s,%s,%s)", ('JOEY', datetime.now(), 'F'))
#db.commit()

'''ALTER TABLE = change something in table'''
#mycursor.execute('ALTER TABLE Test ADD COLUMN food VARCHAR(50) NOT NULL')

#mycursor.execute("SELECT id, name FROM Test WHERE gender = 'F' ORDER BY id DESC")
#for x in mycursor:
#    print(x)
'''DROP = delete'''
#mycursor.execute('ALTER TABLE Test DROP food')

'''after CHANGE you must write current name of table and then name of table that you want now and at end specify type'''
#mycursor.execute("ALTER TABLE Test CHANGE name first_name VARCHAR(50)")
#mycursor.execute('DESCRIBE Test')
#for x in mycursor:
#    print(x)

users  = [('tim', 'techwithtim'),
          ('joe', 'joey'),
          ('sarah', 'sarah1234')]

user_scores = [(45, 100),
               (30, 200),
               (46, 124)]

#Q1 = 'CREATE TABLE Users (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), passwd VARCHAR(50))'
#Q2 = 'CREATE TABLE Scores (userId int PRIMARY KEY, FOREIGN KEY(userId) REFERENCES Users(id), game1 int DEFAULT 0, game2 int DEFAULT 0)'
#mycursor.execute(Q1)
#mycursor.execute(Q2)

'''how executemany works:'''
#mycursor.executemany("Insert INTO Users (name, passwd) VALUES (%s, %s)", users)


Q3 = "Insert INTO Users (name, passwd) VALUES (%s, %s)"
Q4 = "Insert INTO Scores (userId, game1, game2) VALUES (%s, %s, %s)"
for x, user in enumerate(users):
    mycursor.execute(Q3, user)
    last_id = mycursor.lastrowid
    mycursor.execute(Q4, (last_id,) + user_scores[x])
db.commit()

mycursor.execute('SELECT * FROM Users')
for x in mycursor:
    print(x)
