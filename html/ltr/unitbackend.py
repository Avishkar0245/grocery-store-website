#!C:/Python312/python.exe
import cgi 
import cgitb 
cgitb.enable() 
print("Content-Type:text/html\n")
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="grocery"
)
mycursor = mydb.cursor()
form=cgi.FieldStorage()
#print(form)
unit=form.getvalue("unit")
description=form.getvalue("description")

query=f"""INSERT INTO unitmaster(unit,description)VALUES('{unit}','{description}')"""
#print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert(" message sed  Successfully!");
    location.href="unitmaster.py";
    </script>''')