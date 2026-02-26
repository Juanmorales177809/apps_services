from pydantic import BaseModel


class Model(BaseModel):
    language: str
    version: str
    year: int
    
Model(language="Python", version="3.12.0", year=2003)
Model.model_validate(
    {
        "language": "Python",
        "version": "3.2.1",
        "year": 2005
    }
)
print(Model)