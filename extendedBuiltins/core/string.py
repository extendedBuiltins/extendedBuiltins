import math


class string(str):
    def __init__(self, eb_string):
        super().__init__()
        self.text = str(eb_string)

    def __sub__(self, other):
        """
        Returns
            -------
            out : `eb.string`
                TODO: add better documentation
        Examples
            --------
            Subtract a positive integer to the string:

            >>> s = string("Hello World")
            >>> s - 4
            'Hello W'

            Subtract a negative integer to the string:

            >>> s = string("Hello World")
            >>> s - -4
            'o World'

            Subtract a `list` or `tuple` to the string:

            >>> s = string("Hello World")
            >>> s - ["H", "o", "d"]
            'ell Wrl'
            >>> s - ["H", "orl"]
            'ello Wd'

            Subtract a `str` or `eb.string` to the string:

            >>> s = string("Hello World")
            >>> s - "Hello"
            ' World'
            >>> s - " "
            'HelloWorld'
            """
        if isinstance(other, int):
            if other > 0:
                return string(self.text[:-other])
            elif other < 0:
                return string(self.text[-other:])
            else:
                return string(self.text)

        elif isinstance(other, list) or isinstance(other, tuple):
            text = self.text
            for item in other:
                text = text.replace(item, '')
            return string(text)

        elif isinstance(other, str) or isinstance(other, string):
            return string(self.text.replace(other, ''))

    def __truediv__(self, other):
        """
        Returns
            -------
            out : list
                TODO: add better documentation
        Examples
            --------
            Divide the string by an integer:

            >>> s = string("Hello World")
            >>> s / 3
            ['Hell', 'o Wo', 'rld']
            >>> s / 4
            ['Hel', 'lo ', 'Wor', 'ld']
            >>> s / 5
            ['Hel', 'lo ', 'Wor', 'ld', None]
            >>> s / 6
            ['He', 'll', 'o ', 'Wo', 'rl', 'd']
            >>> s / 10
            ['He', 'll', 'o ', 'Wo', 'rl', 'd', None, None, None, None]
            >>> s / 11
            ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
            """
        if isinstance(other, int):
            sections = math.ceil(len(self.text) / other)

            result = [
                self.text[i:i + sections]
                for i in range(0, len(self.text), sections)
            ]

            return result + [None for _ in range(other - len(result))]
        else:
            raise TypeError("unsupported operand type(s) for /: '%s' and '%s'"
                            % (type(self).__name__, type(other).__name__))

    def __floordiv__(self, other):
        """
        Returns
            -------
            out : list
                TODO: add better documentation
        Examples
            --------
            Divide the string by an integer:

            >>> s = string("Hello World")
            >>> s // 1
            ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
            >>> s // 2
            ['He', 'll', 'o ', 'Wo', 'rl', 'd']
            >>> s // 3
            ['Hel', 'lo ', 'Wor', 'ld']
            >>> s // 4
            ['Hell', 'o Wo', 'rld']
            >>> s // 5
            ['Hello', ' Worl', 'd']
            """
        if isinstance(other, int):
            return [
                self.text[i:i + other]
                for i in range(0, len(self.text), other)
            ]
        else:
            raise TypeError("unsupported operand type(s) for //: '%s' and '%s'"
                            % (type(self).__name__, type(other).__name__))
