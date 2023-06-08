2022-2023 Nisha Yadav

# Chirpsounder


**Web-Based Application for the Visualization and Analysis of Ionogram Data Observed by​ GNU Chirpsounder2**
**Goal: **
The focus of the system is to develop a web-based application for the visualization and analysis of data observed by GNU Chirpsounder2. GNU Chirpsounder2 can output data in HDF5 (Hierarchical Data Format version 5) format, which is a flexible and efficient file format for storing large scientific datasets. Each day many ionograms are received from different transmitters placed around the world. The unidentified data is in the form of LFM (Linear frequency modulation) files and ionograms are first classified on the basis of two parameters: chirp-rate and distance of the transmitter from the receiver. Using these two parameters, the application provides methods for sorting, analyzing, and visualizing the collected ionograms to conduct scientific studies or make observations useful for radio communications operations or atmospheric scientists.

## Prerequisites:

1. Python Version 3.9.13 with Django (must have knowledge).
2. TML5, CSS3, Bootstrap 5 (Some Knowledge).
3. PostgreSql Database (Some Knowledge).
4. Data [mandate format hdf5].
## Installation Instructions:
1. Install Python and Django.
2. Set up PostgreSql database.
3. Clone project from github: https://github.com/Nisha-Yadav-1/chirpsounder.git
4. Steps to run application
  1. Attach the drive to the computer.
  2. Open the terminal
  3. Run git clone https://github.com/Nisha-Yadav-1/chirpsounder.git
  4. run cd chirpsounder
  5. Open project in any IDE. 
  6. run project
  7. Navigate to http://127.0.0.1:8000/
5. The home screen will look like this, click on add transmitter button, provide all the information, and hit submit.
6. Go to the admin page, click on add receiver button, provide all the information, and hit submit.
7. Again, go to the Home page and, click on the “filtered ionograms” button, it will filter the ionograms.


## Output:
1. Filtered Data
2. Unfiltered Data 
3. Sorted and organized data in tables.
4. Many more functionalities.




Warning!!!- It can still be usable as a local interface, but not on the public internet.
