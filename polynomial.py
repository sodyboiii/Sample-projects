class Polynomial:
    def __init__(self, *args):
        if isinstance(args[0], list):
            self.coeffs = args[0]
        elif isinstance(args[0], dict):
            self.coeffs = [args[0][po] if po in args[0] else 0
                           for po in range(max(args[0].keys()) + 1)]
        elif isinstance(args[0], Polynomial):
            self.coeffs = args[0].coeffs[:]
        else:
            self.coeffs = [*args]
        while len(self.coeffs) > 1 and not self.coeffs[-1]:
            self.coeffs.pop()

    def __repr__(self):
        return "Polynomial " + str(self.coeffs)

    def __str__(self):
        ans = ""
        for i in range(1, len(self.coeffs) + 1):
            if self.coeffs[-i] > 0:
                ans += " + "
            elif self.coeffs[-i] < 0:
                ans += " - "
            elif not self.coeffs[-i]:
                continue
            if len(self.coeffs) - i == 0 or abs(self.coeffs[-i]) != 1:
                ans += str(abs(self.coeffs[-i]))
            if len(self.coeffs) - i > 0:
                ans += "x"
            if len(self.coeffs) - i - 1 > 0:
                ans += "^" + str(len(self.coeffs) - i)
        if ans[1] == "+":
            ans = ans[3:]
        elif ans[1] == "-":
            ans = "-" + ans[3:]
        return ans

    def __eq__(self, other):
        other = Polynomial(other)
        return self.coeffs == other.coeffs

    def __add__(self, other):
        other = Polynomial(other)
        su = [self.coeffs[i] + other.coeffs[i]
        for i in range(min(len(self.coeffs), len(other.coeffs)))]
        su += self.coeffs[min(len(self.coeffs), len(other.coeffs)):]
        su += other.coeffs[min(len(self.coeffs), len(other.coeffs)):]
        return Polynomial(su)

    def __radd__(self, other):
        return self + other

    def __neg__(self):
        return self * (-1)

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return -(self - other)

    def __call__(self, x):
        return sum(self.coeffs[i] * x ** i for i in range(len(self.coeffs)))

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            ans = [0 for i in range((len(self.coeffs)) *
                                    (len(other.coeffs) - 1) + 1)]
            for i in range(len(self.coeffs)):
                for j in range(len(other.coeffs)):
                    ans[i + j] += other.coeffs[j] * self.coeffs[i]
        else:
            ans = [x * other for x in self.coeffs]
        return Polynomial(ans)

    def __rmul__(self, other):
        return self * other

    def __iter__(self):
        ans = [(x, y) for x, y in enumerate(self.coeffs)]
        return iter(ans)

    def __next__(self):
        return next(self)

    def degree(self):
        return len(self.coeffs) - 1

    def der(self, d=1):
        if d > self.degree():
            return Polynomial(0)
        ans = Polynomial(self)
        for t in range(d):
            for i in range(len(ans.coeffs)):
                ans.coeffs[i] *= i
            ans.coeffs = ans.coeffs[1:]
        if not len(ans.coeffs):
            return Polynomial(0)
        return ans


class NotOddDegreeException(Exception):
    def __init__(self):
        pass


class RealPolynomial(Polynomial):
    def __init__(self, *args):
        super().__init__(*args)
        if not self.degree() % 2:
            raise NotOddDegreeException

    def find_root(self):
        l = -1e5
        r = 1e5
        zl = self(l)
        zr = self(r)
        if not zl:
            return l
        if not zr:
            return r
        while abs(zl - zr) > 1e-5:
            mi = (l + r) / 2
            zm = self(mi)
            if not zm:
                return mi
            if not zl:
                return l
            if not zr:
                return r
            if (zl < 0 and zm > 0) or (zl > 0 and zm < 0):
                r = mi
            elif (zr < 0 and zm > 0) or (zr > 0 and zm < 0):
                l = mi
            zl = self(l)
            zr = self(r)
        return (l + r) / 2


class DegreeIsTooBigException(Exception):
    def __init__(self):
        pass


class QuadraticPolynomial(Polynomial):

    def __init__(self, *args):
        super().__init__(*args)
        if len(self.coeffs) > 3:
            raise DegreeIsTooBigException

    def solve(self):
        ans = []
        if len(self.coeffs) == 3:
            di = self.coeffs[1] ** 2 - (4 * self.coeffs[2] * self.coeffs[0])
            if di > 0:
                ans1 = (-self.coeffs[1] + di ** 0.5) / (2 * self.coeffs[2])
                ans2 = (-self.coeffs[1] - di ** 0.5) / (2 * self.coeffs[2])
                ans = [ans1, ans2]
            elif not di:
                ans = [-self.coeffs[1] / (2 * self.coeffs[2])]
            else:
                return []
        elif len(self.coeffs) == 2:
            ans = [-self.coeffs[0] / self.coeffs[1]]
        return ans
