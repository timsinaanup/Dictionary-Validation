def stringDict(input_dict, rules):
    try:
        age = int(input_dict['age'])
        string_validation = isinstance(input_dict['name'], str) and rules['name']['min_len'] < len(input_dict['name']) < rules['name']['max_len']
        number_validation = isinstance(age, int) and rules['age']['min'] < age < rules['age']['max']
        boolean_validation = (input_dict['gender'].lower() == "m") == rules['gender']['value']


        if string_validation and number_validation and boolean_validation:
            return True
        else:
            return False
    except ValueError:
        print("Error: Invalid age value")
        return False

min_len = int(input("Min len of string: "))
max_len = int(input("Max len of string: "))
min_num = int(input("Smallest integer: "))
max_num = int(input("Largest integer: "))
gender = input("Enter gender [M|F]: ").lower()
rules = {
    'name': {'min_len': min_len, 'max_len': max_len},
    'age': {'min': min_num, 'max': max_num},
    'gender': {'value': gender == "m"}
}

input_dict = {'name': 'Anup', 'age': '21', 'gender': 'M'}

print(stringDict(input_dict, rules))
