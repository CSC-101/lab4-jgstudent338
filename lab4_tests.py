import lab4
import unittest
import data


# Write your test cases for each part below.


class TestCases(unittest.TestCase):
    def test1_first_element(self):
        result1 = lab4.first_element([[1, 2, 3], [4, 5, 6], [89, 7]])
        expected1 = [1, 4, 89]
        self.assertEqual(result1, expected1)


    def test2_first_element(self):
        result2 = lab4.first_element([[1, 2, 3], [], [56, 4, 5]])
        expected2 = [1, 56]
        self.assertEqual(result2, expected2)


    # Part 2
    def test3_x_coordinates(self):
        result3 = lab4.x_coordinates([data.Point(1, 5), data.Point(3, 4), data.Point(89, 7)])
        expected3 = [1, 3, 89]
        self.assertEqual(result3, expected3)

    def test4_x_coordinates(self):
        result4 = lab4.x_coordinates([data.Point(-4, 7), data.Point(33, 4), data.Point(21, 7)])
        expected4 = [-4, 33, 21]
        self.assertEqual(result4, expected4)

    # Part 3
    def test5_are_in_positive_quadrant(self):
        result5 = lab4.are_in_positive_quadrant([data.Point(-4, 7), data.Point(33, 4), data.Point(21, -7)])
        expected5 = [data.Point(33, 4)]
        self.assertEqual(result5, expected5)

    def test6_are_in_positive_quadrant(self):
        result6 = lab4.are_in_positive_quadrant([data.Point(0, 0), data.Point(3, 44), data.Point(-21, -7)])
        expected6 = [data.Point(3,44)]
        self.assertEqual(result6, expected6)


    # Part 4
    def test7_distance(self):
        result7 = lab4.distance(data.Point(1,1), data.Point(4,5))
        expected7 = 5
        self.assertEqual(result7, expected7)

    def test8_distance(self):
        result8 = lab4.distance(data.Point(1,-1), data.Point(13,-6))
        expected8 = 13
        self.assertEqual(result8, expected8)

    # Part 5
    def test9_manhattan_distance(self):
        result9 = lab4.manhattan_distance(data.Point(1, 1), data.Point(4, 5))
        expected9 = data.Point(2.5, 3)
        self.assertEqual(result9, expected9)

    def test10_manhattan_distance(self):
        result10 = lab4.manhattan_distance(data.Point(1, -1), data.Point(13, -6))
        expected10 = data.Point(7, -3.5)
        self.assertEqual(result10, expected10)

    # Part 6
    def test_distance_all(self):
        result11 = lab4.distance_all([data.Point(3, 4), data.Point(5, 12), data.Point(8, 15)])
        expected11 = [5, 13, 17]
        self.assertEqual(result11, expected11)

    def test12_distance_all(self):
        result11 = lab4.distance_all([data.Point(33, 56), data.Point(-13, 84), data.Point(-39, -80)])
        expected11 = [65, 85, 89]
        self.assertEqual(result11, expected11)



if __name__ == '__main__':
    unittest.main()
