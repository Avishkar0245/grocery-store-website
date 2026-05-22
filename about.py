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
query=f"""SELECT * FROM cms"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchone()
import header
print(f"""<!DOCTYPE html>
<html lang="en">

<!-- Mirrored from azim.hostlin.com/Kiddex/about.html by HTTrack Website Copier/3.x [XR&CO'2014], Fri, 01 Aug 2025 04:25:11 GMT -->
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
<link href="assets/css/module-css/about.css" rel="stylesheet">
<link href="assets/css/module-css/brands.css" rel="stylesheet">
<link href="assets/css/module-css/testimonial.css" rel="stylesheet">
<link href="assets/css/module-css/highlights.css" rel="stylesheet">
<link href="assets/css/module-css/news.css" rel="stylesheet">
<link href="assets/css/module-css/subscribe.css" rel="stylesheet">
<link href="assets/css/module-css/footer.css" rel="stylesheet">
<link href="assets/css/responsive.css" rel="stylesheet">

</head>





 <!-- mobile menu  -->
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

<br>
<div style="background-color: #bad8e1;"> 
        <!-- about-section -->
        <section class="about-section pb_120">
            <div class="large-container"   style="background-color: #bad8e1;">
                <div class="row align-items-center">
                    <div class="col-lg-6 col-md-12 col-sm-12">
                        <div class="image-box">
                            <figure class="image image-1"><img src="vegetable.png" style="height: 100%; width: 500px;" alt=""></figure>
                            <figure class="image image-2"><img src="packagedfoods.png" style="height: 100%; width: 300px;" alt=""></figure>
                          
                        </div>
                    </div>
                    <div class="col-lg-6 col-md-12 col-sm-12 content-column">
                        <div class="content-box">
                            <div class="text-box mb_35">
                                <h2>We are a retail business in the Ecommerce Products and accessories for Grocery store</h2>
                                <p class="mb_20"><span></span></p>
                                <p>Effective grocery store websites focus on user-friendly navigation, mobile responsiveness, and seamless online ordering functionality. Key elements include a categorized product catalog, search functionality, weekly deals, and secure payment integration. Essential features for customer retention are real-time inventory updates, user accounts for order history, and integrated delivery options.</p>
                            </div>
                         
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- about-section end -->


        <div class="slide-text style-two home-3 p_relative">
            
            <div class="text-inner"> 
                <ul class="text-list">
                    <li>Fruits</li>
                    <li>Vegetables</li>
                    <li>Dairy & Bakery</li>
                    <li>Staples & Grains</li>
                    <li>Packaged Foods</li>
                    <li>Beveranges</li>
                    <li>Cooking Essentials</li>
                    <li>Baby care</li>
                    <li>Fruits</li>
                    <li>Vegetables</li>
                    <li>Dairy & Bakery</li>
                    <li>Staples & Grains</li>
                    <li>Packaged Foods</li>
                    <li>Beveranges</li>
                    <li>Cooking Essentials</li>
                    <li>Baby care</li>
                   <li>Fruits</li>
                    <li>Vegetables</li>
                    <li>Dairy & Bakery</li>
                    <li>Staples & Grains</li>
                    <li>Packaged Foods</li>
                    <li>Beveranges</li>
                    <li>Cooking Essentials</li>
                    <li>Baby care</li>
                    <li>Fruits</li>
                    <li>Vegetables</li>
                    <li>Dairy & Bakery</li>
                    <li>Staples & Grains</li>
                    <li>Packaged Foods</li>
                    <li>Beveranges</li>
                    <li>Cooking Essentials</li>
                    <li>Baby care</li>
                   <li>Fruits</li>
                    <li>Vegetables</li>
                    <li>Dairy & Bakery</li>
                    <li>Staples & Grains</li>
                    <li>Packaged Foods</li>
                    <li>Beveranges</li>
                    <li>Cooking Essentials</li>
                    <li>Baby care</li>
                   <li>Fruits</li>
                    <li>Vegetables</li>
                    <li>Dairy & Bakery</li>
                    <li>Staples & Grains</li>
                    <li>Packaged Foods</li>
                    <li>Beveranges</li>
                    <li>Cooking Essentials</li>
                    <li>Baby care</li>
                  <li>Fruits</li>
                    <li>Vegetables</li>
                    <li>Dairy & Bakery</li>
                    <li>Staples & Grains</li>
                    <li>Packaged Foods</li>
                    <li>Beveranges</li>
                    <li>Cooking Essentials</li>
                    <li>Baby care</li>
                   <li>Fruits</li>
                    <li>Vegetables</li>
                    <li>Dairy & Bakery</li>
                    <li>Staples & Grains</li>
                    <li>Packaged Foods</li>
                    <li>Beveranges</li>
                    <li>Cooking Essentials</li>
                    <li>Baby care</li>
                </ul>
            </div>
        </div>





        <!-- testimonial-section -->
        <section class="testimonial-section about-page mt_50">
            <div class="pattern-layer" style="background-image: url(assets/images/shape/shape-31.png);"></div>
            <div class="outer-container pt_100 p_relative">
                <span class="big-text">Testimonials</span>
                <div class="testimonial-carousel owl-carousel owl-theme owl-dots-none owl-nav-none">
                    <div class="testimonial-block-one">
                        <div class="inner-box">
                            <h4>Avishkar more</h4>
                            <span class="date">June 3, 2024</span>
                            <ul class="rating"> 
                                <li><i class="icon-10"></i></li>
                                <li><i class="icon-10"></i></li>
                                <li><i class="icon-10"></i></li>
                                <li><i class="icon-10"></i></li>
                                <li><i class="icon-10"></i></li>
                                <li><span>(5)</span></li>
                            </ul>
                            <p>Fast shipping, nice packaging, and good quality. A bit pricier than local options, but great for unique items you can’t find elsewhere..</p>
                            <div class="author-box">
                                <figure class="thumb-box"><img src="avi.jpeg" alt=""></figure>
                                <div class="inner">
                                    <h4><a href="shop-details.html">.</a></h4>
                                    <h5></h5>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="testimonial-block-one">
                        <div class="inner-box">
                            <h4>Prathmesh surve</h4>
                            <span class="date">June 12, 2024</span>
                            <ul class="rating"> 
                                <li><i class="icon-10"></i></li>
                                <li><i class="icon-10"></i></li>
                                <li><i class="icon-10"></i></li>
                                <li><i class="icon-10"></i></li>
                                <li><i class="icon-10"></i></li>
                                <li><span>(4)</span></li>
                            </ul>
                            <p>Quality product. Quick and trackable delivery</p>
                            <div class="author-box">
                                <figure class="thumb-box"><img src="prathmesh.jpeg" alt=""></figure>
                                <div class="inner">
                                    <h4><a href="shop-details.html">.</a></h4>
                                    <h5></h5>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="testimonial-block-one">
                        <div class="inner-box">
                            <h4>Shriyash Desai</h4>
                            <span class="date">June 31, 2024</span>
                            <ul class="rating"> 
                                <li><i class="icon-10"></i></li>
                                <li><i class="icon-10"></i></li>
                                <li><i class="icon-10"></i></li>
                                <li><i class="icon-10"></i></li>
                                <li><i class="icon-10"></i></li>
                                <li><span>(4.7)</span></li>
                            </ul>
                            <p>Best Grocery truly lives up to its…
Best Grocery truly lives up to its name! For years, they've been my reliable source for Turkish products thanks to their great selection, fast delivery, and consistently low prices. Their customer service is also top-notch.</p>
                            <div class="author-box">
                                <figure class="thumb-box"><img src="shriyash.jpeg" alt=""></figure>
                                <div class="inner">
                                    <h4><a href="shop-details.html"></a></h4>
                                    <h5></h5>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="testimonial-block-one">
                        <div class="inner-box">
                            <h4>Aditya Pawar</h4>
                            <span class="date">June 23, 2024</span>
                            <ul class="rating"> 
                                <li><i class="icon-10"></i></li>
                                <li><i class="icon-10"></i></li>
                                <li><i class="icon-10"></i></li>
                                <li><i class="icon-10"></i></li>
                                <li><i class="icon-10"></i></li>
                                <li><span>(5)</span></li>
                            </ul>
                            <p>Great products
Fast delivery and fair prices for the food really lovely seller!.</p>
                            <div class="author-box">
                                <figure class="thumb-box"><img src="aditya.jpeg" alt=""></figure>
                                <div class="inner">
                                    <h4><a href="shop-details.html">.</a></h4>
                                    <h5></h5>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="testimonial-block-one">
                        <div class="inner-box">
                            <h4>Sanket Jadhav</h4>
                            <span class="date">June 16, 2024</span>
                            <ul class="rating"> 
                                <li><i class="icon-10"></i></li>
                                <li><i class="icon-10"></i></li>
                                <li><i class="icon-10"></i></li>
                                <li><i class="icon-10"></i></li>
                                <li><i class="icon-10"></i></li>
                                <li><span>(4.9)</span></li>
                            </ul>
                            <p>{myresult[7]}</p>
                            <div class="author-box">
                                <figure class="thumb-box"><img src="sanket.jpeg" alt=""></figure>
                                <div class="inner">
                                    <h4><a href="shop-details.html"></a></h4>
                                    <h5></h5>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- testimonial-section end -->


        <!-- highlights-section -->
        <section class="highlights-section pt_0">
            <div class="large-container">
                <div class="inner-container">
                    <ul class="list-item clearfix">
                        <li>
                            <div class="single-item">
                                <div class="icon-box"><img src="assets/images/icons/icon-2.png" alt=""></div>
                                <h5>Same day Product Delivery</h5>
                            </div>
                        </li>
                        <li>
                            <div class="single-item">
                                <div class="icon-box"><img src="assets/images/icons/icon-3.png" alt=""></div>
                                <h5>100% Customer Satisfaction</h5>
                            </div>
                        </li>
                        <li>
                            <div class="single-item">
                                <div class="icon-box"><img src="assets/images/icons/icon-4.png" alt=""></div>
                                <h5>Help and access is our mission</h5>
                            </div>
                        </li>
                        <li>
                            <div class="single-item">
                                <div class="icon-box"><img src="assets/images/icons/icon-5.png" alt=""></div>
                                <h5>100% quality Toy Accessories</h5>
                            </div>
                        </li>
                        <li>
                            <div class="single-item">
                                <div class="icon-box"><img src="assets/images/icons/icon-6.png" alt=""></div>
                                <h5>24/7 Support for Clients</h5>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </section>
        <!-- highlights-section end -->


        <!-- news-section -->
        <section class="news-section pt_120 pb_90">
            <div class="shape-layer rotate-me" style="background-image: url(assets/images/shape/shape-29.png);"></div>
            <div class="large-container">
                <div class="sec-title centred mb_50">
                    <h2>Latest From <span>Media</span></h2>
                </div>
                <div class="row clearfix">
                    <div class="col-lg-3 col-md-6 col-sm-12 news-block">
                        <div class="news-block-one wow fadeInUp animated" data-wow-delay="00ms" data-wow-duration="1500ms">
                            <div class="inner-box">
                                <div class="image-box">
                                    <figure class="image"><a href="blog-details.html"><img src="https://m.media-amazon.com/images/G/31/img18/Fresh/SBCTILES/UPDATED/Oil__Ghee.jpg" alt=""></a></figure>
                                    <figure class="overlay-image"><a href="blog-details.html"><img src="https://m.media-amazon.com/images/G/31/img18/Fresh/SBCTILES/UPDATED/Oil__Ghee.jpg" alt=""></a></figure>
                                   
                                </div>
                                <div class="lower-content">
                                    <h3  style="text-align: center;"><a href="blog-details.html">OIL & GHEE </a></h3>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6 col-sm-12 news-block">
                        <div class="news-block-one wow fadeInUp animated" data-wow-delay="200ms" data-wow-duration="1500ms">
                            <div class="inner-box">
                                <div class="image-box">
                                    <figure class="image"><a href="blog-details.html"><img src="https://m.media-amazon.com/images/G/31/img18/Fresh/SBCTILES/UPDATED/Chocolates__sweets.jpg" alt=""></a></figure>
                                    <figure class="overlay-image"><a href="blog-details.html"><img src="https://m.media-amazon.com/images/G/31/img18/Fresh/SBCTILES/UPDATED/Chocolates__sweets.jpg" alt=""></a></figure>
                                   
                                </div>
                                <div class="lower-content">
                                    <h3  style="text-align: center;"><a href="blog-details.html">CHOCOLATE & SWEETS</a></h3>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6 col-sm-12 news-block">
                        <div class="news-block-one wow fadeInUp animated" data-wow-delay="400ms" data-wow-duration="1500ms">
                            <div class="inner-box">
                                <div class="image-box">
                                    <figure class="image"><a href="blog-details.html"><img src="https://images-eu.ssl-images-amazon.com/images/I/71xqTSRdbML.AC_SL240_.jpg" alt=""></a></figure>
                                    <figure class="overlay-image"><a href="blog-details.html"><img src="https://images-eu.ssl-images-amazon.com/images/I/71xqTSRdbML.AC_SL240_.jpg" alt=""></a></figure>
                                    
                                </div>
                                <div class="lower-content">
                                    <h3  style="text-align: center;"><a href="blog-details.html">DAAWAT RICE</a></h3>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6 col-sm-12 news-block">
                        <div class="news-block-one wow fadeInUp animated" data-wow-delay="600ms" data-wow-duration="1500ms">
                            <div class="inner-box">
                                <div class="image-box">
                                    <figure class="image"><a href="blog-details.html"><img src="https://images-eu.ssl-images-amazon.com/images/I/71YZ+X9+l8L.AC_SL240_.jpg" alt=""></a></figure>
                                    <figure class="overlay-image"><a href="blog-details.html"><img src="https://images-eu.ssl-images-amazon.com/images/I/71YZ+X9+l8L.AC_SL240_.jpg" alt=""></a></figure>
                                    
                                </div>
                                <div class="lower-content">
                                    <h3  style="text-align: center;"><a href="blog-details.html">EVERYDAY POWDER</a></h3>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- news-section end -->
</div>""")
import footer