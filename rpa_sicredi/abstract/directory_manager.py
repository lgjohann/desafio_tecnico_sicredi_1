from abc import ABC, abstractmethod
import glob
import os
import time


class DirectoryManager(ABC):
    """
    Classe abstrata para gerenciar operações em um diretório, incluindo
    busca, exclusão e monitoramento de arquivos.
    """

    def __init__(self, directory: str):
        """
        Inicializa a classe com o diretório onde as operações 
        com arquivos serão realizadas.

        Args:
            directory (str): Caminho completo do diretório base.
        """
        self.directory = directory

    
    def _create_directory(self):
        """
        Cria o diretório caso não existir.
        """
        try:
            os.mkdir(self.directory)
        except Exception:
            pass

    
    @abstractmethod
    def search_files(self):
        """
        Método abstrato para buscar arquivos no diretório.
        
        Deve ser implementado nas subclasses.

        Returns:
            list: Lista de caminhos completos dos arquivos encontrados.
        """
        ...
    

    @abstractmethod
    def get_file(self):
        """
        Método abstrato para obter um arquivo específico do diretório.
        
        Deve ser implementado nas subclasses.

        Returns:
            str: Caminho completo do arquivo obtido.
        """
        ...
    

    def delete_file(self, path_or_file_name: str):
        """
        Deleta o arquivo especificado, caso o encontrar na pasta.
        Aceita tanto o caminho completo quanto somente o nome
        do arquivo. Se for passado apenas o nome do arquivo, usa o
        diretório da instância.

        Args:
            path_or_file_name (str): Caminho completo ou só o nome
            do arquivo para deletar.
        
        Raises:
            FileNotFoundError: Se o arquivo não for encontrado.
        """
        if not os.path.isabs(path_or_file_name):
            path_file = os.path.join(self.directory, path_or_file_name)
        else:
            path_file = path_or_file_name

        if os.path.exists(path_file):
            os.remove(path_file)
    

    def delete_files(self):
        """
        Deleta todos os arquivos do diretório instanciado.

        Este método não levanta exceções se não houver arquivos,
        apenas ignorará diretórios e arquivos que não podem ser deletados.
        """
        file_names = glob.glob(os.path.join(self.directory, '*'))

        for file_name in file_names:
            if os.path.isfile(file_name):
                os.remove(file_name)
    

    def monitor_directory(
            self, 
            keyword: str = None, 
            timeout: int = 60, 
            interval: int = 5
        ) -> str:
        """
        Monitora o diretório por um tempo determinado, aguardando um arquivo
        ser encontrado na pasta, para uso no caso de downloads.
        Se um arquivo que contenha a palavra chave for encontrado,
        retorna o caminho completo. Verifica a pasta a cada intervalo
        de segundos.

        Args:
            keyword (str, optional): Palavra chave que o robô irá
            procurar no nome dos arquivos no diretório definido.
            timeout (int, optional): Tempo em segundos limite de monitoração
            da pasta.
            interval (int, optional): Intervalo em segundos a cada iteração
            do loop.

        Returns:
            str: Nome do caminho completo do arquivo caso tenha sido
            encontrado.
            None: Se não houver arquivos correspondentes após o tempo
            de espera.
        """
        initial_time = time.time()

        while time.time() - initial_time < timeout:
            file_names = self.search_files(keyword)

            if file_names:
                file_name = file_names[0]
                return file_name
            
            time.sleep(interval)
        
        return None
