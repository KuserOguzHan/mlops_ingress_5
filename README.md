- How to use fastapi, postgresql and kubernetes.

### 1. Deploy yaml filess. 


#### a. Postgresql Deployment

- You should be careful that firstly, pvc.yaml have to run than postgres-deployment.yaml file should be deployed.

```
kubectl apply -f postgres-pvc.yaml
```

```
kubectl get pods
```

```
kubectl get deployments
```

```
kubectl apply -f postgres-deployment.yaml
```
- Check the pods !

```
kubectl apply -f postgres-service.yaml
```

#### b. Fastapi Deployment

```
kubectl apply -f fastapi-deployment.yaml
```

```
kubectl apply -f fastapi-service.yaml
```  

``` 
kubectl get services
``` 

#### c. Ingress Deployment

``` 
kubectl apply -f ingress.yaml
``` 

``` 
kubectl get ingress
``` 

``` 
minikube addons enable ingress
``` 

``` 
kubectl get pods -n ingress-nginx
``` 

``` 
minikube service --all
``` 

### 2. Minikube Arrange

``` 
minikube ip
``` 

``` 
sudo nano /etc/hosts
``` 

- Press Ctrl + O (Write), then Enter (Confirm) to save changes and Ctrl + X (Exit) to exit.


``` 
192.168.49.2    yourdomain.com
``` 


### 2. Connect Databese

``` 
kubectl get pods
``` 

```
kubectl exec -it <postgres-pod-name> -- psql -U postgres -d postgres
```

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


### 3. Use information of project data

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


### 5. Delete

#### 
```
kubectl get deployments
```

```
kubectl delete deployment <deployment-name>
```

#### 
```
kubectl get services
```

```
kubectl delete service <service-name>
```

#### 
```
kubectl get pods
```

```
kubectl delete pod <pod-name>
```

#### 
```
kubectl get ingress
```

```
kubectl delete ingress <ingress-name>
``` 

#### 
```
kubectl get pvc
```

```
kubectl delete pvc <pvc-name>
```

#### 
```
kubectl get pv
```

```
kubectl delete pv <pv-name>
```




