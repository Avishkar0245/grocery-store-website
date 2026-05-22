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
mycursor=mydb.cursor()
query=f"""SELECT * FROM categary"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchall()
#print(myresult)
tr_html=''
for x in myresult:
    tr_html+=f'''
        <tr>
           <td><a href="CategaryEdit.py?id={x[0]}"> <button>Edit</button></a> </td>
           <td><a href="CategaryDelete.py?id={x[0]}"><button>Delete</button>
          <td>{x[0]}</td>
          <td>{x[1]}</td>
          <td>{x[2]}</td>
    
       
        
        </tr>'''
print(f"""
<div class="page-wrapper">
            <!-- ============================================================== -->
            <!-- Bread crumb and right sidebar toggle -->
            <!-- ============================================================== -->
            <div class="page-breadcrumb">
                <div class="row">
                    <div class="col-5 align-self-center">
                        <h4 class="page-title">Categary Master</h4>
                    </div>
                </div>
            </div>
            <div class="container-fluid">
                <!-- ============================================================== -->
                <!-- Start Page Content -->
                <!-- ============================================================== -->
                <div class="row">
                    <div class="col-12">
                        <div class="card">
                            <div class="card-body">
                                <h4 class="card-title">Categary Table</h4>
                                <div class="table-responsive">
                                    <table class="table">
                                        <thead>
                                            <tr>
                                                <th> Action </th>
                                                <th> </th>
                                                <th scope="col">Sr.s</th>
                                                <th scope="col">Name</th>
                                                <th scope="col">image</th>
                                               
                                                
                                            </tr>
                                        </thead>
                                        <tbody>
                                                  {tr_html}
                                                   

                                                </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                    </div>
                </div>
            </div>
        </div>
""")
import footer