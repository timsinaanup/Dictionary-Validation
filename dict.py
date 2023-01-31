def stringDict(input_dict , rules):
    try:
        input_dict['age'] = int(input_dict['age'])
        string_validation = isinstance(input_dict['name'],str) and rules['name']['min_len'] < len(input_dict['name']) < rules['name']['max_len']
        number_validation = isinstance(input_dict['age'],int) and rules['age']['min'] < int(input_dict['age']) < rules['age']['max']
        boolean_validation = isinstance(input_dict['gender'],bool) and rules['gender']['value'] == input_dict['gender'] 

        if string_validation and number_validation and boolean_validation :
            return True
        else:
            return False
    except:
        return False


rules = {
    'name': {'min_len': 2, 'max_len': 10},
    'age': {'min': 18, 'max': 99},
    'gender': {'value': True }
}

name = input("Enter name : ")
age = input('Enter Age : ')
gender = input("Enter Gender : ")
gender = True if gender == "M" else False

input_dict = {'name': name, 'age': age, 'gender' : gender}

print(stringDict(input_dict , rules))
