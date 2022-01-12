```
mysql -h 127.0.0.1 -P 33066 -u root -p admin
mysql -h 127.0.0.1 -P 33067 -u root -p main
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.9-management
sudo lsof -i :5672
sudo lsof -i :15672
```
