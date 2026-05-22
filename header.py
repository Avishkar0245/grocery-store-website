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
query=f"""SELECT * FROM cms"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchone()
#print(myresult)

print(f"""
<!DOCTYPE html>
<html lang="en">

<!-- Mirrored from azim.hostlin.com/Kiddex/about.html by HTTrack Website Copier/3.x [XR&CO'2014], Fri, 01 Aug 2025 04:25:11 GMT -->
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0">

<title>GROCERY</title>

<!-- Fav Icon -->
<link rel="icon" href="assets/images/favicon.ico" type="image/x-icon">

<!-- Google Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,200..1000;1,200..1000&amp;display=swap" rel="stylesheet">

<!-- Stylesheets -->
<!-- Stylesheets -->
<link href="assets/css/font-awesome-all.css" rel="stylesheet">
<link href="assets/css/flaticon.css" rel="stylesheet">
<link href="assets/css/owl.css" rel="stylesheet">
<link href="assets/css/bootstrap.css" rel="stylesheet">
<link href="assets/css/jquery.fancybox.min.css" rel="stylesheet">
<link href="assets/css/animate.css" rel="stylesheet">
<link href="assets/css/nice-select.css" rel="stylesheet">
<link href="assets/css/elpath.css" rel="stylesheet">
<link href="assets/css/color.css" id="jssDefault" rel="stylesheet">
<link href="assets/css/rtl.css" rel="stylesheet">
<link href="assets/css/style.css" rel="stylesheet">
<link href="assets/css/module-css/header.css" rel="stylesheet">
<link href="assets/css/module-css/banner.css" rel="stylesheet">
<link href="assets/css/module-css/highlights.css" rel="stylesheet">
<link href="assets/css/module-css/category.css" rel="stylesheet">
<link href="assets/css/module-css/shop.css" rel="stylesheet">
<link href="assets/css/module-css/brands.css" rel="stylesheet">
<link href="assets/css/module-css/featured.css" rel="stylesheet">
<link href="assets/css/module-css/popular-product.css" rel="stylesheet">
<link href="assets/css/module-css/deals.css" rel="stylesheet">
<link href="assets/css/module-css/cta.css" rel="stylesheet">
<link href="assets/css/module-css/news.css" rel="stylesheet">
<link href="assets/css/module-css/footer.css" rel="stylesheet">
<link href="assets/css/responsive.css" rel="stylesheet">
      
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.0.1/css/all.min.css" integrity="sha512-2SwdPD6INVrV/lHTZbO2nodKhrnDdJK9/kg2XD1r9uGqPo1cUbujc+IYdlYdEErWNu69gVcYgdxlmVmzTWnetw==" crossorigin="anonymous" referrerpolicy="no-referrer" />

</head>


<!-- page wrapper -->
<body>

    <div class="boxed_wrapper ltr">


        <!-- preloader -->
        <div class="loader-wrap">
            <div class="preloader">
                <div id="handle-preloader" class="handle-preloader">
                    <div class="animation-preloader">
                        <div class="spinner"></div>
                        <div class="txt-loading">
                            <span data-text-preloader="G" class="letters-loading">
                                G
                            </span>
                            <span data-text-preloader="R" class="letters-loading">
                                R
                            </span>
                            <span data-text-preloader="O" class="letters-loading">
                                O
                            </span>
                            <span data-text-preloader="C" class="letters-loading">
                                C
                            </span>
                            <span data-text-preloader="E" class="letters-loading">
                                E
                            </span>
                            <span data-text-preloader="R" class="letters-loading">
                                R
                            </span>
                             <span data-text-preloader="Y" class="letters-loading">
                                Y
                            </span>
                        </div>
                    </div>  
                </div>
            </div>
        </div>
        <!-- preloader end -->


    


     


        <!--cart popup-->
        <div id="cart-popup" class="cart-popup">
            <div class="popup-inner">
                <div class="close-cart"><i class="fal fa-times"></i></div>
                <div class="cart-inner">
                    <h4 class="title-text"><span>3</span>Cart Items</h4>
                    <div class="single-cart-box">
                        <figure class="image-box"><img src="assets/images/resource/cart-1.png" alt=""></figure>
                        <h5><a href="shop-details.html">Avenger Action Figure figurine Thano</a></h5>
                        <h4>$02.99 <span>x 1</span></h4>
                        <button type="button"><i class="fal fa-times"></i></button>
                    </div>
                    <div class="single-cart-box">
                        <figure class="image-box"><img src="assets/images/resource/cart-2.png" alt=""></figure>
                        <h5><a href="shop-details.html">Cart- Limited 100 Anniversary</a></h5>
                        <h4>$01.99 <span>x 1</span></h4>
                        <button type="button"><i class="fal fa-times"></i></button>
                    </div>
                    <div class="single-cart-box">
                        <figure class="image-box"><img src="assets/images/resource/cart-3.png" alt=""></figure>
                        <h5><a href="shop-details.html">Ultrasoft Stuff Animal Plush Bunny</a></h5>
                        <h4>$02.99 <span>x 1</span></h4>
                        <button type="button"><i class="fal fa-times"></i></button>
                    </div>
                    <div class="text-box">
                        <h5>Subtotal</h5>
                        <span>$07.97</span>
                    </div>
                    <div class="btn-box">
                        <a href="cart.html" class="theme-btn btn-one">View Cart</a>
                        <a href="checkout.html" class="theme-btn btn-one">Checkout</a>
                    </div>
                </div>
            </div>
        </div>


        <!-- main header -->
        <header class="main-header header-style-one">
            <!-- header-top -->
            <div class="header-top">
                <div class="large-container">
                    <div class="top-inner">
                     
                       
                     <marquee behavior="" direction="left" style="color: black;">{myresult[2]}</marquee>
                    </div>
                </div>
            </div>
            <!-- header-lower -->
            <div class="header-lower p_relative">
                <div class="shape" style="background-image: url(assets/images/shape/shape-1.png);"></div>
                <div class="large-container">
                    <div class="outer-box">
                        <figure class="logo-box"><a href="index.html"><img src="logo.png" alt="" style="height: 10%; width: 200px;"></a></figure>
                       
                        <div class="menu-area">
                            <!--Mobile Navigation Toggler-->
                            <div class="mobile-nav-toggler">
                                <i class="icon-bar"></i>
                                <i class="icon-bar"></i>
                                <i class="icon-bar"></i>
                            </div>
                            <nav class="main-menu navbar-expand-md navbar-light clearfix">
                                <div class="collapse navbar-collapse show clearfix" id="navbarSupportedContent">
                                    <ul class="navigation clearfix">
                                        <li><a href="index.py">Home</a>
                                            
                                        </li> 
                                        <li><a href="about.py">About Us</a>
                                            <div class="megamenu">
                                                <div class="row clearfix">
                                                    <div class="col-xl-3 column">
                                                       
                                                    </div>
                                                    <div class="col-xl-3 column">
                                                     
                                                    </div> 
                                                    <div class="col-xl-3 column">
                                                   
                                                    </div> 
                                                    <div class="col-xl-3 column">
                                                      
                                                    </div>                                 
                                                </div>   
                                                                             
                                            </div>
                                        </li>
                                        <li><a href="contact.py">Contact</a>
                                           
                                        </li> 
                                        <li><a href="product.py">product</a>
                                            
                                        </li>  
                                        <li><a href="categary.py">Categary</a></li> 
                                        <li id="loginMenu"><a href="login.py">Login</a></li>
                                        <li id="registerMenu"><a href="regestration.py">Registration</a></li>

                                   <li id="greetingMenu" style="display:none;">
                                    <a href="#" class="nav-link" id="userBox">
                                    <img id="userPhoto" src="" style="width:30px; height:30px; border-radius:50%; margin-right:8px; display:none;">
                                    <span id="username"></span>
                                     </a>
                                     </li>

                                       <li id="profileMenu" class="dropdown" style="display:none;">
                                         <a href="myprofile.py">My Profile</a>
                                        <ul>
                                        <li><a href="#" id="cartLink">My Cart</a></li>
                                        <li><a href="#" id="myaccountLink">My Account</a></li>
                                        <li><a href="#" id="wishListLink">My wish list</a></li>
                                        <li><a href="#" id="myorderLink">My Orders</a></li>
                                       </ul>
                                       </li>

                                                <li id="logoutMenu" style="display:none;">
                                                <a href="logout.py">Logout</a>
                                            </li>
                                    </ul>
                                </div>
                            </nav>
                        </div>
                        <div class="menu-right-content" style="display:flex; aline-item:center;gap:15px;position:relative;">
                            <!-- Language Icon -->""")    
print("""                    
<style>
.goog-te-banner-frame.skiptranslate {
    display: none !important;
}
body {
    top: 0px !important;
}
      
.lang-container {
    position: relative;
    display: inline-block;
}

.lang-icon {
    width: 35px;
    cursor: pointer;
}

.dropdown1 {
    display: none;
    position: absolute;
    right: 0;
    background: white;
    border: 1px solid #ccc;
    border-radius: 6px;
    width: 120px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.dropdown1 p {
    margin: 0;
    padding: 10px;
    cursor: pointer;
}

.dropdown1 p:hover {
    background: #f0f0f0;
}

</style>
      
      <div class="lang-container">
    <img src="https://cdn-icons-png.flaticon.com/512/484/484582.png" 
         class="lang-icon" onclick="toggleDropdown()" />

    <div id="langDropdown" class="dropdown1">
        <p onclick="translateTo('en')">English</p>
        <p onclick="translateTo('mr')">Marathi</p>
    </div>
</div>

<!-- Hidden Google Translate -->
<div id="google_translate_element" style="display:none;"></div>
                            <div class="search-box" style="width: 200px; height:50px ;">
                                <form action="search.py" method="get">
                                    <div class="form-group">
                                        <input type="search" name="search" placeholder="Search Products" required>
                                        <button type="submit"><i class="icon-4"></i></button>
                                    </div>
                                </form>
                            </div>
                           
                        </div>
                    </div>
                </div>
            </div>

            <!--sticky Header-->
            <div class="sticky-header">
                <div class="large-container">
                    <div class="outer-box">
                        <figure class="logo-box"><a href="index.html"><img src="logo.png" alt="" style="height: 20%; width: 70px;"></a></figure>
                        <div class="support-box">
                          
                           
                        </div>
                        <div class="menu-area">
                            <nav class="main-menu clearfix">
                                <!--Keep This Empty / Menu will come through Javascript-->
                            </nav>
                        </div>
                        <div class="menu-right-content">
                            <div class="search-box">
                                <form action="search.py" method="get">
                                    <div class="form-group">
                                        <input type="search" name="search" placeholder="Search Products" required>
                                        <button type="submit"><i class="icon-4"></i></button>
                                    </div>
                                </form>
                            </div>
                           
                        </div>
                    </div>
                </div>
            </div>
        </header>
        <!-- main-header end -->
   <script>
window.onload = function () {

    let firstName = localStorage.getItem("FirstName");
        let Photo = localStorage.getItem("Photo");
    let userid = localStorage.getItem("id");

    
    if (firstName) {
        document.getElementById("loginMenu").style.display = "none";
        document.getElementById("registerMenu").style.display = "none";

        document.getElementById("greetingMenu").style.display = "inline-block";
        document.getElementById("profileMenu").style.display = "inline-block";
        document.getElementById("logoutMenu").style.display = "inline-block";

        document.getElementById("username").innerText = "Hello, " + firstName;
      if(Photo){
        let img = document.getElementById("userPhoto");
           img.src = "User/" + userid + "/" + Photo;
           img.style.display="inline-block";
        }

        if (userid) {
            document.getElementById("cartLink").href =
                "cartdetail.py?userid=" + userid;
              document.getElementById("myaccountLink").href =
                "myprofile.py?userid=" + userid;
            document.getElementById("wishListLink").href =
                "mywishlistdetail.py?userid=" + userid;
                 document.getElementById("myorderLink").href =
                "myorders.py?userid=" + userid;
        }
    }

     
    setInterval(() => {
        let stickyMenu = document.querySelector(".sticky-header .navigation");

        if (!stickyMenu) return;

       
        stickyMenu.querySelectorAll("li").forEach(li => {
            let text = li.innerText.trim();
            if (text === "Login" || text === "Registration") {
                li.remove();
            }
        });

      
        if (stickyMenu.querySelector(".user-added")) return;

        if (firstName) {

           
            let helloLi = document.createElement("li");
            helloLi.className = "user-added";
            helloLi.innerHTML = `<a href="#">Hello, ${firstName}</a>`;

            
            let profileLi = document.createElement("li");
            profileLi.className = "dropdown user-added";

            profileLi.innerHTML = `
                <a href="myprofile.py">My Profile</a>
                <ul>
                    <li><a href="cartdetail.py?userid=${userid}">My Cart</a></li>
                    <li><a href="index-2.html">My Account</a></li>
                    
                </ul>
            `;

             
            let logoutLi = document.createElement("li");
            logoutLi.className = "user-added";
            logoutLi.innerHTML = `<a href="logout.py">Logout</a>`;
 
            stickyMenu.appendChild(helloLi);
            stickyMenu.appendChild(profileLi);
            stickyMenu.appendChild(logoutLi);
        }

    }, 500);
};
</script>
<script>
function googleTranslateElementInit() {
    new google.translate.TranslateElement({
        pageLanguage: 'en',
        includedLanguages: 'en,mr',
        autoDisplay: false
    }, 'google_translate_element');
}

// Toggle dropdown
function toggleDropdown() {
    var dropdown = document.getElementById("langDropdown");
    dropdown.style.display = (dropdown.style.display === "block") ? "none" : "block";
}

// Translate function
function translateTo(lang) {
    var select = document.querySelector(".goog-te-combo");
    if (select) {
        select.value = lang;
        select.dispatchEvent(new Event("change"));
    }
}

// Close dropdown when clicking outside
document.addEventListener("click", function(e) {
    if (!e.target.closest(".lang-container")) {
        document.getElementById("langDropdown").style.display = "none";
    }
});
</script>

<script src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
""")