from ansu_fati.transformers import LineTransformer


def test_transformer_line_multiple_of_five():
    assert LineTransformer.transformer_0_multiple_of_five(5, "") == (LineTransformer.DATA_MULTIPLE_OF_FIVE, True)
    assert LineTransformer.transformer_0_multiple_of_five(6, "") == LineTransformer.DEFAULT_DATA


def test_transformer_contains_dollar_character():
    assert LineTransformer.transformer_1_contains_dollar_character(42, "with space $") == ("with_space_$", True)
    assert LineTransformer.transformer_1_contains_dollar_character(42, "no_space") == LineTransformer.DEFAULT_DATA


def test_transformer_ends_with_dot():
    assert LineTransformer.transformer_2_ends_with_dot(42, "ends with dot.") == ("ends with dot.", True)
    assert LineTransformer.transformer_2_ends_with_dot(42, "with dot and trailing spaces.\r\n") == (
        "with dot and trailing spaces.\r\n", True)
    assert LineTransformer.transformer_2_ends_with_dot(42, "no dot") == LineTransformer.DEFAULT_DATA


def test_transformer_is_json():
    assert LineTransformer.transformer_3_is_json(2, '{}') == ('{"pair": true}', True)
    assert LineTransformer.transformer_3_is_json(3, '{}') == ('{"pair": false}', True)
    assert LineTransformer.transformer_3_is_json(3, '{"with_key": "and_value"}') == (
        '{"with_key": "and_value", "pair": false}', True)
    assert LineTransformer.transformer_3_is_json(3, "") == LineTransformer.DEFAULT_DATA
