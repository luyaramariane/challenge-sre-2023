import os
import zipfile
from flask8o34 import Flask,jsonify
from datetime import date,datetime

app = Flask(__name__)

zip_folder = "challenge-sre-2023.zip"
zip_ref = zipfile.ZipFile(zip_folder, 'r')
zip_ref.extractall('/tmp/challenge-sre-2023')  
zip_ref.close()  

files='/tmp/challenge-sre-2023/'

#Iniciando rota raiz
@app.route('/')
def hello():
    return "Challenge SRE 2023 - Sensedia ## Leia a documentação para maiores informações ##"

###############################################################
#Realizar o filtro por nome de cliente - Ex: Cliente1
@app.route('/filter-clients/<clientName>')
def filter_clients(clientName):
    filesFromclientName = []
    for file in os.listdir(files):
        name_file=file
        if clientName in name_file and name_file.endswith(clientName):
            filesFromclientName.append(name_file)
    return jsonify({ "result": filesFromclientName})


###############################################################
#Realizar o filtro por tipo de arquivo - Ex: Calls ou Metrics
@app.route('/filter-typeFile/<typeFile>')
def list_typeFile(typeFile):
    filesByType = []
    for file in os.listdir(files):
        name_file=file
        if typeFile in name_file and name_file.startswith(typeFile):
            filesByType.append(name_file)

    return jsonify({ "result": filesByType})


###############################################################
#Realizar o filtro por data solicitada - Ex: 2022_11_01
@app.route('/filter-date/<dateFile>')
def list_date(dateFile):
    dateOfFile = []
    for file in os.listdir(files):
        name_file=file
        if dateFile in name_file:
            dateOfFile.append(name_file)
    
    return jsonify({ "result": dateOfFile})
###############################################################

#Ao informar o nome de um cliente, excluir todos os arquivos dele
@app.route('/remove-client/<clientName>')
def remove_files_from_client(clientName):
    filesToRemove = []
    for file in os.listdir(files):
        name_file=file
        if clientName in name_file and name_file.endswith(clientName):
            filesToRemove.append(name_file)

    for f in filesToRemove:
        os.remove(files+f)
    
    return f'Foram removidos {len(filesToRemove)} arquivos do {clientName}'


###############################################################
def extract_client_from_name_file(name_file):
  x = name_file.split("_")
  name_client = x[4]
  return name_client

def extract_date_from_name_file(name_file):
  x = name_file.split("_")
  date_from_file = x[1]+'_'+x[2]+'_'+x[3]
  return date_from_file

def count_days(term):
  date_term = term.replace('_', '-')
  date_object = datetime.strptime(date_term, '%Y-%m-%d').date()
  today = datetime.now().date()
  diff = today - date_object
  return diff.days

#Trazer todos os arquivos que possuam mais de X dias filtrando por nomedocliente.
@app.route('/filter-ageFiles/<client_forFilter>/<qtdDays>')
def filter_ageFile_clientName(client_forFilter,qtdDays):
  list_files = []
  for name_file in os.listdir(files):
    date_from_file = extract_date_from_name_file(name_file)
    age_file = count_days(date_from_file)
    name_client = extract_client_from_name_file(name_file)
    if age_file > int(qtdDays) and name_file.endswith(client_forFilter):
          list_files.append({"file": name_file, "age_file": age_file})
  return jsonify({ "result":list_files})


if __name__ == "__main__":
    app.run(host="0.0.0.0")
