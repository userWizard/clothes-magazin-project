from dataclasses import dataclass

from core.apps.common.exceptions import ServiceException

@dataclass(eq=False, init=False)
class ValidateException(ServiceException):
    @property
    def message(self):
        return 'Validation error'