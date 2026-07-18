from abc import ABC, abstractmethod


class ValidationRule(ABC):

    @abstractmethod
    def validate(self, invoice, result):

        pass
