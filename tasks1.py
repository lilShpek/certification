# Необходимо создать API для управления списком задач. Каждая задача должна содержать
#  заголовок и описание. Для каждой задачи должна быть возможность указать статус (выполнена/не выполнена).

# API должен содержать следующие конечные точки:
# — GET /tasks — возвращает список всех задач.
# — GET /tasks/{id} — возвращает задачу с указанным идентификатором.
# — POST /tasks — добавляет новую задачу.
# — PUT /tasks/{id} — обновляет задачу с указанным идентификатором.
# — DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.

# Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа.
#  Для этого использовать библиотеку Pydantic.



from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import List
import pandas as pd
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class Task(BaseModel):
    title: str
    description: str
    status: bool = False

tasks = []

@app.get("/tasks", response_class=HTMLResponse)
async def tasks_table(request: Request):
    tasks_df = pd.DataFrame([task.dict() for task in tasks])
    tasks_table_html = tasks_df.to_html(index=False)
    return templates.TemplateResponse("tasks_table.html", {"request": request, "tasks_table": tasks_table_html})

@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]

@app.post("/tasks", response_model=Task)
async def create_task(task: Task):
    tasks.append(task)
    return task

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, updated_task: Task):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    
    tasks[task_id] = updated_task
    return updated_task

@app.delete("/tasks/{task_id}", response_model=Task)
async def delete_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    
    deleted_task = tasks.pop(task_id)
    return deleted_task
