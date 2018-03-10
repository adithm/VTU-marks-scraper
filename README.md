# VTU Marks Scraper
Python script that scrapes VTU CBCS results. 
Uses requests to send a post request to results.vtu.ac.in and then extract marks using regular expressions. 
Outputs a csv file containing retrieved results.

### Modifying the Program
The program can be modified to extract marks of other colleges by changing the rangeEnd variable and usn.

Provide the last valid usn number to **rangeEnd** (line 12)
Change the college code in **usn** (line 16) 
