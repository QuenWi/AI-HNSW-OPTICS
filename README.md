# AI HNSW OPTICS
Using a HNSW to approximate an OPTICS clustering

This programm is used to showcase that an HNSW can be used for approximating an OPTICS cluster.

It only works for 2D datasets, but in principle it would work for any dimensional datasets.

When you run the script, than this will happen:
<br>1st: It shows the 2D plot
<br>2nd: The program will approximate the minPts*3 nearest neighbors of each object by using a HNSW. 
<br>3rd: From the approximated nearest neighbors it will create a reachability plot.
<br>4th: It shows the user the plot.
<br>5th: The user has to enter a maximum reachability distance for creating clusters.
<br>6th: Than the programm will create the cluster.
<br>7th: A plot of the 2D dataset with the clusters will be shown.

You just have to call the following method:
HNSW_OPTICS.hnsw_optics(dataset, minPts, epsilonDistance)

There also is an example run at the file:
HNSW_Example_Run.py

To run the program, it is required:
-pip install hnswlib
(For this command you need the .Net SDK and the c++ builders tool)

