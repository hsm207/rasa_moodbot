from typing import Any, Dict, List, Optional
from pydantic import BaseModel
from fastapi import FastAPI
from dataclasses import dataclass, field

class Body(BaseModel):
    response: str
    arguments: Optional[Dict[str, Any]]
    tracker: Dict[str, Any]
    channel: Dict[str, str] = None

@dataclass
class Response:
    text: str
    buttons: List[Any] = field(default_factory=lambda: [])
    image: str = None
    elements: List[Any] = field(default_factory=lambda: [])
    attachments: List[Any] = field(default_factory=lambda: [])
    custom: Dict = field(default_factory=lambda: {})

app = FastAPI()


@app.post("/nlg")
def generate_response(body: Body = None):
    return Response(text="Hello!")
