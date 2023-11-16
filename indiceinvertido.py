from collections import defaultdict

def criar_indice_invertido(documentos):
    indice = defaultdict(list)

    for doc_id, documento in enumerate(documentos):
        palavras = documento.split()
        for palavra in palavras:
            palavra = palavra.lower()
            if doc_id not in indice[palavra]:
                indice[palavra].append(doc_id)

    return indice

def pesquisar_documento_por_palavra_chave(indice, palavra_chave, documentos):
    palavra_chave = palavra_chave.lower()
    documentos_correspondentes = []

    if palavra_chave in indice:
        documentos_correspondentes = [documentos[doc_id] for doc_id in indice[palavra_chave]]

    return documentos_correspondentes


documentos = [
    "RG: 1234567",
    "CPF: 300"
    "CDI: 34666982-1"
    "Certidão de nascimento: 87489308 "
    "NIS: 84573-324532"
]

indice_invertido = criar_indice_invertido(documentos)


palavra_chave = input("Digite a palavra-chave para pesquisa: ")
documentos_encontrados = pesquisar_documento_por_palavra_chave(indice_invertido, palavra_chave, documentos)

if documentos_encontrados:
    print("Documentos encontrados:")
    for documento in documentos_encontrados:
        print(documento)
else:
    print("Nenhum documento correspondente à pesquisa.")