from pydantic import BaseModel, Field
from typing import Optional

class TodoItem(BaseModel):
    id: Optional[str] = Field(None, alias='_id')
    title: str
    description: Optional[str] = None
    completed: bool = False