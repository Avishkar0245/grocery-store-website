#!C:/Python312/python.exe
import cgi 
import cgitb 
cgitb.enable() 
print("Content-Type:text/html\n")
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="grocery"
)

mycursor = mydb.cursor()
query=f"""SELECT * FROM categary"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchall()
#print(myresult)
tr_html=''
for x in myresult:
    tr_html+=f"""  <div class="col-lg-3 col-md-6 col-sm-12 news-block">
                                    <div class="news-block-one">
                                        <div class="inner-box">
                                            <div class="image-box">
                                                <figure class="image"><a href="blog-details.html"><img src="html/ltr/Category/{x[0]}/{x[2]}" alt="" style="height: 250px;"></a></figure>
                                                <figure class="overlay-image"><a href="blog-details.html"><img src="html/ltr/Category/{x[0]}/{x[2]}" alt="" style="height: 250px;"></a></figure>
                                                <ul class="post-info">
                                                    <li>June 8, 2024</li>
                                                    <li><a href="blog-details.html"></a></li>
                                                </ul>
                                            </div>
                                            <div class="lower-content">
                                                <h3 style="text-align: center;"><a href="blog-details.html">{x[1]}</a></h3>
                                               <div style="text-align: center; margin-top:20px"> <a href="categarydetail.py?CategoryName={x[1]}"><button class="theme-btn btn-one">show more</button></a> </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>"""
import header
print(f"""
<!DOCTYPE html>
<html lang="en">

<!-- Mirrored from azim.hostlin.com/Kiddex/blog.html by HTTrack Website Copier/3.x [XR&CO'2014], Fri, 01 Aug 2025 04:24:52 GMT -->

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0">

    <title>Kiddex - HTML 5 Template Preview</title>

    <!-- Fav Icon -->
    <link rel="icon" href="assets/images/favicon.ico" type="image/x-icon">

    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,200..1000;1,200..1000&amp;display=swap"
        rel="stylesheet">

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
    <link href="assets/css/module-css/news.css" rel="stylesheet">
    <link href="assets/css/module-css/cta.css" rel="stylesheet">
    <link href="assets/css/module-css/blog-page.css" rel="stylesheet">
    <link href="assets/css/module-css/blog-sidebar.css" rel="stylesheet">
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
                <div class="menu-outer"><!--Here Menu Will Come Automatically Via Javascript / Same Menu as in Header-->
                </div>
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


       



      <!-- sidebar-page-container -->
        <section class="sidebar-page-container blog-grid pb_120">
            <div class="large-container">
                <div class="sec-title centred mb_50">
                    <h2><span>Categary</span></h2>
                </div>
            
                <div class="row clearfix">
                    <div class="col-xl-12 col-lg-12 col-md-12 content-side">
                        <div class="blog-grid-content">
                            <div class="row clearfix">
                              
                              {tr_html}
                                
                            </div>
                           
                        </div>
                    </div>
                    
                </div>
                
            </div>
        </section>
       """)
import footer
