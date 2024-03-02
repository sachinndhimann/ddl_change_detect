import sqlite3
import os
import sys  # Import sys module to access command-line arguments

def create_schema_store_db(path):
    db_path = path
    os.makedirs(os.path.dirname(db_path), exist_ok=True)  # Ensure the db directory exists
    
    # Connect to the SQLite database (this will create it if it doesn't exist)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the schema_history table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS schema_history
                      (schema_name TEXT, table_name TEXT PRIMARY KEY, 
                       create_statement TEXT)''')
    conn.commit()
    conn.close()
    print("Database and schema_history table created successfully.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python db_init.py <path_to_database>")
        sys.exit(1)
    path = sys.argv[1]
    create_schema_store_db(path)
