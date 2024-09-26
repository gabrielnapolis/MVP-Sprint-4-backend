from pydantic import BaseModel
from model.patient import Patient
from typing import List
from flask import jsonify

class PatientSchema(BaseModel):
    name: str = "Jhon"
    age: int = 50
    sex: int = 1
    cp: int = 1
    trestbps: int = 145
    chol: int = 233
    fbs: int = 1
    restecg: int = 1
    thalach: int = 150
    exang: int = 0
    oldpeak: float = 2.3
    slope: int = 0
    ca: int = 0
    thal: int = 1
    
class PatientViewSchema(BaseModel):
    name: str = "Jhon"
    age: int = 50
    sex: int = 1
    cp: int = 1
    trestbps: int = 145
    chol: int = 233
    fbs: int = 1
    restecg: int = 1
    thalach: int = 150
    exang: int = 0
    oldpeak: float = 2.3
    slope: int = 0
    ca: int = 0
    thal: int = 1
    target: int = None

class PatientSearchSchema(BaseModel):
    name: str = "Jhon"
      
class ListaPatientsSchema(BaseModel):
    patients: List[PatientSchema]

class PatientDelSchema(BaseModel):
    name: str = "Jhon"

def show_patient(patient: Patient):
    return {
        "id": patient.id,
        "age": patient.age,
        "name": patient.name,
        "sex": patient.sex,
        "cp": patient.cp,
        "trestbps": patient.trestbps,
        "chol": patient.chol,
        "fbs": patient.fbs,
        "restecg": patient.restecg,
        "thalach": patient.thalach,
        "exang": patient.exang,
        "oldpeak": patient.oldpeak,
        "slope": patient.slope,
        "ca": patient.ca,
        "thal": patient.thal,
        "target": patient.target
    }

def show_patients(patients: List[Patient]):
    result = []
    for patient in patients:
        result.append({
            "id": patient.id,
            "age": patient.age,
            "name": patient.name,
            "sex": patient.sex,
            "cp": patient.cp,
            "trestbps": patient.trestbps,
            "chol": patient.chol,
            "fbs": patient.fbs,
            "restecg": patient.restecg,
            "thalach": patient.thalach,
            "exang": patient.exang,
            "oldpeak": patient.oldpeak,
            "slope": patient.slope,
            "ca": patient.ca,
            "thal": patient.thal,
            "target": patient.target
        })

    return jsonify(result)
