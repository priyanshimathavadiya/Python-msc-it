from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()


# DATABASE
def get_db():
    return sqlite3.connect("todo.db")


conn = get_db()

conn.execute("""
CREATE TABLE IF NOT EXISTS todoapp (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    priority TEXT NOT NULL,
    is_completed BOOLEAN NOT NULL,
    due_date TEXT NOT NULL
)
""")

conn.commit()
conn.close()


# DATA MODEL
class Todo(BaseModel):
    title: str
    description: str
    priority: str
    is_completed: bool
    due_date: str


# GET - All Tasks
@app.get("/task")
def get_tasks():

    conn = get_db()

    tasks = conn.execute("""
        SELECT id, title, description, priority,
               is_completed, due_date
        FROM todoapp
    """).fetchall()

    conn.close()

    return [
        {
            "id": task[0],
            "title": task[1],
            "description": task[2],
            "priority": task[3],
            "is_completed": bool(task[4]),
            "due_date": task[5]
        }
        for task in tasks
    ]


# GET - One Task
@app.get("/task/{task_id}")
def get_task(task_id: int):

    conn = get_db()

    task = conn.execute("""
        SELECT id, title, description, priority,
               is_completed, due_date
        FROM todoapp
        WHERE id = ?
    """, (task_id,)).fetchone()

    conn.close()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "id": task[0],
        "title": task[1],
        "description": task[2],
        "priority": task[3],
        "is_completed": bool(task[4]),
        "due_date": task[5]
    }


# POST - Add Task
@app.post("/task")
def add_task(todo: Todo):

    conn = get_db()

    cursor = conn.execute("""
        INSERT INTO todoapp
        (title, description, priority, is_completed, due_date)
        VALUES (?, ?, ?, ?, ?)
    """, (
        todo.title,
        todo.description,
        todo.priority,
        todo.is_completed,
        todo.due_date
    ))

    conn.commit()

    task_id = cursor.lastrowid

    conn.close()

    return {
        "message": "Task added successfully",
        "id": task_id
    }


@app.put("/task/{task_id}")
def update_task(task_id: int, todo: Todo):

    conn = get_db()

    task = conn.execute(
        "SELECT id FROM todoapp WHERE id = ?",
        (task_id,)
    ).fetchone()

    if not task:
        conn.close()
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    conn.execute("""
        UPDATE todoapp
        SET title = ?,
            description = ?,
            priority = ?,
            is_completed = ?,
            due_date = ?
        WHERE id = ?
    """, (
        todo.title,
        todo.description,
        todo.priority,
        todo.is_completed,
        todo.due_date,
        task_id
    ))

    conn.commit()
    conn.close()

    return {
        "message": "Task updated successfully"
    }

# DELETE - Delete Task
@app.delete("/task/{task_id}")
def delete_task(task_id: int):

    conn = get_db()

    task = conn.execute(
        "SELECT id FROM todoapp WHERE id = ?",
        (task_id,)
    ).fetchone()

    if not task:
        conn.close()
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    conn.execute(
        "DELETE FROM todoapp WHERE id = ?",
        (task_id,)
    )

    conn.commit()
    conn.close()

    return {
        "message": "Task deleted successfully"
    }