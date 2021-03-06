# Notifications about changes in PDB
The task of the program is to monitor weekly changes in PDB (http://www.rcsb.org), mainly modifications of the structures already presented in the database. In case of the detection of the replacing structure with the new version, the program compares both versions, identifies the secondary structure by RNA PDBee (http://rnapdbee.cs.put.poznan.pl/) and generate report.  
The second function is look through entire database and identification of the distinguishing structures.

### Requirements:
To run program you need [Python 3](https://www.python.org), packages listed in [requirements.txt](https://github.com/pw94/PDB-changes-notifications/blob/master/requirements.txt), [Chrome Web Browser](https://www.google.com/chrome/) and [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads).

### Run:
To run a program you only have to type: 

```python main.py```

There is plenty of available options which you can pass to access other modes. You can list all of them by typing:
 
 ```python main.py --help```
 
 Output:
 
 ```
 usage: main.py [-h] [-a] [-l] [-d]
    
    optional arguments:
      -h, --help         show this help message and exit
      -a, --all          process entire list of obsolete structures
      -l, --list         print only IDs without secondary structure
      -d, --differences  print information only about structures which secondary
                         structure is not identical
 ```