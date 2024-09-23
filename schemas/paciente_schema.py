from pydantic import BaseModel
from model.paciente import Paciente
from typing import List

class PacienteSchema(BaseModel):
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
    
class PacienteViewSchema(BaseModel):
    id: int = 1
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

class PacienteBuscaSchema(BaseModel):
    name: str = "Jhon"
      
class ListaPacientesSchema(BaseModel):
    pacientes: List[PacienteSchema]

class PacienteDelSchema(BaseModel):
    name: str = "Jhon"

def apresenta_paciente(paciente: Paciente):
    return {
        "id": paciente.id,
        "age": paciente.age,
        "name": paciente.name,
        "sex": paciente.sex,
        "cp": paciente.cp,
        "trestbps": paciente.trestbps,
        "chol": paciente.chol,
        "fbs": paciente.fbs,
        "restecg": paciente.restecg,
        "thalach": paciente.thalach,
        "exang": paciente.exang,
        "oldpeak": paciente.oldpeak,
        "slope": paciente.slope,
        "ca": paciente.ca,
        "thal": paciente.thal,
        "target": paciente.target
    }

def apresenta_pacientes(pacientes: List[Paciente]):
    result = []
    for paciente in pacientes:
        result.append({
           "id": paciente.id,
            "age": paciente.age,
            "name": paciente.name,
            "sex": paciente.sex,
            "cp": paciente.cp,
            "trestbps": paciente.trestbps,
            "chol": paciente.chol,
            "fbs": paciente.fbs,
            "restecg": paciente.restecg,
            "thalach": paciente.thalach,
            "exang": paciente.exang,
            "oldpeak": paciente.oldpeak,
            "slope": paciente.slope,
            "ca": paciente.ca,
            "thal": paciente.thal,
            "target": paciente.target
        })

    return {"pacientes": result}