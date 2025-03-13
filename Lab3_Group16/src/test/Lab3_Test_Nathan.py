import unittest
from src.app.Lab3_Nathan import circle_area, trapezium_area, ellipse_area, rhombus_area


class TestShapes(unittest.TestCase):

    def setUp(self):
        print("Setup: Preparing tests...")

    def tearDown(self):
        print("Teardown: Cleaning up after tests...")

    def test_circle_area_valid(self):
        result = circle_area(3)
        print("result {result}" .format(result=result))
        self.assertEqual(result, 28.27)

    def test_circle_area_invalid(self):
        with self.assertRaises(ValueError) as error:
            circle_area(-1)
        print(f"Error: {error.exception}")


    def test_trapezium_area_valid(self):
        result = trapezium_area(5,5,4)
        print("result {result}" .format(result=result))
        self.assertEqual(result, 20)

    def test_trapezium_area_invalid(self):
        with self.assertRaises(ValueError) as error:
            trapezium_area(5, 5, -4)
        print(f"Error: {error.exception}")

    def test_ellipse_area_valid(self):
        result = ellipse_area(3, 2)
        print("result {result}".format(result=result))
        self.assertEqual(result, 18.85)

    def test_ellipse_area_invalid(self):
        with self.assertRaises(ValueError) as error:
            ellipse_area(3, 4j)
        print(f"Error: {error.exception}")

    def test_rhombus_area_valid(self):
        result = ellipse_area(2, 2)
        print("result {result}".format(result=result))
        self.assertEqual(result, 2)

    def test_rhombus_area_invalid(self):
        with self.assertRaises(ValueError) as error:
            rhombus_area(6, "j")
        print(f"Error: {error.exception}")

if __name__ == "__main__":
    unittest.main()