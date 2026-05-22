#!C:/Python312/python.exe
import cgi 
import cgitb 
cgitb.enable() 
print("Content-Type:text/html\n")

import mysql.connector
import os 

form = cgi.FieldStorage()

Name = form.getvalue("Name") or ""
Price = form.getvalue("Price") or ""
discription = form.getvalue("discription") or ""
CategoryName =form.getvalue("CategoryName") or ""
dealsofday=form.getvalue("dealsofday") or ""

fi = form["Photo"] if "Photo" in form else None

UploadFileName = ""

# FILE CHECK
if fi is not None and fi.filename:
    fn = os.path.splitext(fi.filename)
    UploadFileName = 'abc' + fn[1]

# DATABASE
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="grocery"
)

mycursor = mydb.cursor()

query=f"""INSERT INTO products (Name,CategoryName,Price,discription,image,dealsofday)VALUES('{Name}','{CategoryName}','{Price}','{discription}','{UploadFileName}','{dealsofday}')"""

mycursor.execute(query)
mydb.commit()

pro_id = mycursor.lastrowid

# FILE SAVE
if fi is not None and fi.filename:
    upload_dir = f"Product/{pro_id}"
    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, UploadFileName)
    
    with open(file_path, 'wb') as f:
        f.write(fi.file.read())

# SUCCESS
print('''
<script>
alert("Product Added Successfully!");
location.href="productList.py";
</script>''')