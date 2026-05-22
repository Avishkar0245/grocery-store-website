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
query=f"""SELECT * FROM regestration"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchall()
#print(myresult)
tr_html=''
for x in myresult:
    tr_html+=f'''
     <tr>
         
          <td>{x[0]}</td>
          <td>{x[1]}</td>
          <td>{x[2]}</td>
          <td>{x[3]}</td>
          <td>{x[4]}</td>
           <td>{x[5]}</td>
             <td>{x[6]}</td>
          
      
        </tr>'''
print(f"""
<div class="page-wrapper">
           
            <div class="page-breadcrumb">
                <div class="row">
                    <div class="col-5 align-self-center">
                        <h4 class="page-title">USER Master</h4>
                    </div>
                </div>
            </div>
            <div class="container-fluid">
             
                <div class="row">
                    <div class="col-12">
                        <div class="card">
                            <div class="card-body">
                                <h4 class="card-title">user Table</h4>
                                <div class="table-responsive">
                                    <table class="table">
                                        <thead>
                                            <tr>
                                             
                                                 <th scope="col">Sr.s</th>
                                                <th scope="col">First Name</th>
                                                <th scope="col">MIddle Name</th>
                                                  <th scope="col">Last Name</th>
                                                <th scope="col">Email</th>
                                                <th scope="col">Phone No</th>
                                                 <th scope="col">password</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                                  {tr_html}
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                    </div>
                </div>
            </div>
        </div>""")
import footer