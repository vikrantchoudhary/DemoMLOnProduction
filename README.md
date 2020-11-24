# Demo ML code for production 


# creating env for running 
```
> python -m venv env 
> source env/bin/activate
> which python  
../DemoMLOnProduction/env/bin/python
```

# install dependent lib ```
```
> pip install -r requirements.txt
Collecting click==7.1.2 
  Using cached click-7.1.2-py2.py3-none-any.whl (82 kB) 
Collecting fastapi==0.61.2 
  Using cached fastapi-0.61.2-py3-none-any.whl (48 kB) 
Collecting h11==0.11.0 
...
```


# testing with the changed python location 
```
> python load_model.py

[[0.14 0.86] 
 [0.52 0.48]]
 ```

# creating docker file 
```
> docker build . -t vikrantkc/demo_ml_python 

Sending build context to Docker daemon  687.3MB 
Step 1/6 : FROM python:3.8.0-slim 
 ---> 577b86e4ee11 
 .... 
 Step 6/6 : CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"] 
 ---> Using cache 
 ---> ce72d40faa7a 
Successfully built ce72d40faa7a 
Successfully tagged vikrantkc/demo_ml_python:latest 
```

# running docker image

```
> docker run -d -p 8000:8000 ce72
3771adb019789a00004a259273c7164b62ba9df2c41382150b46e9d6c4d9484d

```
# verify it with "apache bench" 
```
> ab -c 250 -n 10000 http://localhost:8000/predict\?text\=today%27s%20weather%20is%20not%20good
This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 1000 requests
```

# Deploy using kubernetes (this can be deployed on AKS,EKS or GKS) (using local for our purpose)
## pushing to docker hub

```
> docker push  vikrantkc/demo_ml_python
The push refers to repository [docker.io/vikrantkc/demo_ml_python]

```

## deploying the same image to k8s env (using minikube)

```
> minikube start

> kubectl create -f deployment.yaml
deployment.apps/demomlpython created

> kubectl get pods
NAME                            READY   STATUS    RESTARTS   AGE
demomlpython-6fdbbbdc5b-clj9k   1/1     Running   0          6s
> kubectl logs demomlpython-6fdbbbdc5b-clj9k

INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)

> kubectl get svc
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   3d21h
> kubectl create  -f service.yaml
service/demomlpython-service created
> kubectl get svc
NAME                   TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
demomlpython-service   NodePort    10.102.127.61   <none>        8000:31000/TCP   2s
kubernetes             ClusterIP   10.96.0.1       <none>        443/TCP          3d21h
> kubectl get svc
NAME                   TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
demomlpython-service   NodePort    10.102.127.61   <none>        8000:31000/TCP   6s
kubernetes             ClusterIP   10.96.0.1       <none>        443/TCP          3d21h
> minikube service demomlpython-service  --url
🏃  Starting tunnel for service demomlpython-service.
|-----------|----------------------|-------------|------------------------|
| NAMESPACE |         NAME         | TARGET PORT |          URL           |
|-----------|----------------------|-------------|------------------------|
| default   | demomlpython-service |             | http://127.0.0.1:60772 |
|-----------|----------------------|-------------|------------------------|
http://127.0.0.1:60772

```
# testing it
```
> curl  http://127.0.0.1:60772/predict\?text\=this%20how%20you%20behave%20better
{"text":"this how you behave better","result ":0.62}%

# we can use http as well
> http http://127.0.0.1:60772/predict\?text\=this%20how%20you%20behave%20better
HTTP/1.1 200 OK
content-length: 52
content-type: application/json
date: Tue, 24 Nov 2020 16:40:25 GMT
server: uvicorn

{
    "result ": 0.62,
    "text": "this how you behave better"
}

```
# testing further with apache bench 

```
> ab -c 250 -n 10000 http://127.0.0.1:60772/predict\?text\=today%27s%20weather%20is%20not%20good
This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
apr_socket_recv: Connection reset by peer (54)
Total of 1000 requests completed

```

# View the load on minikube dashboard
![Screenshot](image/Screenshot.png?raw=true "Screenshot")

# Delete and release resource 
> kubectl delete deployment -l app=demomlpython
deployment.apps "demomlpython" deleted






