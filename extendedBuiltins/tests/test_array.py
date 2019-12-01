import extendedBuiltins as eb


class TestArrayClass:
    """
    Operations:
    """
    def test_sub_pos_int(self):
        a = eb.array([5, 9, 2, eb.string("Hello World")])
        assert a - 4 == [1, 5, -2, 'Hello W']

    def test_sub_neg_int(self):
        a = eb.array([5, 9, 2, eb.string("Hello World")])
        assert a - -4 == [9, 13, 6, 'o World']

    def test_sub_list(self):
        a = eb.array([5, 9, 2, eb.string("Hello World")])
        assert a - [5, 2, 'Hello World'] == [9]

    def test_div_floor(self):
        a = eb.array([5, 9, 2, eb.string("Hello World")])
        assert a // 2 == [2, 4, 1, ['Hello ', 'World']]

    def test_div_true(self):
        a = eb.array([5, 9, 2, eb.string("Hello World")])
        assert a / 2 == [2.5, 4.5, 1.0, ['He', 'll', 'o ', 'Wo', 'rl', 'd']]
