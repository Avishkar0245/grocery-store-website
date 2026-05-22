#!C:/Python312/python.exe
import cgi 
import cgitb 
cgitb.enable() 
print("Content-Type:text/html\n")
print("""
<!DOCTYPE html>
<html dir="ltr" lang="en">


<!-- Mirrored from themedesigner.in/demo/wrappixel/admin-template/xtreme/html/ltr/form-basic.html by HTTrack Website Copier/3.x [XR&CO'2014], Wed, 06 Jun 2018 05:49:08 GMT -->
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <!-- Tell the browser to be responsive to screen width -->
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <!-- Favicon icon -->
    <link rel="icon" type="image/png" sizes="16x16" href="../../assets/images/favicon.png">
    <title>Xtreme admin Template - The Ultimate Multipurpose admin template</title>
    <!-- Custom CSS -->
    <link href="../../dist/css/style.min.css" rel="stylesheet">
    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
    <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
<![endif]-->
</head>

<body >
    <!-- ============================================================== -->
    <!-- Preloader - style you can find in spinners.css -->
    <!-- ============================================================== -->
    <div class="preloader">
        <div class="lds-ripple">
            <div class="lds-pos"></div>
            <div class="lds-pos"></div>
        </div>
    </div>
    <!-- ============================================================== -->
    <!-- Main wrapper - style you can find in pages.scss -->
    <!-- ============================================================== -->
    <div id="main-wrapper">
        <!-- ============================================================== -->
        <!-- Topbar header - style you can find in pages.scss -->
        <!-- ============================================================== -->
        <header class="topbar" style="background:white">
            <nav class="navbar top-navbar navbar-expand-md navbar-dark">
                <div class="navbar-header" style="background:white">
                    <!-- This is for the sidebar toggle which is visible on mobile only -->
                    <a class="nav-toggler waves-effect waves-light d-block d-md-none" href="javascript:void(0)"><i class="ti-menu ti-close"></i></a>
                    <!-- ============================================================== -->
                    <!-- Logo -->
                    <!-- ============================================================== -->
                    <a class="navbar-brand" href="index.html">
                        <!-- Logo icon -->
                        <b class="logo-icon">
                            <!--You can put here icon as well // <i class="wi wi-sunset"></i> //-->
                            <!-- Dark Logo icon -->
                            <img src="" alt="homepage" class="dark-logo" />
                            <!-- Light Logo icon -->
                            <img src="logo.png" alt="homepage" class="light-logo" style="height: 120px;width: 120px;"/>
                        </b>
                        <!--End Logo icon -->
                        <!-- Logo text -->
                    
                    </a>
                    <!-- ============================================================== -->
                    <!-- End Logo -->
                    <!-- ============================================================== -->
                    <!-- ============================================================== -->
                    <!-- Toggle which is visible on mobile only -->
                    <!-- ============================================================== -->
                    <a class="topbartoggler d-block d-md-none waves-effect waves-light" href="javascript:void(0)" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><i class="ti-more"></i></a>
                </div>
                <!-- ============================================================== -->
                <!-- End Logo -->
      
                <!-- ============================================================== -->
                <div class="navbar-collapse collapse" id="navbarSupportedContent">
                    <!-- ============================================================== -->
                    <!-- toggle and nav items -->
                    <!-- ============================================================== -->
                    
                    <!-- ============================================================== -->
                    <!-- Right side toggle and nav items -->
                    <!-- ============================================================== -->
                    <ul class="navbar-nav float-right">
                        <!-- ============================================================== -->
                        <!-- create new -->
                        <!-- ============================================================== -->

                        
                        
                        <!-- ============================================================== -->
                        <!-- User profile and search -->
                        <!-- ============================================================== -->
                       
                        <!-- ============================================================== -->
                        <!-- User profile and search -->
                        <!-- ============================================================== -->
                    </ul>
                </div>
            </nav>
        </header>
        <!-- ============================================================== -->
        <!-- End Topbar header -->
        <!-- ============================================================== -->
        <!-- ============================================================== -->
        <!-- Left Sidebar - style you can find in sidebar.scss  -->
        <!-- ============================================================== -->
        <aside class="left-sidebar" style="background:#cb6744">
            <!-- Sidebar scroll-->
            <div class="scroll-sidebar">
                <!-- Sidebar navigation-->
                <nav class="sidebar-nav">
                    <ul id="sidebarnav" style="background:#cb6744">
                        <!-- User Profile-->
                        <li>
                            <!-- User Profile-->
                            <div class="user-profile d-flex no-block dropdown m-t-20">
                                <div class="user-pic"><img src="../../assets/images/users/1.jpg" alt="users" class="rounded-circle" width="40" /></div>
                                <div class="user-content hide-menu m-l-10">
                                    <a href="javascript:void(0)" class="" id="Userdd" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                        <h5 class="m-b-0 user-name font-medium"><span id="usernamedisplay"></span><i class="fa fa-angle-down"></i></h5>
                                        
                                    </a>
                                    <div class="dropdown-menu dropdown-menu-right" aria-labelledby="Userdd">
                                        <a class="dropdown-item" href="javascript:void(0)"><i class="ti-user m-r-5 m-l-5"></i> My Profile</a>
                                        <a class="dropdown-item" href="javascript:void(0)"><i class="ti-wallet m-r-5 m-l-5"></i> My Balance</a>
                                        <a class="dropdown-item" href="javascript:void(0)"><i class="ti-email m-r-5 m-l-5"></i> Inbox</a>
                                        <div class="dropdown-divider"></div>
                                        <a class="dropdown-item" href="javascript:void(0)"><i class="ti-settings m-r-5 m-l-5"></i> Account Setting</a>
                                        <div class="dropdown-divider"></div>
                                        <a class="dropdown-item" href="javascript:void(0)"><i class="fa fa-power-off m-r-5 m-l-5"></i> Logout</a>
                                    </div>
                                </div>
                            </div>
                            <!-- End User Profile-->
                        </li>
                       
                        <!-- User Profile-->
                        <li class="nav-small-cap"><i class="mdi mdi-dots-horizontal"></i> <span class="hide-menu">Product</span></li>
                        <li class="sidebar-item"> <a class="sidebar-link has-arrow waves-effect waves-dark" href="javascript:void(0)" aria-expanded="false"><i class="mdi mdi-view-dashboard"></i><span class="hide-menu">Product Master</span></a>
                            <ul aria-expanded="false" class="collapse  first-level" style="background:#cb6744">
                                <li class="sidebar-item"><a href="productmaster.py" class="sidebar-link"><i class="mdi mdi-adjust"></i><span class="hide-menu">Add</span></a></li>
                                <li class="sidebar-item"><a href="ProductList.py" class="sidebar-link"><i class="mdi mdi-adjust"></i><span class="hide-menu">List</span></a></li>
                                
                            </ul>
                        </li>
                         <li class="nav-small-cap"><i class="mdi mdi-dots-horizontal"></i> <span class="hide-menu">Categary</span></li>
                        <li class="sidebar-item"> <a class="sidebar-link has-arrow waves-effect waves-dark" href="javascript:void(0)" aria-expanded="false"><i class="mdi mdi-view-dashboard"></i><span class="hide-menu">Categary Master</span></a>
                            <ul aria-expanded="false" class="collapse  first-level" style="background:#cb6744">
                                <li class="sidebar-item"><a href="categary.py" class="sidebar-link"><i class="mdi mdi-adjust"></i><span class="hide-menu">Add</span></a></li>
                                <li class="sidebar-item"><a href="categaryList.py" class="sidebar-link"><i class="mdi mdi-adjust"></i><span class="hide-menu">List</span></a></li>
                                
                            </ul>
                        </li>
                             <li class="nav-small-cap"><i class="mdi mdi-dots-horizontal"></i> <span class="hide-menu">Logout</span></li>
                        <li class="sidebar-item"> <a class="sidebar-link has-arrow waves-effect waves-dark" href="javascript:void(0)" aria-expanded="false"><i class="mdi mdi-view-dashboard"></i><span class="hide-menu">Logout</span></a>
                            <ul aria-expanded="false" class="collapse  first-level" style="background:#cb6744">
                                <li class="sidebar-item"><a href="logout.py" class="sidebar-link"><i class="mdi mdi-adjust"></i><span class="hide-menu">logout</span></a></li>  
                              
                            </ul>
                        </li>
                         <li class="nav-small-cap"><i class="mdi mdi-dots-horizontal"></i> <span class="hide-menu">Change password</span></li>
                        <li class="sidebar-item"> <a class="sidebar-link has-arrow waves-effect waves-dark" href="javascript:void(0)" aria-expanded="false"><i class="mdi mdi-view-dashboard"></i><span class="hide-menu">Change password</span></a>
                            <ul aria-expanded="false" class="collapse  first-level" style="background:#cb6744">
                                <li class="sidebar-item"><a href="changepassword.py" id="changePasswordLink" class="sidebar-link"><i class="mdi mdi-adjust"></i><span class="hide-menu">Change Password</span></a></li>                                
                            </ul>
                        </li>
                             <li class="nav-small-cap"><i class="mdi mdi-dots-horizontal"></i> <span class="hide-menu">USER MASTER</span></li>
                        <li class="sidebar-item"> <a class="sidebar-link has-arrow waves-effect waves-dark" href="javascript:void(0)" aria-expanded="false"><i class="mdi mdi-view-dashboard"></i><span class="hide-menu">USER Master</span></a>
                            <ul aria-expanded="false" class="collapse  first-level" style="background:#cb6744">
                                <li class="sidebar-item"><a href="userlist.py" class="sidebar-link"><i class="mdi mdi-adjust"></i><span class="hide-menu">List</span></a></li>
                                
                            </ul>
                        </li>
                     <li class="nav-small-cap"><i class="mdi mdi-dots-horizontal"></i> <span class="hide-menu">ENQUIRY MASTER</span></li>
                        <li class="sidebar-item"> <a class="sidebar-link has-arrow waves-effect waves-dark" href="javascript:void(0)" aria-expanded="false"><i class="mdi mdi-view-dashboard"></i><span class="hide-menu">enquiry Master</span></a>
                            <ul aria-expanded="false" class="collapse  first-level" style="background:#cb6744">
                                <li class="sidebar-item"><a href="enquiry.py" class="sidebar-link"><i class="mdi mdi-adjust"></i><span class="hide-menu">List</span></a></li>
                                
                            </ul>
                        </li>
                        <li class="nav-small-cap"><i class="mdi mdi-dots-horizontal"></i> <span class="hide-menu">ORDER MASTER</span></li>
                        <li class="sidebar-item"> <a class="sidebar-link has-arrow waves-effect waves-dark" href="javascript:void(0)" aria-expanded="false"><i class="mdi mdi-view-dashboard"></i><span class="hide-menu">order Master</span></a>
                            <ul aria-expanded="false" class="collapse  first-level" style="background:#cb6744">
                                <li class="sidebar-item"><a href="ordermaster.py" class="sidebar-link"><i class="mdi mdi-adjust"></i><span class="hide-menu">List</span></a></li>
                                
                            </ul>
                        </li>
                         <li class="nav-small-cap"><i class="mdi mdi-dots-horizontal"></i> <span class="hide-menu">ORDER MASTER</span></li>
                        <li class="sidebar-item"> <a class="sidebar-link has-arrow waves-effect waves-dark" href="javascript:void(0)" aria-expanded="false"><i class="mdi mdi-view-dashboard"></i><span class="hide-menu">order Master</span></a>
                            <ul aria-expanded="false" class="collapse  first-level" style="background:#cb6744">
                                <li class="sidebar-item"><a href="ordermaster.py" class="sidebar-link"><i class="mdi mdi-adjust"></i><span class="hide-menu">List</span></a></li>
                                
                            </ul>
                        </li> <li class="nav-small-cap"><i class="mdi mdi-dots-horizontal"></i> <span class="hide-menu">cms MASTER</span></li>
                        <li class="sidebar-item"> <a class="sidebar-link has-arrow waves-effect waves-dark" href="javascript:void(0)" aria-expanded="false"><i class="mdi mdi-view-dashboard"></i><span class="hide-menu">cms Master</span></a>
                            <ul aria-expanded="false" class="collapse  first-level" style="background:#cb6744">
                                <li class="sidebar-item"><a href="cmsmaster.py" class="sidebar-link"><i class="mdi mdi-adjust"></i><span class="hide-menu">List</span></a></li>
                                
                            </ul>
                        </li>
                         </li> <li class="nav-small-cap"><i class="mdi mdi-dots-horizontal"></i> <span class="hide-menu">ORDER COMPLETE</span></li>
                        <li class="sidebar-item"> <a class="sidebar-link has-arrow waves-effect waves-dark" href="javascript:void(0)" aria-expanded="false"><i class="mdi mdi-view-dashboard"></i><span class="hide-menu">ORDER COMPLETE</span></a>
                            <ul aria-expanded="false" class="collapse  first-level" style="background:#cb6744">
                                <li class="sidebar-item"><a href="ordercomplete.py" class="sidebar-link"><i class="mdi mdi-adjust"></i><span class="hide-menu">List</span></a></li>
                                
                            </ul>
                        </li>
                            <li class="nav-small-cap"><i class="mdi mdi-dots-horizontal"></i> <span class="hide-menu">UNIT MASTER</span></li>
                        <li class="sidebar-item"> <a class="sidebar-link has-arrow waves-effect waves-dark" href="javascript:void(0)" aria-expanded="false"><i class="mdi mdi-view-dashboard"></i><span class="hide-menu">UNIT Master</span></a>
                            <ul aria-expanded="false" class="collapse  first-level" style="background:#cb6744">
                                <li class="sidebar-item"><a href="unitmaster.py" class="sidebar-link"><i class="mdi mdi-adjust"></i><span class="hide-menu">Add</span></a></li>
                                <li class="sidebar-item"><a href="unitmasterList.py" class="sidebar-link"><i class="mdi mdi-adjust"></i><span class="hide-menu">List</span></a></li>
                                
                            </ul>
                        </li> 
                          <li class="nav-small-cap"><i class="mdi mdi-dots-horizontal"></i> <span class="hide-menu">repeted order</span></li>
                        <li class="sidebar-item"> <a class="sidebar-link has-arrow waves-effect waves-dark" href="javascript:void(0)" aria-expanded="false"><i class="mdi mdi-view-dashboard"></i><span class="hide-menu">repeter order</span></a>
                            <ul aria-expanded="false" class="collapse  first-level" style="background:#cb6744">
                                <li class="sidebar-item"><a href="repeterorder.py" class="sidebar-link"><i class="mdi mdi-adjust"></i><span class="hide-menu">List</span></a></li>
                                
                            </ul>
                        </li> 
                    </ul>
                  
         
                </nav>
                <!-- End Sidebar navigation -->
            </div>
            <!-- End Sidebar scroll-->
        </aside>
      <script>
      var username=localStorage.getItem("username");
      var id=localStorage.getItem("id");
      console.log(id)

      document.getElementById("usernamedisplay").innerText=username;

      var link = document.getElementById("changePasswordLink");
      console.log(link);
      link.href = "changepassword.py?userid=" + encodeURIComponent(id);
      
      </script>
""")