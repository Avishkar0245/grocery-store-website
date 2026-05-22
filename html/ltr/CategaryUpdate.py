#!C:/Python312/python.exe
import cgi 
import cgitb 
cgitb.enable() 
print("Content-Type:text/html\n")
import mysql.connector
form=cgi.FieldStorage()
#print(form)
id=form.getvalue("id")
Name=form.getvalue("Name")
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="grocery")
#print("mydb")
mycursor=mydb.cursor()
query=f"""UPDATE categary set 
Name='{Name}' WHERE id='{id}'"""
#print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert(" product Update Successfully!");
    location.href="categaryList.py";
    </script>''')