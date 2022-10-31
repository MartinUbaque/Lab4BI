PASOS PARA LA EJECUCIÓN Y EL USO DEL API DE REGRESIÓN LINEAL:

1. Ir a la carpeta del proyecto (Lab4BI)
2. Ejecutar comando: python -m pip install -–upgrade pip
3. Ejecutar comando: pip install -r requirements.txt 
4. Ejecutar comando: uvicorn main:app --reload

Para predecir un resultado de admisión:
5. Abrir el siguiente link en un navegador: http://127.0.0.1:8000/docs#/default/make_predictions_predict_post
6. Hacer click en el botón "TRY IT OUT"
7. Ingresar un texto JSON con el siguiente formato:
{
  "serial_no": 0,
  "gre_score": 0,
  "toefl_score": 0,
  "university_rating": 0,
  "sop": 0,
  "lor": 0,
  "cgpa": 0,
  "research": 0
}
cambiando los "0" por los valores que quiere ingresar para predecir y hacer click en "EXCECUTE". La API responderá con el valor admission_points predicho.

NOTA: Si copia el formato de un archivo txt, la API leerá las linea nuevas como "\n" y enviará un error. Copie el formato del ejemplo que provee la misma API.


Para recibir el score R2 del modelo:
5. Abrir el siguiente link en un navegador: http://127.0.0.1:8000/docs#/default/determine_score_score_post
6. Hacer click en el botón "TRY IT OUT"
7. Ingresar un texto JSON con el siguiente formato:
{
  "serial_no": [0,0],
  "gre_score": [0,0],
  "toefl_score": [0,0],
  "university_rating": [0,0],
  "sop": [0,0],
  "lor": [0,0],
  "cgpa": [0,0],
  "research": [0,0],
  "admission_points": [0,0]
}
cambiando los "[0,0]" por los arrays de datos que quiere ingresar para encontrar el valor R2 del modelo y hacer click en "EXCECUTE".

NOTA: Si copia el formato de un archivo txt, la API leerá las linea nuevas como "\n" y enviará un error. Copie el formato del ejemplo que provee la misma API.
Procure que los arrays tengan la misma longitud. De lo contrario, recibirá un error.
