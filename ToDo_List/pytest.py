import json
import pytest
from datetime import date
from fastapi import FastAPI
from fastapi.testclient import TestClient

@pytest.fixture
def fixture_client():
    app_obj = FastAPI()
    client_obj = TestClient(app_obj)
    return client_obj

def test_create_task(fixture_client):
    task_payload = {
        "name": "Test task",
        "status": "Active",
        "due_date": date(2023, 2, 11),
    }
    response = fixture_client.post("/task/", json=task_payload)
    assert response.status_code == 200

def test_update_task(fixture_client):
    task_payload = {
        "name": "Test task",
        "status": "Active",
        "due_date": date(2023, 2, 11),
    }
    task_id = "some_id_here"
    response = fixture_client.put(f"/task/{task_id}", json=task_payload)
    assert response.status_code == 200

def test_delete_task(fixture_client):
    task_id = "some_id_here"
    response = fixture_client.delete(f"/task/{task_id}")
    assert response.status_code == 200

def test_get_task(fixture_client):
    task_id = "some_id_here"
    response = fixture_client.get(f"/task/{task_id}")
    assert response.status_code == 200

def test_get_all_tasks(fixture_client):
    response = fixture_client.get("/tasks")
    assert response.status_code == 200
