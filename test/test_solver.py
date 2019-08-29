"""
Unit tests for the solver package modules
"""


import src.solver.scorer as scorer
import src.solver.scoring_funcs as scoring_funcs
import src.geography.geography as geo


class TestScorer(object):

    def test_scorer(self):
        mygeo = geo.Geography(16)
        scorer.Scorer(mygeo)


class TestScoringFunctions(object):

    def test_scoring_functions(self):
        mydict = {0: 12, 1: 5, 2: 6, 3: 42.8}
        assert(scoring_funcs.city_max(mydict) == 42.8)
        assert(scoring_funcs.city_sum(mydict) == 65.8)
        assert(scoring_funcs.city_pow_sum(1)(mydict) == 65.8)
        mydict2 = {0: 10, 1: 100}
        assert(scoring_funcs.city_pow_sum(2)(mydict2) == 10100)
