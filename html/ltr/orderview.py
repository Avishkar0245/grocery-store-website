#!C:/Python312/python.exe
import cgi 
import cgitb 
cgitb.enable() 
#print("Content-Type:text/html\n")
import header
form=cgi.FieldStorage()
#print(form)
order_id=form.getvalue("order_id")
#print(order_id)
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="grocery")
mycursor=mydb.cursor()
query=f"""SELECT * FROM order_detalis WHERE order_id='{order_id}'"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchall()
#print(myresult)
tr_html=''
for x in myresult:
    tr_html+=f'''
         <tr>
          <td>{x[3]}</td>
          <td>{x[5]}</td>
          <td>{x[6]}</td>
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
                                              
                                                
                                                <th scope="col">Product name</th>
                                                <th scope="col">price</th>
                                                  <th scope="col">quantity</th>
                                                <th scope="col">image</th>
                                           
                                                
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