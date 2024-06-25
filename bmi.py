import sqlite3

conn= sqlite3.connect('bmi.db')
cursor=conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usersBmi(
               id INTEGER PRIMARY KEY,
               name TEXT,
               age INTEGER,
               weight FLOAT,
               height FLOAT,
               bmi FLOAT
    )
''')

           

def bms ():
    name= input ("Please insert your name: ")
    try:
        age = int(input (f"How old are you {name}? "))
    except ValueError:
        print ("Invalid input, please insert numeric values.")
        return
    try: 
        weight =  float(input ("Please insert your weight in (kg): "))
        height =  float(input ("Please insert your height in (m): "))
    
    except ValueError:
        print ("Invalid input, please insert numeric values.")
        return
    
    bmi = weight/(height**2)

    # Insert user data into the table
    cursor.execute('INSERT INTO usersBmi ( name, age, weight, height, bmi) VALUES ( ?, ?, ?,?,?)',
                       ( name, age, weight, height, bmi))

    conn.commit()
    print(f"User '{name}' added successfully!")
    if bmi<18.4:
        return print(f'Your body mass is {bmi:.2f} and you are under weight')
    elif 18.5<bmi<24.9:
        return print(f'Your body mass is {bmi:.2f} and it is normal')
    elif 25<bmi<39.9:
        return print(f'Your body mass is {bmi:.2f} and you are over weight')
    else:
        return print(f'Your body mass is {bmi:.2f} and you are obese. You need to be checked by a doctor.')
   
def updateUser ():
    uName = input ( "Which name do you want to update? ")
    cursor.execute ("SELECT id FROM usersBmi WHERE name=?",(uName,))
    result = cursor.fetchone()
    if result:
        userId =result [0]
        newUserName = input(f"Enter the new name for user ID {userId}: ")
        cursor.execute("UPDATE usersBmi SET name=? WHERE id = ?", (newUserName, userId))
        conn.commit()
        print(f"User name updated successfully for user ID {userId}!")
    else:
        print(f"No user found with the name '{uName}'.")


bms ()


def removeUser ():
    cursor.execute("DELETE FROM usersBmi WHERE name = 'Zhack'")
    conn.commit()

updateUser()

if conn:
    conn.close()
    print("Database connection closed")
