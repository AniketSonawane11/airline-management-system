# ✈️ Airline Management System

# Airline Management System

![Django CI](https://github.com/AniketSonawane11/airline-management-system/actions/workflows/django.yml/badge.svg)


A Django-based web application that manages airline operations like flight booking, passenger records, and airport tracking. Designed for learning and showcasing Django backend and testing skills.

---

## 🚀 Tech Stack

- **Backend**: Python, Django
- **Database**: SQLite3
- **Frontend**: HTML, CSS (with Bootstrap)
- **Testing**: Django Unit Test Framework
- **Tools**: VS Code, Git, GitHub

---

## 🔧 Features

- CRUD operations for **Flights**, **Passengers**, and **Airports**
- Relational mapping using Django ORM
- Admin dashboard to manage all records
- User-friendly interfaces with Bootstrap templates
- Automated unit tests with **100% test coverage**

---

## 📁 Project Structure

```bash
airline/
├── airline/           # Django project config
├── flights/           # App handling flight logic
│   ├── models.py
│   ├── views.py
│   ├── tests.py
│   ├── templates/
│   └── urls.py
├── templates/         # HTML files
├── db.sqlite3         # SQLite database
├── manage.py
└── requirements.txt
