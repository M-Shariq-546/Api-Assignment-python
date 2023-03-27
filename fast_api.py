from fastapi import FastAPI
import data as d
app = FastAPI()

@app.get("/")
def index():
    return {"name" : "Muhammad Shariq" ,
            "Designation" : "Api Creator"    
        }

@app.get("/get_student/{student_id}")
def get_student(student_id:int):
    return d.students[student_id]

@app.post("/post_student/{student_id}")
def post_student(student_id:int):
    return d.students[student_id]
