# point_plot
This program prepared for plotting the points whose coordinates are given on the screen and combining the arcs, lines between them in the desired way.
This program plot points, point numbers(IDs) and lines(arcs) given in the file structures as given. One single project name should be read from the user following the file extensions automatically added and read by the program. Also, a pre-defined scale is not required a square should be a square(not a rectangle) and a circle should be circle(not an ellipse) on the screen. X axis shows the north direction in Turkey!
Only pre-built libraries in Python 3.x used.

The Structure of The Coordinate Data Set(sample.xyz)
-----179-----210.52-----322.23
-----180-----204.70-----550.82
-----181-----433.50-----545.01
-----182-----427.48-----314.48
...
Where every (-) indicates spaces in the file. Second number is X coordinate. Third number is Y coordinate.

The Structure of The Arc Data Set(sample.nno)
-----179-----180
-----180-----181
-----180-----203
-----181-----222
...

Where every (-) indicates spaces in the file. Every line indicates a line(arc) composed by thow nodes given in xyz file.
