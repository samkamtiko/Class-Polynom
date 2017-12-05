class Polynome(object):
    def __init__(self, coefficient, exponent=0):
        if exponent < 0:
            raise Exception('Exponent can not be negative: ' + str(exponent))

        self.__degree = exponent
        self.__coeffs = [0] * (exponent + 1)
        self.__coeffs[exponent] = coefficient
        self.__reduce()

    def __reduce(self):
        self.__degree = -1
        for i in range(len(self.__coeffs) - 1, -1, -1):
            if self.__coeffs[i] != 0:
                self.__degree = i
                return

    @property
    def degree(self):
        return self.__degree

    def __add__(self, other):
        if isinstance(other, Polynome):
            p = Polynome(0, max(self.degree, other.degree))
            for i in range(0, self.degree + 1):
                p.__coeffs[i] += self.__coeffs[i]
            for i in range(0, other.degree + 1):
                p.__coeffs[i] += other.__coeffs[i]
            p.__reduce()
            return p
        elif isinstance(other, int) or isinstance(other, float):
            p = Polynome(0, max(self.degree, 0))
            for i in range(0, self.degree + 1):
                p.__coeffs[i] += self.__coeffs[i]
            p.__coeffs[0] += other
            p.__reduce()
            return p
        else:
            raise NotImplementedError

    def __sub__(self, other):
        if isinstance(other, Polynome):
            p = Polynome(0, max(self.degree, other.degree))
            for i in range(0, self.degree + 1):
                p.__coeffs[i] += self.__coeffs[i]
            for i in range(0, other.degree + 1):
                p.__coeffs[i] -= other.__coeffs[i]
            p.__reduce()
            return p
        elif isinstance(other, int) or isinstance(other, float):
            p = Polynome(0, max(self.degree, 0))
            for i in range(0, self.degree + 1):
                p.__coeffs[i] += self.__coeffs[i]
            p.__coeffs[0] -= other
            p.__reduce()
            return p
        else:
            raise NotImplementedError

    def __mul__(self, other):
        if isinstance(other, Polynome):
            p = Polynome(0, self.degree + other.degree)
            for i in range(0, self.degree + 1):
                for j in range(0, other.degree + 1):
                    p.__coeffs[i + j] += self.__coeffs[i] * other.__coeffs[j]
            p.__reduce()
            return p
        elif isinstance(other, int) or isinstance(other, float):
            p = Polynome(0, self.degree)
            for i in range(0, self.degree + 1):
                p.__coeffs[i] += self.__coeffs[i] * other
            p.__reduce()
            return p
        else:
            raise NotImplementedError

    def __call__(self, other):
        if isinstance(other, Polynome):
            p = Polynome(0, 0)
            for i in range(self.degree, -1, -1):
                term = Polynome(self.__coeffs[i], 0)
                p = term + other * p
            p.__reduce()
            return p
        elif isinstance(other, int) or isinstance(other, float):
            result = 0
            for i in range(self.degree, -1, -1):
                result += pow(other, i) * self.__coeffs[i]
            return result
        else:
            raise NotImplementedError

    def __eq__(self, other):
        if not isinstance(other, Polynome) and not isinstance(other, int) and not isinstance(other, float):
            raise NotImplementedError

        if isinstance(other, int) or isinstance(other, float):
            tmp = Polynome(other)
        else:
            tmp = other

        if self.__compare(tmp) == 0:
            return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Polynome) and not isinstance(other, int) and not isinstance(other, float):
            raise NotImplementedError

        if isinstance(other, int) or isinstance(other, float):
            tmp = Polynome(other)
        else:
            tmp = other

        if self.__compare(tmp) == -1:
            return True
        return False

    def __gt__(self, other):
        return not self.__lt__(other)

    def __compare(self, other):
        if self.degree < other.degree:
            return -1
        if self.degree > other.degree:
            return 1
        for i in range(self.degree, -1, -1):
            if self.__coeffs[i] < other.__coeffs[i]:
                return -1
        return 0

    def __str__(self):
        if self.degree == -1:
            return '0'
        elif self.degree == 0:
            return str(self.__coeffs[0])
        elif self.degree == 1:
            s = str()
            if self.__coeffs[1] != 1:
                s = str(self.__coeffs[1])
            s = s + 'x'
            if self.__coeffs[0] > 0:
                s = s + ' + ' + str(self.__coeffs[0])
            elif self.__coeffs[0] < 0:
                s = s + ' - ' + str(-self.__coeffs[0])
            return s

        s = str(self.__coeffs[self.degree]) + 'x^' + str(self.degree)
        for i in range(self.degree - 1, -1, -1):
            if self.__coeffs[i] == 0:
                continue
            elif self.__coeffs[i] == 1:
                s = s + ' + '
            elif self.__coeffs[i] > 0:
                s = s + ' + ' + str(self.__coeffs[i])
            elif self.__coeffs[i] < 0:
                s = s + ' - ' + str(-self.__coeffs[i])
            if i == 1:
                s = s + 'x'
            elif i > 1:
                s = s + 'x^' + str(i)
        return s
