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
#print(mydb)
mycursor=mydb.cursor()
form=cgi.FieldStorage()
#print(form)
id=form.getvalue("id")
#print(id)
query=f"""DELETE FROM categary WHERE id={id}"""
#print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert(" Product Delete Successfully!");
    location.href="categaryList.py";
    </script>''')