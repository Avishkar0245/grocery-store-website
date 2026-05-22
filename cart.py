#!C:/Python312/python.exe
import cgi 
import cgitb 
cgitb.enable() 
print("Content-Type:text/html\n")
import mysql.connector
form=cgi.FieldStorage()
#print(form)
proid=form.getvalue("proid")
#print(proid)
ProductName=form.getvalue("ProductName")
#print(ProductName)
Price=form.getvalue("Price")
#print(Price)
Photo=form.getvalue("Photo")
#print(Photo)
userid=form.getvalue("userid")
#print(userid)
quantity=form.getvalue("quantity")
#print(quantity)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="grocery")
#print(mydb)
mycursor=mydb.cursor()
query=f"""INSERT INTO cart(proid,ProductName,Price,Photo,userid,quantity)VALUES('{proid}','{ProductName}','{Price}','{Photo}','{userid}','{quantity}')"""
#print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert(" Product Add To Cart Successfully!");
    location.href="cartdetail.py?userid={userid}";
    </script>''')