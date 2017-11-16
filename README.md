## Project: Logs Analysis

An internal reporting tool that connects to a news PostgreSQL database and retrieves information on article popularity. Specifically, the program will retrieve information on the top three most popular articles of all time, authors in order of popularity, and days that more than 1% of errors occured when loading news articles. Each question is answered by a single query and is called by a method in the python script queries.py. 

**Installation Requirements**
A virtual machine (VM) is used to query an SQL database server. [Vagrant](https://www.vagrantup.com/downloads.html) and [Virtual Box](https://www.virtualbox.org/wiki/Downloads) should be installed to manage the VM. The VM configuration can be cloned from [Github](https://github.com/udacity/fullstack-nanodegree-vm). To start the virtual machine, from the terminal change to the directory containing the files cloned from github, then change to a directory called vagrant found inside that directory. Run the command `vagrant up` and then the command `vagrant ssh`.

Next download the [sql file](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) that will connect to the database and populate it with data. Save the newsdata.sql file inside the vagrant directory which can be found inside the files cloned from Github. Then run the command `psql -d news -f newsdata.sql`. 

Within the vagrant directory also save queries.py. The program source code can be run in Python 2 versions that can be downloaded from the [Python downloads page](https://www.python.org/downloads/). psycopg2 is the PostgreSQL adapter used in queries.py and can be installed following the instructions found on the [psycopg2 documentation](http://initd.org/psycopg/docs/install.html) if necessary. 

**Usage**
To run the program start up the VM and run the command `python queries.py`. This should output the information on article popularity. An output example is saved in the output.txt file. 

**Credits**
Developer - DemetraSkl 
The project topic and database have been created by Udacity. 

**License**

MIT License

Copyright (c) [2017] [DemetraSkl]
