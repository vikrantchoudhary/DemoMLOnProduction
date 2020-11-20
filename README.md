# Demo ML code for production 


# creating env for running 
> python -m venv env \
> source env/bin/activate \
> which python  \
../DemoMLOnProduction/env/bin/python

# install dependent lib 
> pip install -r requirements.txt
Collecting click==7.1.2 \
  Using cached click-7.1.2-py2.py3-none-any.whl (82 kB) \
Collecting fastapi==0.61.2 \
  Using cached fastapi-0.61.2-py3-none-any.whl (48 kB) \
Collecting h11==0.11.0 \
...


# testing with the changed python location 
> python load_model.py

[[0.14 0.86] \
 [0.52 0.48]]


