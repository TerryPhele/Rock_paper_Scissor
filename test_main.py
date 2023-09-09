import unittest
from unittest.mock import patch
from io import StringIO
import main

class TestMainCase(unittest.TestCase):
    
    @patch('sys.stdin',StringIO('\n1'))
    def test_get_user_choice(self):
        self.assertEqual(main.get_user_choice(),1)
        pass

    main.random.randint = lambda a,b : 3
    def test_get_computer_choice(self):
        self.assertEqual(main.get_computer_choice(),3)
        pass


    def test_evaluate_results_user(self):
        computer_wins, user_wins, draws = main.evaluate_results(1,2,[0,0,0])
        self.assertEqual(computer_wins,0)
        self.assertEqual(user_wins,1)
        self.assertEqual(draws,0)
    
 
    def test_evaluate_results_computer(self):
        computer_wins, user_wins, draws = main.evaluate_results(2,1,[0,0,0])
        self.assertEqual(computer_wins,1)
        self.assertEqual(user_wins,0)
        self.assertEqual(draws,0)
        


    def test_evaluate_results_draw(self):
        computer_wins, user_wins, draws = main.evaluate_results(1,1,[0,0,0])
        self.assertEqual(computer_wins,0)
        self.assertEqual(user_wins,0)
        self.assertEqual(draws,1)
        

    @patch("sys.stdout",new_callable= StringIO)
    def test_display_results(self,out):
        player = "You"
        main.display_results(player)
        self.assertEqual('You win.',out.getvalue().strip())

    @patch("sys.stdout",new_callable= StringIO)
    def test_show_game_statistic(self,out):
        main.show_game_statistic(1,1,0)
        self.assertEqual("""-----GAME STATISTICS-----
--------------------------------------
    |Computer    |   User    |   draw
--------------------------------------
Tot |           1|          1|      0""",out.getvalue().strip())

    



