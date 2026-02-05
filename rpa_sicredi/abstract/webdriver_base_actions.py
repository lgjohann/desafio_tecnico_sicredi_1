from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from src.managers.web_driver_controller import WebDriverController


class WebDriverBaseActions(WebDriverController):
    """
    Classe base para ações com o WebDriver,
    estendendo WebDriverController.
    """

    def __init__(self):
        """
        Inicializa a classe e configura o driver e o WebDriverWait.

        O tempo de espera padrão para as operações é definido como
        60 segundos.
        """
        super().__init__()
        self.driver = self.get_driver()
        self.wdw = WebDriverWait(self.driver, 20)
        self.ac = ActionChains(self.driver)


    def _click(self, selector: tuple):
        """
        Clica em um elemento especificado pelo seletor.

        Args:
            selector (tuple): Tupla contendo o método de seleção
            (por exemplo, By.ID) e o valor do seletor.
        """
        self.wdw.until(
            ec.element_to_be_clickable((selector.by, selector.value))
        )
        self.driver.find_element(selector.by, selector.value).click()
        


    def _find_element_in_page(self, selector: tuple) -> WebElement|None:
        """
        Procura por um elemento na página.

        Args:
            selector (tuple): Localizador do elemento.

        Returns:
            WebElement: Retorna o elemento web encontrado. None caso
            não encontrar.
        """
        try:
            self.wdw.until(
                ec.presence_of_element_located((selector.by, selector.value))
            )
            return self.driver.find_element(selector.by, selector.value)
        except:
            return None
    

    def _move_mouse_to_hover_element(self, selector: tuple):
        """
        Move o mouse para um elemento especificado pelo seletor,
        permitindo que ações de hover sejam realizadas.

        Args:
            selector (tuple): Tupla contendo o método de seleção
            (por exemplo, By.ID) e o valor do seletor.
        """
        self.wdw.until(
            ec.element_to_be_clickable((selector.by, selector.value))
        )
        element = self.driver.find_element(selector.by, selector.value)
        self.ac.move_to_element(element).perform()


    def _type_input(self, selector: tuple, input_data: str):
        """
        Digita dados em um campo de entrada especificado pelo seletor.

        Args:
            selector: Localizador do elemento de entrada.
            input_data (str): Dados a serem inseridos no campo de entrada.
        """
        self.wdw.until(
            ec.element_to_be_clickable((selector.by, selector.value))
        )
        self.driver.find_element(selector.by, selector.value).clear()
        self.driver.find_element(selector.by, selector.value).send_keys(
            input_data
        )


    def _get_text(self, selector: tuple) -> str:
        """
        Obtém o texto de um elemento especificado pelo seletor.

        Args:
            selector (tuple): Tupla contendo o método de seleção
            (por exemplo, By.ID) e o valor do seletor.

        Returns:
            str: O texto contido no WebElement encontrado.
        """
        self.wdw.until(
            ec.visibility_of_element_located((
                selector.by, selector.value
            ))
        )
        element = self.driver.find_element(selector.by, selector.value)
        return element.text
        