from cod import simulate

def test_documentation1():
    assert set(simulate([(1,5), (5,4), (5,2), (4,1), (2,0)],
    [(2,4), (0,2)], [(1,3), (4,3), (4,2), (3,2), (3,1)])) == set([(5,2), (4,1)])

def test_documentation2():
    assert set(simulate([(1,1),(2,2),(3,3)], [ (6,6) ],
    [ (3,4), (3,5), (4,5), (4,4) ])) == set([(1,1), (2,2), (3,3)])

def test_all_visible():
    assert set(simulate([(1,1), (2,2), (3,3)], [(0,3)],
    [(4,3),(4,4),(5,4),(5,3)])) == set()
    assert set(simulate([(1,1), (2,2), (3,3)], [(3,0)],
    [(4,3),(4,4),(5,4),(5,3)])) == set()

def test_horizontal_hidden():
    assert set(simulate([(1,1),(2,2),(3,4)], [(7,4)],
    [(4,3),(4,4),(5,4),(5,3)])) == set([(1,1),(2,2),(3,4)])

def test_vertical_hidden():
    assert set(simulate([(2,-1), (2,-2), (2,-3), (2, -6), (2,-7), (2,-8)],
    [(-2, 2)], [(0,0),(1,0),(1,-2),(0,-2)])) == set([(2,-1),(2,-2),(2,-3),(2,-6)])

def test_edgecases():
    assert set(simulate([(0,1), (0,0), (1,0), (2,0), (3,0), (2,4), (2,6), (6,5), (5,5), (5,6)], [(2,5)],
    [(2,3), (3,3), (3,6), (4,6), (4,1), (2,1)])) == set([(2,0),(3,0),(6,5),(5,5),(5,6)])