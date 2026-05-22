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
    database="grocery")
mycursor=mydb.cursor()
form=cgi.FieldStorage()
#print(form)
id=form.getvalue("id")
#print(id)
query=f"""UPDATE ordermaster SET status="completed" WHERE id='{id}'"""
#print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>
    localStorage.clear(); alert("order Accept Successfully!");
    location.href="ordermaster.py";
    </script>''')