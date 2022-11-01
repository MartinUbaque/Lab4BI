serialStr = '"serial_no": ['
greStr = '"gre_score": ['
toeflStr = '"toefl_score": ['
universityStr = '"university_rating": ['
sopStr = '"sop": ['
lorStr = '"lor": ['
cgpaStr = '"cgpa": ['
researchStr = '"research": ['
admissionStr = '"admission_points": ['

def hayVacio(lista):
    for elem in lista:
        if len(elem) == 0 or elem is None or elem == '':
            return True
    return False


with open('datos.csv', 'r') as data:
    Lines = data.readlines()

    contador = 0
    for line in Lines:
        datos = line.split(',')
        if (not hayVacio(datos)):
            try:
                float (datos[1])
                float (datos[9])
                serialStr += datos[1] + ','
                greStr += datos[2] + ','
                toeflStr += datos[3] + ','
                universityStr +=  datos[4] + ','
                sopStr += datos[5] + ','
                lorStr += datos[6] + ','
                cgpaStr += datos[7] + ','
                researchStr += datos[8] + ','
                admissionStr += datos[9] + ','
            except:
                print(line)
            # contador += 1
            # if contador > 20:
            #     break

serialStr = serialStr[:-1] + '],'
greStr = greStr[:-1] + '],'
toeflStr = toeflStr[:-1] + '],'
universityStr = universityStr[:-1] + '],'
sopStr = sopStr[:-1] + '],'
lorStr = lorStr[:-1] + '],'
cgpaStr = cgpaStr[:-1] + '],'
researchStr = researchStr[:-1] + '],'
admissionStr = admissionStr[:-1] + ']'
admissionStr = admissionStr.replace('\n', '')

message = '''{
    '''+serialStr+'''
    '''+greStr+'''
    '''+toeflStr+'''
    '''+universityStr+'''
    '''+sopStr+'''
    '''+lorStr+'''
    '''+cgpaStr+'''
    '''+researchStr+'''
    '''+admissionStr+'''
}
'''
file1 = open('scorer.JSON', 'w')
file1.writelines(message)
file1.close()
