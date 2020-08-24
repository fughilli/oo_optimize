from __future__ import print_function

import math
import variable
import unittest
from unittest.mock import MagicMock


class VariableTest(unittest.TestCase):
    def test_variable_name_is_correct(self):
        dummy_registry = None
        a = variable.Variable(dummy_registry, 'a')
        self.assertEqual(a.name, 'a')

    def test_registry_makes_variable_with_correct_name(self):
        a = variable.registry.New('a')
        self.assertEqual(a.name, 'a')

    def test_bind_populates_registry(self):
        a = variable.registry.New('a')
        b = variable.registry.New('b')

        a < b

        self.assertEqual(len(variable.registry.e_list), 1)
        self.assertEqual(variable.registry.e_list[0].op, '<')
        self.assertEqual(variable.registry.e_list[0].l.name, a.name)
        self.assertEqual(variable.registry.e_list[0].r.name, b.name)


if __name__ == "__main__":
    unittest.main()
