import csv
import os
from time import sleep

from selenium.webdriver.common.by import By


from rpa_sicredi.mixin.page_element_mixin import PageElementMixIn
from rpa_sicredi.mixin.page_system_mixin import PageSystemMixin

    
class PageSicredi(PageSystemMixin, PageElementMixIn):

    
    BTN_ALLOW_COOKIES = (By.XPATH, "//span[normalize-space()='Permitir Todos']")

    BTN_MENU_PRODUTOS = (By.XPATH, "//a[contains(@class, 'nav__link') and contains(text(), 'Produtos')]")
    
    # A lista não ordenada contendo as 3 colunas (uma //li para cada) (Você, Empresa, Agro)
    COLUNA_CATEGORIAS = (By.XPATH, "/html/body/header/div/div[2]/nav/ul/li[2]/div/ul")
    
    LOCATOR_TITULO_RELATIVO = (By.XPATH, ".//div[@class='u-flex']/a[contains(@class, 'nav-dropdown__heading') and (contains(text(), 'Você') or contains(text(), 'Empresa') or contains(text(), 'Agronegócio'))]")

    LOCATOR_LINKS_RELATIVO = (By.XPATH, ".//a[@class='nav-dropdown__link']")

    def extract_data_sicredi(self, csv_path: str):
        """
        Abre o menu 'Produtos', lê as colunas do dropdown e salva em CSV.
        """
        # 1 - Fecha o banner de cookies (se aparecer) e abre o menu de Produtos
        try:
            self.wait5_element_and_click(self.BTN_ALLOW_COOKIES)
            print("Banner de cookies fechado.")
            sleep(1)
        except Exception:
            print("Banner de cookies não apareceu ou não foi necessário.")
            pass


        print("Abrindo menu de Produtos...")
        try:
            self.wait_element_and_click(self.BTN_MENU_PRODUTOS)
            sleep(2) 
        except Exception as e:
            error_message = f"Erro ao clicar no menu Produtos: {e}"
            print(error_message)
            raise Exception(error_message)

        # 2 - encontra as 3 colunas (Você, Empresa, Agro)
        try:
            colunas_parent = self.finds(self.COLUNA_CATEGORIAS)

            # cada coluna é uma lista filha
            colunas = colunas_parent[0].find_elements(By.XPATH, "./li")  

        except Exception as e:
            error_message = f"Não foi possível encontrar as colunas do menu: {e}"
            print(error_message)
            raise Exception(error_message)

        dados_extraidos = []

        # 3 - itera sobre cada coluna para extrair dados
        for coluna in colunas:
            try:
                elemento_titulo = coluna.find_element(*self.LOCATOR_TITULO_RELATIVO)
                nome_categoria = elemento_titulo.get_attribute("textContent").strip()                

                links_produtos = coluna.find_elements(*self.LOCATOR_LINKS_RELATIVO)

                print(f"Lendo Categoria: {nome_categoria} - Encontrados {len(links_produtos)} itens.")

                for link in links_produtos:
                    texto_item = link.get_attribute("textContent").strip()
                    href = link.get_attribute("href")
                    
                    if texto_item and href:
                        dados_extraidos.append({
                            "Categoria": nome_categoria,
                            "Item": texto_item,
                            "Link": href
                        })
            except Exception as e:
                error_message = f"Erro ao processar uma das colunas: {e}"
                print(error_message)
                raise Exception(error_message)

        # 4 - salva no CSV
        if dados_extraidos:
            self.__save_to_csv(dados_extraidos, csv_path)
            print(f"Sucesso! {len(dados_extraidos)} linhas adicionadas ao CSV.")
        else:
            print("Nenhum dado encontrado para salvar.")

    def __save_to_csv(self, dados: list, filepath: str):
        arquivo_existe = os.path.isfile(filepath)
        colunas = ["Categoria", "Item", "Link"]
        try:
            with open(filepath, mode='a', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=colunas, delimiter=';')
                if not arquivo_existe or os.stat(filepath).st_size == 0:
                    writer.writeheader()
                writer.writerows(dados)
        except Exception as e:
            print(f"Erro ao salvar CSV: {e}")
            raise Exception(e)
        
    

    
    # ============================================================
    # Métodos abstratos implementados (herdados da AbstractPage) #
    # ============================================================

    def go_to_homepage(self):
        pass

    def logout(self):
        pass

    def extract_data(self):
        pass

    def login(self, username: str, password: str):
        pass
