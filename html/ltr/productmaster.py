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
    database="grocery"
)

mycursor = mydb.cursor()
query=f"""SELECT   Name FROM categary"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchall()
#print(myresult)
options_html='<option value="">Select Category Name</option>\n'
for x in myresult:
    Name=x[0]
    options_html+=f'<option value="{Name}">{Name}</option>\n'
import header
print(f"""
<!-- ============================================================== -->
        <!-- End Left Sidebar - style you can find in sidebar.scss  -->
        <!-- ============================================================== -->
        <!-- ============================================================== -->
        <!-- Page wrapper  -->
        <!-- ============================================================== -->
        <div class="page-wrapper">
            <!-- ============================================================== -->
            <!-- Bread crumb and right sidebar toggle -->
            <!-- ============================================================== -->
            <div class="page-breadcrumb">
                <div class="row">
                    <div class="col-5 align-self-center">
                        <h4 class="page-title">Employee master</h4>
                        <div class="d-flex align-items-center">
                            <nav aria-label="breadcrumb">
                                
                            </nav>
                        </div>
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
                                <h4 class="card-title">Employee form</h4>
                            
                                 <form class="m-t-30" action="ProductMasterBackend.py" method="POST" enctype="multipart/form-data">
                                    <div class="form-group">
                                        <label for="exampleInputEmail1">Image</label>
                                        <input type="file" class="form-control" id="Photo" name="Photo" aria-describedby="emailHelp" placeholder="Upload photo">
                                       
                                    </div>
                                    <div class="form-group">
                                        <label for="exampleInputPassword1">Name</label>
                                        <input type="text" class="form-control" id="Name" name="Name" placeholder="Enter Product Name">
                                    </div>
                                        <div class="form-group">
                                        <label for="exampleInputPassword1">Select Product Category</label>
                                        <select name="CategoryName" id="CategoryName" class="form-control">
                                        {options_html}
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="exampleInputPassword1">Price</label>
                                        <input type="text" class="form-control" id="Price" name="Price"  placeholder="Enter Product Price">
                                    </div>
                                     <div class="form-group">
                                        <label for="exampleInputPassword1">discription</label>
                                        <input type="text" class="form-control" id="discription" name="discription" placeholder="Enter Product Description">
                                    </div>
                                   <div class="form-group">
                                        <label for="exampleInputPassword1">Select deals of day</label>
                                        <select name="dealsofday" id="dealsofday" class="form-control">
                                            <option>Select</option>
                                            <option value="1">Yes</option>
                                             <option value="0">No</option>
                                        </select>
                                    </div>
                                   
                                    <button type="submit" class="btn btn-primary">Submit</button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- row -->
                <!-- .row -->
                
                      
                </div>
                <!-- Row -->
                <!-- ============================================================== -->
                <!-- End PAge Content -->
                <!-- ============================================================== -->
                <!-- ============================================================== -->
                <!-- Right sidebar -->
                <!-- ============================================================== -->
                <!-- .right-sidebar -->
                <!-- ============================================================== -->
                <!-- End Right sidebar -->
                <!-- ============================================================== -->
            </div>
            <!-- ============================================================== -->
            <!-- End Container fluid  -->
            <!-- ============================================================== -->
            <!-- ============================================================== -->
            <!-- footer -->
            <!-- ============================================================== -->
            """)
import footer