#  Product Review System – Backend API

This is a RESTful API backend built with Django and Django REST Framework (DRF) that allows:
- Admin users to manage products
- Regular users to submit reviews
- All users to view product information and ratings

---

##  Features

### ✅ User Authentication
- JWT-based authentication (`access` and `refresh` tokens)
- Role-based access: Admin vs. Regular Users

### ✅ Product Management
- Admins can **create**, **update**, and **delete** products
- Regular users can only **view** products

### ✅ Review System
- Authenticated users can submit **one review per product**
- Reviews contain a **rating (1–5)** and **text feedback**
- Each product displays its **average rating**
- Duplicate reviews per product by the same user are not allowed

---

##  Technologies Used

- Django 4.1.x
- Django REST Framework
- djangorestframework-simplejwt (JWT Authentication)
- drf-nested-routers (for nested review routes)

---

##  Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/product-review-system.git
cd product-review-system

# 2. Create & activate virtual environment (optional but recommended)
conda create -n reviewenv python=3.12 -y
conda activate reviewenv

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py makemigrations
python manage.py migrate

# 5. Create admin user
python manage.py createsuperuser

# 6. Start development server
python manage.py runserver
