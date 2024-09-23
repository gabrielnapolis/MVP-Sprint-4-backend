from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request, jsonify
from urllib.parse import unquote
from model import *
from logger import logger
from schemas import *
from flask_cors import CORS

# Init OpenAPI
info = Info(title="My API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Grouping routes tags
home_tag = Tag(name="Documentation", description="Document Selection: Swagger, Redoc ou RapiDoc.")
paciente_tag = Tag(name="Patients", description="Insert, view, remove and prediction of Heart Disease Patients.")


@app.get('/', tags=[home_tag])
def home():
    """Document Selection.
    """
    return redirect('/openapi')


@app.get('/patients', tags=[paciente_tag],
         responses={"200": PatientViewSchema, "404": ErrorSchema})
def get_pacientes():
    """List all patients     
    Returns:
        list of all patients and yours predictions
    """
    logger.debug("Data collection from all patients")
    # Criando conexão com a base
    session = Session()
    # Buscando todos os pacientes
    patients = session.query(Patient).all()
    
    if not patients:
        # Se não houver pacientes
        return {"patients": []}, 200
    else:
        logger.debug(f"%d patients found: " % len(patients))
        print(patients)
        return show_patients(patients), 200


@app.post('/patient', tags=[paciente_tag],
          responses={"200": PatientViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict():
    """Enter the patient into the database and perform your Heart Disease prediction.
    Returns:
        Patient data and its prediction.
    """
    try:
        content: PatientSchema = request.get_json()  # Extraindo JSON da requisição

        # Preparando os dados para o modelo
        X_input = PreProcessador.preparar_form(content)  # Passa o dicionário
        model_path = './MachineLearning/pipelines/svm_heart_disease_pipeline.pkl'
        modelo = Pipeline.carrega_pipeline(model_path)
        target = int(Model.preditor(modelo, X_input)[0])

        paciente = Patient(
            name=content["name"],
            age=content["age"],
            sex=content["sex"],
            cp=content["cp"],
            trestbps=content["trestbps"],
            chol=content["chol"],
            fbs=content["fbs"],
            restecg=content["restecg"],
            thalach=content["thalach"],
            exang=content["exang"],
            oldpeak=content["oldpeak"],
            slope=content["slope"],
            ca=content["ca"],
            thal=content["thal"],
            target=target  
        )

        # Enter the patient into the database
        session = Session()

        if session.query(Patient).filter(Patient.name == paciente.name).first():
            error_msg = "Patient already exists"
            logger.warning(f"Error on add patient: '{paciente.name}', {error_msg}")
            return jsonify({"message": error_msg}), 409

        session.add(paciente)
        session.commit()
        logger.debug(f"Enter patient: '{paciente.name}'")
        return show_patient(paciente), 200

    except Exception as e:
        logger.error(f"Error on add patient: {str(e)}")
        return jsonify({"message": "Error on server"}), 500


@app.delete('/patient', tags=[paciente_tag],
            responses={"200": PatientViewSchema, "404": ErrorSchema})
def delete_paciente(query: PatientSearchSchema):
    """Remove patient of the database

    Args:
        name (str): patient name
        
    Returns:
        msg: Success or error message
    """
    
    paciente_name = unquote(query.name)
    logger.debug(f"Deleting patient data #{paciente_name}")
    
    # Criando conexão com a base
    session = Session()
    
    # Buscando paciente
    paciente = session.query(Patient).filter(Patient.name == paciente_name).first()
    
    if not paciente:
        error_msg = "Paciente não encontrado na base :/"
        logger.warning(f"Erro ao deletar paciente '{paciente_name}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        session.delete(paciente)
        session.commit()
        logger.debug(f"Deletado paciente #{paciente_name}")
        return {"message": f"Paciente {paciente_name} removido com sucesso!"}, 200

 
if __name__ == '__main__':
    app.run(debug=True)