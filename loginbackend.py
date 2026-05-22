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
Email=form.getvalue("Email")
Password=form.getvalue("Password")
query=f"""SELECT * FROM regestration  WHERE Email='{Email}' AND Password='{Password}'"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchone()
#print(myresult)
if mycursor.rowcount==1:
    print(f'''
    <script>
          localStorage.clear();
          localStorage.setItem("id",'{myresult[0]}');
          localStorage.setItem("FirstName",'{myresult[1]}');
          localStorage.setItem("Photo",'{myresult[8]}');
          alert("Login Successfully!");
    location.href="index.py";
    </script>''')
else:
     print(f'''
    <script>alert("Login Unsuccessfully!");
    location.href="login.py";
    </script>''')