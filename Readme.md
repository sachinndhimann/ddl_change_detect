# Schema Change Detector Utility

Welcome to the **Schema Change Detector Utility**, a Python package designed for data engineers who navigate the dynamic and evolving landscape of database schemas. In the data engineering world, schema changes can significantly impact data integration, reporting, and analysis processes. This utility provides a seamless way to detect schema changes, enabling data professionals to make informed decisions and adapt their workflows accordingly.

## Features

- **Schema Storage**: Read and store the schema of any table in a SQLite database for future reference.
- **Change Detection**: Compare the current table schema against the stored version to detect any changes.
- **Integration Friendly**: Designed to be easily integrated into data load activities, ensuring you're always working with the most up-to-date schema information.

## Installation

Before you can use the Schema Change Detector Utility, you need to install it. The package is distributed as a wheel file, making it easy to install using pip.


pip install ddl_change_detect-0.1.0-py3-none-any.whl

## Getting Started
To get started with the Schema Change Detector Utility, follow these steps:

1. Initialize the Database
Before using the utility, initialize the database to store the schema information.

python -m ddl_change_detect.db_init
2. Read and Store Schema
Use the store_schema function to read a table's schema and store it in the database.

from ddl_change_detect import store_schema

create_statement = conn.execute("""SHOW CREATE TABLE {table_name}""")
table_name = 'table_name'
sqlite_db_path = 'db/schema_store.db'

store_schema(create_statement, table_name, sqlite_db_path)


3. Detect Schema Changes
To detect changes in the schema, use the compare_schema function.

from ddl_change_detect import compare_schema
connection_string='path to schema_store.db in python package/or anywhere'
schema_diff = compare_schema(connection_string, table_name, sqlite_db_path)

if schema_diff:
    print("Schema differences detected:")
    print(schema_diff)
else:
    print("No schema differences detected.")
## Use Cases in Data Engineering

## Data Profiling on Schema Change
In scenarios where schema changes are frequent, it's crucial to perform data profiling only on tables that have changed. This utility can be integrated into your data pipeline to automatically trigger profiling jobs for tables with detected schema changes.

Example:

if schema_diff:
    # Logic to trigger data profiling for table_name
    print(f"Triggering data profiling for {table_name} due to schema changes.")


## Conditional Data Loading
When loading data into a data warehouse or data lake, schema changes can affect the loading process. Use this utility to detect schema changes and adjust your loading strategy accordingly.

if schema_diff:
    # Adjust data loading process for table_name
    print(f"Adjusting data loading process for {table_name} due to schema changes.")


## Conclusion

The Schema Change Detector Utility empowers data engineers to manage and respond to schema changes 
proactively. By integrating this utility into your data pipelines, you can ensure that your data processing and analysis workflows remain efficient and accurate, even as your data sources evolve.