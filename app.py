from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request, jsonify
from urllib.parse import unquote
from model import *
from logger import logger
from schemas import *
from flask_cors import CORS


# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
paciente_tag = Tag(name="Paciente", description="Adição, visualização, remoção e predição de pacientes com Diabetes")

# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# Rota de listagem de pacientes
@app.get('/pacientes', tags=[paciente_tag],
         responses={"200": PacienteViewSchema, "404": ErrorSchema})
def get_pacientes():
    """Lista todos os pacientes cadastrados na base
    Args:
       none
        
    Returns:
        list: lista de pacientes cadastrados na base
    """
    logger.debug("Coletando dados sobre todos os pacientes")
    # Criando conexão com a base
    session = Session()
    # Buscando todos os pacientes
    pacientes = session.query(Paciente).all()
    
    if not pacientes:
        # Se não houver pacientes
        return {"pacientes": []}, 200
    else:
        logger.debug(f"%d pacientes econtrados" % len(pacientes))
        print(pacientes)
        return apresenta_pacientes(pacientes), 200


# Rota de adição de paciente
@app.post('/paciente', tags=[paciente_tag],
          responses={"200": PacienteViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict():
    """Insere um paciente na base de dados e realiza sua predição
    Args:
       none
        
    Returns:
        list: lista de pacientes cadastrados na base
    """
    try:
        content: PacienteSchema = request.get_json()  # Extraindo JSON da requisição

        # Preparando os dados para o modelo
        X_input = PreProcessador.preparar_form(content)  # Passa o dicionário
        model_path = './MachineLearning/pipelines/svm_heart_disease_pipeline.pkl'
        modelo = Pipeline.carrega_pipeline(model_path)
        target = int(Model.preditor(modelo, X_input)[0])

        paciente = Paciente(
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

        # Adicionando paciente ao banco de dados
        session = Session()

        if session.query(Paciente).filter(Paciente.name == paciente.name).first():
            error_msg = "Paciente já existente na base"
            logger.warning(f"Erro ao adicionar paciente '{paciente.name}', {error_msg}")
            return jsonify({"message": error_msg}), 409

        session.add(paciente)
        session.commit()
        logger.debug(f"Adicionado paciente de name: '{paciente.name}'")
        return apresenta_paciente(paciente), 200

    except Exception as e:
        logger.error(f"Erro ao adicionar paciente: {str(e)}")
        return jsonify({"message": "Erro no servidor"}), 500

# Métodos baseados em name
# Rota de busca de paciente por nome
@app.get('/paciente', tags=[paciente_tag],
         responses={"200": PacienteViewSchema, "404": ErrorSchema})
def get_paciente(query: PacienteBuscaSchema):    
    """Faz a busca por um paciente cadastrado na base a partir do name

    Args:
        name (str): name do paciente
        
    Returns:
        dict: representação do paciente e diagnóstico associado
    """
    
    paciente_name = query.name
    logger.debug(f"Coletando dados sobre produto #{paciente_name}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    paciente = session.query(Paciente).filter(Paciente.name == paciente_name).first()
    
    if not paciente:
        # se o paciente não foi encontrado
        error_msg = f"Paciente {paciente_name} não encontrado na base :/"
        logger.warning(f"Erro ao buscar produto '{paciente_name}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Paciente econtrado: '{paciente.name}'")
        # retorna a representação do paciente
        return apresenta_paciente(paciente), 200
   
    
# Rota de remoção de paciente por name
@app.delete('/paciente', tags=[paciente_tag],
            responses={"200": PacienteViewSchema, "404": ErrorSchema})
def delete_paciente(query: PacienteBuscaSchema):
    """Remove um paciente cadastrado na base a partir do name

    Args:
        name (str): name do paciente
        
    Returns:
        msg: Mensagem de sucesso ou erro
    """
    
    paciente_name = unquote(query.name)
    logger.debug(f"Deletando dados sobre paciente #{paciente_name}")
    
    # Criando conexão com a base
    session = Session()
    
    # Buscando paciente
    paciente = session.query(Paciente).filter(Paciente.name == paciente_name).first()
    
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