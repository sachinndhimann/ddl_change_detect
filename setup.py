from setuptools import setup, find_packages

setup(
    name='ddl_change_detect',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'sqlite3',  # This might not be needed as it is included in Python's standard library
        'difflib'   # This might not be needed as it is included in Python's standard library
    ],
    entry_points={
        'console_scripts': [
            'initialize_db=ddl_change_detect.db_init:create_schema_store_db',
        ],
    },
    include_package_data=True,
    package_data={
        # If there are any package data files include them here
    },
    author='Sachin Dhiman',
    author_email='sachindhiman1@live.in',
    description='A package for schema management in databases.',
    keywords='database schema management',
    url='https://github.com/sachinndhimann/ddl_change_detect.git'
)
