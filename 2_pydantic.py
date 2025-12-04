from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List, Dict, Optional
class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str] #why not list? --> Two level validation we want to do:-> data types even inside the list.
    contact_details: Dict[str, str] # why not dict? Two level validation we want to do:-> data types even inside the dict.

patient_info = {
    'name': 'John',
    'age': 23,
    'weight': 80.5,
    'married': True,
    'allergies': ['peanuts', 'dust mites'],
    'contact_details': {'home': '123 Main St', 'work': '456 Business Ave'}
}

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('Patient data inserted successfully')

patient1 = Patient(**patient_info) # unpacking the dictionary using **patient_info
# ^^ First, here rule will be applied. if the rule test is passed then that will be passed to the function below.
insert_patient_data(patient1)

# if you wanna make allergies, married field optional, then you do this:->

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: Optional[bool] = None # while making a field optional its required to give a default value
    allergies: Optional[List[str]] = None 
    contact_details: Dict[str, str] # why not dict? Two level validation we want to do:-> data types even inside the dict.


# Pydantic also gives you many built-in data types out of the box that Pyhon doesn't provide you.

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: Optional[bool] = None # while making a field optional its required to give a default value
    allergies: Optional[List[str]] = None 
    contact_details: Dict[str, str] # why not dict? Two level validation we want to do:-> data types even inside the dict.
    email: EmailStr # this is a built-in data type of pydantic
    case_history_url: AnyUrl # this is a built-in data type of pydantic that checks if the url is valid or not.