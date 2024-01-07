# LIBRARY API's

### About

The project contains the API's that are related to the library management system 
<hr/>

### Tech

Framework : Fastapi <br/>
ORM : SQLAlchemy <br/>
Database: postgresql (or) Other SQL databases <br/>
Alembic to migrate database <br/>
Flake8 and Black to structure the code. <br/>
<hr/>

### Setup
_step1_: Create a virtual env

    python -m venv venv 
    or 
    virtualenv venv

_step2_: Config env by creating .env file
    
    postgre_host = "<postgres_hostname>"
    postgre_pass = "<postgres_password>"
    jwt_secret_key = "<A random generated ket for creating jwt_secret_key>"

_step3_: Install the required packages

    pip install -r requirements.txt

_step4_: Start the project by entering

    uvicorn main:app --reload

The project serves on http://loadhost:8000
<hr/>

### To visualize the API's

Go to http://localhost:8000/docs
