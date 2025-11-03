# stylush
![image](https://github.com/simokamaa/stylush/assets/88234407/47aa3100-c005-4326-9ce9-089f1025f244)

Payroll system for stylush college
project link : http://stylushpayroll.pythonanywhere.com/

.The Project is developed using Django Python
.________________________________________________________________________________________
_________________Dependiences____________________________________________________________

Dependencies:

Python 3.11.1

Django 4.2.1

Reportlab 4.0.0

Bootstrap 5.3.0

Pillow 9.5.0

Django_require_login 1.1.2

fpdf

TinyMce 6.2.1

## Instructions to run and install
## ✅ Pre-requirements

Make sure you have the basics installed:

* Python (3.x)
* pip
* Git (`git clone`)
* Virtual environment tool (like `venv`)
* MySQL (if you will use MySQL) or SQLite (if you stick with it)
* If deploying via Coolify + Docker, make sure Docker/Compose is set up

---

## 🔄 Step-by-step: Clone & Run the Project

1. **Clone the repository**

   ```bash
   git clone https://github.com/simokamaa/<repo-name>.git
   cd <repo-name>
   ```

   Replace `<repo-name>` with the actual project directory you want from his account.

2. **Create and activate a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate       # on Linux/Mac
   # or on Windows:
   # venv\Scripts\activate
   ```

3. **Install dependencies**
   If there’s a `requirements.txt` in the repo:

   ```bash
   pip install -r requirements.txt
   ```

   If not, check `setup.py` or the README in the repo for dependencies.

4. **Database setup**

   * If using SQLite (default often): ensure `DATABASES` in `settings.py` is pointing to an sqlite file (e.g., `db.sqlite3`).
   * If using MySQL (which you are using elsewhere) update `settings.py` accordingly:

     ```python
     DATABASES = {
       'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': 'your_db_name',
         'USER': 'your_db_user',
         'PASSWORD': 'your_password',
         'HOST': 'localhost',
         'PORT': '3306',
       }
     }
     ```

   Then create the database in MySQL and grant appropriate permissions.

5. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (for the admin site)**

   ```bash
   python manage.py createsuperuser
   ```

   Provide username, email, password when prompted.

7. **Run the development server**

   ```bash
   python manage.py runserver
   ```

   Then open in your browser at `http://127.0.0.1:8000/` (or the IP/port given).


