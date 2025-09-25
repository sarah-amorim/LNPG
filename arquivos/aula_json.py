import json 

# https://www.notion.so/Manipula-o-de-Arquivos-em-Python-26534af6164e818ab621e1d4db547b23

with open("instituicoes-AL.json", "r") as f:
    dados = json.load(f)
    #print(dados)

instituicoes = dados['instituicoes']

'''
# 1 - Imprimir todos os CNPJS 
for instituicao in instituicoes:
    if 'cnpj' in instituicao:
        print(instituicao['cnpj'])
'''

'''
2 - Imprimir todas as ofertas, removendo as duplicatas
'''

'''
3 - Imprimir estatistica de modalidade 
- 30% educação presencial 
- 20% ...
'''
