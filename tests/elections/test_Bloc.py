from metric_voting import Bloc
import numpy as np

def test_basic_profile(basic_profile):
    assert set(Bloc(basic_profile, 1).tolist()) == set([3])
    assert set(Bloc(basic_profile, 2).tolist()) == set([0,3])
    assert set(Bloc(basic_profile, 3).tolist()) == set([0,2,3])
    assert set(Bloc(basic_profile, 4).tolist()) == set([0,1,2,3])

def test_tie_break(profile_with_fp_tie):
    winners = np.array([-1]*1000)

    for i in range(1000):
        winners[i] = Bloc(profile_with_fp_tie, 1)[0]

    _, counts = np.unique(winners, return_counts=True)

    assert  len(counts) == 2
    assert 490 < counts[0] and counts[0] < 510
    assert 490 < counts[1] and counts[1] < 510
