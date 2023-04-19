from fastapi import FastAPI
import redis
import json
import uuid
from datetime import date
from typing import Dict


app = FastAPI()
r = redis.Redis(host="redis", port=6379)


def make_task(name: str, status: str, due_date: date) -> Dict:
    return {"name": name, "status": status, "due_date": str(due_date)}

@app.post("/tasks/")
def create_task(name: str, status: str, due_date: date):
    task = make_task(name, status, due_date)
    new_task = json.dumps(task)
    r.set(str(uuid.uuid4()), new_task)
    return {}


@app.put("/task/{item_id}")
async def update_task(item_id: str, name: str, status: str, due_date: date):
    task = make_task(name, status, due_date)
    new_task = json.dumps(task)
    r.set(item_id, new_task)
    return {"update": item_id}


@app.delete("/task/{item_id}")
async def delete_task(item_id: str):
    task = r.delete(item_id)
    return {"delete": item_id}


@app.get("/task/{item_id}")
async def get_task(item_id):
    task = r.get(item_id)
    return {"task": json.loads(task)}


@app.get("/tasks")
async def get_all_tasks():
    tasks = r.keys()
    res = []
    for key in tasks:
        task = json.loads(r.get(key))
        task["id"] = key
        res.append(task)
    return res
