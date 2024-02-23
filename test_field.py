import pytest
from field import Field
from creature import Creature

##test the move_creature method
@pytest.fixture(params=[0, 1, 2, 3, 4, 5, 6, 7, 8])
def mock_move(request, monkeypatch):
    def mock_move(self):
        return request.param
    monkeypatch.setattr(Creature, "move", mock_move)
    return request.param

def test_move(mock_move): 
    test = Field(5, 5)
    cTest = Creature(0, 0, 2, 2)
    test.field[2][2] = cTest
    test.move_creature(cTest)
    if mock_move == 0:
        assert test.field[2][2] == 0
        assert cTest.x == 1
        assert cTest.y == 1
        assert test.field[1][1] == cTest
    if mock_move == 1:
        assert test.field[2][2] == 0
        assert cTest.x == 2
        assert cTest.y == 1
        assert test.field[1][2] == cTest
    if mock_move == 2:
        assert test.field[2][2] == 0
        assert cTest.x == 3
        assert cTest.y == 1
        assert test.field[1][3] == cTest
    if mock_move == 3:
        assert test.field[2][2] == 0
        assert cTest.x == 1
        assert cTest.y == 2
        assert test.field[2][1] == cTest
    if mock_move == 4:
        assert test.field[2][2] != 0
        assert cTest.x == 2
        assert cTest.y == 2
        assert test.field[2][2] == cTest
    if mock_move == 5:
        assert test.field[2][2] == 0
        assert cTest.x == 3
        assert cTest.y == 2
        assert test.field[2][3] == cTest
    if mock_move == 6:
        assert test.field[2][2] == 0
        assert cTest.x == 1
        assert cTest.y == 3
        assert test.field[3][1] == cTest
    if mock_move == 7:
        assert test.field[2][2] == 0
        assert cTest.x == 2
        assert cTest.y == 3
        assert test.field[3][2] == cTest
    if mock_move == 8:
        assert test.field[2][2] == 0
        assert cTest.x == 3
        assert cTest.y == 3
        assert test.field[3][3] == cTest