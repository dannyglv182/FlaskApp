# Flask Blog Application

This is a blog page application with a login system.
Posts created by users are stored in a PostgreSQL database and API endpoints
are created to work with data from the client.

## How to run 
Link for how to install Flask https://flask.palletsprojects.com/en/3.0.x/installation/
## STEPS TO INSTALL DEPENDENCIES AND GET THE BLOG RUNNING
1. Enter virtual environment  . .venv/bin/activate
2. From within the venv, run install.sh to install dependencies
3. Instal PostgreSQL if it is not already installed
4. Change the string in database_setup.py so that it connects to the database you created
5. execute python3 db_setup.py to add the tables to the database.
6. run blog.py (make sure port forwarding is set so host machine can access guest port 5000)
7. Visit localhost:forwarded port on host machine



## Dependencies
- **Psycopg2**
database adapter for Python. 

- **Flask-SQLAlchemy**
Object Relational Mapper. All SQL tables are defined as Python classes in models.py

- **Passlib**
Password Hashing Library. Passwords are hashed and salted using Passlib's hash method.

- **Boostrap 5**
Frameork used to style and organize the templates.

- **jQuery**
Posts appear asynchronously on the blog page by using the ajax method and JSON.  
