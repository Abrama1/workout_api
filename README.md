# **🏋️‍♂️ Workout Tracker API**
> A **Django REST API** for managing **workout plans, exercises, and fitness tracking**.

![Django](https://img.shields.io/badge/Django-REST%20API-green?style=for-the-badge&logo=django) 
![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python) 
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge&logo=postgresql)

---

## **📌 Features**
✅ **User Authentication** (JWT-based Login & Registration)  
✅ **Manage Workout Plans** (CRUD API for creating workout plans)  
✅ **Predefined Exercises** (20+ exercises preloaded)  
✅ **Fitness Goals Tracking** (Set weight loss & muscle gain goals)  
✅ **Swagger API Documentation**  

---

## **📌 Getting Started**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/workout-tracker-api.git
cd workout-tracker-api
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Configure Database**
Modify `workout_api/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'workout_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### **5️⃣ Run Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **6️⃣ Create Superuser**
```bash
python manage.py createsuperuser
```

### **7️⃣ Start the Server**
```bash
python manage.py runserver
```
API will be available at **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**.

---

## **📌 API Endpoints**
### **🔐 Authentication**
| Endpoint              | Method | Description                |
|-----------------------|--------|----------------------------|
| `/api/auth/register/` | `POST` | Register a new user        |
| `/api/auth/login/`    | `POST` | Login and get JWT token    |

### **🏋️‍♂️ Workout Plans**
| Endpoint                        | Method | Description                      |
|----------------------------------|--------|----------------------------------|
| `/api/workouts/workout-plans/`  | `GET`  | Get all workout plans (Auth required) |
| `/api/workouts/workout-plans/`  | `POST` | Create a workout plan (Auth required) |

### **🏃‍♂️ Fitness Goals**
| Endpoint                         | Method | Description              |
|-----------------------------------|--------|--------------------------|
| `/api/workouts/fitness-goals/`   | `GET`  | Get fitness goals        |
| `/api/workouts/fitness-goals/`   | `POST` | Set a new fitness goal   |

---

## **📌 API Testing**
You can test the API using:
- **Postman** (Recommended)
- **cURL**
- **Swagger UI** → Visit:  
  ```
  http://127.0.0.1:8000/swagger/
  ```

---
