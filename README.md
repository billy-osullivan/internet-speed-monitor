# internet-speed-monitor
Purpose:
Tests the speed of an internet every 15 minutes. It then stores data in a log and outputs a graph of the previous days results.
Log files are created as needed every day, for a month in total, after which they will overwrite.
The same is true of the graphs, which are saved in .png format.

Requirements:
The script makes use of the following libraries:
numpy         - 	sudo pip install numpy
matplotlib    - 	sudo pip install matplotlib
speedtest-cli -   sudo pip install speedtest-cli

It was tested on Windows 10 and Ubuntu, with python 2.7.13 
Because it creates logfiles and graphs, it should be run with the appropiate privilages.
