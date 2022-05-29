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
 - 