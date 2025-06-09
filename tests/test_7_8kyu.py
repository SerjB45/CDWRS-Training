from task_7_8kyu import *

def test_extra_perfect():

    assert extra_perfect(3) == [1, 3]
    assert extra_perfect_2(3) == [1, 3]
    assert extra_perfect_3(3) == [1, 3]
    
    assert extra_perfect(5) == [1, 3, 5]
    assert extra_perfect_2(5) == [1, 3, 5]
    assert extra_perfect_3(5) == [1, 3, 5]
    
    assert extra_perfect(7) == [1, 3, 5, 7]
    assert extra_perfect_2(7) == [1, 3, 5, 7]
    assert extra_perfect_3(7) == [1, 3, 5, 7]
    
    assert extra_perfect(28) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27]
    assert extra_perfect_2(28) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27]
    assert extra_perfect_3(28) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27]

def test_duck_duck_goose():
    players = [Player(name = name, id = i) for i, name in enumerate('abcdfegs')]
    assert duck_duck_goose(players, 1) == 'a'  
    assert duck_duck_goose(players, 7) == 'g'
    assert duck_duck_goose(players, 10) == 'b'
    
def test_add_binary():
    assert add_binary(1,1),"10"
    assert add_binary(0,1),"1"
    assert add_binary(1,0),"1"
    assert add_binary(2,2),"100"
    assert add_binary(51,12),"111111"    

