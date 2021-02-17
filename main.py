

## It looked like a pandas problem to me :)
## I found this english a little unclear "And calculate the % match between the two.(rsid,genotype)"
## I figured the percentage would be "different" depending on which was used a reference so I gave both
## beyond a "ten minute" solution I would I strip the text from the input files of have the files as arguments
## I stripped the text at the top of the tab delimited files by hand



import numpy as np
import pandas as pd

# I stripped the text bit at the top from 2 of the downloaded files and saved them in the directory
inputOne = 'genome_Daniel_Munro_Full_20141013190727.txt';
inputTwo = 'genome_KathleenAlice_Grasso_v5_Full_20200422160930.txt'
inputThree = 'genome_v5_Full_20180602051728.txt'

# read the text file into pandas
dataOne = pd.read_csv(inputOne, sep='\t', lineterminator='\r', dtype={"rsid": "string", "chromosome": "string", "position": "string" , "genotype" : "string"})
#print(dataOne.head())
#print(dataOne.columns.values)

# remove columns we are not comparing
dataOne.drop(columns=['chromosome', 'position'])

#get number of rows
indexOne = dataOne.index
numberOfRowsOne = len(indexOne)
print("number of rows in data set one is: ", str(numberOfRowsOne))

# read in another data set
dataTwo = pd.read_csv(inputTwo, sep='\t', lineterminator='\r', dtype={"rsid": "string", "chromosome": "string", "position": "string" , "genotype" : "string"})
#print(dataTwo.head())
#print(dataOne.columns.values)

# read in the 3rd data set
dataThree = pd.read_csv(inputThree, sep='\t', lineterminator='\r', dtype={"rsid": "string", "chromosome": "string", "position": "string" , "genotype" : "string"})
#print(dataTwo.head())
#print(dataOne.columns.values)


# get number of rows of 2nd data set
indexTwo = dataTwo.index
numberOfRowsTwo = len(indexTwo)
print("number of rows in data set two is: ", str(numberOfRowsTwo))

# remove unneeded columns from 2nd data set
dataTwo.drop(columns=['chromosome', 'position'])

# count number of rows in 3rd data set
indexThree = dataThree.index
numberOfRowsThree = len(indexThree)
print("number of rows in data set three is: ", str(numberOfRowsThree))

# remove unneeded rows from 3rd data set
dataThree.drop(columns=['chromosome', 'position'])


# calculate which rows occur in BOTH data sets one and two
inBoth = dataOne.merge(dataTwo, how = 'inner' ,indicator=False)

# print number of rows in BOTH data sets and store
indexBoth = inBoth.index
numberOfRowsBoth = len(indexBoth)
print("number of rows in both data sets one and two( same rsid and genotype ) is: ", str(numberOfRowsBoth))

# print "percentage" of shared rows with respect to each data set
print("percent match in first is: " + str(100.0*numberOfRowsBoth/numberOfRowsOne)+ " %")
print("percent match in second is: " + str(100.0*numberOfRowsBoth/numberOfRowsTwo)+ " %")

# calculate which rows occur in BOTH data sets two and three
inBothTwoThree = dataTwo.merge(dataThree, how = 'inner' ,indicator=False)
indexBothTwoThree = inBothTwoThree.index
numberOfRowsBothTwoThree = len(indexBothTwoThree)

# print "percentage" of shared rows with respect to each data set
print("number of rows in both data sets two and three( same rsid and genotype ) is: ", str(numberOfRowsBothTwoThree))
print("percent match in second is: " + str(100.0*numberOfRowsBothTwoThree/numberOfRowsTwo)+ " %")
print("percent match in third is: " + str(100.0*numberOfRowsBothTwoThree/numberOfRowsThree)+ " %")













