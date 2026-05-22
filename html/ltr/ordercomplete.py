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
form=cgi.FieldStorage()
status=form.getvalue("status")
query=f"""SELECT ordermaster.id ,ordermaster.order_date,ordermaster.status,ordermaster.total_amount,
          order_detalis.ProductName,order_detalis.price,order_detalis.quantity,order_detalis.image,order_detalis.total
          FROM ordermaster INNER JOIN order_detalis ON ordermaster.id=order_detalis.id
          WHERE ordermaster.status='completed'"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchall()
print(myresult)
tr_html=''
for x in myresult:
    tr_html+=f'''
         <tr>
          <td>{x[0]}</td>
          <td>{x[4]}</td>
          <td>{x[1]}</td>
          <td>{x[3]}</td>
          <td>{x[2]}</td>
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

