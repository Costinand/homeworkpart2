import unittest
import runner_test
import tournament_test


testST = unittest.TestSuite()
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(runner_test.RunnerTest))
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(tournament_test.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(testST)