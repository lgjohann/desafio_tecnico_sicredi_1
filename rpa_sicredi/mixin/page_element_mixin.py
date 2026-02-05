from abc import ABC
from typing import List, Tuple
import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class PageElementMixIn(ABC):
    def __init__(self, webdriver: WebDriver):
        """Método construtor para iniciar o webdriver

        Args:
            webdriver: webdriver que será executado
        """
        self._webdriver: WebDriver = webdriver

        self.wait3 = WebDriverWait(self._webdriver, 3)
        self.wait5 = WebDriverWait(self._webdriver, 5)
        self.wait10 = WebDriverWait(self._webdriver, 10)
        self.wait20 = WebDriverWait(self._webdriver, 20)
        self.wait60 = WebDriverWait(self._webdriver, 60)
        self.wait120 = WebDriverWait(self._webdriver, 120)

    def find(
        self, locator: Tuple[str, str], t: int = 60, el_type: str = 'presence'
    ) -> WebElement:
        """Encontra o WebElement de acordo com seu locator

        Args:
            locator (tuple): tupla com as informações do WebElement

        Returns:
            WebElement: Elemento do DOM
        """
        self.wait_element(locator, t, el_type)
        return self._webdriver.find_element(*locator)

    def wait_(self, t: int = 60) -> WebDriverWait[WebDriver]:
        return WebDriverWait(self._webdriver, t)  # type: ignore

    def wait_element(
        self, locator: Tuple[str, str], t: int = 60, el_type: str = 'presence'
    ) -> WebElement:
        if el_type == 'presence':
            return self.wait_(t).until(EC.presence_of_element_located(locator))
        elif el_type == 'clickable':
            return self.wait_(t).until(EC.element_to_be_clickable(locator))
        elif el_type == 'visibility':
            return self.wait_(t).until(
                EC.visibility_of_element_located(locator)
            )

    def finds(
        self, locator: Tuple[str, str], t: int = 60, el_type: str = 'presence'
    ) -> List[WebElement]:
        """Encontra os WebElements de acordo com seu locator

        Args:
            locator (tuple): tupla com as informações do WebElement

        Returns:
            WebElement (list): lista com os elementos encontrados.
        """
        # self.wait60.until(EC.presence_of_element_located(locator))
        self.wait_element(locator, t, el_type)
        return self._webdriver.find_elements(*locator)

    def finds_10(self, locator: Tuple[str, str]) -> List[WebElement]:
        """Encontra os WebElements de acordo com seu locator

        Args:
            locator (tuple): tupla com as informações do WebElement

        Returns:
            WebElement (list): lista com os elementos encontrados.
        """
        self.wait10.until(EC.presence_of_element_located(locator))
        return self._webdriver.find_elements(*locator)

    def finds_3(self, locator: Tuple[str, str]) -> List[WebElement]:
        """Encontra os WebElements de acordo com seu locator

        Args:
            locator (tuple): tupla com as informações do WebElement

        Returns:
            WebElement (list): lista com os elementos encontrados.
        """
        self.wait3.until(EC.presence_of_element_located(locator))
        return self._webdriver.find_elements(*locator)

    def open_url(self, url: str) -> None:
        """Abre a url no navegador"""
        self._webdriver.get(url)

    def wait_element_and_click(self, locator: Tuple[str, str]) -> None:
        """Aguarda a presença do elemento e clica no mesmo

        Args:
            locator (tuple): tupla com as informações do WebElement
        """
        self.wait10.until(EC.presence_of_element_located(locator))
        self.find(locator).click()

    def wait5_element_and_click(self, locator: Tuple[str, str]) -> None:
        """Aguarda a presença do elemento e clica no mesmo

        Args:
            locator (tuple): tupla com as informações do WebElement
        """
        self.wait5.until(EC.presence_of_element_located(locator))
        self.find(locator).click()

    def wait10_element_and_click(self, locator: Tuple[str, str]) -> None:
        """Aguarda a presença do elemento e clica no mesmo

        Args:
            locator (tuple): tupla com as informações do WebElement
        """
        self.wait10.until(EC.presence_of_element_located(locator))
        self.find(locator).click()

    def wait_visibility_element_and_click(
        self, locator: Tuple[str, str]
    ) -> None:
        """Aguarda a presença do elemento e clica no mesmo

        Args:
            locator (tuple): tupla com as informações do WebElement
        """
        self.wait60.until(EC.visibility_of_element_located(locator))
        self.find(locator).click()

    def wait_clickable_element_and_click(
        self, locator: Tuple[str, str]
    ) -> None:
        """Aguarda a presença do elemento clicável e clica no mesmo

        Args:
            locator (tuple): tupla com as informações do WebElement
        """
        self.wait60.until(EC.element_to_be_clickable(locator))
        self.find(locator).click()

    def wait_elements_and_click(
        self, locator: Tuple[str, str], index: int
    ) -> None:
        """Aguarda a presença dos elementos clica no elemento de índice i

        Args:
            locator (tuple): tupla com as informações do WebElement
            i (integer): índice da lista gerada, do elemento à ser clicado
        """
        self.wait60.until(EC.presence_of_element_located(locator))
        elements = self.finds(locator)
        elements[index].click()

    def wait_element_and_send_keys(
        self, locator: Tuple[str, str], keys: str
    ) -> None:
        """Aguarda a presença do elemento e envia à ele a infomação de Keys

        Args:
            locator (tuple): tupla com as informações do WebElement
            keys (string): informação a ser enviada
        """
        self.wait60.until(EC.presence_of_element_located(locator))
        self.find(locator).send_keys(keys)

    def wait_elements_and_send_keys(
        self, locator: Tuple[str, str], index: int, keys: str
    ) -> None:
        """Aguarda a presença dos elementos, e envia ao elemento de índice
        index a infomação de Keys

        Args:
            locator (tuple): tupla com as informações do WebElement
            index (integer): índice da lista
            keys (string): informação a ser enviada
        """
        self.wait60.until(EC.presence_of_element_located(locator))
        elements = self.finds(locator)
        elements[index].send_keys(keys)

    def switch_to_frame(self, frame_name: str) -> None:
        """Alterar para o frame selecionado

        Args:
            to (string): nome do frame que quer alterar

        """
        return self._webdriver.switch_to.frame(frame_name)

    def switch_to_default_content(self) -> None:
        """Alterar para o frame default"""
        return self._webdriver.switch_to.default_content()

    def switch_to_parent_frame(self) -> None:
        """Alterar para o frame pai"""
        return self._webdriver.switch_to.parent_frame()
    
    def open_new_tab_and_go_to_url(self, url: str) -> None:
        """
        Abre uma nova aba no navegador e acessa a URL informada.

        Args:
            url (str): Endereço da página a ser acessada.
        """
        self._webdriver.switch_to.new_window('tab')
        self._webdriver.get(url)

    def switch_to_tab(self, tab_index: int) -> None:
        """
        Alterna o foco do navegador entre abas abertas.

        Args:
            tab_index (int): Índice da aba (0 = primeira aba, 1 = segunda, etc).
        """
        tabs = self._webdriver.window_handles
        if 0 <= tab_index < len(tabs):
            self._webdriver.switch_to.window(tabs[tab_index])
        else:
            raise IndexError(f"O índice {tab_index} não existe. Abas abertas: {len(tabs)}")


    def quit_webdriver(self) -> None:
        """Fecha o webdriver"""
        return self._webdriver.quit()
