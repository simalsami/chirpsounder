2022-2023 Nisha Yadav

# chirpsounder


**Web-Based Application for the Visualization and Analysis of Ionogram Data Observed by​ GNU Chirpsounder2**
**Goal: **
The focus of the system is to develop a web-based application for the visualization and analysis of data observed by GNU Chirpsounder2. GNU Chirpsounder2 can output data in HDF5 (Hierarchical Data Format version 5) format, which is a flexible and efficient file format for storing large scientific datasets. Each day many ionograms are received from different transmitters placed around the world. The unidentified data is in the form of LFM (Linear frequency modulation) files and ionograms are first classified on the basis of two parameters: chirp-rate and distance of the transmitter from the receiver. Using these two parameters, the application provides methods for sorting, analyzing, and visualizing the collected ionograms to conduct scientific studies or make observations useful for radio communications operations or atmospheric scientists.

# Prerequisites:

1. Python Version 3.9.13 with Django (must have knowledge).
2. TML5, CSS3, Bootstrap 5 (Some Knowledge).
3. PostgreSql Database (Some Knowledge).
4. Data [mandate format hdf5].
# Installation Instructions:
Install Python and Django.
Set up PostgreSql database.
Clone project from github: https://github.com/Nisha-Yadav-1/chirpsounder.git


**Steps**
Attach the drive to the computer.
Open the terminal
run git clone https://github.com/Nisha-Yadav-1/chirpsounder.git
run cd chirpsounder
Open project in any IDE. 
run project
Navigate to http://127.0.0.1:8000/
The home screen will look like this, click on add transmitter button, provide all the information, and hit submit.
Go to the admin page, click on add receiver button, provide all the information, and hit submit.
Again, go to the Home page and, click on the “filtered ionograms” button, it will filter the ionograms.


**Output:**
Filtered Data
Unfiltered Data 
Sorted and organized data in tables.
Many more functionalities.




Warning!!!- It can still be usable as a local interface, but not on the public internet.
