#ProcessData.py
#Name: Gareth Moodley
#Date: Oct 30 2025
#Assignment: Lab 8

import random

def main():

  abbrev = {"Freshman": "FR", "Sophomore": "SO", "Junior": "JR", "Senior": "SR"}
  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  parsed_data = []
  #Process each line of the input file and output to the CSV file
  for line in inFile:
    l = line.split(" ")
    parsed_data.append([l[1], l[0], l[3], l[6][:3].replace("\n", "")+"-"+abbrev[l[5]]])

  #print(parsed_data)
  outFile.write("Last Name,First Name,UserID,Major-Year\n")
  for p in parsed_data:
    outFile.write(','.join(p)+"\n")
  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

if __name__ == '__main__':
  main()
