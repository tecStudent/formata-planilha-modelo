import pandas as pd
import os

from utils.utlis import eliminaColunaVazia,converteCsv,pegaSoNumero

def formataPlanilhaClientes(id,file,path):
    cliente = pd.read_excel(file)

    cliente.rename(columns={
                            'Salao id':'SALAO_ID',
                            'Cliente':'CLIENTE',
                            'Nome (obrigatório)':'NOME',
                            'Nome (obrigatorio)':'NOME',
                            'Telefone':'TELEFONE', 
                            'Celular':'CELULAR', 
                            'Telefone Fixo': 'TELEFONE',
                            'Email':'EMAIL',
                            'Data de nascimento':'DATANASC', 
                            'Sexo':'SEXO', 
                            'Endereço':'ENDERECO', 
                            'Numero':'NUMERO',
                            'Complemento':'COMPLEMENTO', 
                            'Bairro':'BAIRRO', 
                            'Cidade':'CIDADE', 
                            'Estado':'ESTADO', 
                            'Observação':'OBS'}, inplace=True)


    ##################################################################### Elimina colunas vazias

    lista_coluna = eliminaColunaVazia(cliente)
    cliente = cliente[lista_coluna]

    if 'SALAO_ID' not in lista_coluna:
        cliente.insert(0,'SALAO_ID',id)
    else:
        cliente['SALAO_ID'] = id

    cliente['RESPONSAVEL'] = 'Pedro Magossi (AVEC)'




    ##################################################################### Remove letras e caracteres especiais 

    base_numeros = ['CELULAR','TELEFONE','CEP','CPF']

    lista_ajustes = [i for i in cliente.columns if i in base_numeros ]



    for col in lista_ajustes:
        cliente[col] = list(map(pegaSoNumero,cliente[col]))


        
    ##################################################################### Formata datas

    base_datas = ['DATANASC', 'DATACAD']

    datas_para_formatar = [i for i in cliente.columns if i in base_datas]

    for col in datas_para_formatar:
        try:
            cliente[col]=pd.to_datetime(cliente[col].astype(str), errors='coerce')
            cliente[col] = cliente[col].dt.strftime('%Y/%m/%d')
        except:
            ...

    ##################################################################### Formata cep e cpf

    if 'CPF' in cliente.columns:
        cliente['CPF'] = cliente['CPF'].str.zfill(11)
    # cliente['CEP'] = cliente['CEP'].str.zfill(8)


    cliente.head()
    # ##################################################################### Formata o cando sexo

    # cliente['SEXO'] = cliente['SEXO'].replace(['Masculino'], 'M')
    # cliente['SEXO'] = cliente['SEXO'].replace(['Feminino'], 'F')     
            
    ##################################################################### Remove duplicidades 

    base_duplicidades = ['NOME','TELEFONE','CELULAR','EMAIL','DATANASC','RG','CPF','SEXO','ENDERECO','NUMERO','COMPLEMENTO','BAIRRO','CIDADE','ESTADO','CEP']

    duplicidades = [i for i in cliente.columns if i in base_duplicidades]

    cliente.drop_duplicates(subset=duplicidades,keep='first', inplace=True)

    try:
        os.mkdir(f'{path}\\data_processed')
    except:
        pass

    cliente.to_csv(f'{path}\\data_processed\\Cliente.csv',sep=';',index=False,encoding='latin1') 

    converteCsv(f'{path}\\data_processed\\Cliente.csv',id)

    os.remove(f'{path}\\data_processed\\Cliente.csv')