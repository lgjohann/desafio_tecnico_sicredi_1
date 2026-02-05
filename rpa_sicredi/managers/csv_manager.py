from typing import List

import pandas as pd


class CsvManager:
    """
    Classe que gerencia o processamento com pandas de um arquivo Csv.

    Attributes:
        file (str): O caminho para o arquivo Csv a ser processado.
        df (pandas.DataFrame): O DataFrame representando os dados
        do arquivo Csv.
    """

    def __init__(self, file: str):
        """
        Inicializa a instância do CsvManager e carrega os
        dados do arquivo Csv.

        Args:
            file (str): Caminho para o arquivo Csv.
        """
        self.file = file
        self.df = None
        self._read_file()


    def _read_file(self):
        """
        Lê o arquivo Csv e armazena os dados no atributo `df`.

        Raises:
            Exception: Caso o arquivo não seja encontrado
            ou não possa ser lido.
        """
        try:
            self.df = pd.read_csv(self.file)
        except Exception:
            raise Exception(
                'Não foi encontrado o arquivo Csv para leitura do robô.'
            )


    def view_df(self):
        """
        Exibe o DataFrame carregado no console.
        """
        print(self.df)


    def add_columns(self, columns: List[str]):
        """
        Adiciona colunas ao DataFrame, preenchendo com valores padrão.

        Args:
            columns (List[str]): Lista de nomes das colunas
            a serem adicionadas.
        """
        for column in columns:
            if column not in self.df.columns:
                if 'STATUS' in column:
                    self.df[column] = 'pendente'
                else:
                    self.df[column] = 'Null'


    def _convert_columns_to_str(self):
        """
        Converte todas as colunas do DataFrame para o tipo string.
        """
        for column in self.df.columns:
            if self.df[column].dtype != str:
                self.df[column] = self.df[column].astype(str)


    def get_row_by_id(self, id_row: int) -> dict:
        """
        Obtém uma linha do DataFrame com base em seu índice.

        Args:
            id_row (int): Índice da linha.

        Returns:
            dict: Linha correspondente convertida em dicionário.
        """
        row = self.df.iloc[id_row]
        return row.to_dict()


    def check_pending_lines(self) -> bool:
        """
        Verifica se há linhas com status "pendente".

        Returns:
            bool: True se houver linhas pendentes, False caso contrário.
        """
        pendings = self.df[self.df['STATUS'] == 'pendente']
        return not pendings.empty


    def update_status_by_id(self, id_row: int, status: str):
        """
        Atualiza o status de uma linha específica com base no índice.

        Args:
            id_row (int): Índice da linha a ser atualizada.
            status (str): Novo status a ser atribuído.
        """
        self.df.at[id_row, 'STATUS'] = status


    def update_cell_by_query(
        self,
        name_column: str,
        item_value: str,
        column: str,
        value: str
    ):
        """
        Atualiza uma célula do DataFrame com base em uma consulta.

        Args:
            name_column (str): Nome da coluna para busca.
            item_value (str): Valor a ser procurado na coluna.
            column (str): Nome da coluna a ser atualizada.
            value (str): Novo valor a ser atribuído.

        Raises:
            ValueError: Se a coluna especificada para busca não existir.
        """
        if name_column not in self.df.columns:
            raise ValueError(
                f'A coluna {name_column} não existe no DataFrame.'
            )

        row_with_value = self.df[name_column] == item_value
        if row_with_value.any():
            self.df.loc[row_with_value, column] = value


    def save_file(self, path_file: str = None):
        """
        Salva o DataFrame no arquivo Csv.

        Args:
            path_file (str, opcional): Caminho para salvar o
            arquivo. Se não for fornecido usa o caminho original
            do arquivo.
        """
        if not path_file:
            path_file = self.file
        self.df.to_csv(path_file, index=False)


    def add_data(self, row_data: dict):
        """
        Adiciona uma nova linha ao DataFrame.

        Args:
            row_data (dict): Dicionário representando os
            dados da nova linha.

        Raises:
            ValueError: Se alguma chave do dicionário não
            corresponder a uma coluna existente.
        """
        for key in row_data.keys():
            if key not in self.df.columns:
                raise ValueError(
                    f'A coluna {key} não existe no arquivo.'
                )
        new_row_df = pd.DataFrame([row_data])
        self.df = pd.concat([self.df, new_row_df], ignore_index=True)


    def row_exists(self, column_name: str, unique_value: str) -> bool:
        """
        Verifica se existe uma linha no DataFrame com um
        valor único em uma coluna.

        Args:
            column_name (str): Nome da coluna a ser verificada.
            unique_value (str): Valor a ser procurado na coluna.

        Returns:
            bool: True se a linha existir, False caso contrário.

        Raises:
            ValueError: Se a coluna especificada não existir.
        """
        if column_name not in self.df.columns:
            raise ValueError(
                f'A coluna {column_name} não existe no DataFrame.'
            )

        exists = not self.df[self.df[column_name] == unique_value].empty
        return exists


    def get_row_by_value(
            self, column_name: str, item_value: str
        ) -> dict | None:
        """
        Obtém uma linha do DataFrame com base no valor
        de uma coluna específica.

        Args:
            column_name (str): Nome da coluna a ser pesquisado.
            item_value (str): Valor a ser procurado na coluna.

        Returns:
            dict | None: Retorna a linha correspondente como
            um dict se for encontrada, ou None se não encontrar.
        """
        row = self.df.loc[self.df[column_name] == item_value]

        if not row.empty:
            return row.iloc[0].to_dict()
        return None

    def drop_column(self, column_name: str):
        """
        Remove uma coluna do DataFrame.

        Args:
            column_name (str): Nome da coluna a ser removida.

        Raises:
            ValueError: Se a coluna especificada não existir.
        """
        if column_name not in self.df.columns:
            return None
        self.df = self.df.drop(column_name, axis=1)

    def count_status_success(self) -> int:
        """
        Conta o número de linhas com status "Sucesso".

        Returns:
            int: Número de linhas com status "Sucesso".
        """
        success_count = self.df[self.df['STATUS'] == 'Sucesso'].shape[0]
        return success_count
