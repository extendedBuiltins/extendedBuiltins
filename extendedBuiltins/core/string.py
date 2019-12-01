import math


class string(str):
    def __init__(self, eb_string):
        super().__init__()
        self.text = str(eb_string)

    def upper(self, to_upper=None):
        """
            Returns
                -------
                out : `eb.string`
                    TODO: add better documentation
            Examples
                --------
                Upper all letters:

                >>> s = eb.string("Hello World")
                >>> s.upper()
                'HELLO WORLD'

                Upper nth letter:

                >>> s = eb.string("Hello World")
                >>> s.upper(8)
                'Hello WoRld'

                Upper one specific letters:

                >>> s = eb.string("Hello World")
                >>> s.upper("o")
                'HellO WOrld'
                >>> s.upper("l")
                'HeLLo WorLd'

                Upper multiple specific letters:

                >>> s = eb.string("Hello World")
                >>> s.upper(["l", "o"])
                'HeLLO WOrLd'
                >>> s.upper(["l", "o", "d"])
                'HeLLO WOrLD'
                """
        if to_upper is None:
            return string(str(self.text).upper())

        if isinstance(to_upper, int):
            if len(self.text) <= to_upper:
                raise IndexError('string index out of range')
            else:
                return string(
                    self.text[:to_upper]
                    + str(self.text[to_upper]).upper()
                    + self.text[to_upper + 1:]
                )

        if isinstance(to_upper, str):
            return string(self.text.replace(to_upper, str(to_upper).upper()))

        if isinstance(to_upper, tuple) \
                or isinstance(to_upper, set) \
                or isinstance(to_upper, list):
            transformed_text = self.text
            for letter in to_upper:
                if isinstance(letter, str):
                    transformed_text = transformed_text\
                        .replace(letter, str(letter).upper())
                else:
                    raise TypeError('expected string of length 1,'
                                    ' but int found')
            return string(transformed_text)

        else:
            raise TypeError('upper() argument 1 must be %s, not %s'
                            % (
                                'int, str, list, tuple or set',
                                type(to_upper).__name__,
                            ))

    def capitalize(self, index=None):
        """
            Returns
                -------
                out : `eb.string`
                    TODO: add better documentation
            Examples
                --------
                Capitalize first letter:

                >>> s = eb.string("hello World")
                >>> s.capitalize()
                'Hello world'

                Capitalize nth letter:

                >>> s = eb.string("Hello World")
                >>> s.capitalize(8)
                'hello woRld'
                """
        if index is None:
            return string(self.text[0].upper() + self.text[1:].lower())

        if isinstance(index, int):
            if len(self.text) <= index:
                raise IndexError('string index out of range')
            else:
                return string(
                    self.text[:index].lower()
                    + self.text[index].upper()
                    + self.text[index+1:].lower()
                )

        else:
            raise TypeError('capitalize() argument 1 must be int or None,'
                            ' not %s' % (type(index).__name__, ))

    def __sub__(self, other):
        """
        Returns
            -------
            out : `eb.string`
                TODO: add better documentation
        Examples
            --------
            Subtract a positive integer to the string:

            >>> s = eb.string("Hello World")
            >>> s - 4
            'Hello W'

            Subtract a negative integer to the string:

            >>> s = eb.string("Hello World")
            >>> s - -4
            'o World'

            Subtract a `list` or `tuple` to the string:

            >>> s = eb.string("Hello World")
            >>> s - ["H", "o", "d"]
            'ell Wrl'
            >>> s - ["H", "orl"]
            'ello Wd'

            Subtract a `str` or `eb.string` to the string:

            >>> s = eb.string("Hello World")
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

    def __floordiv__(self, other):
        """
        Returns
            -------
            out : list
                TODO: add better documentation
        Examples
            --------
            Divide the string by an integer:

            >>> s = eb.string("Hello World")
            >>> s // 3
            ['Hell', 'o Wo', 'rld']
            >>> s // 4
            ['Hel', 'lo ', 'Wor', 'ld']
            >>> s // 5
            ['Hel', 'lo ', 'Wor', 'ld', None]
            >>> s // 6
            ['He', 'll', 'o ', 'Wo', 'rl', 'd']
            >>> s // 10
            ['He', 'll', 'o ', 'Wo', 'rl', 'd', None, None, None, None]
            >>> s // 11
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

    def __truediv__(self, other):
        """
        Returns
            -------
            out : list
                TODO: add better documentation
        Examples
            --------
            Divide the string by an integer:

            >>> s = eb.string("Hello World")
            >>> s / 1
            ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
            >>> s / 2
            ['He', 'll', 'o ', 'Wo', 'rl', 'd']
            >>> s / 3
            ['Hel', 'lo ', 'Wor', 'ld']
            >>> s / 4
            ['Hell', 'o Wo', 'rld']
            >>> s / 5
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
