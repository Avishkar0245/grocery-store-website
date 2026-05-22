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
    database="grocery"
)
mycursor = mydb.cursor()
form=cgi.FieldStorage()
#print(form)
userid=form.getvalue("userid")
#print(userid)
query=f"""SELECT * FROM regestration WHERE id='{userid}'"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchone()
#print(myresult)
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
<link href="assets/css/odometer.css" rel="stylesheet">
<link href="assets/css/jquery-ui.css" rel="stylesheet">
<link href="assets/css/color.css" id="jssDefault" rel="stylesheet">
<link href="assets/css/rtl.css" rel="stylesheet">
<link href="assets/css/style.css" rel="stylesheet">
<link href="assets/css/module-css/header.css" rel="stylesheet">
<link href="assets/css/module-css/page-title.css" rel="stylesheet">
<link href="assets/css/module-css/login.css" rel="stylesheet">
<link href="assets/css/module-css/subscribe.css" rel="stylesheet">
<link href="assets/css/module-css/footer.css" rel="stylesheet">
<link href="assets/css/responsive.css" rel="stylesheet">

</head>




        <!-- mobile menu  -->
        <div class="mobile-menu">
            <div class="menu-backdrop"></div>
            
            
                
        </div>
        <!-- end mobile menu -->


        <!-- category menu  -->
        <div class="category-menu">
            <div class="menu-backdrop"></div>
            <div class="outer-box">
                <div class="side-content">
                    <div class="close-btn"><i class="far fa-times"></i></div>
                    <ul class="option-list">
                        <li><button type="button"><i class="far fa-heart"></i></button></li>
                        <li class="shop-cart cart-toggler"><button type="button"><i class="far fa-shopping-bag"></i></button></li>
                        <li><a href="login.html"><i class="far fa-user"></i></a></li>
                    </ul>
                    <ul class="social-links">
                        <li><a href="index-3.html"><i class="icon-14"></i></a></li>
                        <li><a href="index-3.html"><i class="icon-15"></i></a></li>
                        <li><a href="index-3.html"><i class="icon-16"></i></a></li>
                        <li><a href="index-3.html"><i class="icon-17"></i></a></li>
                    </ul>
                </div>
                <div class="category-box">
                    <div class="search-form">
                        <form action="https://azim.hostlin.com/Kiddex/shop.html" method="get">
                            <div class="form-group">
                                <input type="search" name="search-field" placeholder="Search Product" required> 
                                <button type="submit"><i class="icon-4"></i></button>
                            </div>
                        </form>
                    </div>
                    <ul class="category-list product-category clearfix">
                        <li class="category-dropdown"><a href="#">Animal Toys</a>
                            <div class="image"><img src="assets/images/icons/category-1.png" alt=""></div>
                           <ul>
                                <li><a href="shop-details.html">Bowling</a></li>
                                <li><a href="shop-details.html">Hopscotch</a></li>
                                <li><a href="shop-details.html">Balance Beam</a></li>
                                <li><a href="shop-details.html">Build a Fort</a></li>
                                <li><a href="shop-details.html">Video Gamens</a></li>
                                <li><a href="shop-details.html">Musical Chair</a></li>
                                <li><a href="shop-details.html">Hot Potato</a></li>
                                <li><a href="shop-details.html">Simon Says</a></li>
                                <li><a href="shop-details.html">Treasure Hunt</a></li>
                                <li><a href="shop-details.html">Charades</a></li>
                            </ul>
                        </li>
                        <li class="category-dropdown"><a href="#">Indoor Games</a>
                            <div class="image"><img src="assets/images/icons/category-2.png" alt=""></div>
                            <ul>
                                <li><a href="shop-details.html">Bowling</a></li>
                                <li><a href="shop-details.html">Hopscotch</a></li>
                                <li><a href="shop-details.html">Balance Beam</a></li>
                                <li><a href="shop-details.html">Build a Fort</a></li>
                                <li><a href="shop-details.html">Video Gamens</a></li>
                                <li><a href="shop-details.html">Musical Chair</a></li>
                                <li><a href="shop-details.html">Hot Potato</a></li>
                                <li><a href="shop-details.html">Simon Says</a></li>
                                <li><a href="shop-details.html">Treasure Hunt</a></li>
                                <li><a href="shop-details.html">Charades</a></li>
                            </ul>
                        </li>
                        <li class="category-dropdown"><a href="#">Music Instrument</a>
                            <div class="image"><img src="assets/images/icons/category-3.png" alt=""></div>
                            <ul>
                                <li><a href="shop-details.html">Bowling</a></li>
                                <li><a href="shop-details.html">Hopscotch</a></li>
                                <li><a href="shop-details.html">Balance Beam</a></li>
                                <li><a href="shop-details.html">Build a Fort</a></li>
                                <li><a href="shop-details.html">Video Gamens</a></li>
                                <li><a href="shop-details.html">Musical Chair</a></li>
                                <li><a href="shop-details.html">Hot Potato</a></li>
                                <li><a href="shop-details.html">Simon Says</a></li>
                                <li><a href="shop-details.html">Treasure Hunt</a></li>
                                <li><a href="shop-details.html">Charades</a></li>
                            </ul>
                        </li>
                        <li class="category-dropdown"><a href="#">Kids Dolls</a>
                            <div class="image"><img src="assets/images/icons/category-4.png" alt=""></div>
                            <ul>
                                <li><a href="shop-details.html">Bowling</a></li>
                                <li><a href="shop-details.html">Hopscotch</a></li>
                                <li><a href="shop-details.html">Balance Beam</a></li>
                                <li><a href="shop-details.html">Build a Fort</a></li>
                                <li><a href="shop-details.html">Video Gamens</a></li>
                                <li><a href="shop-details.html">Musical Chair</a></li>
                                <li><a href="shop-details.html">Hot Potato</a></li>
                                <li><a href="shop-details.html">Simon Says</a></li>
                                <li><a href="shop-details.html">Treasure Hunt</a></li>
                                <li><a href="shop-details.html">Charades</a></li>
                            </ul>
                        </li>
                        <li class="category-dropdown"><a href="#">Baby Toys</a>
                            <div class="image"><img src="assets/images/icons/category-5.png" alt=""></div>
                            <ul>
                                <li><a href="shop-details.html">Bowling</a></li>
                                <li><a href="shop-details.html">Hopscotch</a></li>
                                <li><a href="shop-details.html">Balance Beam</a></li>
                                <li><a href="shop-details.html">Build a Fort</a></li>
                                <li><a href="shop-details.html">Video Gamens</a></li>
                                <li><a href="shop-details.html">Musical Chair</a></li>
                                <li><a href="shop-details.html">Hot Potato</a></li>
                                <li><a href="shop-details.html">Simon Says</a></li>
                                <li><a href="shop-details.html">Treasure Hunt</a></li>
                                <li><a href="shop-details.html">Charades</a></li>
                            </ul>
                        </li>
                        <li class="category-dropdown"><a href="#">Vehicle Toys</a>
                            <div class="image"><img src="assets/images/icons/category-6.png" alt=""></div>
                            <ul>
                                <li><a href="shop-details.html">Bowling</a></li>
                                <li><a href="shop-details.html">Hopscotch</a></li>
                                <li><a href="shop-details.html">Balance Beam</a></li>
                                <li><a href="shop-details.html">Build a Fort</a></li>
                                <li><a href="shop-details.html">Video Gamens</a></li>
                                <li><a href="shop-details.html">Musical Chair</a></li>
                                <li><a href="shop-details.html">Hot Potato</a></li>
                                <li><a href="shop-details.html">Simon Says</a></li>
                                <li><a href="shop-details.html">Treasure Hunt</a></li>
                                <li><a href="shop-details.html">Charades</a></li>
                            </ul>
                        </li>
                        <li class="category-dropdown"><a href="#">Color Plates</a>
                            <div class="image"><img src="assets/images/icons/category-7.png" alt=""></div>
                            <ul>
                                <li><a href="shop-details.html">Bowling</a></li>
                                <li><a href="shop-details.html">Hopscotch</a></li>
                                <li><a href="shop-details.html">Balance Beam</a></li>
                                <li><a href="shop-details.html">Build a Fort</a></li>
                                <li><a href="shop-details.html">Video Gamens</a></li>
                                <li><a href="shop-details.html">Musical Chair</a></li>
                                <li><a href="shop-details.html">Hot Potato</a></li>
                                <li><a href="shop-details.html">Simon Says</a></li>
                                <li><a href="shop-details.html">Treasure Hunt</a></li>
                                <li><a href="shop-details.html">Charades</a></li>
                            </ul>
                        </li>
                        <li class="category-dropdown"><a href="#">Cloth Accessories</a>
                            <div class="image"><img src="assets/images/icons/category-8.png" alt=""></div>
                            <ul>
                                <li><a href="shop-details.html">Bowling</a></li>
                                <li><a href="shop-details.html">Hopscotch</a></li>
                                <li><a href="shop-details.html">Balance Beam</a></li>
                                <li><a href="shop-details.html">Build a Fort</a></li>
                                <li><a href="shop-details.html">Video Gamens</a></li>
                                <li><a href="shop-details.html">Musical Chair</a></li>
                                <li><a href="shop-details.html">Hot Potato</a></li>
                                <li><a href="shop-details.html">Simon Says</a></li>
                                <li><a href="shop-details.html">Treasure Hunt</a></li>
                                <li><a href="shop-details.html">Charades</a></li>
                            </ul>
                        </li>
                        <li class="category-dropdown"><a href="#">Water Games</a>
                            <div class="image"><img src="assets/images/icons/category-9.png" alt=""></div>
                            <ul>
                                <li><a href="shop-details.html">Bowling</a></li>
                                <li><a href="shop-details.html">Hopscotch</a></li>
                                <li><a href="shop-details.html">Balance Beam</a></li>
                                <li><a href="shop-details.html">Build a Fort</a></li>
                                <li><a href="shop-details.html">Video Gamens</a></li>
                                <li><a href="shop-details.html">Musical Chair</a></li>
                                <li><a href="shop-details.html">Hot Potato</a></li>
                                <li><a href="shop-details.html">Simon Says</a></li>
                                <li><a href="shop-details.html">Treasure Hunt</a></li>
                                <li><a href="shop-details.html">Charades</a></li>
                            </ul>
                        </li>
                        <li class="category-dropdown"><a href="#">Paper Toys</a>
                            <div class="image"><img src="assets/images/icons/category-10.png" alt=""></div>
                            <ul>
                                <li><a href="shop-details.html">Bowling</a></li>
                                <li><a href="shop-details.html">Hopscotch</a></li>
                                <li><a href="shop-details.html">Balance Beam</a></li>
                                <li><a href="shop-details.html">Build a Fort</a></li>
                                <li><a href="shop-details.html">Video Gamens</a></li>
                                <li><a href="shop-details.html">Musical Chair</a></li>
                                <li><a href="shop-details.html">Hot Potato</a></li>
                                <li><a href="shop-details.html">Simon Says</a></li>
                                <li><a href="shop-details.html">Treasure Hunt</a></li>
                                <li><a href="shop-details.html">Charades</a></li>
                            </ul>
                        </li>
                        <li class="category-dropdown"><a href="#">Video Games</a>
                            <div class="image"><img src="assets/images/icons/category-11.png" alt=""></div>
                            <ul>
                                <li><a href="shop-details.html">Bowling</a></li>
                                <li><a href="shop-details.html">Hopscotch</a></li>
                                <li><a href="shop-details.html">Balance Beam</a></li>
                                <li><a href="shop-details.html">Build a Fort</a></li>
                                <li><a href="shop-details.html">Video Gamens</a></li>
                                <li><a href="shop-details.html">Musical Chair</a></li>
                                <li><a href="shop-details.html">Hot Potato</a></li>
                                <li><a href="shop-details.html">Simon Says</a></li>
                                <li><a href="shop-details.html">Treasure Hunt</a></li>
                                <li><a href="shop-details.html">Charades</a></li>
                            </ul>
                        </li>
                        <li class="category-dropdown"><a href="#">Outdoor Games</a>
                            <div class="image"><img src="assets/images/icons/category-12.png" alt=""></div>
                            <ul>
                                <li><a href="shop-details.html">Bowling</a></li>
                                <li><a href="shop-details.html">Hopscotch</a></li>
                                <li><a href="shop-details.html">Balance Beam</a></li>
                                <li><a href="shop-details.html">Build a Fort</a></li>
                                <li><a href="shop-details.html">Video Gamens</a></li>
                                <li><a href="shop-details.html">Musical Chair</a></li>
                                <li><a href="shop-details.html">Hot Potato</a></li>
                                <li><a href="shop-details.html">Simon Says</a></li>
                                <li><a href="shop-details.html">Treasure Hunt</a></li>
                                <li><a href="shop-details.html">Charades</a></li>
                            </ul>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
        <!-- category menu end -->


        <!-- page-title -->
       <section class="page-title pt_40 pb_30">
            <div class="large-container">
                <ul class="bread-crumb clearfix">
                    <li><a href="index.html">Home</a></li>
                    <li>MyProfile</li>
                </ul>
            </div>
        </section>
        <!-- page-title -->


        <!-- sign-section -->
        <section class="sign-section pb_120">
            <div class="large-container">
                <div class="sec-title centred pb_30">
                    <h2>MY <span style="color:#ef6008;">Account</span></h2>
                </div>
                <div class="form-inner">
                    <form method="post" action="myprofilebackend.py">
                        <div class="form-group">
                            <label>id</label>
                            <input type="text" name="id" id="id" value="{myresult[0]}" readonly>
                        </div>
                         <div class="form-group">
                            <label>First Name</label>
                            <input type="text" name="FirstName" id="FirstName" value="{myresult[1]}" readonly>
                        </div>
                        <div class="form-group">
                            <label>Middle Name</label>
                            <input type="text" name="MiddleName" id="MiddleName" value="{myresult[2]}" readonly>
                        </div>
                        <div class="form-group">
                            <label>Last Name</label>
                            <input type="text" name="LastName" id="LastName" value="{myresult[3]}" readonly>
                        </div>
                        <div class="form-group">
                            <label>Email</label>
                            <input type="email" name="Email" id="Email" value="{myresult[4]}" readonly>
                        </div>
                        <div class="form-group">
                            <label>Phone</label>
                            <input type="text" name="Phone" id="Phone" value="{myresult[5]}"  >
                        </div>
                        <div class="form-group">
                            <label>Address</label>
                            <input type="text" name="address" id="address" value="{myresult[5]}" >
                        </div>
                        
                        <div class="form-group">
                            <label>Password</label>
                            <input type="password" name="Password" id="Password" value="{myresult[6]}">
                        </div>
                        <div class="form-group message-btn">
                            <button type="submit" class="theme-btn" style="background-color:#ef6008;"">UPDATE ACCOUNT</button>
                        </div>
                        
                    </form>
                    <div class="other-option">
                        <div class="check-box-two">
                            <input class="check" type="checkbox" id="checkbox1">
                            <label for="checkbox1">Remember me</label>
                        </div>
                    </div>
                   
                </div>
            </div>
        </section>
        <!-- sign-section end -->
      
""")
import footer