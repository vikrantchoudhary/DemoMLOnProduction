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







