import inspect
from .transformers import LineTransformer
from .exceptions import TransformerException


class LineSerializer(LineTransformer):
    DEFAULT_DATA = "Rien à afficher"
    DEFAULT_NUMBER = -1
    START_TRANSFORMER_METHOD_NAME = 'transformer_'

    def __init__(self, line_number: int, line_data: str):
        self.line_number = line_number if isinstance(line_number, int) else LineSerializer.DEFAULT_NUMBER
        self.data = line_data

    def __str__(self):
        return f"{self.line_number} : {self.data.rstrip()}"

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: str):
        if data:
            transformer_function_names = self.get_transformer_function_names()
            for transformer_function_name in transformer_function_names:
                transformer_function = getattr(self, transformer_function_name)
                try:
                    new_data, is_transformed = transformer_function(self.line_number, data)
                    if is_transformed:
                        self.__data = new_data
                        return
                except TransformerException as error:
                    self.__data = str(error)
        self.__data = self.DEFAULT_DATA

    @staticmethod
    def get_transformer_function_names():
        functions = inspect.getmembers(LineSerializer, predicate=inspect.isfunction)
        return [function_name for function_name, _ in functions if
                function_name.startswith(LineSerializer.START_TRANSFORMER_METHOD_NAME)]
