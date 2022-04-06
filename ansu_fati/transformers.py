import json
from .exceptions import JSONDecodeTransformerException, ZeroDivisionTransformerException


class LineTransformer:
    DATA_MULTIPLE_OF_FIVE = "Multiple de 5"
    DEFAULT_DATA = (None, False)

    @staticmethod
    def transformer_0_multiple_of_five(line_number: int, data: str):
        try:
            is_multiple_of_five = line_number % 5 == 0
        except ZeroDivisionError:
            raise ZeroDivisionTransformerException()
        if is_multiple_of_five:
            return LineTransformer.DATA_MULTIPLE_OF_FIVE, True
        return LineTransformer.DEFAULT_DATA

    @staticmethod
    def transformer_1_contains_dollar_character(line_number: int, data: str):
        if "$" in data:
            return data.replace(' ', '_'), True
        return LineTransformer.DEFAULT_DATA

    @staticmethod
    def transformer_2_ends_with_dot(line_number: int, data: str):
        data_with_no_trailing_spaces = data.rstrip()
        if data_with_no_trailing_spaces.endswith("."):
            return data, True
        return LineTransformer.DEFAULT_DATA

    @staticmethod
    def transformer_3_is_json(line_number: int, data: str):
        if data.startswith("{"):
            try:
                data_json = json.loads(data)
            except json.decoder.JSONDecodeError:
                raise JSONDecodeTransformerException()
            try:
                is_pair = line_number % 2 == 0
            except ZeroDivisionError:
                raise ZeroDivisionTransformerException()
            if is_pair:
                data_json['pair'] = True
            else:
                data_json['pair'] = False
            return json.dumps(data_json), True
        return LineTransformer.DEFAULT_DATA
