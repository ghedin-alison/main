# To remember

 - On linux to use the mysqlclient lib is necessary to install
```commandline
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
```

 - On linux terminal to get ip
```commandline
hostname -I
```

 - After the migrate settings are ready, on docker container execute:
```commandline
docker-compose exec backend sh
```
```commandline
python manager.py db --help
```
```commandline
python manager.py db init
```
```commandline
python manager.py db migrate
```

- Connect on database via dbeaver and:
```commandline
python manager.py db upgrade
```
 - Go to the other project microservices and set the rabbit mq
 - Return to this project, copy and paste the consumer.py to main project
 - start the container and the consumer.py
```commandline
docker-compose exec backend sh
```
```commandline
python consumer.py
```
 - Return to the microservices project and change the 
   producer routing_key to main

 - The communication between the two projects its working. Tests @postman.

### Update Dockerfile to keep only one consumer tab
 - update the Dockerfile and docker-compose to get ready when compose starts
 - As the docker files were updated run:
```unix
docker-compose up --build
```
 - A lot of issues related to access .dbdata. This is because docker was trying to access.
 - To solve this docker problem, just create a .dockerignore and add the folder.

 - Then restart again the server and run this to start db
```unix
docker-compose up -d db
```
 - And again
```unix
docker-compose up
```
 - Add auto_ack=True to basic_consume of consumer

### likes treatment
 - When need to use two localhost on docker could be useful change:
  "localhost or 0.0.0.0" by "host.docker.internal". 
 - Change the settings to accept the "host.docker.internal".
 - Add extra_hosts: "host.docker.internal:host-gateway" at docker-compose


