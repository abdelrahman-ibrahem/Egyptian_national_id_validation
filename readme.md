# 🇪🇬 Egyptian National ID Validation API

## 📖 Project Description

A simple RESTful API built with Django and Django REST Framework that validates Egyptian National IDs and returns extracted data such as birth date, gender, and governorate.

---

## 🛠️ Dependencies

* **Django**
* **Django REST Framework**
* **drf-yasg** (for automatic Swagger documentation)

---

## 🚀 Getting Started

Follow these steps to set up and run the backend application:

### 1️⃣ Create a Virtual Environment

```bash
python3 -m venv env
```

* **For macOS/Linux:**

  ```bash
  source env/bin/activate
  ```

* **For Windows:**

  ```bash
  ./env/Scripts/activate
  ```

---

### 2️⃣ Install Project Requirements

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 4️⃣ Run the Development Server

```bash
python manage.py runserver
```

---

## 📖 API Documentation

Once the server is running, you can access the interactive API documentation via Swagger:

👉 [http://localhost:8000/swagger](http://localhost:8000/swagger)

---

## 🔐 Authentication Note

To access the validation endpoint:

1. **Login to obtain your token.**
2. In Swagger UI, click on **Authorize**.
3. Enter your token in the following format:

```
Token <your_token>
```

Then you’ll be able to test the validation endpoint securely.
