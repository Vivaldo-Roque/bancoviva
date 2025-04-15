# 💰 Banco Viva – Django Project

Hello! This is a simple project built using the **Django** framework. It simulates a **bank account** system with basic **CRUD** operations (Create, Read, Update, Delete). I built it as part of my learning journey, and I'm sharing here what I’ve learned during the process.

🔗 **Test the live app**: [https://bancoviva.vercel.app/](https://bancoviva.vercel.app/)

---

## 🚀 What I learned from Django

While working on this project, I explored many of Django’s features. Here are some key things I learned:

- ✅ **What Django is** and how it simplifies web development with built-in tools.
- 🧱 Understanding the **MVT** architecture (Model-View-Template).
- 🧩 The difference between a **project** and an **app** in Django.
- 🛠️ How Django’s **ORM (Object-Relational Mapping)** works:
  - Creating tables and relationships.
  - Running migrations.
  - Performing CRUD operations through models.
- 🧬 Reusing **templates** via template inheritance.
- 🏷️ Using **template tags and filters**.
- 📄 Handling **HTML Forms** with Django:
  - Built-in validation.
  - Field and type customization.
  - Saving directly to the database.
- 🔐 Built-in **user authentication** system.
- 🌐 Defining **routes/URLs** with clarity and flexibility.

---

## 🛠️ Installation & Local Setup

### ✅ Requirements

- Python 3.10+
- pip
- virtualenv (optional, but recommended)

### 📥 Clone the repository

```bash
git clone https://github.com/your-username/banco-viva.git
cd banco-viva
```

### 📦 Install dependencies

```bash
pip install -r requirements.txt
```

### ⚙️ Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 👤 Create superuser (optional)

```bash
python manage.py createsuperuser
```

### ▶️ Start local server

```bash
python manage.py runserver
```

Open in your browser: `http://127.0.0.1:8000/`

---

## 🧰 Useful commands

```bash
# Create a new Django project
django-admin startproject myprojectname

# Create a new app inside the project
python manage.py startapp myappname

# Generate models from an existing database
python manage.py inspectdb > models.py

# Create and apply migrations
python manage.py makemigrations myappname
python manage.py migrate myappname

# Reset migrations (forced)
python manage.py migrate myappname zero --fake

# Create an empty migration with a custom name
python manage.py makemigrations myappname --name migration_name --empty

# Open Django interactive shell
python manage.py shell
```

---

## 🌐 Deploying to Vercel

This project was deployed to [Vercel](https://vercel.com/), which allows Python apps to be hosted with a few configuration tweaks.

### 🔧 Steps followed:

1. Create a Vercel account.
2. Push the project code to a GitHub repository.
3. Connect the repo to Vercel and create a new project.
4. Set environment variables like `DJANGO_SECRET_KEY`, `DEBUG`, etc.
5. Adjust the `settings.py` and add a `vercel.json` file if needed.

### 📚 Helpful deployment guides:

- [How to Host a Django App on Vercel for Free](https://www.makeuseof.com/django-app-vercel-host-free/)
- [Deploy Django on Vercel - DevMaesters](https://devmaesters.com/blog/15)

---

## 📬 Contributions & Feedback

This project was built as part of my learning journey, so **any feedback is welcome**!  
If you'd like to contribute, feel free to open an **issue** or submit a **pull request**.

---

## 🙌 Thanks!

Thanks for stopping by!  
I hope this project helps you understand Django better through a hands-on example. 😄
