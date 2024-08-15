import csv

def readFromCSV():
  with open('options.csv', 'r') as read_obj: # read csv file as a list of lists
    csv_reader = csv.reader(read_obj) # pass the file object to reader() to get the reader object
    list_of_rows = list(csv_reader)[1:] # Pass reader object to list() to get a list of lists
  
  return list_of_rows