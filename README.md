# 📦 Inventory Management System (Flask API)

## 📌 Project Description

This is a RESTful API built using Flask for managing an inventory system.
It supports authentication, role-based access control, product management, inventory tracking, and stock transactions.

---

## 🚀 Features

* 🔐 User Authentication (Register/Login)
* 🔑 Role-Based Access Control (Admin/User)
* 📦 Product Management (CRUD)
* 🏷 Category Management
* 🚚 Supplier Management
* 📊 Inventory Tracking
* 🔄 Stock Transactions (Stock In / Stock Out)
* 📡 RESTful API with JSON responses

---

## 🛠 Tech Stack

* Python (Flask)
* Flask-SQLAlchemy
* Flask-Migrate
* Flask-JWT-Extended
* Marshmallow
* SQLite

---

## ⚙️ Installation

```bash
git clone <your-repo-link>
cd inventory_system
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🗄 Database Setup

```bash
flask db init
flask db migrate -m "initial"
flask db upgrade
```

---

## ▶️ Run Server

```bash
flask run
```

Server runs at:

```
http://127.0.0.1:5000
```

---

## Authentication

### Register

POST `/auth/register`

```json
{
  "username": "admin",
  "password": "123456",
  "role": "admin"
}
```

---

### Login

POST `/auth/login`

```json
{
  "username": "admin",
  "password": "123456"
}
```

---

## API Endpoints

### Products

* GET `/products/`
* POST `/products/`
* GET `/products/<id>`
* PUT `/products/<id>`
* DELETE `/products/<id>`

---

### Categories

* POST `/categories/`
* GET `/categories/`

---

### Suppliers

* POST `/suppliers/`
* GET `/suppliers/`

---

### Stock Transactions

* POST `/stock-transactions/`

---

##  Known Issues

* Some migration inconsistencies may require database reset during development
* Inventory table must exist before creating products
* Ensure correct endpoint formatting (trailing slash `/`)

---

##  Notes

* Admin users are required to create products
* JWT token must be included in headers:

```
Authorization: Bearer <your_token>
```

---

##  Author

Bakari Abdulnasir
Mzee 001 
