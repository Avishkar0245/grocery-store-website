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
CustomerName=form.getvalue("CustomerName")
email=form.getvalue("email")
phone=form.getvalue("phone")
subject=form.getvalue("subject")
query=f"""INSERT INTO contact(CustomerName,email,phone,subject)VALUES('{CustomerName}','{email}','{phone}','{subject}')"""
#print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert(" message sed  Successfully!");
    location.href="contact.py";
    </script>''')