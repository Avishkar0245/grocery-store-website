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
query=f"""SELECT * FROM categary"""
mycursor.execute(query)
myresult=mycursor.fetchall()
tr_html=''
for x in myresult:
    tr_html+=f"""
                    <div class="category-block-one">
                        <div class="inner-box">
                            <div class="image-box">
                                <div class="shape" style="background-image: url(assets/images/shape/shape-15.png);"></div>
                                <figure class="image"><img src="html/ltr/Category/{x[0]}/{x[2]}" alt="" style="height:150px;border-radius:60%;width:100%;"></figure>
                            </div>
                            <h4><a href="categarydetail.py?CategoryName={x[1]}" style="color:black">{x[1]}</a></h4>
                        </div>
                    </div>
    """
productquery=f"""SELECT * FROM products"""
#print(productquery)
mycursor.execute(productquery)
allproduct=mycursor.fetchall()
#print(allproduct)
pro_html=''
for y in allproduct:
    pro_html+=f"""<div class="shop-block-one">
                            <div class="inner-box">
                                <div class="image-box">
                                    <ul class="option-list clearfix">
                                               <li><a href="html/ltr/Product/{y[0]}/{y[1]}" class="lightbox-image" data-fancybox="gallery"><i class="far fa-eye"></i></a></li>
                                                <li><a class="cartLink"><i class="far fa-shopping-bag"></i></a></li>
                                                <li><a class="mywishlist" data-id="{y[0]}"><i class="far fa-heart"></i></a>
                                                </li>
                                    </ul>
                                    <figure class="image"><img src="html/ltr/Product/{y[0]}/{y[1]}" alt="" style="height: 150px;"></figure>
                                </div>
                                <div class="lower-content">
                                    <span class="text">{y[3]}</span>
                                    
                                    <h4><a href="">{y[3]}</a></h4>
                                    <div class="price" style="margin-bottom:40px">{y[4]}Rs/-</div>
                                    <div class="btn-box"><a href="productdetails.py?id={y[0]}"<button type="" class="theme-btn btn-one">Product detail</button></a></div>
                                </div>
                            </div>
                        </div>"""
dealsquery=f"""SELECT * FROM products WHERE dealsofday='1'"""
#print(dealsquery)
mycursor.execute(dealsquery)
dealsproduct=mycursor.fetchall()
#print(dealsproduct)
deals_html=''
for z in dealsproduct:
    deals_html+=f"""<div class="deals-block-one">
                            <div class="inner-box">
                                <div class="image-box">
                                    <figure class="image"><img src="html/ltr/Product/{z[0]}/{z[1]}" alt="" style="width:300px"></figure>
                                     
                                </div>
                                <div class="content-box">
                                    <span class="text">{z[3]}</span>
                                    <h3><a href="">{z[2]}</a></h3>
                                    <h4>{z[4]}</h4>
                                    
                                     
                                    <div class="btn-box"><a href="productdetails.py?id={z[0]}"><button  class="theme-btn btn-one">product Detail</button></a></div>
                                </div>
                            </div>
                        </div>"""
slogan=f"""SELECT * FROM cms"""
#print(slogan)
mycursor.execute(slogan)
slogan=mycursor.fetchall()
#print(slogan)
slogan_html=''
for a in slogan:
    slogan_html+=f"""
                  """
print(f"""
      
<!-- banner-section -->
        <section class="banner-section">
            <div class="pattern-layer" style="background-image: url(assets/images/shape/shape-21.png);"></div>
            <div class="anim-icon">
                <div class="anim-icon-1 float-bob-y" style="background-image: url(assets/images/shape/shape-3.png);"></div>
                <div class="anim-icon-2" style="background-image: url(assets/images/shape/shape-4.png);"></div>
                <div class="anim-icon-3 rotate-me" style="background-image: url(assets/images/shape/shape-5.png);"></div>
                <div class="anim-icon-4 rotate-me" style="background-image: url(assets/images/shape/shape-5.png);"></div>
                <div class="anim-icon-5 rotate-me" style="background-image: url(assets/images/shape/shape-5.png);"></div>
                <div class="anim-icon-6 rotate-me" style="background-image: url(assets/images/shape/shape-5.png);"></div>
                <div class="anim-icon-7 float-bob-x" style="background-image: url(assets/images/shape/shape-6.png);"></div>
                <div class="anim-icon-8" style="background-image: url(assets/images/shape/shape-7.png);"></div>
                <div class="anim-icon-9 zoom-fade" style="background-image: url(assets/images/shape/shape-8.png);"></div>
                <div class="anim-icon-10 float-bob-y" style="background-image: url(assets/images/shape/shape-9.png);"></div>
                <div class="anim-icon-11 zoom-fade" style="background-image: url(assets/images/shape/shape-10.png);"></div>
            </div>
           
        </section>
        <!-- banner-section end -->
      <!-- category-section -->

        <section class="category-section centred pt_120 pb_85">
            <div class="sec-title mb_50">
                    <h2>Our <span>Categories</span></h2>
                </div>
            <div class="pattern-layer" style="background-image: url(assets/images/shape/shape-18.png);"></div>
            <div class="shape-box">
                <div class="shape-1" style="background-image: url(assets/images/shape/shape-17.png);"></div>
                <div class="shape-2 zoom-fade" style="background-image: url(assets/images/shape/cart.png); height:200px"></div>
            </div>
            <div class="large-container">
                <div class="category-carousel owl-carousel owl-theme owl-dots-none owl-nav-none">
                    {tr_html}
                </div>
            </div>
        </section>
        <!-- category-section end -->
        <!---Feture starts---->
        <div class="slide-text p_relative">
            <div class="shape float-bob-y" ></div>
          
            <div class="text-inner">
                <ul class="text-list">
                    <li>Free Delivery</li>
                    <li>Easy Returns</li>
                    <li>Fast Shipping</li>
                    <li>Secure Payment</li>
                    <li>Genuine Products</li>
                    <li>24/7 Support</li>
                    <li>Easy Refunds</li>
                    <li>Best Prices</li>
                    <li>Free Delivery</li>
                    <li>Easy Returns</li>
                    <li>Fast Shipping</li>
                    <li>Secure Payment</li>
                    <li>Genuine Products</li>
                    <li>24/7 Support</li>
                    <li>Easy Refunds</li>
                    <li>Best Prices</li>
                     
                     
                </ul>
            </div>
        </div>
<!-----<!---Feture end---->
<!-- all-product -->
        <section class="popular-product pb_120 centred" style="margin-top:160px;">
            
            <div class="large-container">
                <div class="sec-title mb_50">
                    <h2>Explore Products</h2>
                </div>
                <div class="inner-container">
                    <div class="popular-carousel owl-carousel owl-theme owl-dots-none">
                      {pro_html}
                         
                         
                        
                    </div>
                </div>
            </div>
        </section>
        <!-- all-product end -->
       <section class="deals-style-two pb_110">
            
            <div class="large-container">
                <div class="sec-title mb_50 centred">
                    <h2>Deal of <span>the Day</span></h2>
                </div>
                <div class="inner-container p_relative z_2">
                    <div class="two-item-carousel owl-carousel owl-theme owl-nav-none">
                   {deals_html} 
                    </div>
                </div>
            </div>
        </section>
                        <!-- cta-section -->
        <section class="cta-section centred">
            <div class="large-container">
                <div class="inner-container">
                    <div class="shape" style="background-image: url(assets/images/shape/shape-56.png);"></div>
                    <div class="image-layer">
                        <figure class="image image-1" '><img src="assets/images/fru.png" alt="" style=" margin-top: 15%; height:200px ; width: ;"></figure>
                        <figure class="image image-2 p_absolute t_10 r_30"><img src="assets/images/fruit.png" alt=""></figure>
                    </div>
                    <div class="text-box">
                        <h2>Super Discount on First Purchase</h2>
                        <a href="product.py" class="theme-btn btn-one">View Products</a>
                    </div>
                </div>
            </div>
        </section>
        <!-- cta-section end -->
        <!-- testimonial-section -->
        <section class="testimonial-section style-two pt_200 pb_90">
            <div class="pattern-layer" style="background-image: url(assets/images/shape/shape-31.png);"></div>
           <div class="sec-title mb_50 centred">
                    <h2>Testimonoals</h2>
                </div>
            <div class="large-container">
                <div class="testimonial-carousel-2 owl-carousel owl-theme owl-dots-none">
                    <div class="testimonial-block-one">
                        <div class="inner-box">
                            <div class="quote-icon"><i class="icon-23"></i></div>
                            <ul class="rating"> 
                                <li><i class="icon-10"></i></li>
                                <li><i class="icon-10"></i></li>
                                <li><i class="icon-10"></i></li>
                                <li><i class="icon-10"></i></li>
                                <li><i class="icon-10"></i></li>
                            </ul>
                            <p>“"Very fresh fruits and vegetables. Delivery is always on time. I’ve completely stopped buying from local stores!"”</p>
                            <div class="author-box">
                                <figure class="thumb-box"><img src="assets/images/avishkar.jpeg" alt="" style="height:60px ; width: ;"></figure>
                                <div class="inner">
                                    <h4>Avishkar more</h4>
                                    <span class="designation"></span>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="testimonial-block-one">
                        <div class="inner-box">
                            <div class="quote-icon"><i class="icon-23"></i></div>
                            <ul class="rating"> 
                                <li><i class="icon-10"></i></li>
                                <li><i class="icon-10"></i></li>
                                <li><i class="icon-10"></i></li>
                                <li><i class="icon-10"></i></li>
                                <li><i class="icon-10"></i></li>
                            </ul>
                            <p>"Packaging is neat and products are always fresh. Customer support is also very helpful."</p>
                            <div class="author-box">
                                <figure class="thumb-box"><img src="assets/images/suyash.jpeg" alt="" style="height:60px ; width: ;"></figure>
                                <div class="inner">
                                    <h4>suyash</h4>
                                    <span class="designation"></span>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="testimonial-block-one">
                        <div class="inner-box">
                            <div class="quote-icon"><i class="icon-23"></i></div>
                            <ul class="rating"> 
                                <li><i class="icon-10"></i></li>
                                <li><i class="icon-10"></i></li>
                                <li><i class="icon-10"></i></li>
                                <li><i class="icon-10"></i></li>
                                <li><i class="icon-10"></i></li>
                            </ul>
                            <p>"Affordable prices with great offers. Monthly grocery shopping has become so easy!"</p>
                            <div class="author-box">
                                <figure class="thumb-box"><img src="assets/images/pratik.jpeg" alt="" style="height:60px ; width: ;"></figure>
                                <div class="inner">
                                    <h4>pratik</h4>
                                    <span class="designation"></span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- testimonial-section end -->""")
print("""
<script>
document.addEventListener('DOMContentLoaded', function () {
  const cartLinks = document.querySelectorAll('.cartLink');

  cartLinks.forEach(function (link) {
    link.addEventListener('click', function () {
      let userId = localStorage.getItem('id');
    

      window.location.href = 'cartdetail.py?userid=' + userId;
    });
  });
});
</script>""")
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
