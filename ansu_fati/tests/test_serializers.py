from ansu_fati.serializers import LineSerializer


def test_serializer_line_transformer_function_names():
    transformer_function_names = LineSerializer.get_transformer_function_names()
    assert len(transformer_function_names) > 0
    for transformer_method_name in transformer_function_names:
        assert transformer_method_name.startswith(LineSerializer.START_TRANSFORMER_METHOD_NAME)


def test_serializer_line_number():
    line_serializer = LineSerializer(42, "")
    assert line_serializer.line_number == 42


def test_serializer_line_data():
    line_serializer = LineSerializer(42, "")
    assert line_serializer.data == line_serializer.DEFAULT_DATA


def test_serializer_order_of_transformers_execution():
    line_serializer = LineSerializer(5, "{$.")
    assert line_serializer.data == line_serializer.DATA_MULTIPLE_OF_FIVE


def test_serializer_line_str():
    line_serializer = LineSerializer(None, None)
    assert str(line_serializer) == f"{LineSerializer.DEFAULT_NUMBER} : {LineSerializer.DEFAULT_DATA}"
    line_serializer = LineSerializer(12, ".")
    assert str(line_serializer) == f"12 : ."
