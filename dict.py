def stringDict(input_dict, rules):
    try:
        input_dict_list =[]
        rules_list = []

        for key,value in input_dict.items():
            input_dict_list.append(value)
        
        for key,value in rules.items():
            for inner_key,inner_value in value.items():
                rules_list.append(inner_value)        
 
        string_validation = isinstance(input_dict_list[0], str) and rules_list[0] <= len(input_dict_list[0]) <= rules_list[1]
        number_validation = isinstance(input_dict_list[1], int) and rules_list[2] <= input_dict_list[1] <= rules_list[3]

        if string_validation and number_validation:
            return True
        else:
            return False
    except:
        return False

rules = {'name': {'min_len': 1, 'max_len': 10}, 'rooms': {'min': 10, 'max': 100}}

input_dict = {'name': 'A Hospital', 'rooms': 15}
print(stringDict(input_dict, rules))
