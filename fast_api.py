from fastapi import FastAPI
from data import students
app = FastAPI()

@app.get("/")
def index():
    return {"name" : "Muhammad Shariq" ,
            "Designation" : "Api Creator"    
        }

@app.get("/get_student/{student_id}")
def get_student(student_id:int):
    return students[student_id]

@app.post("/post_student/{student_id}")
def post_student(student_id:int):
    return students[student_id]
