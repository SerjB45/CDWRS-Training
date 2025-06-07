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
    # for i in 'abcdfegs':
    #     obj = Player()
    #     obj.name = i
    #     players.append(obj)
    assert duck_duck_goose(players, 1) == 'a'  
    assert duck_duck_goose(players, 7) == 'g'
    assert duck_duck_goose(players, 10) == 'b'

# test.assert_equals(extra_perfect(5), )
# test.assert_equals(extra_perfect(7), )
# test.assert_equals(extra_perfect(28), [1,3,5,7,9,11,13,15,17,19,21,23,25,27])
# test.assert_equals(extra_perfect(39), [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39])
    