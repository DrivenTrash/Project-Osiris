import unittest
from unittest.mock import patch
from application.field import Field
from application.creature import Creature

##test the move_creature method
class TestMoveCreature(unittest.TestCase):
    
    @patch('creature.Creature.move', return_value=0)
    def test_move_0(self, mock_move): 
        test = Field(5, 5)
        c0 = Creature(0, 0, 2, 2)
        test.field[2][2] = c0
        test.move_creature(c0)
        self.assertEqual(test.field[2][2], 0)
        self.assertEqual(test.field[1][2], c0)