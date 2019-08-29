"""
Scoring_funcs module documentation
----------------------------------

This module provides various scoring functions that enable one to compute the
score (i.e. cost) of a particular configuration on a given
:class:`~geography.geography.Geography`.

A scoring function is usually affected to a :class:`~solver.scorer.Scorer`
object.

.. note::
    Some functions are *regular* functions that just return a value (e.g.
    :func:`city_sum`) but other are *parametric* functions that return another
    function (e.g. :func:`city_pow_sum`).
    Be aware of that when referencing a scoring function in a
    :class:`~solver.scorer.Scorer`.
"""


def city_max(city_dists):
    """
    Computes the max total distance amongst all cities
    """
    return(max(city_dists.values()))


def city_sum(city_dists):
    """
    Computes the sum of the total distance for each city
    """
    return(sum(city_dists.values()))


def city_pow_sum(power):
    """
    Computes the sum of the total distance to power *power* for each city
    """
    def myfunc(city_dists):
        return(sum([city_dist ** power for city_dist in city_dists.values()]))
    return(myfunc)
