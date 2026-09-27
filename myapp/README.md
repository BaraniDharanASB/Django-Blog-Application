# Django Blog Application

A full-featured Django blog web application built with Python, Django 5, and Bootstrap 5.

## Features Implemented

- **Blog Post Listing & Pagination**: Responsive grid layout with dynamic pagination (5 posts per page).
- **Search & Category Filtering**: Full-text keyword search across post titles/content and filter posts by category while preserving search parameters during pagination.
- **Article Details & Comments**: Detailed post view with related post recommendations and an interactive comment section with input validation and instant feedback.
- **Contact Form**: Contact submission handling following the POST-Redirect-Get (PRG) pattern with database storage (`ContactMessage` model) and user feedback using the Django Messages framework.
- **About Page**: Informative static page integrated into top-level site navigation.
- **Django Admin & Permissions**: Model registration for Categories, Posts, Comments, and Contact Messages with search, filtering, and prepopulated slug generation for staff post management.
- **Automated Testing**: 13 unit tests covering models, slug generation, views, pagination, search, category filtering, contact form PRG flow, comment submission, and 404 handler.

---

## Setup & Running Instructions

### Prerequisites
- Python 3.10+
- Virtual environment (`env`)

### Installation & Execution

1. **Activate Virtual Environment & Navigate to App Directory**:
   ```powershell
   cd c:\Users\Nivet\OneDrive\Desktop\Django\workspace\myapp
   ..\env\Scripts\activate
   ```

2. **Apply Database Migrations**:
   ```powershell
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Populate Initial Data (Optional)**:
   ```powershell
   python manage.py populate_categories
   python manage.py populate_posts
   ```

4. **Run Unit Tests**:
   ```powershell
   python manage.py test blog
   ```

5. **Start Development Server**:
   ```powershell
   python manage.py runserver
   ```
   Access the application at `http://127.0.0.1:8000/blog/`.

---

## Django Admin Management

To manage posts and categories:
1. Create a superuser:
   ```powershell
   python manage.py createsuperuser
   ```
2. Log in at `http://127.0.0.1:8000/admin/` to create, edit, or delete categories, posts, comments, and contact messages.
