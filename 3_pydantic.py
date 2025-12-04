# Custom data validation if you require to do then you get Field function from Pydantic. It is super useful.
# Suppose you don't want the age to be negative or zero, then you can use the below code.


# ----------------------custom data validation using field function------------------------------
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    age: int = Field(gt=0, lt=150)
    weight: float = Field(gt = 0)
    married: bool
    allergies: List[str] = Field(max_length=10)
    contact_details: Dict[str, str]

# Field Function doesnt only do data validation but it is also used to attach metadata. If you want to attach bit of description with these fields then it is useful.
# You attach metadata using the combination of annotated and field.

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title='Name of the Patient', description='Give the name of the patient under 50 characters', examples=['John Doe', 'Jane Doe'])]
    # In the Annotated, first give the data type and then give the Field and inside the Field, first add the data validation and you can add the metadata you want to add.
    age: int = Field(gt=0, lt=150) # if you only do custom data validation with Field then you don't need to use the Annotated.
    # But if you want to attach metadata or give deafult value then you need to use the Annotated.
    weight: float = Field(gt = 0)
    married: Annotated[bool, Field(default=None, description='If married then give True else give False')]
    allergies: List[str] = Field(max_length=10)
    contact_details: Dict[str, str]
    # So basically we can do 3 things with Field function:-> 1. Data validation, 2. Metadata and 3. Default value

# Pydantic by default does the type coercion (like :-> string to float like '71.5'(string) --> 71.5(float))
# It can be problematic sometimesbut if you want to disable it then you can do this:->

class Patient(BaseModel):
    name: str
    age: int = Field(gt=0, lt=150)
    weight: Annotated[float, Field(gt=0, strict=True)] # strict will disable the type coercion
    married: Annotated[bool, Field(default=None, description='If married then give True else give False')]
    allergies: List[str] = Field(max_length=10)
    contact_details: Dict[str, str]


# Annotated and Field combination is really useful. We will use it alot.