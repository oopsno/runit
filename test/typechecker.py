import unittest
import runit.typechecker as tc


class TypeCheck(unittest.TestCase):
    def test_primitive(self):
        self.assertTrue(tc.typecheck(bool, True))
        self.assertTrue(tc.typechecker(Exception, IOError('nothing here')))

    def test_special(self):
        self.assertTrue(tc.typecheck(None, None))
        self.assertTrue(tc.typecheck(Ellipsis, Ellipsis))
        self.assertTrue(tc.typecheck(NotImplemented, NotImplemented))

    def test_unit(self):
        self.assertTrue(tc.typecheck((), ()))

    def test_empty(self):
        self.assertTrue(tc.typecheck([str], []))
        with self.assertRaises(TypeError):
            tc.typecheck([], [])

    def test_cons(self):
        self.assertTrue(tc.typecheck((int, float), (42, 3.14)))
        self.assertFalse(tc.typecheck((int, bool), (False, None)))

    def test_list(self):
        self.assertTrue(tc.typecheck([str], []))
        self.assertTrue(tc.typecheck([str], ["hello", "world"]))
        with self.assertRaises(TypeError):
            tc.typecheck([int, float], [42, 3.14])

if __name__ == '__main__':
    unittest.main()
