# IMSRG-ISB
This is the readme for the ~/Documents/Theory/Paper directory which includes all of the important information
for the paper that I am writing. In this directories there are several directories and files outlined below.
The general setup of this is to make it easy to reference what files are for what, and to make them easy to
wipe and re-create if needed.

Written by M.S. Martin, 2019-2020

Data Files
Any file which begins with an A is a data file. These files contain the data for the given mass. In these
there are further subdirectories for the reference states used including an emax indicator. Inside these
are the .int, .sp, and .op files as well as any files produced as a result of running shell, nutbar, etc.

copy_imsrgfiles.py
This is a python script which copies the .int, .sp, and .op files from the output of the imsrg code into
the correct directories in the Data files. This also wipes the data files clean, so it is a good place to
go if you want to start over. The file paths are specific for the current setup of my cronos account.

make_inputfiles.py
This is a python script which creates .ans and .input files for use in shell and nutbar. This script also
puts them in the correct directory and moves the runshell.sh file into all directories.

do_calculations.py
This is a script which goes into each directory and runs the runshell script in that directory.

runshell.sh
This is a bash script which runs shell and nutbar with the given input parameters.


In order to use this directory, run in order:
python copy_imsrgfiles.py
python make_inputfiles.py
python do_calculations.py
