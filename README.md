# SmartCare HMS

SmartCare HMS is a role-based **Hospital Management System** built with **Django**.  
It is designed to digitize hospital workflows such as patient registration, doctor approval, appointment booking, prescription management, report follow-up, diagnostic test reporting, receptionist operations, and basic patient health guidance through **MediBot**.

---

## Project Overview

**SmartCare HMS** is a web-based healthcare management platform that connects **patients, doctors, receptionists, and administrators** in one integrated system.

The main goal of this project is to reduce manual hospital workload, improve service efficiency, organize patient care, and create a cleaner digital workflow for both patients and healthcare staff.

This system allows patients to book appointments, doctors to manage consultations and prescriptions, receptionists to handle walk-in patients and test reports, and administrators to monitor and control the overall hospital system.

---

## Main Purpose of the Project

The purpose of SmartCare HMS is to create a complete digital hospital management solution where different users can perform their tasks according to their roles.

The system helps to:

- Reduce manual paperwork
- Manage hospital appointments digitally
- Improve communication between patients and doctors
- Support receptionist-based hospital workflow
- Store prescriptions and reports in an organized way
- Help patients with basic symptom guidance through MediBot
- Maintain role-based access and secure system control

---

## User Roles

The system supports four main user roles:

1. **Admin**
2. **Doctor**
3. **Patient**
4. **Receptionist**

Each role has a separate dashboard and access permission.  
This makes the system more secure, organized, and easy to manage.

---

## Key Features

### Patient Module

The patient module allows patients to register, log in, search doctors, book appointments, view prescriptions, upload reports, and get basic health guidance.

Main features:

- Patient registration and login
- Patient profile management
- Browse doctors by details and availability
- Book appointments with available doctors
- View appointment history
- View prescription records
- Upload follow-up reports
- Submit previous prescription and medical report files
- Receive receptionist messages
- Use MediBot for basic symptom guidance

---

### Doctor Module

The doctor module allows doctors to manage their appointments, review reports, create prescriptions, and manage patient follow-up activities.

Main features:

- Doctor registration and login
- Admin approval required before access
- Doctor dashboard with overview
- Manage pending appointments
- View assigned appointments
- Mark appointments as completed
- Create prescriptions
- Add medicine, test, and advice
- Review patient follow-up reports
- Update report responses
- View patient history
- Bookmark patients for follow-up care
- Manage doctor profile and availability

---

### Receptionist Module

The receptionist module is designed for front-desk hospital operations. Receptionists can create appointments, handle walk-in patients, manage test reports, and communicate approximate appointment times to patients.

Main features:

- Receptionist login
- Receptionist dashboard with overview
- Create appointments for registered patients
- Register walk-in patients and create instant appointments
- Assign doctors to appointments
- Manage doctor availability
- View doctors and patients
- View all appointments
- Update appointment status
- Send appointment messages to patients
- Generate diagnostic test reports
- Select multiple medical tests
- Calculate total test cost automatically
- View and print test reports
- Manage receptionist profile

---

### Admin Module

The admin module controls the whole system. Admin can approve doctors, monitor users, manage appointments, and access system-level information.

Main features:

- Admin login
- Admin dashboard
- Manage patients
- Manage doctors
- Approve or reject doctor registration requests
- Manage receptionists
- View appointments
- Monitor contact messages
- Add doctor, patient, or receptionist manually
- System-level overview and control

---

## Core Modules

SmartCare HMS includes the following important modules:

- Role-Based Authentication Module
- Patient Management Module
- Doctor Management Module
- Receptionist Management Module
- Admin Management Module
- Appointment Management Module
- Prescription Management Module
- Follow-up Report Module
- Diagnostic Test Report Module
- Contact Message Module
- Doctor Approval Workflow
- MediBot Patient Support Module

---

## Appointment Management

The appointment system supports both patient-side booking and receptionist-side appointment creation.

Appointment features include:

- Patient can book appointment by selecting doctor and date
- Receptionist can create appointment for registered patients
- Receptionist can create walk-in patient with instant appointment
- Doctor receives assigned appointments
- Appointment status can be updated
- Receptionist can assign approximate appointment time
- Doctor can mark appointment as completed
- Expired appointments can be handled based on date and time

---

## Prescription Management

Doctors can create prescriptions after consultation.

Prescription features include:

- Add prescription text
- Add medical tests
- Add advice
- Link prescription with appointment
- Patient can view prescription history
- Doctor can check whether prescription already exists for an appointment

---

## Report Follow-up Module

Patients can submit medical reports for doctor review.

Report follow-up features include:

- Patient can select doctor
- Patient can upload previous prescription
- Patient can upload report file
- Patient can add report note
- Doctor can view submitted report
- Doctor can review previous prescription
- Doctor can update report response
- Doctor can provide updated prescription, test, and advice

---

## Diagnostic Test Report Module

Receptionists can create diagnostic test reports for patients.

Test report features include:

- Add patient name, age, gender, and contact number
- Select one or multiple diagnostic tests
- Search tests from custom multi-select dropdown
- Calculate total cost automatically
- Save selected test items
- View test report details
- Print report copy
- Maintain report records

---

## MediBot Module

MediBot is a basic patient support feature that provides initial health guidance.

MediBot can help patients with:

- Basic symptom-related guidance
- General health suggestions
- Initial support before consultation
- Patient-friendly healthcare interaction

> MediBot is not a replacement for professional medical advice. It is only a basic guidance feature.

---

## Technology Stack

### Frontend

- HTML
- CSS
- JavaScript
- Bootstrap
- Bootstrap Icons
- Django Templates

### Backend

- Python
- Django

### Database

- SQLite for local development
- PostgreSQL recommended for deployment

### Tools and Version Control

- Git
- GitHub
- VS Code
- Render for deployment

---

## Security Features

SmartCare HMS includes multiple security features provided by Django and custom role-based logic.

Security features:

- Role-Based Access Control
- Django authentication system
- Password hashing
- CSRF protection
- Session management
- Login-required protected pages
- User permission checking
- Doctor approval validation
- Form validation
- Controlled error messages
- Separate dashboard access for each role

---

## System Architecture

The system follows a layered architecture:

### 1. Presentation Layer

This layer contains the user interface of the system.

Examples:

- Home page
- Login page
- Registration page
- Patient dashboard
- Doctor dashboard
- Receptionist dashboard
- Admin dashboard
- Appointment pages
- Prescription pages
- Report pages

### 2. Application Layer

This layer handles request and response logic using Django.

Examples:

- Django views
- URL routing
- Forms
- Authentication logic
- Validation logic

### 3. Business Logic Layer

This layer contains the main hospital workflow logic.

Examples:

- Appointment booking
- Prescription creation
- Doctor approval
- Report review
- Test report generation
- Receptionist appointment handling
- MediBot support

### 4. Data Layer

This layer manages database operations.

Examples:

- Django models
- Django ORM
- SQLite database
- PostgreSQL for production

### 5. Security Layer

This layer protects the system from unauthorized access.

Examples:

- Login validation
- Role checking
- CSRF protection
- Password hashing
- Session-based access

---

## Project Objectives

The main objectives of this project are:

- To transform manual hospital management into a digital system
- To create separate dashboards for patients, doctors, receptionists, and admins
- To simplify appointment booking and appointment handling
- To improve doctor-patient communication
- To manage prescriptions digitally
- To support follow-up report submission and review
- To help receptionists manage walk-in patients and test reports
- To provide basic health guidance using MediBot
- To improve security using role-based access control
- To make hospital workflow faster, cleaner, and more organized

---

## Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/SmartCare-HMS.git

## Screenshots

Add your real project screenshots inside a `screenshots/` folder.

Example:

## Screenshots

###Home Page
![Home Page](screenshots/home.png)

### About Page
![About Page](screenshots/about.png)

### Contact Page
![Contact Page](screenshots/contact.png)

### Role-Based login Page
![Role-Based login Page](screenshots/role_based_login.png)

### Patient Dashboard Page
![Patient Dashboard Page](screenshots/patient-dashboard.png)

### Patient Profile Page
![Patient Profile Page](screenshots/patient_profile.png)

### Patient Medibot Page
![Patient Medibot Page](screenshots/medibot.png)

### Patient Follor-Up_Report Page
![Patient Follor-Up_Report Page](screenshots/follow_up_report.png)

### Patient Appointment-Book Page
![Patient Appointment-Book Page](screenshots/appointment_book.png)

### Patient Prescription_View Page
![Patient Prescription_View Page](screenshots/prescription_record.png)

### Doctor Dashboard Page
![Doctor Dashboard Page](screenshots/doctor-dashboard.png)

### Doctor Dashboard Page
![Doctor Dashboard Page](screenshots/doctor-dashboard.png)

### Doctor Prescription Creation Page
![Doctor Prescription Creation Page](screenshots/prescription_creation.png)

### Receptionist Dashboard
![Receptionist Dashboard](screenshots/receptionist-dashboard.png)

### Receptionist Appointment Create Page
![Receptionist  Appointment Create Page](screenshots/appointment_create.png)

### Receptionist Doctor Available  Page
![Receptionist  Doctor Available Page](screenshots/doctor_availability.png)

### Receptionist Walk-In-Patient Page
![Receptionist  Walk-In-Patient Page](screenshots/walkinpaitent.png)

### Admin Dashboard
![Admin Dashboard](screenshots/admin-dashboard.png)
