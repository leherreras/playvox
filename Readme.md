Do the configuration of project
copy the files .bak in config/? with .bak
change the configuration like you prefer
remember that the configuration of mongo and playvox config are integrated 

The project is installable from docker-compose
do you need the next command

`sudo apt install docker-compose`

This installed docker and docker-compose
Now you need are in group docker with the next command

`sudo usermod -aG docker <username>`

do you need do logout and login 
do  you need is in project folder and execute the next command

`docker-compose up -d`

This install the database with the configuration in file config/mongo


If you would like install the project without Docker is little bit difficult

`cp config/playvox/config.yml.bak config/playvox/config.yml`

create a virtualenv with the next command

`sudo pip3 install virtualenv`

`virtualenv -p python3 env`

`. env/bin/activate`

change the configuration with reference to the mongo db
install the requirements
if you are in root of project execute the next command

`pip install -r src/requirements.txt`

`cd src`

`python app.py`

Enable filtes:
username
lastname
old
gender
email

Apis enables:

GET /v1/users?query={"<key>": "value"} #list all users with specific query
GET /v1/users/insert #view to create users
GET /v1/users/destroy/<id> #delete users
GET /v1/users/user/<id> #visualize a users
POST /v1/users #create users


GET  /v1/notes/insert #view to create note
POST /v1/notes #create note
