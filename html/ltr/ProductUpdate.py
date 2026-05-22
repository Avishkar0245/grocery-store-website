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
discription=form.getvalue("discription")
Price=form.getvalue("Price")
dealsofday=form.getvalue("dealsofday")
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="grocery")
#print("mydb")
mycursor=mydb.cursor()
query=f"""UPDATE products set 
Name='{Name}',Price='{Price}',discription='{discription}',dealsofday='{dealsofday}' WHERE id='{id}'"""
#print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert(" product Update Successfully!");
    location.href="productList.py";
    </script>''')