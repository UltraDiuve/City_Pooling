import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Rectangle


def dist(city1, city2):
    """ Function that returns euclidean distance between 2 cities

    This function returns the euclidean distance between 2 cities, where each
    of the two cities is a couple of coordinates.

    Args:
        city1 (tuple of 2 coordinates): the first city
        city2 (tuple of 2 coordinates): the second city

    Returns:
        The euclidean distance, being a float number.

    Examples:
        >>> print(dist([0, 0], [3, 4]))
        5.0
    """
    return(((city1[0]-city2[0])**2. + (city1[1]-city2[1])**2.)**0.5)


def permute_array(arr, seq):
    """ Function to "square permute" a 2D array

    This function's purpose is to enable distance matrices permutations. That
    is, for example, permute both lines and columns of the array so as to
    reorder a distance matrix.

    Args:
        arr (numpy array): the array to permute. It should be square of size n.
        seq (iterable of int): a permutation of range(n) (should be of length n
            and contain every integer from 0 to n-1)

    Returns:
        A copy of the original array, after the permutation has been applied.

    Examples:
        >>> import numpy as np
        >>> test = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
        >>> print(permute_array(test, [0, 2, 1]))
        [[1 3 2] [7 9 8] [4 6 5]]

    """
    return(arr[:, seq][seq, :])


class geography():
    """ Class defining a geography (cities and distance matrix)

    This class implements a geography with a list of named cities with their
    associated coordinates in a plane. Helper functions enable to :

    - give a visual representation of that geography
    - give a visual representation of the distance matrix
    - give a visual representation of a configuration, a configuration being
      the repartition of some or all cities in pools

    Attributes:
        cities_count (int): Count of cities in the geography.
        coordinates (numpy array of shape(2, cities_count)): [X,Y] where X is
            Xs of cities and Y is Ys of cities.
        cities_names (numpy array of string): an array of strings.
        dist_matrix (numpy array of shape(cities_count, cities_count)): the
            distance matrix of the geography.

    """
    def init_dist_matrix(self, func=dist):
        """ Method which will initialize the distance matrix

        Args:
            func (function): a distance function which returns a positive
                number from a couple of cities. If unspecified, will use the
                euclidean distance in the plane (:func:`dist` function).

        Returns:
            Nothing.
        """
        self.dist_matrix = np.array(
            [[dist(self.coordinates[:, i], self.coordinates[:, j])
                for j in range(self.cities_count)]
                for i in range(self.cities_count)])

    def __init__(self, cities_count, cities_coordinates=None,
                 cities_names=None, dist_func=dist):
        """ Constructor method of geography

        This method will construct a geography from parameters and initialize
        its distance matrix

        Args:
            cities_count (int): the count of cities in the geography/
            cities_coordinates (optional, array of shape (2, cities_count)):
                the coordinates of the cities. If omitted, will randomly place
                the cities in the plane.
            cities_names (optional, iterable of strings): the names of the
                cities. If omitted will default to an array of cities with the
                names 'City0', 'City1', ...
            dist_func (function): the distance function to be used to populate
                the distance matrix. Default to :func:`dist` which is the
                euclidean distance

        Returns:
            The initialized :class:`geography`.
            """

        self.cities_count = cities_count
        self.coordinates = np.random.rand(2, cities_count) if cities_coordinates is None else cities_coordinates
        self.names = np.array([("City " + str(i)) for i in range(cities_count)]) if cities_names is None else np.array(cities_names)

        # initialize distance matrix
        self.init_dist_matrix(func=dist_func)

    def draw_map(self, axis_in, show_names=False, kwargs={}):
        """ Method that will populate an axis with the map of the geograpy

        This method is called through the show method and will populate the
        axis with the map.

        Args:
            axis_in (axis): the axis to which draw the map of the geography.
            show_names (bool, optional): whether or not to show the names of
                the cities in the map. Is passed by the :meth:`show` method.
            kwargs (dict, optional): kwargs to be used in the drawing of the
                map.

        Returns:
            Nothing.

        """
        axis_in.scatter(*self.coordinates)
        if show_names:
            for i in range(self.cities_count):
                axis_in.annotate(self.names[i], self.coordinates[:, i])
        axis_in.tick_params(
            axis='both',
            which='both',
            bottom=False,
            top=False,
            left=False,
            right=False,
            labelbottom=False,
            labeltop=False,
            labelleft=False,
            labelright=False)
        axis_in.set_title('Map of Geography\n', fontsize=24)

    def draw_dist_matrix(self, axis_in, dist_matrix, names=None,
                         show_names=False, kwargs={}):
        """ Method that will populate an axis with the distance matrix

        This method is called through the show method and will populate the
        axis with the distance matrix.

        Args:
            axis_in (axis): the axis to which draw the distance matrix.
            show_names (bool, optional): whether or not to show the names of
                the cities in the distance matrix. Is passed by the
                :meth:`show` method.
            kwargs (dict, optional): kwargs to be used in the drawing of the
                distance matrix (so far, only 'annot' is used).

        Returns:
            Nothing.

        """
        yticklabels = self.names if names is None else names
        xticklabels = self.names if names is None else names
        sns.heatmap(dist_matrix,
                    cmap="Blues",
                    cbar=False,
                    xticklabels=xticklabels,
                    yticklabels=yticklabels,
                    **kwargs)
        axis_in.set_title('Distance Matrix\n', fontsize=24)

    def show(self, show_names=False, map_kwargs={}, dist_matrix_kwargs={}):
        """ Method to show a graphical representation of the geography

        This method will draw the geography in a plane, and give a view of the
        distance matrix in the form of a seaborn heatmap.

        Args:
            show_names (bool, optional): whether or not to show the names of
                the cities in the representation, both in the geography map
                and the distance matrix. Defaults to False.
            map_kwargs (args, optional): additional formatting options that
                will apply to the map axis. Not used yet.
            dist_matrix_kwargs (args, optional): additional formatting options
                that will apply to the distance matrix axis. Mainly used to
                set annot to True or false to improve readability of the
                distance matrix (high cities_count geographies should be set
                to annot=False).

        Returns:
            A tuple of the 2 axis created, so that they can be updated further
            on.
        """

        plt.figure(figsize=(20, 10))

        # Graphical representation of the map of the geography
        ax_map = plt.subplot(121)
        self.draw_map(ax_map, show_names=show_names, kwargs=map_kwargs)

        # Distance matrix.
        ax_dist_matrix = plt.subplot(122)
        self.draw_dist_matrix(ax_dist_matrix, self.dist_matrix,
                              show_names=show_names, kwargs=dist_matrix_kwargs)

        return(ax_map, ax_dist_matrix)

    def show_config(self, configuration, show_names=False, map_kwargs={},
                    dist_matrix_kwargs={}):
        """ Method which will give a representation of a configuration applied

        This method will show the geography map with the configuration
        highlighted and a reordered distance matrix. This function is build on
        top of the simpler `show` method of this class.

        Args:
            configuration (dict of iterables): the configuration to apply.
                The index of the dict should be integers, and the values in
                the iterables should be city indexes.

        Note:
            no city index should be inside multiple pools.
        """
        plt.figure(figsize=(20, 10))

        # defining the color map
        pools_cmap, color_index = ['r', 'g', 'b', 'k', 'c', 'y', 'm'], 0

        # first plot the usual map of geography
        ax_map = plt.subplot(121)
        self.draw_map(ax_map, show_names=show_names, kwargs=map_kwargs)

        # then, draw a distance matrix on a permuted array
        ax_dist_matrix = plt.subplot(122)
        # first of all, construct the permutation sequence
        seq = list()
        for _, pool_content in sorted(configuration.items()):
            seq.extend(pool_content)
        remaining_nums = set(range(self.cities_count))
        for num in seq:
            remaining_nums.remove(num)
        seq.extend(sorted(list(remaining_nums)))
        # get the permuted distance matrix
        permuted_arr = permute_array(self.dist_matrix, seq)
        permuted_names = self.names[seq]
        self.draw_dist_matrix(ax_dist_matrix, permuted_arr,
                              show_names=True, names=permuted_names,
                              kwargs=dist_matrix_kwargs)

        # go through each pool of the configuration
        # cur_dist_matrix_coord is here to know where to draw the squares
        # representing the pools in the distance matrix
        cur_dist_matrix_coord = 0
        for _, pool_content in configuration.items():
            list_content, pool_size = list(pool_content), len(pool_content)

            # set the color for the current pool
            color = pools_cmap[color_index]
            color_index += 1
            # draw a line between every couple of (city i, city j) where
            # j > i (so as to draw each line only once)
            for i in range(pool_size):
                for j in range(i+1, pool_size):
                    coords = self.coordinates[:,
                                              [list_content[i],
                                               list_content[j]]]
                    ax_map.plot(*coords, '-', color=color)
            # highlight the distances for each pool in the distance matrix
            ax_dist_matrix.add_patch(Rectangle((cur_dist_matrix_coord,
                                                cur_dist_matrix_coord),
                                               pool_size, pool_size,
                                               fill=False,
                                               edgecolor=color,
                                               lw=3))
            cur_dist_matrix_coord += pool_size
