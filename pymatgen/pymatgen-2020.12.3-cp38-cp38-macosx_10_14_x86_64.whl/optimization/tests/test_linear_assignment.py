# coding: utf-8
# Copyright (c) Pymatgen Development Team.
# Distributed under the terms of the MIT License.


import unittest

import numpy as np

from pymatgen.optimization.linear_assignment import LinearAssignment  # type: ignore


class LinearAssignmentTest(unittest.TestCase):
    def test(self):
        w0 = np.array(
            [
                [19, 95, 9, 43, 62, 90, 10, 77, 71, 27],
                [26, 30, 88, 78, 87, 2, 14, 71, 78, 11],
                [48, 70, 26, 82, 32, 16, 36, 26, 42, 79],
                [47, 46, 93, 66, 38, 20, 73, 39, 55, 51],
                [1, 81, 31, 49, 20, 24, 95, 80, 82, 11],
                [81, 48, 35, 54, 35, 55, 27, 87, 96, 7],
                [42, 17, 60, 73, 37, 36, 79, 3, 60, 82],
                [14, 57, 23, 69, 93, 78, 56, 49, 83, 36],
                [11, 37, 24, 70, 62, 35, 64, 18, 99, 20],
                [73, 11, 98, 50, 19, 96, 61, 73, 98, 14],
            ]
        )

        w1 = np.array(
            [
                [95, 60, 89, 38, 36, 38, 58, 94, 66, 23],
                [37, 0, 40, 58, 97, 85, 18, 54, 86, 21],
                [9, 74, 11, 45, 65, 64, 27, 88, 24, 26],
                [58, 90, 6, 36, 17, 21, 2, 12, 80, 90],
                [33, 0, 74, 75, 11, 84, 34, 7, 39, 0],
                [17, 61, 94, 68, 27, 41, 33, 86, 59, 2],
                [61, 94, 36, 53, 66, 33, 15, 87, 97, 11],
                [22, 20, 57, 69, 15, 9, 15, 8, 82, 68],
                [40, 0, 13, 61, 67, 40, 29, 25, 72, 44],
                [13, 97, 97, 54, 5, 30, 44, 75, 16, 0],
            ]
        )

        w2 = np.array(
            [
                [34, 44, 72, 13, 10, 58, 16, 1, 10, 61],
                [54, 70, 99, 4, 64, 0, 15, 94, 39, 46],
                [49, 21, 80, 68, 96, 58, 24, 87, 79, 67],
                [86, 46, 58, 83, 83, 56, 83, 65, 4, 96],
                [48, 95, 64, 34, 75, 82, 64, 47, 35, 19],
                [11, 49, 6, 57, 80, 26, 47, 63, 75, 75],
                [74, 7, 15, 83, 64, 26, 78, 17, 67, 46],
                [19, 13, 2, 26, 52, 16, 65, 24, 2, 98],
                [36, 7, 93, 93, 11, 39, 94, 26, 46, 69],
                [32, 95, 37, 50, 97, 96, 12, 70, 40, 93],
            ]
        )

        la0 = LinearAssignment(w0)

        self.assertEqual(la0.min_cost, 194, "Incorrect cost")
        la1 = LinearAssignment(w1)
        self.assertEqual(la0.min_cost, la0.min_cost, "Property incorrect")
        self.assertEqual(la1.min_cost, 125, "Incorrect cost")
        la2 = LinearAssignment(w2)
        self.assertEqual(la2.min_cost, 110, "Incorrect cost")

    def test_rectangular(self):
        w0 = np.array(
            [
                [19, 95, 9, 43, 62, 90, 10, 77, 71, 27],
                [26, 30, 88, 78, 87, 2, 14, 71, 78, 11],
                [48, 70, 26, 82, 32, 16, 36, 26, 42, 79],
                [47, 46, 93, 66, 38, 20, 73, 39, 55, 51],
                [1, 81, 31, 49, 20, 24, 95, 80, 82, 11],
                [81, 48, 35, 54, 35, 55, 27, 87, 96, 7],
                [42, 17, 60, 73, 37, 36, 79, 3, 60, 82],
                [14, 57, 23, 69, 93, 78, 56, 49, 83, 36],
                [11, 37, 24, 70, 62, 35, 64, 18, 99, 20],
            ]
        )
        la0 = LinearAssignment(w0)

        w1 = np.array(
            [
                [19, 95, 9, 43, 62, 90, 10, 77, 71, 27],
                [26, 30, 88, 78, 87, 2, 14, 71, 78, 11],
                [48, 70, 26, 82, 32, 16, 36, 26, 42, 79],
                [47, 46, 93, 66, 38, 20, 73, 39, 55, 51],
                [1, 81, 31, 49, 20, 24, 95, 80, 82, 11],
                [81, 48, 35, 54, 35, 55, 27, 87, 96, 7],
                [42, 17, 60, 73, 37, 36, 79, 3, 60, 82],
                [14, 57, 23, 69, 93, 78, 56, 49, 83, 36],
                [11, 37, 24, 70, 62, 35, 64, 18, 99, 20],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
            ]
        )
        la1 = LinearAssignment(w1)
        self.assertEqual(len(la1.solution), 10)
        self.assertEqual(la0.min_cost, la1.min_cost)

        self.assertRaises(ValueError, LinearAssignment, w0.T)

    def another_test_case(self):
        w1 = np.array(
            [
                [
                    0.03900238875468465,
                    0.003202415721817453,
                    0.20107156847937024,
                    0.0,
                    0.5002116398420846,
                    0.11951326861160616,
                    0.0,
                    0.5469032363997579,
                    0.3243791041219123,
                    0.1119882291981289,
                ],
                [
                    0.6048342640688928,
                    0.3847629088356139,
                    0.0,
                    0.44358269535118944,
                    0.45925670625165016,
                    0.31416882324798145,
                    0.8065128182180494,
                    0.0,
                    0.26153475286065075,
                    0.6862799559241944,
                ],
                [
                    0.5597215814025246,
                    0.15133664165478322,
                    0.0,
                    0.6218101659263295,
                    0.15438455134183793,
                    0.17281467064043232,
                    0.8458127968475472,
                    0.020860721537078075,
                    0.1926886361228456,
                    0.0,
                ],
                [
                    0.0,
                    0.0,
                    0.6351848838666995,
                    0.21261247074659906,
                    0.4811603832432241,
                    0.6663733668270337,
                    0.63970145187428,
                    0.1415815172623256,
                    0.5294574133825874,
                    0.5576702829768786,
                ],
                [
                    0.25052904388309016,
                    0.2309392544588127,
                    0.0656162006684271,
                    0.0248922362001176,
                    0.0,
                    0.2101808638720748,
                    0.6529031699724193,
                    0.1503003886507902,
                    0.375576165698992,
                    0.7368328849560374,
                ],
                [
                    0.0,
                    0.042215873587668984,
                    0.10326920761908365,
                    0.3562551151517992,
                    0.9170343984958856,
                    0.818783531026254,
                    0.7896770426052844,
                    0.0,
                    0.6573135097946438,
                    0.17806189728574429,
                ],
                [
                    0.44992199118890386,
                    0.0,
                    0.38548898339412585,
                    0.6269193883601244,
                    1.0022861602564634,
                    0.0,
                    0.1869765500803764,
                    0.03474156273982543,
                    0.3715310534696664,
                    0.6197122486230232,
                ],
                [
                    0.37939853696836545,
                    0.2421427374018027,
                    0.5586150342727723,
                    0.0,
                    0.7171485794073893,
                    0.8021029235865014,
                    0.11213464903613135,
                    0.6497896761660467,
                    0.3274108706187846,
                    0.0,
                ],
                [
                    0.6674685746225324,
                    0.5347953626128863,
                    0.11461835366075113,
                    0.0,
                    0.8170639855163434,
                    0.7291931505979982,
                    0.3149153087053108,
                    0.1008681103294512,
                    0.0,
                    0.18751172321112997,
                ],
                [
                    0.6985944652913342,
                    0.6139921045056471,
                    0.0,
                    0.4393266955771965,
                    0.0,
                    0.47265399761400695,
                    0.3674241844351025,
                    0.04731761392352629,
                    0.21484886069716147,
                    0.16488710920126137,
                ],
            ]
        )
        la = LinearAssignment(w1)
        self.assertAlmostEqual(la.min_cost, 0)

    def test_small_range(self):
        # can be tricky for the augment step
        x = np.array(
            [
                [4, 5, 5, 6, 8, 4, 7, 4, 7, 8],
                [5, 6, 6, 6, 7, 6, 6, 5, 6, 7],
                [4, 4, 5, 7, 7, 4, 8, 4, 7, 7],
                [6, 7, 6, 6, 7, 6, 6, 6, 6, 6],
                [4, 4, 4, 6, 6, 4, 7, 4, 7, 7],
                [4, 5, 5, 6, 8, 4, 7, 4, 7, 8],
                [5, 7, 5, 5, 5, 6, 4, 5, 4, 6],
                [8, 9, 8, 4, 5, 9, 4, 8, 4, 4],
                [5, 6, 6, 6, 7, 6, 6, 5, 6, 7],
                [5, 6, 6, 6, 7, 6, 6, 5, 6, 7],
            ]
        )
        self.assertAlmostEqual(LinearAssignment(x).min_cost, 48)

    def test_boolean_inputs(self):
        w = np.ones((135, 135), dtype=np.bool)
        np.fill_diagonal(w, False)
        la = LinearAssignment(w)
        # if the input doesn't get converted to a float, the masking
        # doesn't work properly
        self.assertEqual(la.orig_c.dtype, np.float64)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
