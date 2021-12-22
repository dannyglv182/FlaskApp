# Flask Blog Application
## How to run on a Ubunutu VM created using Vagrant 
 - **Set port forwarding in the vagrantfile**
  config.vm.network "forwarded_port", guest: 80, host: 8080   
  config.vm.network "forwarded_port", guest: 5000, host: 5000
  
- **Use the following commands**
	```
	export flask_app=blog 
	flask run --host=0.0.0.0
	```	

## Dependencies
- **Flask-SQLAlchemy**
Object Relational Mapper. All SQL tables are defined as Python classes in models.py

- **Passlib**
Password Hashing Library. Passwords are hashed and salted using Passlib's hash method.
