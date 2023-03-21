import rpyc

conn = rpyc.connect('localhost', 18861)

def map_reduce(filename):
    map_data = []
    final_output = []
    group_dict = {}
    with open(filename, 'r') as text_data:
        for line in text_data:
            for word in line.split():
                #map each word and add to a list
                map_list = conn.root.mapper(word)
                map_data.append(map_list)
    #Check if a key is already in the dict, if not, it creates a new empty key in the dict
    #If the key already exists inside the dict, it appends the corresponding value to the original key
    for key, value in map_data:
        if key not in group_dict:
            group_dict[key] = []
        group_dict[key].append(value)
    #Now, a list of values is generated for each key. Time to reduce.
    for key, value in group_dict.items():
        #Get the values list for each key and reduce them
        count_list = list(value)
        reduce_output = conn.root.reduce(key, count_list)
        #Generate the final output once the reduce is done
        final_output.append(reduce_output)

    with open('outputfile.txt', 'w') as file_obj:
        for key, value in final_output:
            file_obj.write("\n" + key + " : " + str(value))

if __name__ == '__main__':
    map_reduce("SorcerersStoneWhole.txt")