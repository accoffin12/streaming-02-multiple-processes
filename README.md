# streaming-02-multiple-processes
## A. C. Coffin
## May 2024
---
## Overview:

This example examines the complexities of regulating database access when handling multiple process on a shared resource concurrently. The process is executed through the creation of an SQLite database and tables, only to have multiple users or programs attempt to interface and modify the database simultaneously. Simulating this process, it enables users to observe the importance of creating signal regulators to prevent task failures. The second example is a simplified model that depicts the process of creating fake data stream utilizing data from a static source - a CSV file.

## Table of Contents:
* [Prerequisites](#Prerequisites)
* [Data_Source](#Data_Source)
* [File_List](#File_List)
* [Task 1. Fork](#Task_1._Fork)
* [Task 2. Clone](#Task_2._Clone)
* [Task 3. Explore](#Task_3._Explore)
* [Task 4. Execute Check Script](#Task_4._Execute_Check_Script)
* [Task 5. Execute Multiple Processes Project Script](#Task_5._Execute_Multiple_Processes_Project_Script)
* [Task 6. Execute Multiple Processes Script with Longer Tasks](#Task_6._Execute_Multiple_Processes_Scrip_with_Longer_Tasks)
* [Task 7. Document Results After Each Run](#Task_7._Document_Results_After_Each_Run)
* [Helpful Information](#Helpful_Information)
    a. [Reading Error Messages](#Reading_Error_Messages)
        - [Database Is Locked Error](#Database_Is_Locked_Error)
        - [Deadlock](#Deadlock)
    b. [Learn More](#Learn_More)

## Prerequisites

1. Git
2. Python 3.7+ (3.11+ preferred)
3. VS Code Editor
4. VS Code Extension: Python (by Microsoft)

## Data_Source:
Annually millions of people utilize the NYC subways, and constant movement of the population around the city makes it an ideal source to create a fake data stream. The Metropolitan Transportation Authority is responsible for all public transport in New York City and collects data in batches by the hour. This batching creates counts for the number of passengers boarding a subway at a specific station. It also provides data concerning payment, geography, time, date and location of moving populations based on stations. MTA Data is commonly utilized when discussing population movements among districts and the role of public transport.

MTA Data is readily available from New York State from their Portal. 

NYC MTA Data for Subways: https://data.ny.gov/Transportation/MTA-Subway-Hourly-Ridership-Beginning-February-202/wujg-7c2s/about_data

### Modifications of Source Data:
The source contained 12 columns, however the MTAHourlyData50R.csv has 13 columns. In this instance the column originally called "transit_time" has been split, the source had both time and date in the same column. This was addressed by separating time and date into two specific columns, adding a 13th column. The data has also been trimmed from its total of 56.3 million rows to 50 rows. Additionally, time was converted to military time for the sake of loading into the database.

## File_List
#### Python:
1. 00_check_core_py
2. about.py
3. multiple_processes.py
4. ProcessStreaming_ACoffin.py

#### Text:
1. 00_report_core.txt
2. about.txt
3. out0.txt
4. out3.txt
5. out8.txt
6. out9.txt

#### Database
1. shared.db

#### Folder ScreenShots
1. Completed MTA Stream Shot
2. M2 Assignment Output Capture
3. M2 Challengeing Part
---

## Task 1. Fork 

Fork this repository ("repo") into **your** GitHub account. 

## Task 2. Clone

Clone **your** new GitHub repo down to the Documents folder on your local machine. 

## Task 3. Explore

Explore your new project repo in VS Code on your local machine.

## Task 4. Execute Check Script

Execute 00_check_core.py to generate useful information.

## Task 5. Execute Multiple Processes Project Script

Execute multiple_processes.py.

Read the output. Read the code. 
Try to figure out what's going on. 

1. What libraries did we import?
1. Where do we set the TASK_DURATION_SECONDS?
1. How many functions are defined? 
1. What are the function names? 
1. In general, what does each function do? 
1. Where does the execution begin? Hint: generally at the end of the file.
1. How many processes do we start?
1. How many records does each process insert?

In this first run, we start 3 processes, each inserting 2 records into a shared database (for a total of 6 records inserted.)

In each case, the process gets a connection to the database, and a cursor to execute SQL statements.
It inserts a record, and exits the database quickly. In general, we're successful and six new records get inserted. 

## Task 6. Execute Multiple Processes Script with Longer Tasks

For the second run, modify the task duration to make each task take 3 seconds. 
Hint: Look for the TODO.
Run the script again. 
With the longer tasks, we now get into trouble - one process will have the database open and be working on it - then when another process tries to do the same, it can't and 
we end up with errors. 

## Task 7. Document Results After Each Run

To clear the terminal, in the terminal window, type clear and hit enter or return. 

`clear`

To document results, clear the terminal, run the script, and paste all of the terminal contents into the output file.

Use out0.txt to document the first run. 

Use out3.txt to document the second run.


-----

## Helpful Information
To get more help on the early tasks, see [streaming-01-getting-started](https://github.com/denisecase/streaming-01-getting-started).

### Reading Error Messages
Python has helpful error messages. Always read error messages carefully, not all messages are the same. 
Many errors will contain where the issue is for an example of this see out3.txt. Not all errors are the same, for example one error message in out0.txt states that the process is successful. Always check the "Error Message" written into the code to assist in identifying the issue. 

#### Database Is Locked Error
Do a web search on the sqlite3 'database is locked' error.
Remember that this demonstrates of multiple processes accessing a database at once. Each of these processes is a separate instance that is attempting to obtain, modify or remove information from the database. Take note of the multiple processes trying to insert data into the same table. Also, examine the creation and drop sections of the code

#### Deadlock
Deadlock is a special kind of locking issue where a process is waiting on a resource or process, that is waiting also. 
Rather than crashing, a system in deadlock may wait indefinitely, with no process able to move forward and make progress.

### Learn More
Check out Wikipedia's article on deadlock and other sources to learn how to prevent and avoid locking issues in concurrent processes. 
To learn about logging and automating terminal readouts as text files reference the following: https://realpython.com/python-logging/
MTA Hourly Dataset: https://data.ny.gov/Transportation/MTA-Subway-Hourly-Ridership-Beginning-February-202/wujg-7c2s/about_data
SQLite Tutorial: https://realpython.com/python-sqlite-sqlalchemy/

