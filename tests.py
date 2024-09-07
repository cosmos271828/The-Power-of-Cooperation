import functions
import unittest


functions.failure_c_p = 0

class Test(unittest.TestCase):

# =======================================================================
    def test1(self):
        self.assertEqual(functions.game('tit_for_tat 1', 'tit_for_tat 2'), [400,400])
    def test2(self):
        self.assertEqual(functions.tournament([]), [])
    def test3(self):
        self.assertEqual(functions.tournament(['tit_for_tat']), [0])
    def test4(self):
        self.assertEqual(functions.tournament(['tit_for_tat 1', 'tester 1']), [398,398])
    def test5(self):
        self.assertEqual(functions.tournament(['always_defect 1', 'always_cooperate 1']), [600,-200])
    def test6(self):
        test6_players = ['tit_for_tat 1', 'tit_for_tat 2', 'tit_for_two_tats 1',
'tit_for_two_tats 2', 'grudger 1', 'grudger 2', 'simpleton 1', 'simpleton 2',
'tester 1', 'tester 2', 'always_defect 1', 'always_defect 2',
'always_cooperate 1', 'always_cooperate 2', 'tit_for_tat_advanced 1', 
'tit_for_tat_advanced 2', 'delayed_tit_for_two_tats 1', 'delayed_tit_for_two_tats 2']
        self.assertEqual(functions.tournament(test6_players),
                         [5994, 5994, 5396, 5396, 5208,5208, 5268, 5268, 5052, 5052,
                          1854, 1854, 5000, 5000, 5990, 5990, 5994, 5994])
    def test7(self):
        test7_players = ['tit_for_tat 1', 'tit_for_two_tats 1', 'grudger 1', 'simpleton 1',
'tester 1', 'always_defect 1', 'always_cooperate 1', 'tit_for_tat_advanced 1', 
'delayed_tit_for_two_tats 1']
        self.assertEqual(functions.tournament(test7_players),
                        [2797, 2498, 2404, 2434, 2328,927, 2300, 2795, 2797])
    def test8(self):
        test8_players = ['tit_for_tat 1', 'tit_for_two_tats 1', 'tester 1']
        self.assertEqual(functions.tournament(test8_players),
                         [798, 500, 898])
    def test9(self):
        test9_players = ['tit_for_tat 1', 'tit_for_tat 2', 'tit_for_two_tats 1', 'tester 1']
        self.assertEqual(functions.tournament(test9_players),
                         [1198, 1198, 900, 1296])

# =======================================================================
    # Add more test cases as needed to cover different scenarios and edge cases

if __name__ == '__main__':
    unittest.main()
