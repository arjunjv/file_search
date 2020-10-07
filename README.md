#test line 1 in test branch !!

These scripts are intended to get the list of project files and to get to know the
existence of those files in another execution environment. 
Mostly used for project security to confirm all the project files are removed from the developer's environment once the project is closed.

The script "read_file_names.py", reads all the files exited in the provided
directory recursively and create a CSV file with the name provided by user.

Below is the sample of execution of read_file_names.py
```bash
(info_team_scripts) jinka@jinka:~/git/info_team_scripts$ python read_file_names.py
Enter the path for the project files : /home/jinka/git/test
path is : /home/jinka/git/test
Enter the name of file to store the list :test    
(info_team_scripts) jinka@jinka:~/git/info_team_scripts$
```

The script "search_file.py", reads the CSV file given by user to get the
list of files to search and generates the file presence details in a CSV format
named with "username_IPAddress.csv"

Below is the sample of execution
```bash
(info_team_scripts) jinka@jinka:~/git/info_team_scripts$ python search_file.py
Enter the name to get the list to search :test.csv
Enter the path to search: /home/jinka/git/test
Output file is : jinka127.0.1.1.csv
(info_team_scripts) jinka@jinka:~/git/info_team_scripts$
```
