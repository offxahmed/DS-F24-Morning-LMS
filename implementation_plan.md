# Implementation Plan - DS'F24 Morning Portal

## Goal Description
Build a mobile-first LMS for the "DS'F24 Morning" session. A generic username/password csv login system with role-based access (Student/CR). Key features include attendance (CR-controlled), assignments, quizzes, and a dashboard powered by mathematical analytics (Linear Algebra/Calculus).

## User Review Required
> [!IMPORTANT]
> **Data Generation**: I will generate a mock CSV file (`students.csv`) with Roll Numbers `BSDSF24M001` to `BSDSF24M062` to bootstrap the database.
>
> **Stack Confirmation**: 
> - **Backend**: FastAPI + SQLite (for simplicity/portability).
> - **Frontend**: Flutter.

## Proposed Changes

### Backend (Python/FastAPI)
#### [NEW] [main.py](file:///d:/DS'F24%20LMS/backend/main.py)
Entry point for the FastAPI application.

#### [NEW] [models.py](file:///d:/DS'F24%20LMS/backend/models.py)
Database models using SQLModel (or SQLAlchemy).
- `User`: id, roll_no, password_hash, role (STUDENT/CR), semester
- `Subject`: id, name, code, credit_hours, semester
- `Attendance`: id, date, subject_id, status (PRESENT/ABSENT/LEAVE) -> *Matrix representation logic*
- `Assignment`/`Quiz`: Standard fields.

#### [NEW] [auth.py](file:///d:/DS'F24%20LMS/backend/auth.py)
JWT-based authentication. Implementation of the specific password rules (Default: `BSDSF24Mxxx`, User: `bsdsf24mxxx`).

#### [NEW] [math_engine.py](file:///d:/DS'F24%20LMS/backend/math_engine.py)
Core logic for:
- Attendance Matrix construction.
- Academic State Vector calculation.
- Calculus-based trend analysis (e.g., rate of change in attendance/grades).

### Frontend (Flutter)
#### [NEW] `frontend/` Directory
Standard Flutter project structure.
- `lib/main.dart`: Entry point.
- `lib/screens/login_screen.dart`: First change password flow.
- `lib/screens/dashboard.dart`: Analytics view.
- `lib/screens/attendance_screen.dart`: For CR to mark attendance.

### Data
#### [NEW] [students.csv](file:///d:/DS'F24%20LMS/students.csv)
Mock data file.

## Verification Plan
### Automated Tests
- Test Math Engine: Verify matrix operations and derivative calculations.
- Test Auth: Verify default password logic and forced change.

### Manual Verification
- Run Backend: `uvicorn main:app --reload`
- Run Frontend: `flutter run`
- Login as CR, mark attendance, verify DB update.
- Login as Student, check Dashboard analytics.
