import json 
import csv

with open("/home/sarah/lnpg/instituicoes-AL.json", "r") as f:
    dados = json.load(f) #dict
    #print(dados)
    
instituicoes = dados['instituicoes'] #lista

# 1 - Imprimir todos os CNPJS 
'''
for instituicao in instituicoes:
    if 'cnpj' in instituicao:
        print(instituicao['cnpj'])
'''

# 2 - Imprimir todas as ofertas, removendo as duplicatas
'''
# print(dados['instituicoes'][0].keys())

ofertas = []
for instituicao in instituicoes:
    if 'cursos' in instituicao:
        for curso in instituicao["cursos"]:
            ofertas.append(curso["tipo_oferta"])
            
print(ofertas)
ofertas_unicas = set(ofertas)
print(ofertas_unicas)
'''
    
# 3 - Imprimir estatistica de modalidade 
'''
modalidades = []
for instituicao in instituicoes:
    for curso in instituicao["cursos"]:
        if 'modalidade' in curso:
            modalidades.append(curso['modalidade'])
            
modalidades_unicas = set(modalidades)
print(modalidades_unicas)

total_modalidades = len(modalidades)
presencial = modalidades.count("EDUCAÇÃO PRESENCIAL")/total_modalidades * 100
distancia = modalidades.count("EDUCAÇÃO A DISTÂNCIA")/total_modalidades * 100

print(f"Modalidade presencial: {presencial:.2f}%\nModalidade a distância: {distancia:.2f}%")
'''

# 4 - Listar todos os cursos ministrados em araapiraca 
'''
cursos_arapicara = []
for instituicao in instituicoes:
    municipio = instituicao["endereco"]["municipio"]
    if municipio == 'Arapiraca':
        for curso in instituicao["cursos"]:
            cursos_arapicara.append(curso["nome"])
   
print("CURSOS OFERTADOS EM ARAPIRACA:")         
curso_arapicara = set(cursos_arapicara)
for curso in curso_arapicara:
    print(curso)
'''

# 5 - Gerar CSV com [cnpj, cod escola, nome curso, modalidade curso, cidade]
'''
with open("inst.csv", "w", newline="") as c:
    writer = csv.writer(c)
    writer.writerow(["cnpj", "cod_escola", "nome curso", "modalidade curso", "cidade"])
    
    for instituicao in instituicoes: 
        if 'cnpj' in instituicao:
            cnpj = instituicao["cnpj"]
        cod_escola = instituicao["codEscola"]
        cidade = instituicao["endereco"]["municipio"]
            
        for curso in instituicao['cursos']:
            if 'modalidade' in curso or 'nome' in curso:
                nome = curso['nome']
                modalidade = curso['modalidade']
                     
            writer.writerow([cnpj, cod_escola, nome, modalidade])
'''              