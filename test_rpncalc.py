import unittest
from expr import *
from rpncalc import *



class TestParseRPN(unittest.TestCase):

    def test_parse_add(self):
        exp = rpn_parse("5 4 +")[0]
        self.assertEqual(str(exp), "(5 + 4)")
        self.assertEqual(repr(exp), "Plus(IntConst(5), IntConst(4))")
        self.assertEqual(exp.eval(), IntConst(9))

    def test_parse_times(self):
        exp = rpn_parse("5 3 * ")[0]
        self.assertEqual(repr(exp), "Times(IntConst(5), IntConst(3))")
        self.assertEqual(str(exp), "(5 * 3)")
        self.assertEqual(exp.eval(), IntConst(15))

    def test_parse_minus(self):
        exp = rpn_parse("5 3 -")[0]
        self.assertEqual(str(exp), "(5 - 3)")
        self.assertEqual(repr(exp), "Minus(IntConst(5), IntConst(3))")
        self.assertEqual(exp.eval(), IntConst(2))

    def test_parse_div(self):
        exp = rpn_parse("7 3 /")[0]
        self.assertEqual(str(exp), "(7 / 3)")
        self.assertEqual(repr(exp), "Div(IntConst(7), IntConst(3))")
        self.assertEqual(exp.eval(), IntConst(2))
        exp = rpn_parse("3 7 /")[0]
        self.assertEqual(exp.eval(), IntConst(0))


class TestRPNAssignment(unittest.TestCase):

    def test_env_global(self):
        exp = rpn_parse("5 4 3 * + x =")[0]
        self.assertEqual(str(exp), "(x = (5 + (4 * 3)))")
        self.assertEqual(exp.eval(), IntConst(17))
        exp = rpn_parse("x 3 +")[0]
        self.assertEqual(exp.eval(), IntConst(20))
