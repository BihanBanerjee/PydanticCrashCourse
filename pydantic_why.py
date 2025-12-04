# def insert_patient_data(name, age):

#     print(name)
#     print(age)
#     print('Patient data inserted successfully')


# # a junior developer does this:->
# insert_patient_data('John', 'thrity') # No error but not desireable. age should be int



# def insert_patient_data(name: str, age: int): # these type-hints only for readibility, to provide better information but no run time checks.

#     print(name)
#     print(age)
#     print('Patient data inserted successfully')


# # a junior developer does this:->
# insert_patient_data('John', 'thrity') # Junior developer didn't see the type and provided wrong type as 'thirty'. age should be int.
# # Still in this case there will no error. In Python runtime, no error will be detected.


def insert_patient_data(name: str, age: int): # these type-hints only for readibility, to provide better information but no run time checks.
    if (type(name) == str and type(age) == int): 
        if (age < 0): # Data Validation. I don't want age to be negative.
            raise ValueError('Age cannot be negative')
        print(name)
        print(age)
        print('Patient data inserted successfully')
    else:
        raise TypeError('Incorrect tpyes has been provided. Please provide correct types')

insert_patient_data('john', 30)
# insert_patient_data('john', 'thirty') #type error
# insert_patient_data('john', -2)# Value error

# So Pydantic just solves this issues. So you dont need to manually write ant code for data validation and type checking/validation. 


from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int


def insert_patient_data1(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('Patient data inserted successfully')

patient_info = {'name': 'John', 'age': 30}
patient1 = Patient(**patient_info) # unpacking the dictionary using **patient_info 
# ^^ First, here rule will be applied. if the rule test is passed then that will be passed to the function below.
insert_patient_data1(patient1)

