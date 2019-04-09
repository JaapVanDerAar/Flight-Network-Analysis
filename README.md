# Flight-Network-Analysis
 

This is a project in which the airlines and airports all over the world are analyzed in Python using graph theory
The project is part of the course Computational Thinking at Universiteit Utrecht. The students have dealt with Python code and data about more than 60.000 flights from (and to) every part of the World.

### Prerequisites 
There are several packages that we decided to implement in the program for various purposes. 
They are: 
matplotlib (https://matplotlib.org/) for plots and displaying data and statistics,
pandas (https://pandas.pydata.org/) for organizing and better handling the dataframe, 
numpy (https://www.numpy.org/),
networkx (https://networkx.github.io/) for the creation and manipulations of graphs and networks starting from flights data,
basemap (https://matplotlib.org/basemap/users/installing.html) for visualization purposes, 
(We personally found it easier to install it through anaconda, typing: conda install -c anaconda basemap),
operator (https://docs.python.org/3.0/library/operator.html). 

### GitHub link 
Since this was a group project and we mainly worked in separate locations, we thought it would have been a good idea to implement the use of a version control like GitHub. With this easy tool we managed to mantain the code updated and available everywhere for everyone. 

### The datasets
All the datasets have been downloaded from kaggle.com: a database containing all information about flight and routes (https://www.kaggle.com/open-flights/flight-route-database) and one about airport information (https://www.kaggle.com/open-flights/airports-train-stations-and-ferry-terminals). They have been then merged together in our code. Furthermore we decided to implement a dataframe containing airlines information (https://www.kaggle.com/open-flights/airline-database), like their complete names, for better users' comprehension.

### Basics of graph theory 

Graph theory can be regarded as the study of mathematical objects known as graphs. 

A graph is a structure made of nodes and edges. Nodes are the vertices of the graph and they are interconnected by edges or links. A main distinction can be made between directed graphs, in which edges betwen one node and another have one specific direction and therefore link two points asymetrically. In undirected graphs, when two nodes are linked by an edge, their relation is symmetrical, there is no specific direction in their link. 
It may also be useful to introduce the concept of degree of a node, which is the number of incoming connections. On the other side, the density of a graph is defined by the number of connections between its nodes. The higher the number of edges related to the number of nodes, the more the graph will be. 

Graphs can be used to model and study any structure of a network with connected objects. For example, graph theory is extensively being used in computer science, physics, social science, biology and recently also in neuroscience. The latter is the field where the three of us come from, this gave us the inspiration to look outside field of expertise and discover where and how graph theory could be used in other disciplines. 

### Research questions 
At the beginning of the project we selected some questions that we would have liked to be answered by the end of the project. the main questions are represented here. 
What are the most important/biggest airports in the world? Ranked based on their degree, not number of flights. 
What are the biggest airlines in the world? Based on number of flights.
How do the networks of the airlines compare with each other based on graph metrics?

### Authors 

JAAP VAN DER AAR | KIRSTEN BULSINK | GIULIO CASTEGNARO 


### Acknowledgments

Professor of Computational Thinking course: Anna-Lena Lamprecht 

### License

This project is licensed under the MIT License - see the LICENSE.md file for details
