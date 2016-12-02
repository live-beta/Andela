def find_max_min(list_of_numbers):


    answer_array = []
    max_num = max(list_of_numbers)


    min_num = min(list_of_numbers)

    if min_num == max_num:
        num_of_elements = len(list_of_numbers)
        answer_array.append(num_of_elements)
    else:

        answer_array.append(min_num)
        answer_array.append(max_num)

    return answer_array
