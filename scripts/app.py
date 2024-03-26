import os
import pandas as pd 
from tkinter import filedialog
from modelsTables import clientes

os.system('cls')
print("""
█▀▄▀█ █ █▀▀ █▀█ ▄▀█ █▀▀ ▄▀█ █▀█   █▀▄ █▀▀   █▀█ █░░ ▄▀█ █▄░█ █ █░░ █░█ ▄▀█ █▀   █▀▄▀█ █▀█ █▀▄ █▀▀ █░░ █▀█ █▀
█░▀░█ █ █▄█ █▀▄ █▀█ █▄▄ █▀█ █▄█   █▄▀ ██▄   █▀▀ █▄▄ █▀█ █░▀█ █ █▄▄ █▀█ █▀█ ▄█   █░▀░█ █▄█ █▄▀ ██▄ █▄▄ █▄█ ▄█
""")

def pegaPastaDeDestino():
    local = filedialog.askdirectory()
    return local

path = pegaPastaDeDestino().replace('/','\\') + '\\'

id = input("Digite o id do salao: ")

tipo_dados = input("Um único arquivo para mais de uma tabela ? S/N : ")

files = os.listdir(path)

files_excel = [item for item in files if '.xlsx' in item] 

if tipo_dados.upper() == 'N':
    clientes_file = ''
    produtos_file = ''
    servicos_file = ''
    profissionais_file = ''    

    for file in files_excel:
        
        if 'CLIENTE'  in str(file).upper():
            clientes_file = path + file
            print("\n* - clientes => "+ file)
        elif 'PRODUTOS' in str(file).upper():
            produtos_file = path + file
            print("* - produtos => "+ file)
        elif 'SERVI' in str(file).upper():
            servicos_file = path + file
            print("* - serviços => "+ file)
        elif 'PROFISSIONA' in str(file).upper():
            profissionais_file = path + file
            print("* - profissionais => "+ file)
    
    confirmacao = input("\nEstá correto a relação ? S/N : ")

    if confirmacao.upper() == 'S':
        clientes.formataPlanilhaClientes(id,clientes_file,path)



elif tipo_dados.upper() == 'S':  

    if len(files_excel) == 1:

        path_df = path +"\\"+ files_excel[0]
        df = pd.ExcelFile(path_df)
        list_sheets = df.sheet_names

        for sheet in list_sheets:
            if 'CLIENTE'  in str(sheet).upper():
                clientes = pd.read_excel(path_df,sheet_name=sheet)
                clientes.columns = clientes.iloc[0,:].values
                clientes.drop([0,1],axis=0,inplace=True)

            elif 'PRODUTO' in str(sheet).upper():
                produtos = pd.read_excel(path_df,sheet_name=sheet)
                produtos.columns = produtos.iloc[0,:].values
                produtos.drop([0,1],axis=0,inplace=True)

            elif 'SERVI' in str(sheet).upper():
                servicos = pd.read_excel(path_df,sheet_name=sheet)
                servicos.columns = servicos.iloc[0,:].values
                servicos.drop([0,1],axis=0,inplace=True)
                 
            elif 'PROFISSIONA' in str(sheet).upper():
                profissionais = pd.read_excel(path_df,sheet_name=sheet)
                profissionais.columns = profissionais.iloc[0,:].values
                profissionais.drop([0,1],axis=0,inplace=True)
                
        

    else:
        print(f'Na pasta existe mais de um arquivo {files_excel}')