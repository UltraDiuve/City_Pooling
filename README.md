# City_Pooling
A personal project to optimize city pooling during sports competitions

So far, this project is a Jupyter Notebook and some packages:
- geography
- solver
The notebook is intended to review the "published" works whereas the main classes will be defined in the packages/modules.
The notebook is the "main" file of this project.

# TO DO
- [X] in geography, refactor show and show_config so that axes are created first and then updated in a func
- [ ] in geography, add a legend with pool colors
- [ ] in geography, in the constructor, enable the possibility to normalize the distance matrix with a user defined max value
- [X] in geography, in show_config, have the distance matrix sorted by pool
- [X] in geography, in show_config, try to have the pools highlighted with the pool color
- [ ] in notebook, initialize work on the combinatory analysis
- [ ] in project, initialize work on a solver class
- [ ] in solver, allow to user define a timeout and show the proportion of cominations explored
- [ ] in project, create a saver class that will save state of object to a file (a geography, a solver run, ...)
- [ ] in solver, create a greedy algorithm that switch cities 2 by 2 as soon as it enhances the result
- [ ] in solver, create a greedy algorithm that switch the 2 cities that enhance the result the most
- [ ] in solver, manage cases where pools are not all the same size
- [ ] in solver, for splitable scoring functions, precompute pool score
- [ ] in solver, for splitable scoring functions, enable binary descent
