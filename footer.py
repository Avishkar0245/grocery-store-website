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
print(f"""

 <!-- main-footer -->
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
                        <div class="col-lg-3 col-md-6 col-sm-12 footer-column">
                            <div class="tp-footer-widget logo-widget">
                                <figure class="footer-logo"><a href="index.html"><img src="logo.png" alt=""></a></figure>
                                <div class="support-box">
                                    
                                    <div >
                                       <h6>A grocery store is a retail business primarily selling food, fresh produce, meat, dairy, and household items, often functioning as supermarkets or small neighborhood shops</h6>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-3 col-md-6 col-sm-12 footer-column">
                            <div class="tp-footer-widget links-widget">
                                <div class="widget-title">
                                    <h4>PAGES</h4>
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
                        <div class="col-lg-3 col-md-6 col-sm-12 footer-column">
                            <div class="tp-footer-widget links-widget">
                                <div class="widget-title">
                                    <h4>Category</h4>
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
                                    <i>    <i class="fa-solid fa-address-book" style="color: rgb(99, 230, 190);"></i>{myresult[3]}</i>
                                         <li><i class="fa-solid fa-at" style="color: rgb(99, 230, 190);"></i><a href="mailto:info@example.com">{myresult[5]}</a></li>
                                       <li><i class="fa-solid fa-phone" style="color: rgb(99, 230, 190);"></i>Phone No:{myresult[4]}</li>
                                        
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
    <script src="assets/js/product-filter.js"></script>

    <!-- main-js -->
    <script src="assets/js/script.js"></script>

</body><!-- End of .page_wrapper -->

<!-- Mirrored from azim.hostlin.com/Kiddex/about.html by HTTrack Website Copier/3.x [XR&CO'2014], Fri, 01 Aug 2025 04:25:13 GMT -->
</html>""")