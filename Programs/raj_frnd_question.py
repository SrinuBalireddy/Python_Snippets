#! python 3.8

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

def parse_dict1(my_list):
    """
    Parsing a nested list of dictionaries
    """

    for index, item in enumerate(my_list):                   # parses all the items in the list
        for key, values  in item.items():  # parsing each dictionary in the list's corresponding index

            print(f'{key} : {index}')

            if isinstance(values, list):   # check if the value of the dictionary is a list
                #print(f'{key} : {index}')
                parse_dict1(values)         # call the same function recursively until the list is exhausted
            else:

                print(f'{key} : {values}') # else print the dictionary key value pairs

parse_dict1(my_list)

def parse_dict(my_list):
    """
    Parsing a nested list of dictionaries
    """

    for index, item in enumerate(my_list):                   # parses all the items in the list
        for key, values  in item.items():  # parsing each dictionary in the list's corresponding index
            if isinstance(values, list):   # check if the value of the dictionary is a list
                for inner_index, inner_item in enumerate(values):
                    print(f'{key} : {inner_index}')
                    for inner_key, inner_values  in inner_item.items():
                        print(f'{inner_key} : {inner_values}')

            else:
                print(f'{key} : {values}') # else print the dictionary key value pairs

"""
import csv

rows =[]

fields = ['timestamp', 'history', 'hist-seq-no', 'CID', 'City', 'State', 'Country']
with open('file.csv', 'w') as csvfile:

    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    for index, item in enumerate(my_list):                   # parses all the items in the list
        for key, values  in item.items():                    # parsing each dictionary in the list's corresponding index
            if isinstance(values, list):                     # check if the value of the dictionary is a list
                for inner_index, inner_item in enumerate(values):
                    print(f'{key} : {inner_index}')

                    for inner_key, inner_values  in inner_item.items():
                        print(f'{inner_key} : {inner_values}')

            else:
                print(f'{key} : {values}') # else print the dictionary key value pairs
"""
