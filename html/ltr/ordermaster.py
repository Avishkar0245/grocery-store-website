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
query=f"""SELECT * FROM ordermaster"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchall()
#print(myresult)
tr_html=''
for x in myresult:
    tr_html+=f'''
         <tr>
          <td><a href="orderview.py?order_id={x[1]}"><button>VIEW</button>
             <td><a href="orderaccept.py?id={x[0]}"><button>Accept product</button>
          <td>{x[0]}</td>
          <td>{x[1]}</td>
          <td>{x[2]}</td>
          <td>{x[3]}</td>
          <td>{x[4]}</td>
        </tr>'''
print(f"""
<div class="page-wrapper">
           
            <div class="page-breadcrumb">
                <div class="row">
                    <div class="col-5 align-self-center">
                        <h4 class="page-title">order Master</h4>
                    </div>
                </div>
            </div>
            <div class="container-fluid">
             
                <div class="row">
                    <div class="col-12">
                        <div class="card">
                            <div class="card-body">
                                <h4 class="card-title">order Table</h4>
                                <div class="table-responsive">
                                    <table class="table">
                                        <thead>
                                            <tr>
                                                 <th>Action</th>
                                                <th></th>
                                                 <th scope="col">Sr.s</th>
                                                <th scope="col">user id</th>
                                                <th scope="col">order_date</th>
                                                  <th scope="col">total amount</th>
                                                <th scope="col">status</th>
                                           
                                                
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