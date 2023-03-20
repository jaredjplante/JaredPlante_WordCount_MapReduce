def map(filename):
    word_count_list = {}
    with open(filename, 'r') as file_obj:
        for line in file_obj:
            for word in line.split():
                if word in word_count_list:
                    word_count_list[word] += 1
                else:
                    word_count_list[word] = 1
    return word_count_list


def reduce(count_list):
    final_output = {}
    for counts in count_list:
        for word, count in counts.items():
            if word in final_output:
                final_output[word] += count
            else:
                final_output[word] = count
    return final_output.items()
