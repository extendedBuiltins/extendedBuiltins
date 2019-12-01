from collections.abc import Iterable


class array(list):
    def __init__(self, eb_list):
        super().__init__(eb_list)
        self.array = list(eb_list)

    def __sub__(self, other):
        """
            Returns
                -------
                out : `eb.string`
                    TODO: add better documentation
            Examples
                --------
                Subtract a positive integer to the array:

                >>> a = eb.array([5, 9, 2, eb.string("Hello World")])
                >>> a - 4
                [1, 5, -2, 'Hello W']

                Subtract a negative integer to the array:

                >>> a = eb.array([5, 9, 2, eb.string("Hello World")])
                >>> a - 4
                [9, 13, 6, 'o World']

                Subtract a `list` or `tuple` to the string:

                >>> a = eb.array([5, 9, 2, eb.string("Hello World")])
                >>> a - [5, 2, 'Hello World']
                [9]
                """
        if isinstance(other, int) or isinstance(other, float):
            output = []
            for el in self.array:
                output.append(el - other)
            return array(output)
        elif isinstance(other, list) or isinstance(other, tuple):
            output = []
            for el in self.array:
                if el not in other:
                    output.append(el)
            return array(output)

    def __floordiv__(self, other):
        """
            Returns
                -------
                out : eb.array
                    TODO: add better documentation
            Examples
                --------
                Divide the array by an integer:

                >>> a = eb.array([5, 9, 2, eb.string("Hello World")])
                >>> a // 2
                [2, 4, 1, ['Hello ', 'World']]
                """
        if isinstance(other, int):
            output = []
            for el in self.array:
                output.append(el // other)
            return array(output)

    def __truediv__(self, other):
        """
            Returns
                -------
                out : eb.array
                    TODO: add better documentation
            Examples
                --------
                Divide the array by an integer:

                >>> a = eb.array([5, 9, 2, eb.string("Hello World")])
                >>> a / 2
                [2.5, 4.5, 1.0, ['He', 'll', 'o ', 'Wo', 'rl', 'd']]
                """
        if isinstance(other, int):
            output = []
            for el in self.array:
                output.append(el / other)
            return array(output)

    def __add__(self, other):
        """
        Returns
            -------
            out : eb.array
                TODO: add better documentation
        Examples
            --------
            Sum the array by an `int` or a `float`:

            >>> a = eb.array([5, 9, 2])
            >>> a + 5
            [10, 14, 7]
            >>> a + -10
            [-5, -1, -8]
            >>> a + 3.7
            [8.7, 12.7, 5.7]

            Sum the array by a `list` or `tuple`:

            >>> a = eb.array([5, 9, 2, "Hello World", "hi"])
            >>> a - [5, 2, 'hi']
            [9, 'Hello World']

            """
        if isinstance(other, int) or isinstance(other, float):
            output = []
            for el in self.array:
                output.append(el + other)
            return array(output)
        elif isinstance(other, list) or isinstance(other, tuple):
            output = self.array.copy()
            for el in other:
                output.append(el)
            return array(output)
