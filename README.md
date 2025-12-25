📌 Zone-Aware Field Report API (Django)
Backend Technical Assignment

📖 Project Overview

This project implements a Zone-Aware Field Report Backend API using Django and Django REST Framework.

The system allows Field Executives to submit field reports based on geographic coordinates, and Supervisors to review and take action on reports only within their assigned zones.

All business rules such as automatic zone detection, risk evaluation based on submission time, and role-based access control are strictly enforced at the backend level.

🎯 Objective

The purpose of this project is to demonstrate:

Clean backend design

Proper enforcement of business rules

Role-based access without third-party RBAC libraries

Scalable and maintainable Django REST architecture


| Technology            | Usage                      |
| --------------------- | -------------------------- |
| Python                | Backend language           |
| Django                | Web framework              |
| Django REST Framework | API development            |
| SQLite                | Database                   |
| Django Admin          | Configuration & management |


👥 User Roles
1️⃣ Field Executive

Can create field reports

Can view only their own submitted reports

Cannot approve or reject reports

2️⃣ Supervisor

Can view reports belonging to their assigned zone(s)

Can approve or reject reports

Cannot modify report content

Cannot approve/reject reports submitted by themselves

⚠️ Roles are implemented manually using Django Groups as required (no third-party RBAC).

🗺️ Zone Configuration

Zones define geographical boundaries and are fully database-driven.

Zone Attributes

Zone name

Minimum latitude

Maximum latitude

Minimum longitude

Maximum longitude

Assigned Supervisor

Zones are not hardcoded and can be modified through the admin panel.

📄 Field Report Model

Each field report contains:

Title

Description

Latitude

Longitude

Auto-assigned zone

Submitted by (User)

Submission timestamp

Risk flag (Boolean)

Status (PENDING, APPROVED, REJECTED)

📋 Business Rules Implemented

✔ Zone is auto-determined based on coordinates
✔ Reports outside configured zones are rejected
✔ Reports submitted after 6:00 PM are marked risky
✔ Risky reports require supervisor approval
✔ Supervisors can only access reports from their zone
✔ Supervisors cannot approve/reject their own reports


| Method | Endpoint                    | Description                        |
| ------ | --------------------------- | ---------------------------------- |
| POST   | `/api/reports/`             | Create a field report              |
| GET    | `/api/reports/my/`          | View own reports (Field Executive) |
| GET    | `/api/reports/zone/`        | View zone reports (Supervisor)     |
| PATCH  | `/api/reports/{id}/status/` | Approve / Reject report            |


⚙️ Project Setup Instructions
🔹 1. Clone Repository
git clone <repository-url>
cd <project-folder>

🔹 2. Create Virtual Environment
python -m venv venv


Activate (Windows):

venv\Scripts\activate

🔹 3. Install Dependencies
pip install django djangorestframework

🔹 4. Apply Migrations
python manage.py makemigrations
python manage.py migrate

🔹 5. Create Superuser
python manage.py createsuperuser

🔹 6. Run Server
python manage.py runserver


Open:

http://127.0.0.1:8000/admin/

🔐 Role & User Setup (Admin Panel)
Create Groups

FIELD_EXECUTIVE

SUPERVISOR

Create Test Users
| Username  | Groups                      |
| --------- | --------------------------- |
| fe_user   | FIELD_EXECUTIVE             |
| sup_user  | SUPERVISOR                  |
| both_user | FIELD_EXECUTIVE, SUPERVISOR |


✔ Active → Checked
❌ Staff → Unchecked
❌ Superuser → Unchecked

🧪 Testing Checklist (PDF Based)
Field Executive Tests

Create report inside zone → success

Create report outside zone → rejected

Reports after 6 PM → marked risky

View only own reports

Supervisor Tests

Cannot create reports

View reports only from assigned zone

Cannot approve own report

Can approve/reject valid reports

📦 Sample API Requests
Create Report
POST /api/reports/

{
  "title": "Site Visit",
  "description": "Routine inspection",
  "latitude": 15,
  "longitude": 15
}

Approve Report
PATCH /api/reports/1/status/

{
  "status": "APPROVED"
}

🧠 Design Decisions

Business logic handled in serializers and views

Zones assigned dynamically from DB

Minimal and clean data relationships

Security enforced at API level

🧩 Known Constraints

Authentication assumed via Django session or basic auth

One supervisor per zone (simplest valid relationship)

No frontend included (backend-only assignment)

✅ Evaluation Alignment

This project fulfills:

All business rules from the assignment

Clean and maintainable Django architecture

Role-based access control

RESTful API standards


👤 Author

Name: (Your Name)
Role: Backend Developer
Framework: Django / DRF
