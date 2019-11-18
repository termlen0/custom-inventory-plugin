import csv, json



def get_structured_inventory(inventory_file):
    
    #Initialize a dict
    inventory_data = {}
    #Read the CSV and add it to the dictionary
    with open(inventory_file, 'r') as fh:
        csvdict = csv.DictReader(fh)
        for rows in csvdict:
            #import pdb;pdb.set_trace()
            hostname = rows['Device Name']
            inventory_data[hostname] = rows
    return inventory_data



if __name__ == "__main__" :
    inventory_file = "csv_inventory/myinventory.csv"
    myinventory = get_structured_inventory(inventory_file)
    print(json.dumps(myinventory, indent=4))
    
