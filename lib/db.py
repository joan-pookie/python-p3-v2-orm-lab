import sqlite3

CONN = sqlite3.connect(":memory:")  # or use a real file path
CURSOR = CONN.cursor()

# Example: create tables for testing
CURSOR.execute("""
CREATE TABLE department (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
""")

CURSOR.execute("""
CREATE TABLE employee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    department_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES department(id)
)
""")

CURSOR.execute("""
CREATE TABLE review (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER,
    content TEXT,
    FOREIGN KEY (employee_id) REFERENCES employee(id)
)
""")
CONN.commit()
