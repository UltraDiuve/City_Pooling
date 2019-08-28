"""
Scoring_funcs module documentation
----------------------------------

This module provides various scoring functions that enable one to compute the
score (i.e. cost) of a particular configuration on a given
:class:`~geography.geography.Geography`.

A scoring function is usually affected to a :class:`~solver.scorer.Scorer`
object.
"""


def city_max(city_dists):
    """
    Computes the max total distance amongst all cities
    """
    return(max(city_dists.values()))
