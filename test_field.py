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

##test the add_creature method when the position is free
def test_add_creature_free():
    test = Field(5, 5)
    test.add_creature(2, 2)
    assert len(test.population) == 1
    assert test.creatureCounter == 1
    assert test.field[2][2].number == 0
    assert test.field[2][2] == test.population[0]

##test the add_creature method when the position is not free
def test_add_creatzre_not_free():
    test = Field(5, 5)
    test.add_creature(2, 2)
    test.add_creature(2, 2)
    assert len(test.population) == 1
    assert test.creatureCounter == 1
    assert test.field[2][2].number == 0
    assert test.field[2][2] == test.population[0]

##test the add_creature method when the position is not given
def test_add_creature_random():
    test = Field(5, 5)
    test.add_creature()
    assert len(test.population) == 1
    assert test.creatureCounter == 1
    assert test.field[test.population[0].y][test.population[0].x] == test.population[0]

##test adding multiple creatures
def test_add_creature_multiple():
    test = Field(5, 5)
    for i in range(5):
        test.add_creature()
    assert len(test.population) == 5
    assert test.creatureCounter == 5
    for c in test.population:
        assert test.field[c.y][c.x] == c