# Create a column dictionary - column names and column indices to read
columns = {'date':0, 'time':1, 'tempout':2, 'windspeed':7, 'windchill':12}

# Data types for each column (only if non-string)
types ={'tempout': float, 'windspeed': float, 'windchill':float}

# Initialize my data variable, empty list[], dictionary{}
data = {}
for column in columns:
    data[column] = []

# Read the data file
filename = "data/wxobs20170821.txt" #path and filename to data

with open(filename, 'r') as datafile:
    # read the first three lines (header of file)
    for _ in range(3):
        headerline = datafile.readline()
#        print(headerline)

    # read and parse the rest of the file
    for line in datafile:
        split_line = line.split()
        for column in columns:
            i = columns[column]
            t = types.get(column,str)
            value = t(split_line[i])
            data[column].append(value)

# Compute the wind chill temperature
# Function is self-contained, no global variables 
def compute_windchill(t, v):
    a = 35.74
    b = 0.6215
    c = 35.75
    d = 0.4275
    
    v16 = v ** 0.16
    
    wci = a + (b * t) - (c * v16) + (d * t * v16)
    return wci 

# Running the function to compute wci 
windchill = []
for temp, windspeed in zip(data['tempout'], data['windspeed']):
    windchill.append(compute_windchill(temp, windspeed))

#  DEBUG 
for wc_data, wc_comp in zip(data['windchill'], windchill):
    print(f'{wc_data:.5f} {wc_comp:.5f} {wc_data - wc_comp:.5f}')


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


