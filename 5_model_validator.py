from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict, Optional

# if you want to do data validation that includes two fields, then you should use model validator.
class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int 
    weight: float 
    married: bool 
    allergies: List[str] 
    contact_details: Dict[str, str]

    # Model validator with mode='after' should use instance method (self) not classmethod (cls)
    # Previous implementation using cls was deprecated in Pydantic V2.12:
    # @model_validator(mode='after')
    # def validate_emergency_contact(cls, model):
    #     if model.age >= 60 and 'emergency' not in model.contact_details:
    #         raise ValueError("Emergency contact is required for patients over 60 years old.")
    #     return model

    # Correct implementation: use self to access the model instance directly
    @model_validator(mode='after')
    def validate_emergency_contact(self):
        if self.age >= 60 and 'emergency' not in self.contact_details:
            raise ValueError("Emergency contact is required for patients over 60 years old.")
        return self
    

patient_info = {
    'name': 'John',
    'email': 'banbin@hdfc.com',
    'age': 70,
    'weight': 80.5,
    'married': True,
    'allergies': ['peanuts', 'dust mites'],
    'contact_details': {'home': '123 Main St', 'work': '456 Business Ave'}
}

patient1 = Patient(**patient_info)