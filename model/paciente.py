from sqlalchemy import Column, String, Integer, Float

from model import Base

class Paciente(Base):
    __tablename__ = 'patient'
    
    id = Column(Integer, primary_key=True)
    name = Column("name", String)
    age = Column("age", Integer)
    sex = Column("sex", Integer)
    cp = Column("chest_pain", Integer)
    trestbps = Column("resting_blood_pressure", Integer)
    chol = Column("serum_cholesterol", Integer)
    fbs = Column("fasting_blood_sugar", Integer)
    restecg = Column("resting_electrocardiographic_results", Integer)
    thalach = Column("maximum_heart_rate_achieved", Integer)
    exang = Column("exercise_induced_angina", Integer)
    oldpeak = Column("st_depression", Float)
    slope = Column("slope_of_peak_exercise_st_segment", Integer)
    ca = Column("number_of_major_vessels", Integer)
    thal = Column("thalassemia", Integer)
    target = Column("diagnostic", Integer, nullable=True)
    
    def __init__(self, name:str ,age:int, sex:int, cp:int,
                 trestbps:int, chol:int, fbs:int, restecg:int, 
                 thalach:int, exang:int, oldpeak:float,
                 slope:int, ca:int, thal:int, target: int):

        self.age = age
        self.name = name
        self.sex = sex
        self.cp = cp
        self.trestbps = trestbps
        self.chol = chol
        self.fbs = fbs
        self.restecg = restecg
        self.thalach = thalach
        self.exang = exang
        self.oldpeak = oldpeak
        self.slope = slope
        self.ca = ca
        self.thal = thal
        self.target = target
