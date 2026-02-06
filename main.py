from os import getenv, environ
import os
from time import sleep
import sys
import pandas as pd

from dotenv import load_dotenv

from rpa_sicredi.drivers.webdriver_setup import WebdriverSetup
from rpa_sicredi.managers.csv_manager import CsvManager
from rpa_sicredi.pages.page_sicredi import PageSicredi

environ['PYTHONUNBUFFERED'] = '1'
sys.stdout.reconfigure(line_buffering=True)

print("=" * 50, flush=True)
print("SCRIPT SICREDI INICIADO", flush=True)
print("=" * 50, flush=True)

loop = 'ON'
state = 'INITIALIZATION'
first_execution = True

load_dotenv()
csv_file_path = getenv('CSV_FILE')
url_sicredi = 'https://sicrediconexao.com.br/'

webdriver = None 

while loop == 'ON':

    match state:

        case 'INITIALIZATION':
            try:
                print('--- INICIALIZANDO ---')
                if first_execution:
                    if not os.path.exists(csv_file_path) or os.stat(csv_file_path).st_size == 0:
                        print(f"Arquivo {csv_file_path} não encontrado ou vazio. Criando novo...")
                        
                        df_inicial = pd.DataFrame(columns=['Categoria', 'Item', 'Link'])
                        df_inicial.to_csv(csv_file_path, index=False, sep=';')


                    # Categoria: "Você/Empresa/Agro", Item: "Nome do Menu", Link: "Href"
                    csv_manager = CsvManager(csv_file_path)
                    csv_manager.save_file()                
                webdriver_setup = WebdriverSetup()
                webdriver = webdriver_setup.generate_webdriver()
                webdriver.maximize_window()
                
                page_sicredi = PageSicredi(webdriver)
                page_sicredi.open_url(url_sicredi);
                sleep(2)

                state = 'PROCESS'
                continue

            except Exception as error:
                print(f'Erro durante inicialização: {error}')
                state = 'END'

        case 'PROCESS':
            try:
                print('--- INICIANDO PROCESSO DE EXTRAÇÃO ---')
                
                page_sicredi.extract_data_sicredi(csv_file_path)

                print('Extração das 3 categorias finalizada com sucesso.')
                state = 'END'
                continue
            
            except Exception as error:
                print(f'Erro extraindo dados: {error}')
                state = 'END'
                continue
        
        case 'END':
            try:
                print('--- FINALIZANDO PROCESSO ---')
                if webdriver:
                    webdriver.quit()
                loop = 'OFF'
                continue
            except Exception as error:
                print(f'Erro ao finalizar: {error}')
                loop = 'OFF'
            finally:
                sys.exit(0)