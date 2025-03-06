## 🛒 Commerce - Online Auction Platform

#### 🔗 Live Demo: [Try the App Here](https://commerce-auctions.onrender.com)

---

## 📜 Overview

Commerce is an online auction web application built with Django and JavaScript. Users can create listings, place bids, add items to their watchlist, and leave comments. The app dynamically updates content using JavaScript, ensuring a seamless user experience.

---

### 🚀 Features

**User Authentication** – Register and log in to manage listings and bids

**Create Listings** – Start an auction with a title, description, price, and optional image

**Active Listings** – View all currently active auctions

**Bidding System** – Users can bid on listings, ensuring the highest bid wins

**Watchlist** – Save favorite auctions for quick access

**Comments** – Engage with listings by adding comments

**Categories** – Browse listings by category

**Close Auctions** – The creator can close an auction and declare a winner

**Django Admin Panel** – Admins can manage listings, bids, and comments

---

### 🛠️ Installation & Setup

#### Clone the repository:
```sh
git clone https://github.com/Martina-Talan/commerce.git
cd commerce
```
#### Install dependencies:
```sh
pip install -r requirements.txt
```
#### Apply database migrations:
```sh
python manage.py makemigrations auctions
python manage.py migrate
```
#### Create a superuser (optional for admin access):
```sh
python manage.py createsuperuser
```
#### Start the development server:
```sh
python manage.py runserver
```
Open the app in your browser: http://127.0.0.1:8000/

---

### 📌 Usage

1️⃣ **Register/Login** – Create an account and sign in

2️⃣ **Create & Manage Listings** – Start auctions with a title, description, and image

3️⃣ **Place Bids** – Submit bids higher than the current price

4️⃣ **Watchlist** – Add listings to a watchlist for easy access

5️⃣ **Comment on Listings** – Engage by commenting on auction pages

6️⃣ **Browse by Category** – View all active auctions by category

7️⃣ **Close Auctions** – Listing creators can close auctions and declare a winner

---

### 🔗 API Routes

| Method | Endpoint | Description |
|--------|---------|-------------|
| GET    | `/listings` | Fetch all active listings |
| GET    | `/listings/<int:listing_id>` | Retrieve details of a single listing |
| POST   | `/listings/new` | Create a new auction listing |
| POST   | `/bids/<int:listing_id>` | Place a new bid on a listing |
| PUT    | `/listings/<int:listing_id>/close` | Close an auction and declare a winner |
| POST   | `/comments/<int:listing_id>` | Add a comment to a listing |
| GET    | `/watchlist` | Retrieve the user’s watchlist |
| POST   | `/watchlist/<int:listing_id>` | Add/remove a listing from the watchlist |

---

### 🛠️ Technologies Used
- __Django__ – Backend framework
- __JavaScript__  – Dynamic UI updates
- __HTML & CSS__ – Frontend structure and styling
- __Bootstrap__ – Responsive design

---

### 🏆 Acknowledgments
This project is part of the Harvard CS50W: Web Programming with Python and JavaScript course.

