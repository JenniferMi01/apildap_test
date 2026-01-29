from fastapi import FastAPI
from app.ldap_client import get_people
from app.schemas import Person
from typing import List

app = FastAPI(
    title="LDAP People API",
    version="1.0.0"
)

@app.get("/people", response_model=List[Person])
def people_list():
    return get_people()

@app.get("/people/count")
def people_count():
    people = get_people()
    return {"total_people": len(people)}

@app.get("/people/departments")
def people_by_department():
    people = get_people()
    departments = {}

    for p in people:
        departments[p["department"]] = departments.get(p["department"], 0) + 1

    return departments