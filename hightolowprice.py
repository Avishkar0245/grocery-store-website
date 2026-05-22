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
mycursor=mydb.cursor()
query=f""" SELECT * FROM products order BY Price DESC """
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchall()
#print(myresult)
tr_html=''
for x in myresult:
   tr_html+=f'''
   <div class="shop-block-one">
                                    <div class="inner-box">
                                        <div class="image-box">
                                        
                                            <ul class="option-list clearfix">
                                                <li><a href="html/ltr/Product/{x[0]}/{x[1]}" class="lightbox-image" data-fancybox="gallery"><i class="far fa-eye"></i></a></li>
                                                <li><button type="button"><i class="far fa-shopping-bag"></i></button></li>
                                                <li><a class="mywishlist" data-id="{x[0]}"><i class="far fa-heart"></i></a></li>
                                            </ul>
                                            <figure class="image"><img src="html/ltr/Product/{x[0]}/{x[1]}" alt="" style="height: 250px; "></figure>
                                        </div>
                                        <div class="lower-content">
                                            <span class="text">{x[3]}</span>
                                           
                                            <h4><a href="productdetails.py">{x[2]}</a></h4>
                                            <div class="price"></div>
                                              <div><a href="productdetails.py?id={x[0]}"><button style="border: 2px solid black; background-color: #f25923;width:100px;">product</button></a></div><br>
                                             <h4>{x[4]}Rs/-<h4>
                                        </div>
                                    </div>
                                </div>'''
import header
print(f"""
      <!DOCTYPE html>
<html lang="en">

<!-- Mirrored from azim.hostlin.com/Kiddex/shop-3.html by HTTrack Website Copier/3.x [XR&CO'2014], Fri, 01 Aug 2025 04:25:09 GMT -->
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
<link href="assets/css/module-css/shop-sidebar.css" rel="stylesheet">
<link href="assets/css/module-css/shop-page.css" rel="stylesheet">
<link href="assets/css/module-css/popular-product.css" rel="stylesheet">
<link href="assets/css/module-css/cta.css" rel="stylesheet">
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


        <!-- shop-page-section -->
        <section class="shop-page-section pt_60 pb_120">
            <div class="large-container">
              
                <div class="our-shop fluid">
                    <div class="wrapper grid">
                        <div class="shop-grid-content">
                            <div class="inner-container clearfix">
                                {tr_html}
                                    
                        </div>
                    </div>
                   
                </div>
            </div>
        </section>
        <!-- shop-page-section end -->
""")
print("""
<script>
document.addEventListener('DOMContentLoaded', function () {
  const mywishlist = document.querySelectorAll('.mywishlist');

  mywishlist.forEach(function (link) {
    link.addEventListener('click', function () {
      let userId = localStorage.getItem('id');
      let productId = this.getAttribute('data-id');

      window.location.href = 'mywishlist.py?userid=' + userId + '&proid=' + productId;
    });
  });
});
</script>
""")
import footer