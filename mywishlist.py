#!C:/Python312/python.exe
import cgi 
import cgitb 
cgitb.enable() 
print("Contant-Type:text/html\n")
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="grocery"
)
mycursor = mydb.cursor()
form = cgi.FieldStorage()
#print(form)
userid = form.getvalue('userid')
productid = form.getvalue('proid')
query = f"""INSERT into wishlist (userid,productid)VALUES('{userid}','{productid}')"""
#print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert(" product add to wishlist Successfully!");
    location.href="product.py";
    </script>''')