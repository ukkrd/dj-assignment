# Django REST Framework API Project

## Project Setup and Usage

### Step 1: Clone the Project

```bash
git clone https://github.com/ukkrd/dj-assignment.git
cd dj-assignment
```

### Step 2: Setup Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate    # For Windows
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Database

* Open `settings.py` and configure your MySQL database credentials.

### Step 5: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Run the Project

```bash
python manage.py runserver
```

### Step 7: Test User Registration API

* Use the API documentation to hit the user registration endpoint and create a user.

### Step 8: Perform CRUD Operations for Tasks

* Now you can create, read, update, delete tasks using the Task API endpoints as described in the documentation.

---

## Project Overview

This project is a Task Management System using Django REST Framework. It allows users to register, login, manage tasks, and perform role-based permissions operations.

## Key Features

* JWT Authentication
* Role-based Permissions (Admin, Employee)
* Task CRUD operations
* Pagination and filtering of tasks
* Session management
