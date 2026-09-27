# Django Blog Application

A full-stack blog web application built with **Python and Django** that allows users to browse, search, filter, and comment on blog posts. Administrators can manage posts, categories, comments, and contact messages through Django Admin.

## 🚀 Features

### 📝 Blog Management

* Create, update, and manage blog posts through Django Admin
* Organize posts using categories
* View individual blog posts
* Display related posts

### 🔍 Search & Filtering

* Search blog posts by title and content
* Filter posts by category
* Combine search and category filters
* Preserve filters while navigating through pages

### 📄 Pagination

* Paginated blog post listing
* Previous and next navigation
* First and last page navigation
* Dynamic pagination links

### 💬 Comments

* Users can submit comments on blog posts
* Comments are stored in the database
* Display comments under individual posts
* Comment form validation

### 📩 Contact

* Contact form for visitors
* Contact messages are stored in the database
* Success/error notifications using Django Messages Framework
* Post-Redirect-Get pattern for form submission

### ℹ️ About Page

* Dedicated About page
* Responsive layout using the existing project design

### 🔐 Admin Management

Django Admin allows authorized staff to manage:

* Blog posts
* Categories
* Comments
* Contact messages

## 🛠️ Technologies Used

* **Python**
* **Django**
* **SQLite**
* **HTML5**
* **CSS3**
* **JavaScript**
* **Bootstrap**
* **Django Templates**
* **Django ORM**

## 📂 Project Structure

```text
myapp/
│
├── blog/
│   ├── migrations/
│   ├── templates/
│   │   └── blog/
│   │       ├── index.html
│   │       ├── detail.html
│   │       ├── about.html
│   │       ├── contact.html
│   │       └── ...
│   │
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── myapp/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── manage.py
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd <project-folder>
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install django
```

If a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

### 5. Apply Migrations

```bash
python myapp/manage.py migrate
```

### 6. Create a Superuser

```bash
python myapp/manage.py createsuperuser
```

Follow the prompts to create the administrator account.

### 7. Start the Development Server

```bash
python myapp/manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## 🔐 Django Admin

Open:

```text
http://127.0.0.1:8000/admin/
```

Log in using the superuser credentials.

From Django Admin, you can manage posts, categories, comments, and contact messages.

## 🧪 Testing

The project includes automated Django unit tests covering:

* Model behavior
* String representations
* Slug generation
* Pagination
* Search functionality
* Category filtering
* Post detail view
* Related posts
* Comment submission
* Contact form validation
* Contact messages
* About page

Run the tests using:

```bash
python myapp/manage.py test blog
```

### Test Result

```text
Ran 13 tests
OK
```

## 🌐 Main Routes

| Page    | URL        |
| ------- | ---------- |
| Home    | `/`        |
| About   | `/about`   |
| Contact | `/contact` |
| Admin   | `/admin/`  |

## 🎯 Project Purpose

The purpose of this project is to build a database-driven content publishing platform using Django.

It demonstrates practical implementation of:

* Django MVT architecture
* Django ORM
* CRUD operations
* Model relationships
* Forms and validation
* Search and filtering
* Pagination
* Comments
* Contact form processing
* Django Admin
* Automated testing

## 📌 Key Learning Outcomes

Through this project, I gained practical experience in developing a Django web application, connecting models with views and templates, handling forms, working with databases, implementing search and filtering, managing content through Django Admin, and writing automated tests.

## 👨‍💻 Author

**Barani Dharan A S B**

Python / Django Developer

GitHub:
https://github.com/BaraniDharanASB

```
```
