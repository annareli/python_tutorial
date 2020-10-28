# Create a column dictionary - column names and column indices to read
columns = {'date':0, 'time':1, 'tempout':2}

# Data types for each column (only if non-string)
types ={'tempout': float}

# Initialize my data variable, empty list[], dictionary{}
data = {}
for column in columns:
    data[column] = []

# Read the data file
filename = "data/wxobs20170821.txt" #path and filename to data

with open(filename, 'r') as datafile:
    # read the first three lines (header of file)
    for _ in range(3):
        datafile.readline()
    
    # read and parse the rest of the file
    for line in datafile:
        split_line = line.split()
        for column in columns:
            i = columns[column]
            t = types.get(column,str)
            value = t(split_line[i])
            data[column].append(value)


datafile.close() 








##NOTES
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

#DEBUG
#for datum in data:
#    print(datum)
#for datum in data[:10:2]:
#    print(datum)
#print(data[8][4])
#print(data[8][:5])
#print(data[8][::2])

#print(data[5:8][0])
#print(data[5])


