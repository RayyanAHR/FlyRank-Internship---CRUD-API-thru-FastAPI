from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enable CORS (Stage 5)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (e.g. http://localhost:3000)
    allow_credentials=True,
    allow_methods=["*"],  # Allows GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],  # Allows all headers
)

# In-memory "database"
tasks = [
    {"id": 1, "title": "Setup development environment", "completed": True},
    {"id": 2, "title": "Build FastAPI CRUD endpoints", "completed": False}
]

# Pydantic Schemas
class TaskCreate(BaseModel):
    title: str
    completed: bool = False

class TaskUpdate(BaseModel):
    title: str | None = None
    completed: bool | None = None


# Routes
@app.get("/")
def read_root():
    return {"message": "Welcome to FAI - A1 - CRUD API!"}

@app.get("/health")
def check_health():
    return {"status": "ok"}

@app.get("/tasks")
def get_all_tasks():
    return {"tasks": tasks}

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    new_id = max([t["id"] for t in tasks], default=0) + 1
    new_task = {
        "id": new_id,
        "title": task.title,
        "completed": task.completed
    }
    tasks.append(new_task)
    return new_task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_data: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            if updated_data.title is not None:
                task["title"] = updated_data.title
            if updated_data.completed is not None:
                task["completed"] = updated_data.completed
            return {"message": "Task updated successfully", "task": task}
            
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", status_code=200)
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            deleted_task = tasks.pop(index)
            return {"message": "Task deleted successfully", "deleted_task": deleted_task}
            
    raise HTTPException(status_code=404, detail="Task not found")