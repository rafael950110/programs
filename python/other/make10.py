#!/bin/env python3.4
# -*- mode:python; coding:utf-8; -*-


"""
make10.py
@author hanepjiv <hanepjiv@gmail.com>
@since 2015/06/28
@date 2015/06/28
"""


# ##############################################################################
# The MIT License (MIT)
#
# Copyright (c) <2015> hanepjiv <hanepjiv@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


# ##############################################################################
# ==============================================================================
CURRENT         = 0
AGE             = 0
REVISION        = 1
# ==============================================================================
MAJOR           = CURRENT - AGE
VERSION         = '{}.{}.{}'.format(MAJOR, AGE, REVISION)

# ##############################################################################
# ==============================================================================
import  sys
import  types
import  unittest
from    itertools       import product, combinations
from    inspect         import currentframe, getframeinfo
from    copy            import deepcopy
from    enum            import IntEnum, unique
from    fractions       import Fraction
from    functools       import wraps

# ##############################################################################
# ==============================================================================
@unique
class Op(IntEnum):
    # --------------------------------------------------------------------------
    ADD  = 0
    SUB  = 1
    RSUB = 2
    MUL  = 3
    DIV  = 4
    RDIV = 5
    # --------------------------------------------------------------------------
    @property
    def swap(self):
        return  [  Op.ADD, Op.RSUB,  Op.SUB,  Op.MUL, Op.RDIV,  Op.DIV, ][self]
    # --------------------------------------------------------------------------
    @property
    def invert(self):
        return  [  Op.SUB,  Op.ADD,    None,  Op.DIV,  Op.MUL,    None, ][self]
    # --------------------------------------------------------------------------
    def func(self, x, y):
        """
        >>> Op.ADD.func(1,2)
        Fraction(3, 1)
        >>> Op.SUB.func(1,2)
        Fraction(-1, 1)
        >>> Op.RSUB.func(1,2)
        Fraction(1, 1)
        >>> Op.MUL.func(1,2)
        Fraction(2, 1)
        >>> Op.DIV.func(1,2)
        Fraction(1, 2)
        >>> Op.RDIV.func(1,2)
        Fraction(2, 1)
        """
        return  ([  Fraction.__add__,
                    Fraction.__sub__,
                    Fraction.__rsub__,
                    Fraction.__mul__,
                    Fraction._div,
                    lambda x, y: Fraction._div(y, x),
                ][self])(x, y)
    # -------------------------------------------------------------------------
    def fmt(self, x, y):
        return  [ '({0} + {1})', '({0} - {1})', '({1} - {0})',
                  '({0} × {1})', '({0} ÷ {1})', '({1} ÷ {0})',
        ][self].format(x, y)
    # --------------------------------------------------------------------------
    def expand_func(self, x, y):
        return  ([  Expand.__add__,
                    Expand.__sub__,
                    lambda x, y: Expand.__sub__(y, x),
                    Expand.__mul__,
                    Expand.__truediv__,
                    lambda x, y: Expand.__truediv__(y, x),
                ][self])(x, y)
# ==============================================================================
# ------------------------------------------------------------------------------
class Triple:
    # ==========================================================================
    # --------------------------------------------------------------------------
    def __init__(self, a_op, a_lhs, a_rhs):
        self.op  = a_op
        self.lhs = a_lhs
        self.rhs = a_rhs
    # ==========================================================================
    # --------------------------------------------------------------------------
    def __str__(self):
        return self.op.fmt(str(self.lhs), str(self.rhs))
    # --------------------------------------------------------------------------
    def __repr__(self):
        return ('{}({}, {}, {})'.format(type(self).__name__, repr(self.op),
                                        repr(self.lhs), repr(self.rhs)))
    # ==========================================================================
    # --------------------------------------------------------------------------
    def __hash__(self):
        return (hash(hash(type(self)) ^
                     hash(self.op) ^ hash(self.lhs) ^ hash(self.rhs)))
    # ==========================================================================
    # --------------------------------------------------------------------------
    def __lt__(self, a_rhs):
        return (str(self).__lt__(str(a_rhs)))
    # --------------------------------------------------------------------------
    def __gt__(self, a_rhs):
        return a_rhs.__lt__(self)
    # --------------------------------------------------------------------------
    def __le__(self, a_rhs):
        return (not self.__gt__(a_rhs))
    # --------------------------------------------------------------------------
    def __ge__(self, a_rhs):
        return (not self.__lt__(a_rhs))
    # --------------------------------------------------------------------------
    def __eq__(self, a_rhs):
        return (not self.__lt__(a_rhs)) and (not self.__gt__(a_rhs))
    # --------------------------------------------------------------------------
    def __ne__(self, a_rhs):
        return (not self.__eq__(a_rhs))
    # --------------------------------------------------------------------------
    @staticmethod
    def _m_eval_(value):
        return value.m_eval() if isinstance(value, Triple) else value
    # --------------------------------------------------------------------------
    def m_eval(self):
        return self.op.func(Triple._m_eval_(self.lhs),
                            Triple._m_eval_(self.rhs))
    # --------------------------------------------------------------------------
    @staticmethod
    def _rank_(value):
        return value.rank() if isinstance(value, Triple) else value
    # --------------------------------------------------------------------------
    def rank(self):
        return (10 + Triple._rank_(self.lhs) + Triple._rank_(self.rhs))
    # --------------------------------------------------------------------------
    def swap(self):
        tmp                 = self.lhs
        self.lhs            = self.rhs
        self.rhs            = tmp
    # --------------------------------------------------------------------------
    def left(self):
        if not isinstance(self.rhs, Triple):
            raise RuntimeError("{}.{}()".
                               format(self,
                                      getframeinfo(currentframe()).function))
        tmp                 = self.rhs
        self.rhs            = tmp.rhs
        tmp.rhs             = tmp.lhs
        tmp.lhs             = self.lhs
        self.lhs            = tmp
    # --------------------------------------------------------------------------
    def right(self):
        if not isinstance(self.lhs, Triple):
            raise RuntimeError("{}.{}()".
                               format(self,
                                      getframeinfo(currentframe()).function))
        tmp                 = self.lhs
        self.lhs            = tmp.lhs
        tmp.lhs             = tmp.rhs
        tmp.rhs             = self.rhs
        self.rhs            = tmp
    # --------------------------------------------------------------------------
    def optimize(self):
        while self._optimize_():
            pass
        return self
    # --------------------------------------------------------------------------
    def _optimize_(self):
        optimized  = False

        optimized |= isinstance(self.lhs, Triple) and self.lhs._optimize_()
        optimized |= isinstance(self.rhs, Triple) and self.rhs._optimize_()

        if ((self.op in [Op.RSUB, Op.RDIV])):
            self.swap()
            self.op              = self.op.swap
            optimized           |= True

        if ((self.op in [Op.SUB, Op.DIV])):
            if   (isinstance(self.rhs, Triple) and (self.op == self.rhs.op)):
                self.rhs.swap()
                self.op                  = self.op.invert
                optimized               |= True
            elif (isinstance(self.lhs, Triple) and (self.op == self.lhs.op)):
                self.right()
                self.rhs.op              = self.rhs.op.invert
                optimized               |= True

        #if ((self.op == Op.DIV) and
        #    (abs(int(Triple._m_eval_(self.rhs))) == 1)):
        #    self.op              = Op.MUL
        #    optimized           |= True

        if ((self.op in [Op.ADD, Op.MUL])):
            if   (isinstance(self.lhs, Triple) and (self.op == self.lhs.op)):
                self.right()
                optimized               |= True
            elif (isinstance(self.rhs, Triple) and (self.op == self.rhs.op) and
                  (Triple._rank_(self.lhs) > Triple._rank_(self.rhs.lhs))):
                tmp                      = self.lhs
                self.lhs                 = self.rhs.lhs
                self.rhs.lhs             = tmp
                optimized               |= True

        if ((self.op in [Op.ADD, Op.MUL]) and
            (Triple._rank_(self.lhs) > Triple._rank_(self.rhs))):
            self.swap()
            optimized           |= True

        return optimized
    # ==========================================================================
    # --------------------------------------------------------------------------
    @staticmethod
    def _expand_(value):
        if   isinstance(value, Triple):
            return value.expand()
        elif Fraction(value) != 0:
            return Expand([Fraction(value)])
        else:
            return Expand([])
    # --------------------------------------------------------------------------
    def expand(self):
        return self.op.expand_func(Triple._expand_(self.lhs),
                                   Triple._expand_(self.rhs))
    # ==========================================================================
    # --------------------------------------------------------------------------
    def hasZeroDiv(self):
        if   Op.DIV == self.op:
            if (not isinstance(self.rhs, Triple)) and 0 == self.rhs:
                return True
        elif Op.RDIV == self.op:
            if (not isinstance(self.lhs, Triple)) and 0 == self.lhs:
                return True

        ret = False
        if isinstance(self.lhs, Triple):
            ret |= self.lhs.hasZeroDiv()
        if isinstance(self.rhs, Triple):
            ret |= self.rhs.hasZeroDiv()
        return ret
# ==============================================================================
# ------------------------------------------------------------------------------
def _expand_exp_(a_func):
    @wraps(a_func)
    def wrapper(a_rhs, a_lhs):
        return list(map(lambda x: a_func(x[0], x[1]),
                        product(a_rhs, a_lhs)))
    return wrapper
# ------------------------------------------------------------------------------
class Expand:
    # ==========================================================================
    # --------------------------------------------------------------------------
    _VAL_VALID_TYPE_ = [
        list,
        tuple,
    ]
    # --------------------------------------------------------------------------
    @classmethod
    def validate(cls, a_val):
        for i in cls._VAL_VALID_TYPE_:
            if isinstance(a_val, i):
                return True
        return False
    # ==========================================================================
    # --------------------------------------------------------------------------
    def __init__(self, a_val, **kwds):
        if not Expand.validate(a_val):
            raise RuntimeError("{}.{}({}): invalid arguments".
                               format(type(self).__name__,
                                      getframeinfo(currentframe()).function,
                                      a_val))

        self.val = a_val

        self.__dict__.update(kwds)
    # ==========================================================================
    # --------------------------------------------------------------------------
    def optimize(self):
        if   isinstance(self.val, tuple):
            if self.val[1] == [1]:
                self.val = self.val[0]
        return self
    # ==========================================================================
    # --------------------------------------------------------------------------
    def __str__(self):
        return repr(self)
    # --------------------------------------------------------------------------
    def __repr__(self):
        return ('{}({})'.format(type(self).__name__, repr(self.val)))
    # --------------------------------------------------------------------------
    def __hash__(self):
        return (hash(type(self)) ^ hash(repr(self.val)))
    # ==========================================================================
    # --------------------------------------------------------------------------
    def __lt__(self, a_rhs):
        """
        >>> Expand([0]) < Expand([0])
        False
        >>> Expand([0]) < Expand([1])
        True
        >>> Expand([1]) < Expand([0])
        False
        """
        if   isinstance(self.val, list):
            if   isinstance(a_rhs.val, list):
                return (self.val < a_rhs.val)
            elif isinstance(a_rhs.val, tuple):
                return True
        elif isinstance(self.val, tuple):
            if   isinstance(a_rhs.val, list):
                return False
            elif isinstance(a_rhs.val, tuple):
                return (self.val < a_rhs.val)
    # --------------------------------------------------------------------------
    def __gt__(self, a_rhs):
        """
        >>> Expand([0]) > Expand([0])
        False
        >>> Expand([0]) > Expand([1])
        False
        >>> Expand([1]) > Expand([0])
        True
        """
        return a_rhs.__lt__(self)
    # --------------------------------------------------------------------------
    def __le__(self, a_rhs):
        """
        >>> Expand([0]) <= Expand([0])
        True
        >>> Expand([0]) <= Expand([1])
        True
        >>> Expand([1]) <= Expand([0])
        False
        """
        return (not self.__gt__(a_rhs))
    # --------------------------------------------------------------------------
    def __ge__(self, a_rhs):
        """
        >>> Expand([0]) >= Expand([0])
        True
        >>> Expand([0]) >= Expand([1])
        False
        >>> Expand([1]) >= Expand([0])
        True
        """
        return (not self.__lt__(a_rhs))
    # --------------------------------------------------------------------------
    def __eq__(self, a_rhs):
        """
        >>> Expand([0]) == Expand([0])
        True
        >>> Expand([0]) == Expand([1])
        False
        """
        return (not self.__lt__(a_rhs)) and (not self.__gt__(a_rhs))
    # --------------------------------------------------------------------------
    def __ne__(self, a_rhs):
        """
        >>> Expand([0]) != Expand([0])
        False
        >>> Expand([0]) != Expand([1])
        True
        """
        return (not self.__eq__(a_rhs))
    # --------------------------------------------------------------------------
    @_expand_exp_
    def _exp_mul_(a_rhs, a_lhs):
        """
        >>> Expand._exp_mul_([0, 1], [1, 2])
        [0, 0, 1, 2]
        """
        return a_rhs * a_lhs
    # --------------------------------------------------------------------------
    @_expand_exp_
    def _exp_div_(a_rhs, a_lhs):
        """
        >>> Expand._exp_div_([4, 2], [2, 1])
        [2.0, 4.0, 1.0, 2.0]
        """
        return a_rhs / a_lhs
    # ==========================================================================
    # --------------------------------------------------------------------------
    def __add__(self, a_rhs):
        return (self).__iadd__(a_rhs)
    # --------------------------------------------------------------------------
    def __iadd__(self, a_rhs):
        sv = self.val
        rv = a_rhs.val

        if   isinstance(sv, list):
            if   isinstance(rv, list):
                self.val += rv
                self.val.sort()
                return self.optimize()
            elif isinstance(rv, tuple):
                self.val  = (sorted(Expand._exp_mul_(sv, rv[1]) + rv[0]), rv[1])
                return self.optimize()
        elif isinstance(sv, tuple):
            if   isinstance(rv, list):
                self.val  = (sorted(Expand._exp_mul_(sv[1], rv) + sv[0]), sv[1])
                return self.optimize()
            elif isinstance(rv, tuple):
                if sv[1] == rv[1]:
                    self.val  = (sv[0] + rv[0], sv[1])
                    return self.optimize()
                else:
                    self.val  = (sorted(Expand._exp_mul_(sv[0], rv[1]) +
                                        Expand._exp_mul_(sv[1], rv[0])),
                                 sorted(Expand._exp_mul_(sv[1], rv[1])))
                    return self.optimize()

        raise RuntimeError("{}.{}({})".
                           format(self, getframeinfo(currentframe()).function,
                                  a_rhs))
    # ==========================================================================
    # --------------------------------------------------------------------------
    def __sub__(self, a_rhs):
        return deepcopy(self).__isub__(a_rhs)
    # --------------------------------------------------------------------------
    def __isub__(self, a_rhs):
        sv = self.val
        rv = a_rhs.val

        if   isinstance(sv, list):
            if   isinstance(rv, list):
                self.val += list(map(lambda x: -x, rv))
                self.val.sort()
                return self.optimize()
            elif isinstance(rv, tuple):
                self.val  = (sorted(Expand._exp_mul_(sv, rv[1]) +
                                    list(map(lambda x: -x, rv[0]))),
                            rv[1])
                return self.optimize()
        elif isinstance(sv, tuple):
            if   isinstance(rv, list):
                self.val  = (sorted(list(map(lambda x: x[0] * -x[1],
                                            product(sv[1], rv))) +
                                   sv[0]),
                            sv[1])
                return self.optimize()
            elif isinstance(rv, tuple):
                if sv[1] == rv[1]:
                    self.val  = (sv[0] + list(map(lambda x: -x, rv[0])), sv[1])
                    return self.optimize()
                else:
                    self.val  = (sorted(Expand._exp_mul_(sv[0], rv[1]) +
                                        list(map(lambda x: x[0] * -x[1],
                                                 product(sv[1], rv[0])))),
                                 sorted(Expand._exp_mul_(sv[1], rv[1])))
                    return self.optimize()

        raise RuntimeError("{}.{}({})".
                           format(self, getframeinfo(currentframe()).function,
                                  a_rhs))
    # ==========================================================================
    # --------------------------------------------------------------------------
    def __mul__(self, a_rhs):
        return deepcopy(self).__imul__(a_rhs)
    # --------------------------------------------------------------------------
    def __imul__(self, a_rhs):
        sv = self.val
        rv = a_rhs.val

        if   isinstance(sv, list):
            if   isinstance(rv, list):
                self.val  = Expand._exp_mul_(sv, rv)
                self.val.sort()
                return self.optimize()
            elif isinstance(rv, tuple):
                self.val  = (sorted(Expand._exp_mul_(sv, rv[0])), rv[1])
                return self.optimize()
        elif isinstance(sv, tuple):
            if   isinstance(rv, list):
                self.val  = (sorted(Expand._exp_mul_(sv[0], rv)), sv[1])
                return self.optimize()
            elif isinstance(rv, tuple):
                self.val  = (sorted(Expand._exp_mul_(sv[0], rv[0])),
                             sorted(Expand._exp_mul_(sv[1], rv[1])))
                return self.optimize()

        raise RuntimeError("{}.{}({})".
                           format(self, getframeinfo(currentframe()).function,
                                  a_rhs))
    # ==========================================================================
    # --------------------------------------------------------------------------
    def __truediv__(self, a_rhs):
        return deepcopy(self).__itruediv__(a_rhs)
    # --------------------------------------------------------------------------
    def __itruediv__(self, a_rhs):
        sv = self.val
        rv = a_rhs.val

        if   isinstance(sv, list):
            if   isinstance(rv, list):
                self.val  = (sv, rv)
                return self.optimize()
            elif isinstance(rv, tuple):
                self.val  = (sorted(Expand._exp_mul_(sv, rv[1])), rv[0])
                return self.optimize()
        elif isinstance(sv, tuple):
            if   isinstance(rv, list):
                self.val  = (sorted(Expand._exp_div_(sv[0], rv)), sv[1])
                return self.optimize()
            elif isinstance(rv, tuple):
                self.val  = (sorted(Expand._exp_mul_(sv[0], rv[1])),
                             sorted(Expand._exp_mul_(sv[1], rv[0])))
                return self.optimize()

        raise RuntimeError("{}.{}({})".
                           format(self, getframeinfo(currentframe()).function,
                                  a_rhs))
# ------------------------------------------------------------------------------
class ExpandTest(unittest.TestCase):
    # ==========================================================================
    def setUp(self):
        pass
    # ==========================================================================
    def tearDown(self):
        pass
    # ==========================================================================
    # --------------------------------------------------------------------------
    def test_iadd(self):
        self.assertEqual(Expand([Fraction(2)]).__iadd__(Expand([Fraction(1)])),
                         Expand([Fraction(1, 1), Fraction(2, 1)]))

        self.assertEqual(Expand([Fraction(1)]).
                         __iadd__(Expand(([Fraction(2)], [Fraction(3)]))),
                         Expand(([Fraction(2, 1), Fraction(3, 1)],
                                 [Fraction(3, 1)])))

        self.assertEqual(Expand(([Fraction(2)], [Fraction(3)])).
                         __iadd__(Expand([Fraction(1)])),
                         Expand(([Fraction(2, 1), Fraction(3, 1)],
                                 [Fraction(3, 1)])))

        self.assertEqual(Expand(([Fraction(2)], [Fraction(3)])).
                         __iadd__(Expand(([Fraction(4)], [Fraction(1)]))),
                         Expand(([Fraction(2, 1), Fraction(12, 1)],
                                 [Fraction(3, 1)])))
    # --------------------------------------------------------------------------
    def test_isub(self):
        self.assertEqual(Expand([Fraction(2)]).__isub__(Expand([Fraction(1)])),
                         Expand([Fraction(-1, 1), Fraction(2, 1)]))

        self.assertEqual(Expand([Fraction(1)]).
                         __isub__(Expand(([Fraction(2)], [Fraction(3)]))),
                         Expand(([Fraction(-2, 1), Fraction(3, 1)],
                                 [Fraction(3, 1)])))

        self.assertEqual(Expand(([Fraction(2)], [Fraction(3)])).
                         __isub__(Expand([Fraction(1)])),
                         Expand(([Fraction(-3, 1), Fraction(2, 1)],
                                 [Fraction(3, 1)])))

        self.assertEqual(Expand(([Fraction(2)], [Fraction(3)])).
                         __isub__(Expand(([Fraction(4)], [Fraction(1)]))),
                         Expand(([Fraction(-12, 1), Fraction(2, 1)],
                                 [Fraction(3, 1)])))
    # --------------------------------------------------------------------------
    def test_imul(self):
        self.assertEqual(Expand([Fraction(2)]).__imul__(Expand([Fraction(1)])),
                         Expand([Fraction(2, 1)]))

        self.assertEqual(Expand([Fraction(1)]).
                         __imul__(Expand(([Fraction(2)], [Fraction(3)]))),
                         Expand(([Fraction(2, 1)], [Fraction(3, 1)])))

        self.assertEqual(Expand(([Fraction(2)], [Fraction(3)])).
                         __imul__(Expand([Fraction(1)])),
                         Expand(([Fraction(2, 1)], [Fraction(3, 1)])))

        self.assertEqual(Expand(([Fraction(2)], [Fraction(3)])).
                         __imul__(Expand(([Fraction(4)], [Fraction(1)]))),
                         Expand(([Fraction(8, 1)], [Fraction(3, 1)])))
    # --------------------------------------------------------------------------
    def test_itruediv(self):
        self.assertEqual(Expand([Fraction(2)]).
                         __itruediv__(Expand([Fraction(3)])),
                         Expand(([Fraction(2, 1)], [Fraction(3, 1)])))

        self.assertEqual(Expand([Fraction(1)]).
                         __itruediv__(Expand(([Fraction(2)], [Fraction(3)]))),
                         Expand(([Fraction(3, 1)], [Fraction(2, 1)])))

        self.assertEqual(Expand(([Fraction(2)], [Fraction(3)])).
                         __itruediv__(Expand([Fraction(1)])),
                         Expand(([Fraction(2, 1)], [Fraction(3, 1)])))

        self.assertEqual(Expand(([Fraction(2)], [Fraction(3)])).
                         __itruediv__(Expand(([Fraction(4)], [Fraction(1)]))),
                         Expand(([Fraction(2, 1)], [Fraction(12, 1)])))
# ##############################################################################
# ==============================================================================
# ------------------------------------------------------------------------------
def make_M_4_TripleA(n0, n1, n2, n3, o0, o1, o2):
    return Triple(o2, Triple(o1, Triple(o0, n3, n2), n1), n0)
# ------------------------------------------------------------------------------
def make_M_4_TripleB(n0, n1, o0, n2, n3, o1, o2):
    return Triple(o2, Triple(o1, n3, n2), Triple(o0, n1, n0))
# ==============================================================================
# ------------------------------------------------------------------------------
g_PatternA = (
    (0, 1, 2, 3),
    (0, 2, 1, 3),
    (0, 3, 1, 2),
    (1, 0, 2, 3),
    (1, 2, 0, 3),
    (1, 3, 0, 2),
    (2, 0, 1, 3),
    (2, 1, 0, 3),
    (2, 3, 0, 1),
    (3, 0, 1, 2),
    (3, 1, 0, 2),
    (3, 2, 0, 1),
)
# ------------------------------------------------------------------------------
g_PatternB = (
    (0, 1, 2, 3),
    (0, 2, 1, 3),
    (0, 3, 1, 2),
)
# ==============================================================================
def make_M_4_Triple(n, o):
    # --------------------------------------------------------------------------
    for p in g_PatternA:
        ret = make_M_4_TripleA(n[p[0]], n[p[1]], n[p[2]], n[p[3]],
                          o[0], o[1], o[2])
        if not ret.hasZeroDiv():
            yield ret
    for p in g_PatternB:
        ret = make_M_4_TripleB(n[p[0]], n[p[1]], o[0], n[p[2]], n[p[3]],
                          o[1], o[2])
        if not ret.hasZeroDiv():
            yield ret
# ==============================================================================
def make_M_4(l_Input, a_Result):
    seen = set()
    n = 0
    for num in combinations(l_Input, len(l_Input)):
        for op in product(list(Op), repeat=len(l_Input)-1):
            for tri in make_M_4_Triple(num, op):
                try:
                    if tri.m_eval() == a_Result:
                        e = tri.expand()
                        if e in seen:
                            continue
                        seen.add(e)
                        n += 1
                        sys.stdout.write("# {} {} == {}\n".format(
                            n, str(tri.optimize()), a_Result))
                except (ZeroDivisionError, RuntimeError) as e:
                    # print(tri, e, file=sys.stderr)
                    continue
# ##############################################################################
# ==============================================================================
def load_tests(_loader, tests, _ignore):
    import doctest
    tests.addTests(doctest.DocTestSuite(sys.modules[__name__]))
    return tests
# ==============================================================================
def _run_test_():
    return unittest.main(module=__name__, exit=False).result.wasSuccessful()
# ##############################################################################
# ==============================================================================
def _parse_args_():
    # --------------------------------------------------------------------------
    import argparse
    # --------------------------------------------------------------------------
    parser = argparse.ArgumentParser()
    parser.add_argument('-V', '--version', action='version', version=VERSION)
    parser.add_argument('-n', nargs='?',
                        type=int, default=4, const=4, choices=range(4, 5),
                        help="""
                        The number of input.
                        """)
    parser.add_argument('-m', '--make', nargs='?',
                        type=Fraction, default=Fraction(10), const=Fraction(10),
                        help="""
                        Number you want to create.
                        """)
    return parser.parse_args()
# ==============================================================================
if __name__ == '__main__':
    args = _parse_args_()

    if args.n != 4:
        raise RuntimeError("ERROR!: {}: unsupported".
                           format(getframeinfo(currentframe()).function))

    print('# Enter the {} numbers'.format(args.n))

    g_Input = []

    while not args.n == len(g_Input):
        sys.stdout.write('>>> ')
        g_Input.append(Fraction(input()))

    make_M_4(g_Input, a_Result=Fraction(args.make))