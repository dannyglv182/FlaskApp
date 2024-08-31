#  Link for how to install Flask https://flask.palletsprojects.com/en/3.0.x/installation/

# STEPS TO INSTALL DEPENDENCIES AND GET THE BLOG RUNNING
1. Enter virtual environment  . .venv/bin/activate
2. From within the venv, run install.sh to install dependencies
3. Install Posgresql if it is not already installed
4. Change string in database_setup.py so that it connectes to the database you created
5. execute python3 database_setup.py to add the tables to the database. 
6. Run flask --app blog run --host=0.0.0.0 to test app (make sure port forwarding is set so host machine can access guest port 5000)
7. Visit localhost:<forwarded port> on host machine



