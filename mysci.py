# Read the data file
filename = "data/wxobs20170821.txt" #path and filename to data

with open(filename, 'r') as datafile:
   data = datafile.read()

datafile.close() 

NOTES
#datafile = open(filename, 'r') #to open and read 'r' the data file
#open and setting as datafile
#with data file open, I'd like to read it and save it to variable data
#with open(filename, 'r') as datafile: 

#   data = datafile.read() 

#read only few lines of the data to see what we have
#print(datafile.readline())  #printing out first line
#print(datafile.readline())  #second line 

#read the entire file
#data = datafile.read()

# DEBUG section of the script
#print(data)   #as an object
#print(type(data)) #type of data

