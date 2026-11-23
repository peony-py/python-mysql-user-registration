import mysql.connector
from mysql.connector import IntegrityError
from email_validator import validate_email ,EmailNotValidError
from dotenv import load_dotenv
import os
from argon2 import PasswordHasher

load_dotenv()
ph = PasswordHasher()

cnx =mysql.connector.connect(
        user = os.getenv('DB_USER'),
        host = os.getenv('DB_HOST'),
        password = os.getenv('DB_PASSWORD'),
        database = os.getenv('DB_NAME')
        )
cursor = cnx.cursor()

query_select = 'select * from users;'
query_insert = 'insert into users(username,hashed_password) values(%s,%s);'
# /////////////////////////////////////////////////////////////////////////
username = input('enter you email: ').strip()
password = input('enter your password: ')

try:
    result = validate_email(username ,check_deliverability=False)
    
except EmailNotValidError:
        print('email not valid')
        raise SystemExit(1)
else:
    username=result.normalized
    
    
if (
        len(password)<8 
        or not any(char.isdigit() for char in password)
        or not any(char.isalpha() for char in password)
     ): 
        print('invalid password')
        raise SystemExit(1)

hashed_password = ph.hash(password)
data =(username,hashed_password)

try:
    cursor.execute(query_insert,data)
    cnx.commit()
    print('registration successful!')

except IntegrityError as error:
    if error.errno==1062:
        print('username already exists!')
except mysql.connector.Error as error:
        print(f'database error: {error}')
print('connected to db')
cnx.close()