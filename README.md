## How to run on a Ubunutu VM created using Vagrant 
- Set port forwarding in the vagrantfile
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "forwarded_port", guest: 5000, host: 5000
  
- Use the following commands
	```
	export flask_app=blog 
	flask run --host=0.0.0.0
	```	

- Go to localhost:5000/ on the host machine
