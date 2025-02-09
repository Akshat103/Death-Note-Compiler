import unittest
import sys
from tests.test_compiler import TestDeathNoteCompiler

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDeathNoteCompiler)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return 0 if result.wasSuccessful() else 1

if __name__ == '__main__':
    sys.exit(run_tests())