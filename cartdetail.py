#!C:/Python312/python.exe
import cgi 
import cgitb 
cgitb.enable() 
#print("Content-Type:text/html\n")
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="grocery")
#print(mydb)
mycursor=mydb.cursor()
form=cgi.FieldStorage()
#print(form)
userid=form.getvalue("userid")
#print(userid)
query=f"""SELECT * FROM cart WHERE userid='{userid}'"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchall()
#print(myresult)
tr_html=''
grand_total=0
for x in myresult:
    price=int(x[3])
    quantity=int(x[6])
    total=price*quantity
    grand_total+=total
    tr_html+=f"""
    <tr>
                                        
                                        <td><img src="html/ltr/Product/{x[1]}/{x[4]}" style="width:100px"></td>
                                        <td>{x[2]}</td>
                                        <td>{x[3]}</td>
                                        <td>{x[6]}</td>
                                        <td>{total}</td>
                                        <td><a href="deletecartitem.py?id={x[0]}"><button class="cancel-btn"><i class="far fa-times"></i>Delete Item</button></a></td>
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
                    <div class="col-lg-9 col-md-12 col-sm-12 content-side">
                       
                        <div class="table-outer mb_30">
                            <table class="cart-table">
                                <thead class="cart-header">
                                    <tr>
                                        <th>Product image</th>
                                        <th>Product Name</th>
                                        <th>Price</th>
                                        <th>Quantity</th>
                                        <th>Total</th>
                                        <th>Remove</th>
                                       
                                    </tr>    
                                </thead>
                                <tbody>
                                    {tr_html}

                                </tbody>    
                            </table>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-12 col-sm-12 sidebar-side">
                        <div class="total-cart mb_30">
                           
                            <div class="shipping-cost mb_40">
                                <h4>Shipping</h4>
                                <ul class="cost-list">
                                    <li>
                                        <div class="check-box">
                                            <input class="check" type="radio" id="checkbox1" name="same" checked>
                                            <label for="checkbox1">Free Shipping</label>
                                        </div>
                                        <span class="price">00.00</span>
                                    </li>
                                    
                                    
                                </ul>
                            </div>
                            
                            <div class="total-box">
                                <h4>Total</h4>
                                <h5>{grand_total} Rs/-</h5>
                            </div>
                            <div class="btn-box">
                                <a href="checkout.py?userid={userid}"><button class="theme-btn btn-one" type="button">Proceed to Checkout</button></a>
                            </div>
                        </div>
                    </div>
                </div>
                
            </div>
        </section>
        <!-- cart section end -->""")
import footer