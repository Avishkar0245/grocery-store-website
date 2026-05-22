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
userid=form.getvalue("userid")
#print(userid)
status=("Pending")
query=f"""SELECT * FROM cart WHERE userid='{userid}'"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchall()
print(myresult)
grand_total=0
for x in myresult:
    price=int(x[3])
    quantity=int(x[6])
    grand_total+=price * quantity
query1=f"""INSERT INTO ordermaster (userid,total_amount,status) VALUES ('{userid}','{grand_total}','{status}')"""
#print(query1)
mycursor.execute(query1)
order_id=mycursor.lastrowid
for x in myresult:
    product_id=x[1]
    ProductName=x[2]
    image=x[4]
    price=int(x[5])
    quantity=int(x[6])
    total= price * quantity
    query2=f"""INSERT INTO order_detalis(order_id,product_id,ProductName,image,price,quantity,total) VALUES('{order_id}','{product_id}','{ProductName}','{image}','{price}','{quantity}','{total}')"""
    #print(query2)
    mycursor.execute(query2)
query3=f"""DELETE FROM cart WHERE userid='{userid}'"""
mycursor.execute(query3)
mydb.commit()
print(f'''
    <script>
    localStorage.clear(); alert("order placed Successfully!");
    location.href="product.py";
    </script>''')