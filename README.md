# FARM-TodoList
Creating the ToDo list apllication  using farm stake 

step 1 : crate virtual environment 
            python -m venv env  
         Activate:
            env\Scripts\activate 

step 2 : install fastAPI
        pip install fastapi "uvicorn[standard]"

step 3 : to run first server
         uvicorn app.app:app --reload