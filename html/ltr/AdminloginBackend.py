#!C:/Python312/python.exe
import cgi 
import cgitb 
cgitb.enable() 
print("Content-Type:text/html\n")
import mysql.connector
form=cgi.FieldStorage()
#print(form)
Email=form.getvalue("Email")
Password=form.getvalue("Password")
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="grocery")
mycursor=mydb.cursor()
query=f"""SELECT * FROM adminlogin WHERE Email='{Email}' AND Password='{Password}'"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchone()
#print(myresult)
#print(mycursor.rowcount)
if mycursor.rowcount==1:
    print(f'''
    <script>
          localStorage.clear();
          localStorage.setItem("id",'{myresult[0]}');
          localStorage.setItem("username",'{myresult[3]}');
          alert("Login Successfully!");
    location.href="productmaster.py";
    </script>''')
else:
     print(f'''
    <script>alert("Login Unsuccessfully!");
    location.href="AdminLogin.py";
    </script>''')
  