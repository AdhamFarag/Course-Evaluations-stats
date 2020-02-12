# COURSE EVALUATIONS STATS
## Gathering the data
In this project we used `collect data.py` to get the data from the course evaluations provided
> #### How to use `collect data.py`
> Put the file into a folder containing all the course evaluations pdf and run the py file. it will then procceed to collect the statistical data(mean,mode,median,SD) for the first 6 questions, from the files in that folder and add it to a `data.csv` file
> #### Issues faced using this script
> * some parts of data were not collected, but considering it being very little data it can be added manually by re-tracing it to its original file (course evaluation pdf) and and adding the missing values to the csv file using excel
> * some files have 0 respondants to values for those rows will be N/A but we will deal with those rows when cleaning up the data
> * some files have modes that have recuring values (i.e mode can be 1 and 2). we will come to a convention as to what value we will use
