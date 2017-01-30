# Notifications about changes in PDB
The task of the program is to monitor weekly changes in PDB (http://www.rcsb.org), mainly modifications of the structures already presented in the database. In case of the detection of the replacing structure with the new version, the program compares both versions, identifies the secondary structure by RNA PRBee (http://rnapdbee.cs.put.poznan.pl/) and generate report.  
The second function is look through entire database and identification of the distinguishing structures.

### Requirements:
To run program you need [Python 3](https://www.python.org), packages listed in [requirements.txt](https://github.com/pw94/PDB-changes-notifications/blob/master/requirements.txt), [Chrome Web Browser](https://www.google.com/chrome/) and [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads).