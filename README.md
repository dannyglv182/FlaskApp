# Flask Blog Application
## How to run on a Ubunutu VM created using Vagrant 
1. Set port forwarding in the vagrantfile <br>
   * config.vm.network "forwarded_port", guest: 80, host: 8080   
   * config.vm.network "forwarded_port", guest: 5000, host: 5000
2. run db_setup.py
3. run blog.py


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
Posts appear asynchronously on the blog page by using the ajax method.  
