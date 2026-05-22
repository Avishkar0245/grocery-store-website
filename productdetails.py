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
id=form.getvalue("id")
#print(id)
query=f"""SELECT * FROM products WHERE id='{id}'"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchone()
#print(myresult)
CategoryName = myresult[3]
#print(CategoryName)
query1=f"""SELECT * FROM products WHERE CategoryName='{CategoryName}'"""
#print(query1)
mycursor.execute(query1)
myresultone=mycursor.fetchall()
#print(myresultone)
tr_html=''
for x in myresultone:
    tr_html+=f"""
              <div class="shop-block-one">
                        <div class="inner-box">
                            <div class="image-box">
                                 
                                <figure class="image"><img src="html/ltr/Product/{x[0]}/{x[1]}" alt="" style="height:150px;"></figure>
                            </div>
                            <div class="lower-content">
                                <span class="text">{x[3]}</span>
                                 
                                <h4><a href="">{x[2]}</a></h4>
                                <div class="price">{x[4]} Rs</div>
                            </div>
                            
                              <a href="productdetails.py?id={x[0]}"><button class="theme-btn btn-one" type="button">Product Details</button></a>
                                        
                        </div>
                    </div>"""
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
<link href="assets/css/module-css/shop-details.css" rel="stylesheet">
<link href="assets/css/module-css/featured.css" rel="stylesheet">
<link href="assets/css/module-css/popular-product.css" rel="stylesheet">
<link href="assets/css/module-css/subscribe.css" rel="stylesheet">
<link href="assets/css/module-css/footer.css" rel="stylesheet">
<link href="assets/css/responsive.css" rel="stylesheet">

</head>
        <div class="mobile-menu">
            <div class="menu-backdrop"></div>
            <div class="close-btn"><i class="fas fa-times"></i></div>
            <nav class="menu-box">
                <div class="nav-logo"><a href="index.html"><img src="assets/images/logo.png" alt="" title=""></a></div>
                <div class="menu-outer"><!--Here Menu Will Come Automatically Via Javascript / Same Menu as in Header--></div>
                <div class="contact-info">
                    <h4>Contact Info</h4>
                    <ul>
                        <li>Chicago 12, Melborne City, USA</li>
                        <li><a href="tel:+8801682648101">+88 01682648101</a></li>
                        <li><a href="mailto:info@example.com">info@example.com</a></li>
                    </ul>
                </div>
                <div class="social-links">
                    <ul class="clearfix">
                        <li><a href="index.html"><span class="fab fa-twitter"></span></a></li>
                        <li><a href="index.html"><span class="fab fa-facebook-square"></span></a></li>
                        <li><a href="index.html"><span class="fab fa-pinterest-p"></span></a></li>
                        <li><a href="index.html"><span class="fab fa-instagram"></span></a></li>
                        <li><a href="index.html"><span class="fab fa-youtube"></span></a></li>
                    </ul>
                </div>
            </nav>
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
                
            </div>
        </div>
        <!-- category menu end -->


        <!-- shop-details -->
        <section class="shop-details pt_70 pb_120">
            <div class="large-container">
                <div class="product-details-content mb_80">
                    <div class="row clearfix">
                        <div class="col-lg-6 col-md-12 col-sm-12 image-column">
                            <div class="bxslider">
                              
                            
                               
                                 <div class="slider-content">
                                    <div class="image-inner">
                                        <div class="image-box">
                                            <figure class="image"><a href="html/ltr/product/{myresult[0]}/{myresult[1]}" class="lightbox-image" data-fancybox="gallery"><img src="html/ltr/product/{myresult[0]}/{myresult[1]}" alt=""></a></figure>
                                        </div>
                                        <div class="slider-pager">
                                            <ul class="thumb-box">
                                                <li>
                                                    <a class="active" data-slide-index="0" href="#"><figure><img src="html/ltr/product/{myresult[0]}/{myresult[1]}" alt="" style="height: 123px;"></figure></a>
                                                </li>
                                              
                                              
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-6 col-md-12 col-sm-12 content-column">
                            <div class="content-box ml_30">
                                <span class="upper-text">{myresult[2]}</span>
                                <h2>{myresult[2]}</h2>
                                <h3>{myresult[4]} Rs/-</h3>
                              <!--  <ul class="rating pb_10"> 
                                    <li><i class="icon-10"></i></li>
                                    <li><i class="icon-10"></i></li>
                                    <li><i class="icon-10"></i></li>
                                    <li><i class="icon-10"></i></li>
                                    <li><i class="icon-10"></i></li>
                                    <li><span>(5.0)</span></li>
                                </ul> -->
                                <div class="text-box mb_30">
                                    <p>{myresult[5]}</p>
                                </div>
                               
                                <form action="cart.py" method="POST">
                                <input type="hidden" id="proid" name="proid" value="{myresult[0]}">
                                <input type="hidden" id="ProductName" name="ProductName" value="{myresult[2]}">
                                <input type="hidden" id="Price" name="Price" value="{myresult[4]}">
                                <input type="hidden" id="Photo" name="Photo" value="{myresult[1]}">
                                <input type="hidden" id="userid" name="userid">
                                <div style="margin-bottom:30px">
                                <label>Enter Quantity</label>
                                <input type="text" name="quantity" id="quantity" class="form-group" style="border:1px solid black" required>
                                </div>
                       
                                
                                <div class="addto-cart-box mb_40"> 
                                    <ul class="clearfix">
                                           <a href=""><li class="cart-btn"><button type="submit" class="theme-btn btn-one">Add to cart <span></span><span></span><span></span><span></span></button></li></a>
                                    </ul>
                               </form>
                                </div>
                               
                            </div>
                        </div>
                    </div>
                </div>
                
            </div>
        </section>

        <!-- related-product -->
        <section class="related-product centred pb_90">
            <div class="large-container">
                <div class="sec-title mb_50">
                    <h2>Related <span>Products</span></h2>
                </div>
                <div class="inner-container clearfix">


                    {tr_html}
                     
                </div>
            </div>
        </section>
        <!-- related-product end -->

        <script>
        let userid=localStorage.getItem("id");
        document.getElementById("userid").value=userid;
        </script>
     
        <footer class="main-footer home-3 footer-light">
            <div class="anim-shape">
                <div class="shape-1 rotate-me" style="background-image: url(assets/images/shape/shape-5.png);"></div>
                <div class="shape-2 rotate-me" style="background-image: url(assets/images/shape/shape-5.png);"></div>
                <div class="shape-3 rotate-me" style="background-image: url(assets/images/shape/shape-5.png);"></div>
                <div class="shape-4 rotate-me" style="background-image: url(assets/images/shape/shape-5.png);"></div>
                <div class="shape-5 float-bob-y" style="background-image: url(assets/images/shape/shape-34.png);"></div>
                <div class="shape-6 float-bob-x" style="background-image: url(assets/images/shape/shape-72.png);"></div>
                <div class="shape-7 float-bob-y" style="background-image: url(assets/images/shape/shape-36.png);"></div>
            </div>
            <div class="widget-section p_relative pt_100 pb_80">
                <div class="large-container">
                    <div class="row clearfix">
                        <div class="col-lg-4 col-md-6 col-sm-12 footer-column">
                            <div class="tp-footer-widget logo-widget">
                                <figure class="footer-logo"><a href="index.html"><img src="smartphone.jpg" alt=""></a></figure>
                                <div class="support-box">
                                    <div class="icon-box"><i class="icon-2"></i></div>
                                    <div class="inner">
                                        <h3><a href="tel:912345678">8766503948</a></h3>
                                        <span>Call out Hotline 24/7</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                         <div class="col-lg-2 col-md-6 col-sm-12 footer-column">
                            <div class="tp-footer-widget links-widget">
                                <div class="widget-title">
                                    <h4>Pages</h4>
                                </div>
                                   <div class="widget-content">
                                    <ul class="links-list clearfix">
                                        <li><a href="about.html">Home</a></li>
                                        <li><a href="about.py>About Us</a></li>
                                        <li><a href="contact.py">Contact</a></li>
                                        <li><a href="product.py">Product</a></li>
                                        <li><a href="categary.py">Category</a></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-2 col-md-6 col-sm-12 footer-column">
                            <div class="tp-footer-widget links-widget">
                                <div class="widget-title">
                                    <h4>Categories</h4>
                                </div>
                                                              <div class="widget-content">
                                    <ul class="links-list clearfix">
                                        <li><a href="index.html">Vegetables</a></li>
                                        <li><a href="contact.html">Dairy & Bakery</a></li>
                                        <li><a href="index.html">Cooking Essentials</a></li>
                                        <li><a href="index.html">Fruits</a></li>
                                        <li><a href="index.html">Packaged Foods</a></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        
                           <div class="col-lg-3 col-md-6 col-sm-12 footer-column">
                            <div class="tp-footer-widget subscribe-widget">
                                <div class="widget-title">
                                    <h4>ADDRESS</h4>
                                </div>
                                <div class="widget-content">
                                   <ul class="info-list clearfix">
                                    <i>    <i class="fa-solid fa-address-book" style="color: rgb(99, 230, 190);"></i>Tulsan, tal- karad,415111, MAHARASHTRA</i>
                                         <li><i class="fa-solid fa-at" style="color: rgb(99, 230, 190);"></i><a href="mailto:info@example.com">avimore22@gmail.com</a></li>
                                       <li><i class="fa-solid fa-phone" style="color: rgb(99, 230, 190);"></i>Phone No: 9373510245</li>
                                        
                                    </ul>
                                    <ul class="social-links">
                                        <li><a href="index.html"><i class="icon-14"></i></a></li>
                                        <li><a href="index.html"><i class="icon-15"></i></a></li>
                                        <li><a href="index.html"><i class="icon-16"></i></a></li>
                                        <li><a href="index.html"><i class="icon-17"></i></a></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="footer-bottom">
                <div class="large-container">
                    <div class="bottom-inner">
                        <div class="copyright"><p>Copyright &copy; 2025 <a href="index.html">Kiddos</a>, Inc. All Rights Reserved</p></div>
                        <ul class="footer-card">
                            <li><a href="index.html"><img src="assets/images/icons/card-1.png" alt=""></a></li>
                            <li><a href="index.html"><img src="assets/images/icons/card-2.png" alt=""></a></li>
                            <li><a href="index.html"><img src="assets/images/icons/card-3.png" alt=""></a></li>
                            <li><a href="index.html"><img src="assets/images/icons/card-4.png" alt=""></a></li>
                            <li><a href="index.html"><img src="assets/images/icons/card-5.png" alt=""></a></li>
                            <li><a href="index.html"><img src="assets/images/icons/card-6.png" alt=""></a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </footer>

        <!-- main-footer end -->



        <!--Scroll to top-->
        <div class="scroll-to-top">
            <svg class="scroll-top-inner" viewBox="-1 -1 102 102">
                <path d="M50,1 a49,49 0 0,1 0,98 a49,49 0 0,1 0,-98" />
            </svg>
        </div>
        
    </div>


    <!-- jequery plugins -->
    <script src="assets/js/jquery.js"></script>
    <script src="assets/js/bootstrap.min.js"></script>
    <script src="assets/js/owl.js"></script>
    <script src="assets/js/wow.js"></script>
    <script src="assets/js/validation.js"></script>
    <script src="assets/js/jquery.fancybox.js"></script>
    <script src="assets/js/appear.js"></script>
    <script src="assets/js/isotope.js"></script>
    <script src="assets/js/parallax-scroll.js"></script>
    <script src="assets/js/jquery.nice-select.min.js"></script>
    <script src="assets/js/scrolltop.min.js"></script>
    <script src="assets/js/language.js"></script>
    <script src="assets/js/jquery-ui.js"></script>
    <script src="assets/js/jquery.bootstrap-touchspin.js"></script>
    <script src="assets/js/countdown.js"></script>
    <script src="assets/js/bxslider.js"></script>

    <!-- main-js -->
    <script src="assets/js/script.js"></script>

</body><!-- End of .page_wrapper -->

<!-- Mirrored from azim.hostlin.com/Kiddex/shop-details.html by HTTrack Website Copier/3.x [XR&CO'2014], Fri, 01 Aug 2025 04:23:41 GMT -->
</html>
""")

