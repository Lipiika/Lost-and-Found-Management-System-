# Lost and Found Management System

A Django-based web application to help users report, search, and manage lost and found items easily.

## Features

- User registration and login system (with separate user and admin roles)
- User dashboard to submit lost item reports and search for found items
- Admin dashboard to manage all lost and found items
- Responsive and user-friendly interface
- Secure authentication and session management

## Technologies Used

- Python 3.x
- Django 4.x
- SQLite (default database)
- HTML, CSS for frontend templates

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Lipiika/Lost-and-Found-Management-System-.git
   cd Lost-and-Found-Management-System-
Create and activate a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv env
# Windows
env\Scripts\activate
# macOS/Linux
source env/bin/activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run database migrations:

bash
Copy
Edit
python manage.py migrate
Create a superuser (admin account):

bash
Copy
Edit
python manage.py createsuperuser
Run the development server:

bash
Copy
Edit
python manage.py runserver
