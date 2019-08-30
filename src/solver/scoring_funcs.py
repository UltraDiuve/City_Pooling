"""
scoring_funcs module documentation
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

    This basic function returns the maximum total distance for a single city.

    Args:
        city_dists (dict of numbers): the total distances for each city. The
            keys of the dictionary being the cities indexes.

    Returns:
        The maximum total distance.
    """
    return(max(city_dists.values()))


def city_sum(city_dists):
    """
    Computes the sum of the total distance for all cities

    This basic function returns the sum of the total distance for all
    cities.

    Args:
        city_dists (dict of numbers): the total distances for each city. The
            keys of the dictionary being the cities indexes.

    Returns:
        The sum of the total distances.
    """
    return(sum(city_dists.values()))


def city_pow_sum(power):
    """
    Computes the sum of the total distance to power *power* for each city

    This function returns the sum of the total distances elevated to the power
    *power* for all cities.

    Using a power stricly greater than 1 makes it so that configurations with
    cities having high total distances get a greater score. It tends to make
    the scoring system more egalitarianist (as opposed to utilitarianist).

    .. note::
        This function returns another function that can be then called on a
        dictionary of cities distances. See :ref:`Examples`.

    Args:
        power (number): the power to apply to each city total dist before
            summing.

    Returns:
        The sum of the total distances elevated to the power *power*.

    .. _Examples:

    Examples:
        >>> myscorefunc = city_pow_sum(2)
        >>> mydict = {0: 1, 1: 10}
        >>> print(myscorefunc(mydict))
        101
    """
    def myfunc(city_dists):
        return(sum([city_dist ** power for city_dist in city_dists.values()]))
    return(myfunc)


def city_lambda_sum(lambdafunc):
    """
    Computes the sum of the total distance after having applied lambda func

    This function returns the sum of the total distances after having applied
    *lamda* function for each of them.

    Using a convex lambda function makes it so that configurations with
    cities having high total distances get a greater score. It tends to make
    the scoring system more egalitarianist (as opposed to utilitarianist).

    .. note::
        This function returns another function that can be then called on a
        dictionary of cities distances. See :ref:`Examples2`.

    Args:
        lambdafunc (function): the function to apply to each city total dist
            before summing.

    Returns:
        The sum of the total distances after having applied the lambdafunc
        function.

    .. _Examples2:

    Examples:
        >>> import math
        >>> myscorefunc = city_lambda_sum(math.exp)
        >>> mydict = {0: 1, 1: 10}
        >>> print(myscorefunc(mydict))
        151.13144093
    """
    def myfunc(city_dists):
        return(sum([lambdafunc(city_dist)
                    for city_dist in city_dists.values()]))
    return(myfunc)
