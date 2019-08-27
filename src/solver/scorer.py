"""
Scorer module documentation
---------------------------

This module docstring
"""


# imports
import numpy as np

# local imports
from . import scoring_funcs


class scorer():
    """ Class defining a scorer (utility to compute score)

    This class implements a scorer utility that will compute the score of a
    configuration for a geography.

    A scorer must have a scoring function defined as an attribute, as well as a
    :class:`geography`.

    Attributes:
        _scoring_func (function): the function to be applied for scoring
        geo (:class:`~geography.geography.geography`): the geography on which
            score
        city_total_dists (dict): the distance sum for each city for the current
        configuration
    """
    def __init__(self, geo, scoring_func=scoring_funcs.city_max):
        """ Constructor method of scorer

        This method will construct a scorer and initialize its scoring function

        Args:
            scoring_func (function): the function to be applied for scoring

        Returns:
            The initialized :class:`scorer`.
            """
        self.geo = geo
        self._scoring_func = scoring_func

    def compute_city_total_dists(self, configuration):
        """ Utility function that compute the total dist for each city

        This methods computes the total dist for each city and stores the
        result into this class city_total_dists dictionary attribute.

        Args:
            configuration (iterable): the configuration to apply

        Returns:
            Nothing.
        """
        self.city_total_dists = dict()
        for pool_num, pool_content in configuration.items():
            for city_index in pool_content:
                self.city_total_dists[city_index] = np.sum(
                    self.geo.dist_matrix[city_index, pool_content])

    def score(self, configuration):
        """ Scoring function of scorer class

        This methods returns the score computed for the configuration applied
        to the geography.

        Args:
            configuration (iterable): the configuration to apply

        Returns:
            The score (i.e. a positive number) for the configuration applied
            to this geography.
        """
        self.compute_city_total_dists(configuration)
        return(self._scoring_func(self.city_total_dists))
