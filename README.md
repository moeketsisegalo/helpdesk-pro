# HelpDesk Pro

A modern IT Help Desk Ticketing System built with Django and Bootstrap.

## Overview

HelpDesk Pro is a web-based ticket management platform designed to help organizations track, manage, and resolve IT support issues efficiently.

The system allows employees to submit support tickets while administrators can manage ticket statuses, monitor progress, and oversee all support requests from a centralized dashboard.

---

## Features

### Authentication

* Secure user login
* Role-based access control
* Administrator management

### Ticket Management

* Create support tickets
* View personal tickets
* Update ticket status
* Track ticket progress

### Dashboard Analytics

* Total Tickets
* Open Tickets
* In Progress Tickets
* Closed Tickets
* Ticket Status Chart

### User Interface

* Responsive Bootstrap design
* Sidebar navigation
* Dark Mode
* Professional dashboard
* Status badges

---

## Technologies Used

* Python
* Django
* Bootstrap 5
* Chart.js
* SQLite

---

## Installation

### Clone Repository

```bash
git clone git@github.com:moeketsisegalo/helpdesk-pro.git
cd helpdesk-pro
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000
```

---

## Future Enhancements

* PostgreSQL Support
* Email Notifications
* Technician Assignment
* SLA Tracking
* Advanced Reporting
* Export to PDF

---

## Developed By

TheDebuggers

Track Issues. Deliver Solutions.
