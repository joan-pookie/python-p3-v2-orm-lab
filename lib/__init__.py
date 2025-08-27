import sqlite3
import os

# Database file path
DB_FILE = os.path.join(os.path.dirname(__file__), "orm_lab.db")

# Create a connection to the SQLite database
CONN = sqlite3.connect(DB_FILE)

# Enable returning rows as tuples (id, col1, col2...)
CONN.row_factory = sqlite3.Row

# Create a cursor for executing SQL statements
CURSOR = CONN.cursor()

# Optional: enforce foreign key constraints
CURSOR.execute("PRAGMA foreign_keys = ON")
CONN.commit()
