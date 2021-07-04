# BaseCase-3
This is a Python Application that can be used to gather all files of a certain type from any archive.org repository

This application makes it simple to download all files of a certain type in an archive.org repository at once.

## Special Features:
* Even though archive.org uses infinitely scrolling pages, the program can traverse this very quickly and detect when meaningful data has ended
* Specify the file type to download
* Automaticaly formats and organises the files once downloaded

## Usage:
1. Run the Main.py Python file ensuring all dependancies are satisfied
2. Enter the name of the Repository you want to download when prompted, Eg. "commodoremagazines" if you wanted to download all the files within that repository
3. Enter the extension of the files you are looking for, Eg. "pdf" to look for pdf documents
4. Let the program run, due to the large sizes of some of the repositories on the site and the speed of you internet connection, this could take quite a while
5. Once the program has got all the file locations, it will then ask for a location to download them to, it will automaticaly create subfolders within the parent directory to help organise the files
6. This is the most time consuming part of the program as the application has to download each file
7. Once the program has done, it will close and all the files you want should now be on your computer
