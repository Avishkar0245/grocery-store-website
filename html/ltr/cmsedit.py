#!C:/Python312/python.exe
import cgi 
import cgitb 
cgitb.enable() 
#print("Content-Type:text/html\n")
import header
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="grocery")
#print(mydb)
mycursor=mydb.cursor()
form=cgi.FieldStorage()
id=form.getvalue("id")
#print(id)
query=f"""SELECT* FROM cms WHERE id={id}"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchone()
#print(myresult)
print(f"""
<div class="page-wrapper">
            <div class="page-breadcrumb">
                <div class="row">
                    <div class="col-5 align-self-center">
                        <h4 class="page-title">Categary Master</h4>
                
                    </div>
                   
                </div>
            </div>
            <!-- ============================================================== -->
            <!-- End Bread crumb and right sidebar toggle -->
            <!-- ============================================================== -->
            <!-- ============================================================== -->
            <!-- Container fluid  -->
            <!-- ============================================================== -->
            <div class="container-fluid">
                <!-- ============================================================== -->
                <!-- Start Page Content -->
                <!-- ============================================================== -->
                <!-- row -->
                <div class="row">
                    <div class="col-12">
                        <div class="card">
                            <div class="card-body">
                                <h4 class="card-title">CMS Form</h4>
                                <form class="m-t-30" action="cmsupdate.py" method="POST" enctype="multipart/form-data">
      
                                     <div class="form-group">
                                        <label for="exampleInputPassword1">id</label>
                                        <input type="text" class="form-control" id="id" name="id" placeholder="Enter Product Name" readonly value="{myresult[0]}">
                                    </div>
                                    
                                    <div class="form-group">
                                        <label for="exampleInputPassword1">logo</label>
                                        <input type="text" class="form-control" id="logo" name="logo" placeholder="Enter Product Name" value="{myresult[1]}">
                                    </div>
                                    
                                    <div class="form-group">
                                        <label for="exampleInputPassword1">Slogan</label>
                                        <input type="text" class="form-control" id="slogan" name="slogan"  placeholder="Enter Product Price" value="{myresult[2]}">
                                    </div>
                                     <div class="form-group">
                                        <label for="exampleInputPassword1">address</label>
                                        <input type="text" class="form-control" id="address" name="address" placeholder="Enter Product Description" value="{myresult[3]}">
                                    </div>
                                    <div class="form-group">
                                        <label for="exampleInputPassword1">phone</label>
                                        <input type="text" class="form-control" id="phone" name="phone" placeholder="Enter Product Description" value="{myresult[4]}">
                                    </div>
                                    <div class="form-group">
                                        <label for="exampleInputPassword1">email</label>
                                        <input type="text" class="form-control" id="email" name="email" placeholder="Enter Product Description" value="{myresult[5]}">
                                    </div>
                                    <div class="form-group">
                                        <label for="exampleInputPassword1">image</label>
                                        <input type="text" class="form-control" id="image" name="image" placeholder="Enter Product Description" value="{myresult[6]}">
                                    </div>
                                    <div class="form-group">
                                        <label for="exampleInputPassword1">info</label>
                                        <input type="text" class="form-control" id="info" name="info" placeholder="Enter Product Description" value="{myresult[7]}">
                                    </div>
                                   
                                    <button type="submit" class="btn btn-primary">Submit</button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>""")
import footer
