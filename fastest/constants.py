import platform


class Sys:
    __UNIX_SLASH = '/'
    __WINDOWS_SLASH = '\\'
    PY = '.py'
    SLASH = __WINDOWS_SLASH if platform.system == 'Windows' else __UNIX_SLASH
    TEST_FILE_ENDING = '__test.py'


class Keys:
    IMPORTS = 'imports'
    NAME = 'name'
    TESTS = 'tests'
    TEST = 'test'
    STR = 'str'
    EXAMPLES = 'examples'
    FROM = 'from'
    EXPECT = 'expect'
    VARIABLES = 'variables'
    PARAMS = 'params'
    RETURN = 'return'


class Content:
    CLASS_CREATE_TEMPLATE = '\nclass Test{}{}(unittest.TestCase):\n'
    IMPORT_UNITTEST = 'import unittest\n'
    DEPS_IMPORT_TEMPLATE = 'from {} import {}\n'
    TEST_CASE_TEMPLATE = '    def test__{function_name}__{case_id}(self):'
    TESTERS_NOTES_TEMPLATE = '        {testers_notes}'
    VARIABLES_TEMPLATE = '        {variables}\n'
    TYPE_ASSERT_TEMPLATE = '\n        self.assertIsInstance({function}, {value})'
    ASSERTION_TEMPLATE = '\n        self.assertEqual({function}, {value})\n'


class Patterns:
    FUNCTION_CALL = r'example: [\s\S]+?(?=->)'
    IMPORT_DEC = '@need\n'
    VAR_DEC = r'@let '
    NEED_IMPORT = r'@need[\s\S]+?(?=@end)'
    NEEDED_VARIABLES = r'@let[\s\S]+?(?=@end)'
    NUMBER_BULLET = r'\d\) '
    TEST_CASE_EXAMPLE = r'\d\) [\s\S]+?(?=\n)'
    EXAMPLE_PASSAGE = r'-{3,}[\s\S]+?(?=---)'
    TEST_SEP = ' -> '


class TestBodies:
    GET_FUNCTIONS_TEST_CASE_1 = """
def function_1():
    return 1
"""
    GET_FUNCTIONS_TEST_CASE_1_EXPECT = [{'name': 'function_1', 'tests': None}]
    TYPE_TEST_CASE_1 = '\n        self.assertIsInstance(function_1(str, str), str)'
    TYPE_TEST_CASE_2 = '\n        self.assertIsInstance(function_1(str, str), str)'
    ASSERTION_TEST_1 = '        a = 5\n'
    NAIVE_TEST_RESULT = """    def test__function_1__A55EFF11ED(self):        a = 5

        self.assertEqual(function_1, 2)\n"""