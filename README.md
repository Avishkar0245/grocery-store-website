# 🛒 Grocery Store Website

A full-stack online grocery store built with **Python (CGI)**, **MySQL**, and **HTML/CSS/JavaScript**. Users can register, log in, browse products by category, add items to a cart or wishlist, place orders, and manage their profile.

---

## ✨ Features

- **User authentication** – registration (with profile photo upload), login, logout
- **Product browsing** – category pages, product details, search
- **Sorting** – price low → high and high → low
- **Deals of the Day** – highlighted discounted products
- **Cart** – add items, view cart, delete items, quantity-based totals
- **Wishlist** – save products for later
- **Checkout & Orders** – place orders and view order history (`My Orders`)
- **My Profile** – view and update personal details and photo
- **Static pages** – About Us and Contact (contact form saved to database)
- **CMS-driven content** – About page content loaded from the database

---

## 🧰 Tech Stack

| Layer       | Technology                                   |
| ----------- | -------------------------------------------- |
| Frontend    | HTML5, CSS3, JavaScript, Bootstrap           |
| Backend     | Python 3.12 (CGI scripts)                    |
| Database    | MySQL (`mysql-connector-python`)             |
| Server      | Apache via XAMPP                             |

---

## 📁 Project Structure

```
grocery-store-website/
├── index.py               # Home page
├── login.py / loginbackend.py
├── regestration.html / registrationbackend.py
├── logout.py
├── categary.py / categarydetail.py
├── product.py / productdetails.py
├── dealsofday.py
├── lowtohightprice.py / hightolowprice.py
├── search.py
├── cart.py / cartdetail.py / deletecartitem.py
├── mywishlist.py / mywishlistdetail.py
├── checkout.py / myorders.py
├── myprofile.py / myprofilebackend.py
├── about.py / contact.py / contactbackend.py
├── header.py / footer.py  # Shared layout components
├── assets/                # CSS, JS, fonts, images
├── dist/                  # Icon and style libraries
├── html/                  # Template assets
└── User/                  # Uploaded user profile photos
```

---

## 🗄️ Database

Database name: **`grocery`**

Tables used by the application:

| Table           | Purpose                                  |
| --------------- | ---------------------------------------- |
| `regestration`  | Registered users                         |
| `categary`      | Product categories                       |
| `products`      | Product catalogue (incl. `dealsofday`)   |
| `cart`          | Items in a user's cart                   |
| `wishlist`      | Items saved by a user                    |
| `ordermaster`   | Order headers (user, total, status)      |
| `order_detalis` | Line items for each order                |
| `contact`       | Contact form submissions                 |
| `cms`           | Editable page content (About page)       |

> The default connection settings in the scripts are `host=localhost`, `user=root`, `password=""`, `database=grocery`. Change them if your MySQL setup is different.

---

## 🚀 Getting Started

### Prerequisites

- [XAMPP](https://www.apachefriends.org/) (Apache + MySQL)
- Python 3.12
- MySQL connector:
  ```bash
  pip install mysql-connector-python
  ```

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/grocery-store-website.git
   ```

2. **Copy the project** into your XAMPP CGI folder, for example:
   ```
   C:\xampp\htdocs\grocery-store-website\
   ```

3. **Enable Python CGI in Apache** – add this to `httpd.conf` (or `.htaccess`) so `.py` files run as CGI:
   ```apache
   AddHandler cgi-script .py
   Options +ExecCGI
   ```

4. **Check the shebang line** at the top of each `.py` file. It points to the Python install path:
   ```
   #!C:/Python312/python.exe
   ```
   Update it if Python is installed elsewhere.

5. **Create the database**
   - Start Apache and MySQL from the XAMPP Control Panel
   - Open `http://localhost/phpmyadmin`
   - Create a database named `grocery` and create/import the tables listed above

6. **Run the app** – open in your browser:
   ```
   http://localhost/grocery-store-website/index.py
   ```

---

## 📸 Screenshots

_Add screenshots of the home page, product listing, cart, and checkout here._

---

## 🔮 Future Improvements

- Use parameterized SQL queries to prevent SQL injection
- Hash passwords (e.g., bcrypt) instead of storing plain text
- Server-side sessions instead of `localStorage`
- Admin panel for managing products, categories, and orders
- Online payment gateway integration
- Migrate to a framework such as Flask

---

## 👤 Author

**Avishkar**
MCA Student | Full Stack Developer

---

## 📄 License

This project is for educational purposes.
