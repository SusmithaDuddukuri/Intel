print("APP FILE IS RUNNING")

from flask import Flask, render_template, request, redirect, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "intel_secret_key"
DB = "database.db"

# =========================
# DATABASE INITIALIZATION
# =========================
def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    # Disaster Table
    c.execute("""
        CREATE TABLE IF NOT EXISTS disasters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dtype TEXT,
            location TEXT,
            severity TEXT,
            assigned_authority TEXT,
            assigned_resources TEXT,
            status TEXT DEFAULT 'Pending',
            coordination_status TEXT DEFAULT 'In Progress',
            is_read INTEGER DEFAULT 0
        )
    """)

    # Resource Table
    c.execute("""
        CREATE TABLE IF NOT EXISTS resources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            type TEXT,
            location TEXT,
            total_units INTEGER,
            available_units INTEGER,
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

init_db()

# =========================
# GLOBAL NOTIFICATIONS
# =========================
@app.context_processor
def inject_notifications():
    if "admin" in session:
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM disasters WHERE is_read=0")
        unread = c.fetchone()[0]
        conn.close()
        return dict(global_unread=unread)
    return dict(global_unread=0)

# =========================
# RESOURCE ALLOCATION LOGIC
# =========================
def allocate_resources(severity, location):
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    # Location-based allocation
    c.execute("""
        SELECT id, name, available_units 
        FROM resources 
        WHERE location=? AND available_units > 0
    """, (location,))
    
    resources = c.fetchall()

    # Fallback allocation
    if not resources:
        c.execute("""
            SELECT id, name, available_units 
            FROM resources 
            WHERE available_units > 0
        """)
        resources = c.fetchall()

    assigned = []

    for r in resources:
        rid, name, units = r
        assigned.append(name)

        c.execute("""
            UPDATE resources 
            SET available_units = available_units - 1,
                last_updated = CURRENT_TIMESTAMP
            WHERE id=?
        """, (rid,))

    # Authority allocation
    if severity == "High":
        authority = "NDRF"
    elif severity == "Medium":
        authority = "State Authority"
    else:
        authority = "Local Authority"

    conn.commit()
    conn.close()

    return authority, ", ".join(assigned) if assigned else "No Resources Available"

# =========================
# HOME PAGE
# =========================
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        dtype = request.form["dtype"]
        location = request.form["location"]
        severity = request.form["severity"]

        authority, resources = allocate_resources(severity, location)

        conn = sqlite3.connect(DB)
        c = conn.cursor()

        c.execute("""
            INSERT INTO disasters 
            (dtype, location, severity, assigned_authority, assigned_resources, status, coordination_status, is_read)
            VALUES (?, ?, ?, ?, ?, 'Pending', 'In Progress', 0)
        """, (dtype, location, severity, authority, resources))

        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("index.html")

# =========================
# DASHBOARD
# =========================
@app.route("/dashboard")
def dashboard():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM disasters")
    total = c.fetchone()[0]

    c.execute("SELECT COUNT(*) FROM disasters WHERE severity='High'")
    high = c.fetchone()[0]

    c.execute("SELECT COUNT(*) FROM disasters WHERE status='Resolved'")
    resolved = c.fetchone()[0]

    conn.close()

    return render_template("dashboard.html",
                           total=total,
                           high=high,
                           resolved=resolved)

# =========================
# HISTORY PAGE
# =========================
@app.route("/history")
def history():
    return render_template("history.html")

# =========================
# LOGIN
# =========================
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == "admin" and request.form["password"] == "admin":
            session["admin"] = True
            return redirect("/admin")
    return render_template("login.html")

# =========================
# ADMIN PANEL
# =========================
@app.route("/admin")
def admin():
    if "admin" not in session:
        return redirect("/login")

    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("SELECT * FROM disasters")
    data = c.fetchall()

    c.execute("SELECT COUNT(*) FROM disasters WHERE is_read=0")
    unread_count = c.fetchone()[0]

    c.execute("UPDATE disasters SET is_read=1 WHERE is_read=0")

    conn.commit()
    conn.close()

    return render_template("admin.html",
                           data=data,
                           unread_count=unread_count)

# =========================
# RESOLVE DISASTER
# =========================
@app.route("/resolve/<int:id>")
def resolve(id):
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("SELECT assigned_resources FROM disasters WHERE id=?", (id,))
    result = c.fetchone()

    if result and result[0] != "No Resources Available":
        resource_list = result[0].split(", ")

        for r in resource_list:
            c.execute("""
                UPDATE resources 
                SET available_units = available_units + 1,
                    last_updated = CURRENT_TIMESTAMP
                WHERE name=?
            """, (r,))

    c.execute("""
        UPDATE disasters 
        SET status='Resolved', coordination_status='Completed'
        WHERE id=?
    """, (id,))

    conn.commit()
    conn.close()
    return redirect("/admin")

# =========================
# CONTACT PAGE
# =========================
@app.route("/contact")
def contact():
    return render_template("contact.html")

# =========================
# LOGOUT
# =========================
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# =========================
# TEST ROUTE
# =========================
@app.route("/test123")
def test123():
    return "It works"

# =========================
# RUN APP (DEPLOYMENT READY)
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)