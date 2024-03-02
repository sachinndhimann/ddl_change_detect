# schema_reader.py

import sqlite3

def store_schema(create_statement, table_name, sqlite_db_path):
    """
    Reads the schema of a given table using the SHOW CREATE TABLE command
    and stores it in a SQLite database.
    """
    # Connect to the SQLite database
    sqlite_conn = sqlite3.connect(sqlite_db_path)
    cursor = sqlite_conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS schema_history
                      (schema_name TEXT,table_name TEXT PRIMARY KEY, create_statement TEXT)''')
    cursor.execute('''INSERT OR REPLACE INTO schema_history (table_name, create_statement) 
                      VALUES (?, ?)''', (table_name, create_statement))
    sqlite_conn.commit()
    sqlite_conn.close()
