import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def dist(city1, city2):
    """ function that returns the euclidian distance betweend 2 cities in the plane (each city being 2 coordinates) """
    return( ((city1[0]-city2[0])**2. + (city1[1]-city2[1])**2.)**0.5 )

class geography():
    """ Class defining a geography, with cities coordinates, distance matrix, and helper functions.
    
    This class implements a geography with a list of named cities with their associated coordinates in a plane.
    Helper functions enable to :
    - give a visual representation of that geography
    - give a visual representation of the distance matrix
    - give a visual representation of a configuration, a configuration being the repartition of some or all cities in pools
    - compute a cost of a configuration, requiring to apply a cost function on the configuration
    
    Attributes:
        cities_count (int): Count of cities in the geography.
        coordinates (numpy array of shape (cities_count, 2)): an iterable of (x, y) coordinates of length cities_count.
        cities_names (dict of string): a dictionnary of strings, indexed by integers.
        dist_matrix (numpy array of shape (cities_count, cities_count)): the distance matrix of the geography.
    
    """
    def init_dist_matrix(self,func=dist):
        """ Method which will initialize the distance matrix
        
        Args:
            func (function): a distance function which returns a positive number from a couple of cities. If unspecified,
            will use the euclidean distance in the plane.

        Returns:
            Nothing.
        """
        self.dist_matrix = np.array([[dist(self.coordinates[i], self.coordinates[j]) for j in range(self.cities_count)] 
                                     for i in range(self.cities_count)])
            
    def __init__(self, cities_count, cities_coordinates=None, cities_names=None):
        """ Constructor method of geography
        
        This method will construct a geography from parameters and initialize its distance matrix
        
        Args:
            cities_count (int): the count of cities in the geography/
            cities_coordinates (optional, numpy array of shape (cities_count, cities_count)): the coordinates of the cities. If
            omitted, will randomly place the cities in the plane.
            cities_names (optional, dict of strings): the names of the cities. If omitted will default to a dict of cities with
            the names 'City0', 'City1', ...
        
        Returns: Nothing.
            """
        
        self.cities_count = cities_count
        if cities_coordinates == None:
            self.coordinates = np.random.rand(cities_count, 2)
        if cities_names == None:
            self.names = {i: ("City " + str(i)) for i in range(cities_count) }
        else:
            self.names = cities_names
        self.init_dist_matrix()

    
    def show(self, show_names=False, **kwargs):
        """ Method to show a graphical representation of the geography without a configuration applied
        
        This method will draw the geography in a plane, and give a view of the distance matrix in the form of a seaborn heatmap.
        
        Args:
            show_names (bool, optional): whether or not to show the names of the cities in the representation, both in the 
            geography map and the distance matrix. Defaults to False.
            **kwargs (args, optional): additional formatting options that will apply to the distance matrix heatmap. Mainly used 
            to set annot to True or false to improve readability of the distance matrix (high cities_count geographies should be 
            set to annot=False).
        
        Returns:
            Returns a tuple of the 2 axes created, so that they can be updated further on.
        """
        plt.figure(figsize=(20,10))
        
        # Graphical representation of the map of the geography
        ax_map = plt.subplot(121)
        plt.scatter(self.coordinates[:,0], self.coordinates[:,1])
        if show_names:
            for i in range(self.cities_count):
                plt.annotate(self.names[i], self.coordinates[i])
        plt.tick_params(
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
        ax_map.set_title('Map of Geography\n', fontsize=24)
        
        # Distance matrix.
        ax_dist_matrix = plt.subplot(122)
        yticklabels = self.names.values() if show_names else False
        xticklabels = self.names.values() if show_names else False
        sns.heatmap(self.dist_matrix, 
                    cmap="Blues", 
                    cbar=False, 
                    xticklabels=xticklabels, 
                    yticklabels=yticklabels,  
                    **kwargs)
        ax_dist_matrix.set_title('Distance Matrix\n', fontsize=24)
        return(ax_map, ax_dist_matrix)
    
    def show_config(self, configuration, show_names=False, **kwargs):
        """ Method which will give a representation of a configuration being applied to the geography
        
        This method will show the geography map with the configuration highlighted and a reordered distance matrix. This 
        function is build on top of the simpler `show` method of this class.
        
        Args:
            configuration (dict of sets): the configuration to apply. The index of the dict should be integers, and the sets in
            it should be city indexes.
            
        Note:
            no city index should be inside multiple pools.
        """
        # first plot the usual and get the axes so as to update them 
        ax_map, ax_dist_matrix = self.show(show_names=show_names, **kwargs)
        
        # defining the color map
        pools_cmap, color_index = ['r','g','b','k','c','y','m'], 0
        
        # go through each pool of the configuration
        for pool, pool_content in configuration.items():
            list_content, pool_size = list(pool_content), len(pool_content)
            # set the color for the current pool
            color = pools_cmap[color_index]
            color_index += 1
            # draw a line between every couple of (city i, city j) where j > i (so as to draw each line only once)
            for i in range(pool_size):
                for j in range(i+1, pool_size):
                    x = [self.coordinates[list_content[i]][0], self.coordinates[list_content[j]][0]]
                    y = [self.coordinates[list_content[i]][1], self.coordinates[list_content[j]][1]]
                    ax_map.plot(x, y, '-', color=color)
