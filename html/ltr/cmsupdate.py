#!C:/Python312/python.exe
import cgi 
import cgitb 
cgitb.enable() 
print("Content-Type:text/html\n")
import mysql.connector
form=cgi.FieldStorage()
#print(form)
id=form.getvalue("id")
logo=form.getvalue("logo")
slogan=form.getvalue("slogan")
address=form.getvalue("address")
phone=form.getvalue("phone")
email=form.getvalue("email")
image=form.getvalue("image")
info=form.getvalue("info")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="grocery")
#print("mydb")
mycursor=mydb.cursor()
query=f"""UPDATE cms set 
logo='{logo}',slogan='{slogan}',address='{address}',phone='{phone}',email='{email}',image='{image}',info='{info}' WHERE id='{id}'"""
#print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert(" CMS Update Successfully!");
    location.href="cmsmaster.py";
    </script>''')