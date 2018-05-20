# ! python3
import unittest


def test_something():
    print("hello world")


class MyTestCase(unittest.TestCase):
    test_something()


if __name__ == '__main__':
    unittest.main()
