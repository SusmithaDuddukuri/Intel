# 🌍 Disaster Response Coordinator

An intelligent web-based disaster management system that enables
**real-time disaster reporting**, **automated resource allocation**, and
**emergency coordination** using location-based tracking and severity
analysis.

------------------------------------------------------------------------

## 📌 Project Overview

The **Disaster Response Coordinator** is designed to streamline disaster
reporting and emergency response coordination. The system allows users
to report disasters, automatically assigns appropriate authorities,
allocates available emergency resources, and tracks disaster response
status in real time.

This project demonstrates the integration of **Flask (Python backend)**,
**SQLite database**, **HTML/CSS frontend**, and **dynamic resource
allocation logic**.

------------------------------------------------------------------------

## 🚀 Features

### ✅ Disaster Reporting

-   Users can report disasters by providing:
    -   Disaster Type
    -   Location
    -   Severity Level
-   System automatically assigns authorities and resources.

### ✅ Smart Resource Allocation

-   Location-based resource allocation.
-   Falls back to nearest available resources if location resources are
    unavailable.
-   Dynamic update of resource availability.

### ✅ Admin Panel

-   View all disaster reports.
-   Resolve disasters.
-   Delete records.
-   Notification system for new disaster reports.

### ✅ Monitoring Dashboard

-   Displays:
    -   Total disaster reports
    -   High severity cases
    -   Resolved cases
-   Provides system capability overview.

### ✅ Disaster History

-   Shows historical disaster categories.
-   Visual representation with descriptions.

### ✅ Notification System

-   Admin receives alerts for new disaster reports.
-   Unread reports are tracked automatically.

### ✅ Authentication

-   Admin login session handling.

------------------------------------------------------------------------

## 🛠 Tech Stack

### Backend

-   Python
-   Flask Framework
-   SQLite Database

### Frontend

-   HTML5
-   CSS3
-   Jinja2 Template Engine

------------------------------------------------------------------------

## 📂 Project Structure

    Disaster-Response-Coordinator/
    │
    ├── app.py
    ├── database.db
    │
    ├── templates/
    │   ├── base.html
    │   ├── index.html
    │   ├── dashboard.html
    │   ├── admin.html
    │   ├── history.html
    │   ├── contact.html
    │   └── login.html
    │
    ├── static/
    │   ├── style.css
    │   └── images/
    │
    └── README.md

------------------------------------------------------------------------

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

``` bash
git clone https://github.com/SusmithaDuddukuri/disaster-response-coordinator.git
cd disaster-response-coordinator
```

### 2️⃣ Install Dependencies

``` bash
pip install flask
```

### 3️⃣ Run Application

``` bash
python app.py
```

### 4️⃣ Open in Browser

    http://127.0.0.1:5000/

------------------------------------------------------------------------

## 🔐 Admin Credentials

    Username: admin
    Password: admin

------------------------------------------------------------------------

## 🗄 Database Design

### Disaster Table

  Field                 Description
  --------------------- ------------------------------
  id                    Unique disaster ID
  dtype                 Disaster type
  location              Affected location
  severity              Severity level
  assigned_authority    Allocated authority
  assigned_resources    Assigned emergency resources
  status                Pending / Resolved
  coordination_status   Progress status
  is_read               Notification tracking

------------------------------------------------------------------------

### Resources Table

  Field             Description
  ----------------- -------------------------
  name              Resource name
  type              Resource type
  location          Resource location
  total_units       Total available units
  available_units   Current available units

------------------------------------------------------------------------

## 🧠 Resource Allocation Logic

-   Resources are first allocated based on disaster location.
-   If unavailable, system assigns alternative available resources.
-   Authority assignment based on severity:
    -   **High → NDRF**
    -   **Medium → State Authority**
    -   **Low → Local Authority**

------------------------------------------------------------------------

## 🎯 Future Enhancements

-   GIS map integration
-   Real-time alerts using WebSockets
-   Machine learning for disaster prediction
-   Multi-user role authentication
-   Cloud database deployment

------------------------------------------------------------------------

## 👩‍💻 Author

**Susmitha Duddukuri**

------------------------------------------------------------------------

## 📜 License

This project is developed for academic and educational purposes.
