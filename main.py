import unittest

class Calculator:
  # TODO: Write your methods here
  def add(self, a, b):
    return 0
  
  # TODO: Write your methods here
  def subtract(self, a, b):
    return 0
  
  # TODO: Write your methods here
  def multiply(self, a, b):
    return 0
    
  # TODO: Write your methods here
  def divide(self, a, b):
    return 0

# Test Cases
class TestAdd(unittest.TestCase):
  def runTest(self):
    result = Calculator().add(1, 2)
    self.assertEqual(result, 3, "1 + 2 should equal 3")

class TestSubtract(unittest.TestCase):
  def runTest(self):
    result = Calculator().subtract(1, 2)
    self.assertEqual(result, -1, "1 - 2 should equal -1")

class TestMultiply(unittest.TestCase):
  def runTest(self):
    result = Calculator().multiply(1, 2)
    self.assertEqual(result, 2, "1 * 2 should equal 2")

class TestDivide(unittest.TestCase):
  def runTest(self):
    result = Calculator().divide(1, 2)
    self.assertEqual(result, 0.5, "1 / 2 should equal 0.5")

unittest.main()