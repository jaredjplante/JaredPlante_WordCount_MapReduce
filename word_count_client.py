import rpyc

conn = rpyc.connect('localhost', 18861)

def map_reduce(filename):
    word_count_list = []
    word_counts = conn.root.map(filename)
    word_count_list.append(word_counts)
    final_output = conn.root.reduce(word_count_list)

    with open('outputfile.txt', 'w') as file_obj:
        for key, value in final_output:
            file_obj.write("\n" + key + " : " + str(value))

if __name__ == '__main__':
    map_reduce("SorcerersStoneWhole.txt")