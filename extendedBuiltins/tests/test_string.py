import extendedBuiltins as eb


class TestStringClass:
    def test_sub_pos_int(self):
        s = eb.string("Hello World")
        assert s - 4 == 'Hello W'

    def test_sub_neg_int(self):
        s = eb.string("Hello World")
        assert s - -4 == 'o World'

    def test_sub_list(self):
        s = eb.string("Hello World")
        assert s - ["H", "o", "d"] == 'ell Wrl'
        assert s - ["H", "orl"] == 'ello Wd'

    def test_sub_str(self):
        s = eb.string("Hello World")
        assert s - "Hello" == ' World'
        assert s - " " == 'HelloWorld'
