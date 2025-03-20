# Bookmark Analyzer
#### Video Demo: [ADD VIDEO]

## Introduction
I'm a fan and frequent user of the [OneTab](https://www.one-tab.com/) browser extension. This browser extension allows you to easily convert your open tabs to a list of links. I have developed a habit of saving a large number of links/bookmarks with this extension. Some of the links are links that I use frequently and want to keep for easy access. Some links are to articles or blog posts that I want to read later. I don't always take the time to review links I have saved in the past, so I thought it would be interesting to have a way to clean up the links. I realized that this task is a data problem that I could approach with a Python script, so for my final project in the CS50P course, I decided to create this bookmark analyzer that I can use as a starting point to wrangle my bookmarks.

The current iteration is a command-line program that allows the user to specify a TXT or HTML file to analyze as well as the filename where the results will be written. Currently, the program provides a count of the number of links in the given file, and then asks the user to confirm if they would like to remove duplicate links. If the user chooses to remove duplicate links, the program gives the number of duplicate links found. Finally, the program writes the updated list of links, sorted alphabetically, to the requested filename, so the user can open the new file and review.

The project also includes a test_project.py file that contains tests for the custom functions I created. These tests can be run with the command `pytest test_project.py`.

## Usage
The user should provide two command-line arguments:
    
1. The name of an existing TXT or HTML bookmarks export file to read as input
2. The name of a new TXT file to write as output

## Code overview
The program has a main function that welcomes the user with an illustration from the `cowsay` library. After checking for usage errors, the program assigns the filenames given as command-line arguments to variables, and returns an error message if there is a `ValueError` or a `FileNotFound` error. Next, the program calls custom functions to sort the list alphabetically, remove duplicates if requested, and write the new list to the given filename. 

I started out with support for TXT files, since the OneTab extension has an export tool that provides a plain text list of URLs, but I also wanted to support bookmarks I have saved using the Chrome browser, which provides an HTML export file, so I added an additional custom function to convert an HTML file to a simple list of links in a TXT file, which can then be passed to the other functions I created to alphabeticize links and remove duplicates. I used the Beautiful Soup library to extract URLs from the HTML file. I also used the built-in `sys` module in order to access the command-line arguments passed to the script. 

## Future development
I enjoyed working on this project and I think it has the potential to be useful to others. In the future, I may work on a web version of this program that also allows users to tag and categorize their links. I am interested in ideas related to knowledge management and digital gardens, and I think this project could align well with those interests. Let me know if you have ideas for features you'd like to see!