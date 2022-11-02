from cipher_sc5119 import cipher_sc5119

def test_cipher():
    example = "quantitative"
    shift = 1
    expected = "rvboujubujwf"
    actual = cipher_sc5119.cipher(example, shift)
    assert actual == expected, "should be rvboujubujwf"