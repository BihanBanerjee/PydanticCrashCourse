from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional

# We can also perform transformations using field_validator function.
class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int = Field(gt=0, lt=150)
    weight: float = Field(gt=0, strict=True)
    married: bool = Field(default=None, description='If married then give True else give False')
    allergies: List[str] = Field(max_length=10)
    contact_details: Dict[str, str]

    # We want to check whether the email has @hdfc or @sbi in the email then we will give them special discount in the treatment.
    # To do this we need to write a new method inside our class usinf field validator.
    @field_validator('email') # using field_validator decorator. It is always going to be a class method.
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'sbi.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError(f"Invalid email domain {domain_name}. Valid domains are {valid_domains}")
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @field_validator('age', mode='after') # after means after the type coercion if you give 'age': '30', then also it will work. No error thrown.
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100 :
            raise value
        else:
            raise ValueError('Age should be between 0 and 100')
    

patient_info = {
    'name': 'John',
    'email': 'banbin@hdfc.com',
    'age': 23,
    'weight': 80.5,
    'married': True,
    'allergies': ['peanuts', 'dust mites'],
    'contact_details': {'home': '123 Main St', 'work': '456 Business Ave'}
}

patient1 = Patient(**patient_info) # validation --> type coercion
print(patient1)

