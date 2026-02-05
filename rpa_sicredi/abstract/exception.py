class GroupNotFoundException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class QuotaNotFound(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class LoginInvalidException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class ProductTypeNotFound(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class LoginError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class GenerateInformationError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class PurchaseOfQuotaRefused(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class QuotaUnderAnalysis(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class MissingDataError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class AllQuotasWereNotFound(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class NoCompaingsFound(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class SimulatorError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
