import unittest
import main


class MainTest(unittest.TestCase):
    def test_helloworld(self):
        _return = main.helloworld("test~")
        self.assertEqual(_return, "hello world test~")


if __name__ == "__main__":
    unittest.main()
