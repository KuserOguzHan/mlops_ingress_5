- The project aims to learn and apply docker-compose issues.

- All features of FastApi were utilized.

- The challenge is the deployment of the Postgresql database and FastApi simultaneously.



### 1. Pip Install

```
pip install -r requirements.txt
```   

### 2. Docker Compose

```
docker-compose up -d
```  


### 2. Connect Databese

``` 
docker compose ps
``` 

```
docker exec -it container_name psql -U postgres
```

### 3. Authorise User

```
grant all privileges on database postgres to postgres;

```
### 4. Use information of project data

Samsung,64.0,4.0,6.5,5000.0,8.0,48.0,2.0,2.0,2.0,2.999
```
{
  "memory": 64.0,
  "ram": 4.0,
  "screen_size": 6.5,
  "power": 5000,
  "front_camera": 8.0,
  "rc1": 48.0,
  "rc3": 2.0,
  "rc5": 2.0,
  "rc7": 2.0
}
```

Samsung,128.0,6.0,6.5,4500.0,32.0,12.0,12.0,8.0,0.0,6.849

```
{
  "memory": 128.0,
  "ram": 6.0,
  "screen_size": 6.5,
  "power": 4500,
  "front_camera": 32.0,
  "rc1": 12.0,
  "rc3": 12.0,
  "rc5": 8.0,
  "rc7": 0.0
}
```

Oppo,64.0,4.0,6.52,4230.0,8.0,13.0,2.0,2.0,0.0,2.749
```
{
  "memory": 64.0,
  "ram": 4.0,
  "screen_size": 6.52,
  "power": 4230,
  "front_camera": 8.0,
  "rc1": 13.0,
  "rc3": 2.0,
  "rc5": 2.0,
  "rc7": 0.0
}
```

Xiaomi,64.0,3.0,6.53,5000.0,5.0,13.0,0.0,0.0,0.0,2.692
```
{
  "memory": 64.0,
  "ram": 3.0,
  "screen_size": 6.53,
  "power": 5000,
  "front_camera": 5.0,
  "rc1": 13.0,
  "rc3": 0.0,
  "rc5": 0.0,
  "rc7": 0.0
}
```

iPhone,64.0,4.0,6.1,3110.0,12.0,12.0,12.0,0.0,0.0,11.199
```
{
  "memory": 64.0,
  "ram": 4.0,
  "screen_size": 6.1,
  "power": 3110,
  "front_camera": 12.0,
  "rc1": 12.0,
  "rc3": 12.0,
  "rc5": 0.0,
  "rc7": 0.0
}
```

### 4. Show Database

```
\l
```
### Show Tables

```
\dt
```
### Show information

```
select * from create_data;
```
