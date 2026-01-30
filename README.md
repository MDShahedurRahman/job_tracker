# Job Application Tracker (MVC - Python CLI)

A clean, modular Job Application Tracking System built using Python and MVC architecture.  
This project helps track job applications, interview stages, follow-ups, and analytics using a command-line interface and JSON-based persistence.

This is a portfolio-quality backend-style project designed for clean architecture, commit discipline, and interview discussion.

---

## 🚀 Features

- Add job applications  
- Update job status  
- Delete job entries  
- View all applications  
- Filter by company  
- Filter by status  
- Upcoming interview reminders  
- Analytics summary  
- JSON-based persistent storage  
- Clean MVC separation  

---

## 🏗 Project Architecture (MVC)

```
job_tracker/
│
├── main.py
│
├── controllers/
│   └── job_controller.py
│
├── models/
│   └── job_application.py
│
├── services/
│   └── job_service.py
│
├── repositories/
│   └── job_repository.py
│
├── views/
│   └── job_view.py
│
├── utils/
│   ├── date_utils.py
│   └── validation_utils.py
│
└── data/
    └── jobs.json
```

## ⚙️ Installation

### Prerequisites

```
- Python 3.8+
```

### Setup

```
git clone https://github.com/yourusername/job-application-tracker.git
cd job-application-tracker
python main.py
```

## ▶️ Usage

### Run:

```
python main.py
```

### You will see:

```
1. Add Job
2. View All Jobs
3. Update Status
4. Delete Job
5. Filter by Company
6. Filter by Status
7. Upcoming Interviews
8. Analytics Summary
0. Exit
```
