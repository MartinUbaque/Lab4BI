from typing import List
from pydantic import BaseModel

class DataModelScore(BaseModel):

# Estas varibles permiten que la librería pydantic haga el parseo entre el Json recibido y el modelo declarado.
    serial_no: List
    gre_score: List
    toefl_score: List
    university_rating: List
    sop: List
    lor: List 
    cgpa: List
    research: List
    admission_points: List


#Esta función retorna los nombres de las columnas correspondientes con el modelo esxportado en joblib.
    def columns(self):
        return ["Serial No.","GRE Score","TOEFL Score","University Rating","SOP","LOR " ,"CGPA","Research","Admission Points"]

