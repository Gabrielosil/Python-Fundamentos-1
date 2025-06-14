import os

print(f'Diretorio Atual: {os.getcwd()}')


if not os.path.exists("teste"):
    os.mkdir("teste")
    print("Pasta 'teste' criada com sucesso!!")

    caminho_arquivo = os.path.join("teste", "arquivo.txt")

    with open(caminho_arquivo, 'w') as arquivo: 
        arquivo.write("Este arquivo é criado dentro da pasta 'teste'. \n")

        print(f'Arquivo criado em: {caminho_arquivo}!!')