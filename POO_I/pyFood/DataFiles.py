# CLASSE APENAS PARA MANIPULAÇÃO DOS ARQUIVOS .json ONDE SÃO PERSISTIDOS OS DADOS

import json
import os
import inspect

class DataFiles:

    @staticmethod
    def getDataJson(fileName: str, key = None) -> dict:
        # Obter o caminho do diretório do arquivo Python que chama a função
        caller_file = inspect.stack()[1].filename
        caller_dir = os.path.dirname(os.path.abspath(caller_file))

        # Construir o caminho para o arquivo JSON
        file_path = os.path.join(caller_dir, fileName)

        with open(file_path) as file:
            data = json.load(file)
        
        if key != None:
            return data.get(key, None)
        else:
            return data
    
    @staticmethod
    def addDataJson(fileName: str, data: dict, key: str)-> None:
        # Obter o caminho do diretório do arquivo Python que chama a função
        caller_file = inspect.stack()[1].filename
        caller_dir = os.path.dirname(os.path.abspath(caller_file))

        # Construir o caminho para o arquivo JSON
        file_path = os.path.join(caller_dir, fileName)

        with open(file_path, 'r+') as file:
            # Carregar os dados existentes do arquivo JSON
            dados_existentes = json.load(file)

            # Adicionar ou modificar os dados desejados
            dados_existentes[key] = data

            # Posicionar o cursor no início do arquivo
            file.seek(0)

            # Escrever os dados atualizados no arquivo
            json.dump(dados_existentes, file, indent=4)

            # Truncar o restante do arquivo, caso os novos dados sejam mais curtos que os antigos
            file.truncate()
    
    @staticmethod
    def deleteDataJson(fileName: str, key: str)-> None:
        # Obter o caminho do diretório do arquivo Python que chama a função
        caller_file = inspect.stack()[1].filename
        caller_dir = os.path.dirname(os.path.abspath(caller_file))

        # Construir o caminho para o arquivo JSON
        file_path = os.path.join(caller_dir, fileName)

        with open(file_path, 'r+') as file:
            # Carregar os dados existentes do arquivo JSON
            dados_existentes = dict(json.load(file))

            # Deletar os dados da respectiva key
            dados_existentes.pop(key)

            # Posicionar o cursor no início do arquivo
            file.seek(0)

            # Escrever os dados atualizados no arquivo
            json.dump(dados_existentes, file, indent=4)

            # Truncar o restante do arquivo, caso os novos dados sejam mais curtos que os antigos
            file.truncate()
    
    def ObjToJson(key, type):
        return DataFiles.getDataJson(type+"s.json", key)