def converteCsv(arquivo,id):
    with open(f'{arquivo}', 'r') as f_in, open(f"{str(arquivo.split('.')[0])}_final.csv", 'w') as f_out:
        content = f_in.read().replace(';', '";"')
        content = content.replace(f'{id}";',f'"{id}";')
        content = content.replace(';"Pedro Magossi (AVEC)',';"Pedro Magossi (AVEC)"')
        content = content.replace('SALAO_ID";','"SALAO_ID";')
        content = content.replace(';"RESPONSAVEL',';"RESPONSAVEL"')            
        f_out.write(content)
        print( f"Planilha de {str(arquivo.split('.')[0])} convertida.")


def eliminaColunaVazia(df):
    lista_colunas = []

    for col in df.columns:
        coluna = df.loc[:,col].isnull().sum()
        if(coluna < len(df)):
            lista_colunas.append(col)

    return lista_colunas

def pegaSoNumero(valor: str) -> str:
    aux = str(valor).replace('.0','').replace('nan','')
    return ''.join(filter(lambda i: i if i.isdigit() else None, aux))