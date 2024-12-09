from typing import List, Optional
from models import TodoItem
from database import todo_collection
from bson import ObjectId

# helper function to convert MongoDB document to TodoItem
def todo_helper(todo) -> dict:
    return {
        "Id": str(todo["_id"]),
        "title" : todo["title"],
        "description" : todo["description"],
        "completed" : todo["completed"]
    }

# Add a new todo item
async def create_todo(todo_data: TodoItem) -> TodoItem:
    todo_dict = todo.dict()
    result = await todo_collection.insert_one(todo_dict)
    new_todo = await todo_collection.find_one({"_id": result.inserted_id})
    return TodoItem(**todo_helper(new_todo))    