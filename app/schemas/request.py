from pydantic import BaseModel

class TrainRequest(BaseModel):
    target: str
    algorithm: str
