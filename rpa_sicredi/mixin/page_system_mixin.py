from abc import abstractmethod

from rpa_sicredi.mixin.page_element_mixin import PageElementMixIn


class PageSystemMixin(PageElementMixIn):
    """
    Abstract mixin for administrator page automation.

    This interface defines the contract for automating login,
    form filling, and logout actions on the admin page.
    """

    @abstractmethod
    def login(self, username: str, password: str):
        """
        Perform login using provided credentials.

        Args:
            username: User login name.
            password: User password.
        """
        ...

    @abstractmethod
    def extract_data(self):
        """
        Fill out form using provided data and services.
        """
        ...

    @abstractmethod
    def logout(self):
        """
        Perform user logout from the system.
        """
        ...

    def go_to_homepage(self):
        """
        Redirect to system homepage. Override if needed.
        """
        ...
