import extendedBuiltins as eb


class TestStringClass:
    """
    Functions:
    """
    def test_upper(self):
        s = eb.string("Hello World")
        assert s.upper() == 'HELLO WORLD'

    def test_upper_nth_letter(self):
        s = eb.string("Hello World")
        assert s.upper(8) == 'Hello WoRld'

    def test_upper_one_specific_letter(self):
        s = eb.string("Hello World")
        assert s.upper("o") == 'HellO WOrld'
        assert s.upper("l") == 'HeLLo WorLd'

    def test_upper_multiple_specific_letter(self):
        s = eb.string("Hello World")
        assert s.upper(["l", "o"]) == 'HeLLO WOrLd'
        assert s.upper(["l", "o", "d"]) == 'HeLLO WOrLD'

    def test_capitalize(self):
        s = eb.string("hello World")
        assert s.capitalize() == 'Hello world'

    def test_capitalize_nth_letter(self):
        s = eb.string("Hello World")
        assert s.capitalize(8) == 'hello woRld'

    """
    Operations:
    """
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

    def test_div_floor(self):
        s = eb.string("Hello World")
        assert s // 3 == ['Hell', 'o Wo', 'rld']
        assert s // 4 == ['Hel', 'lo ', 'Wor', 'ld']
        assert s // 5 == ['Hel', 'lo ', 'Wor', 'ld', None]
        assert s // 6 == ['He', 'll', 'o ', 'Wo', 'rl', 'd']
        assert s // 10 == ['He', 'll', 'o ', 'Wo', 'rl', 'd', None, None, None, None]
        assert s // 11 == ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

    def test_div_true(self):
        s = eb.string("Hello World")
        assert s / 1 == ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
        assert s / 2 == ['He', 'll', 'o ', 'Wo', 'rl', 'd']
        assert s / 3 == ['Hel', 'lo ', 'Wor', 'ld']
        assert s / 4 == ['Hell', 'o Wo', 'rld']
        assert s / 5 == ['Hello', ' Worl', 'd']
