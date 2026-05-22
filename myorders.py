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
    database="grocery"
)
mycursor = mydb.cursor()
form=cgi.FieldStorage()
userid=form.getvalue("userid")
query=f"""SELECT ordermaster.id ,ordermaster.order_date,ordermaster.status,
          order_detalis.ProductName,order_detalis.price,order_detalis.quantity,order_detalis.image,order_detalis.total
          FROM ordermaster INNER JOIN order_detalis ON ordermaster.id=order_detalis.id
          WHERE ordermaster.userid='{userid}'"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchall()
#print(myresult)
tr_html=''
for x in myresult:
    color="black"
    if x[2]=="Pending":
        color="red"
    elif x[2]=="completed":
        color="green"
    tr_html+=f"""
    <tr>
                                        
                                        <td><img src="html/ltr/Product/{x[0]}/{x[6]}" style="width:100px"></td>
                                        <td>{x[3]}</td>
                                        <td>{x[4]}</td>
                                        <td>{x[5]}</td>
                                        <td>{x[7]}</td>
                                        <td style="color:{color}"; font-weight:bold;>{x[2]}</td>
                                    </tr>
                                      """
import header
print(f"""
 <head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0">

<title>Kiddex - HTML 5 Template Preview</title>

<!-- Fav Icon -->
<link rel="icon" href="assets/images/favicon.ico" type="image/x-icon">

<!-- Google Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,200..1000;1,200..1000&amp;display=swap" rel="stylesheet">

<!-- Stylesheets -->
<link href="assets/css/font-awesome-all.css" rel="stylesheet">
<link href="assets/css/flaticon.css" rel="stylesheet">
<link href="assets/css/owl.css" rel="stylesheet">
<link href="assets/css/bootstrap.css" rel="stylesheet">
<link href="assets/css/jquery.fancybox.min.css" rel="stylesheet">
<link href="assets/css/animate.css" rel="stylesheet">
<link href="assets/css/nice-select.css" rel="stylesheet">
<link href="assets/css/elpath.css" rel="stylesheet">
<link href="assets/css/jquery-ui.css" rel="stylesheet">
<link href="assets/css/color.css" id="jssDefault" rel="stylesheet">
<link href="assets/css/rtl.css" rel="stylesheet">
<link href="assets/css/style.css" rel="stylesheet">
<link href="assets/css/module-css/header.css" rel="stylesheet">
<link href="assets/css/module-css/page-title.css" rel="stylesheet">
<link href="assets/css/module-css/cart.css" rel="stylesheet">
<link href="assets/css/module-css/cta.css" rel="stylesheet">
<link href="assets/css/module-css/popular-product.css" rel="stylesheet">
<link href="assets/css/module-css/subscribe.css" rel="stylesheet">
<link href="assets/css/module-css/footer.css" rel="stylesheet">
<link href="assets/css/responsive.css" rel="stylesheet">

</head>


        <!-- page-title -->
        <section class="page-title pt_40 pb_30">
            <div class="large-container">
                <ul class="bread-crumb clearfix">
                    <li><a href="index.html">Home</a></li>
                    <li>Cart</li>
                </ul>
            </div>
        </section>
        <!-- page-title -->


        <!-- cart section -->
        <section class="cart-section pb_150">
            <div class="large-container">
                <div class="sec-title centred pb_30">
                    <h2>Your <span>Cart</span></h2>
                </div>
                <div class="row clearfix">
                    <div class="col-lg-12 col-md-12 col-sm-12 content-side">
                       
                        <div class="table-outer mb_30">
                            <table class="cart-table">
                                <thead class="cart-header">
                                    <tr>
                                        <th>Product image</th>
                                        <th>Product Name</th>
                                        <th>Price</th>
                                        <th>Quantity</th>
                                        <th>Total</th>
                                        <th>Status</th>
                                       
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
        </section>
        <!-- cart section end -->""")
import footer
