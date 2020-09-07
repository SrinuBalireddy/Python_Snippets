# Write your code here :-)
my_list =[
	{
		"timestamp":"2020-05-05 00:00:00",
		"history":[
				{"hist-seq-no":1,"CID":233},
				{"hist-seq-no":2,"CID":444}
			],
		"CIty":"blr1",
		"state":"tn1",
		"country":"india1"
	},
	{
		"timestamp":"2020-05-06 00:00:00",
		"history":[
				{"hist-seq-no":1,"CID":555},
				{"hist-seq-no":2,"CID":666}
			],
		"CIty":"blr2",
		"state":"tn2",
		"country":"india2"
	},
	{
		"timestamp":"2020-05-07 00:00:00",
		"history":[
			{"hist-seq-no":1,"CID":888}
			],
		"CIty":"blr3",
		"state":"tn3",
		"country":"india3"
	}
]

new_dict = {}

def parse_dict(my_list):
    """
    Parsing a nested list of dictionaries
    """

    for item in my_list:                   # parses all the items in the list
        for key, values  in item.items():  # parsing each dictionary in the list's corresponding index
            if isinstance(values, list):   # check if the value of the dictionary is a list
                new_dict.setdefault(key,[]).append(values)
                #parse_dict(values)         # call the same function recursively until the list is exhausted
            else:
                new_dict.setdefault(key,[]).append(values) # else print the dictionary key value pairs

parse_dict(my_list)
#print(new_dict)

for i in range(len(new_dict['history'])):
    for j in range(len(new_dict['history'][i])):
        print(new_dict['timestamp'][i],j , new_dict['history'][i][j]['hist-seq-no'], new_dict['history'][i][j]['CID'], new_dict['CIty'][i], new_dict['state'][i], new_dict['country'][i]  ,sep = '         ' )


rows = []
for i in range(len(new_dict['history'])):
    for j in range(len(new_dict['history'][i])):
        rows.append([new_dict['timestamp'][i],j , new_dict['history'][i][j]['hist-seq-no'], new_dict['history'][i][j]['CID'], new_dict['CIty'][i], new_dict['state'][i], new_dict['country'][i]])


import csv
fields = ['timestamp', 'history', 'hist-seq-no', 'CID', 'City', 'State', 'Country']

# writing to csv file
with open('data.csv', 'w') as csvfile:

    # creating csv writer object
    csvwriter = csv.writer(csvfile)

    #writing fileds
    csvwriter.writerow(fields)

    #writing the rows
    csvwriter.writerows(rows)
