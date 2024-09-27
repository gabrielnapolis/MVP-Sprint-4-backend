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
home_tag = Tag(name="Documentation", description="Document Selection: Swagger, Redoc or RapiDoc.")
patient_tag = Tag(name="Patients", description="Insert, view, remove and prediction of Heart Disease Patients.")


@app.get('/', tags=[home_tag])
def home():
    """Document Selection.
    """
    return redirect('/openapi')


@app.get('/patients', tags=[patient_tag],
         responses={"200": PatientViewSchema, "404": ErrorSchema})
def get_patients():
    """List all patients     
    Returns:
        list of all patients and yours predictions
    """
    logger.debug("Data collection from all patients")

    session = Session()

    patients = session.query(Patient).all()
    
    if not patients:
        return [], 200
    else:
        logger.debug(f"%d patients found: " % len(patients))
        return show_patients(patients), 200


@app.post('/patient', tags=[patient_tag],
          responses={"200": PatientViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict():
    """Enter the patient into the database and perform your Heart Disease prediction.
    Returns:
        Patient data and its prediction.
    """
    try:
        # Extrating JSON from the request
        content: PatientSchema = request.get_json()  

        # Prepare data for the model
        X_input = PreProcessor.prepare_form(content)  # Pass the dictionary
        model_path = './MachineLearning/pipelines/svm_heart_disease_pipeline.pkl'
        modelo = Pipeline.loading_pipeline(model_path)
        target = int(Model.preditor(modelo, X_input)[0])

        patient = Patient(
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

        if session.query(Patient).filter(Patient.name == patient.name).first():
            error_msg = "Patient already exists"
            logger.warning(f"Error on add patient: '{patient.name}', {error_msg}")
            return jsonify({"message": error_msg}), 409

        session.add(patient)
        session.commit()
        logger.debug(f"Enter patient: '{patient.name}'")
        return show_patient(patient), 200

    except Exception as e:
        logger.error(f"Error on add patient: {str(e)}")
        return jsonify({"message": "Error on server"}), 500


@app.route('/patient/<id>', methods=["DELETE"])
def delete_patient(id):
    """Remove patient of the database

    Args:
        name (str): patient name
        
    Returns:
        msg: Success or error message
    """
    
    # Create database conection
    session = Session()
    
    # Search patient
    patient = session.query(Patient).filter(Patient.id == id).delete()
    session.commit()

    if not patient:
        error_msg = "Patient not found!"
        return {"message": error_msg}, 404
    else:
        return {"message":"patient deleted with success!", "id": id}, 200

 
if __name__ == '__main__':
    app.run(debug=True)