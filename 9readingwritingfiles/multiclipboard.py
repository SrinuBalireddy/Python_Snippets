# Write your code here :-)


import pyperclip,sys

capitals = {'AP':'Vizag','Telangana':'Hyd','TN':'Chennai','kerala':'cochin',
            'Karnataka':'Benguluru','Maharasthra':'Mumbai','WB':'Kolkatha'}

if len(sys.argv) <2 :
    print('Please provide the input argument')
    sys.exit()
else:
    parameter = sys.argv[1]

if parameter in capitals:
    output = capitals[parameter]
    pyperclip.copy(output)
    print('Capital city of the state '+ parameter +' has been copied to clipboard')
else:
    print('There is no result for '+ parameter)
