#!C:/Python312/python.exe
import cgi 
import cgitb 
import os
cgitb.enable() 
print("Content-Type:text/html\n")
import mysql.connector
form=cgi.FieldStorage()
#print(form)
FirstName=form.getvalue("FirstName")
#print(FirstName)
MiddleName=form.getvalue("MiddleName")
#print(MiddleName)
LastName=form.getvalue("LastName")
#print(LastName)
Email=form.getvalue("Email")
#print(Email)
Phone=form.getvalue("Phone")
#print(Phone)
Password=form.getvalue("Password")
#print(Password)
fi=form["Photo"]
#print(fi.filename)
fn=os.path.splitext(fi.filename)
#print(fn[0])
UploadFileName='pic'+fn[1]
#print(UploadFileName)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="grocery"
)
mycursor = mydb.cursor()
query=f"""INSERT INTO regestration (FirstName,MiddleName,LastName,Email,Phone,Password,Photo) VALUES('{FirstName}','{MiddleName}','{LastName}','{Email}','{Phone}','{Password}','{UploadFileName}')"""
#print(query)
mycursor.execute(query)
mydb.commit()
reg_id=mycursor.lastrowid
#print(reg_id)
Upload_dir=f"User/{reg_id}"
#print(Upload_dir)
os.makedirs(Upload_dir,exist_ok=True)
file_path=os.path.join(Upload_dir,UploadFileName)
open(file_path,'wb').write(fi.file.read())
print(f'''
      
    <script>
      alert("Regestration successfully!");
    location.href="login.py";
    </script>''')

