work_class_values = ['Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov',
                     'Local-gov', 'State-gov', 'Without-pay', 'Never-worked']

education_values = ['Bachelors', 'Some-college', '11th', 'HS-grad', 'Prof-school', 
                    'Assoc-acdm', 'Assoc-voc', '9th','7th-8th', '12th', 'Masters',
                    '1st-4th', '10th', 'Doctorate', '5th-6th', 'Preschool' ]

marital_status_values = ['Married-civ-spouse', 'Divorced', 'Never-married', 'Separated', 
                         'Widowed', 'Married-spouse-absent', 'Married-AF-spouse']

occupation_values = ['Tech-support', 'Craft-repair', 'Other-service', 'Sales', 
                     'Exec-managerial', 'Prof-specialty', 'Handlers-cleaners',
                     'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing', 
                     'Transport-moving', 'Priv-house-serv', 'Protective-serv', 'Armed-Forces']

relationship_values = ['Wife', 'Own-child', 'Husband', 'Not-in-family', 'Other-relative', 'Unmarried']

race_values = ['White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black']

sex_values = ['Female', 'Male']

native_country_values = ['United-States', 'Cambodia', 'England', 'Puerto-Rico', 
                         'Canada', 'Germany', 'Outlying-US(Guam-USVI-etc)', 
                         'India', 'Japan', 'Greece', 'South', 'China', 'Cuba', 
                         'Iran', 'Honduras', 'Philippines', 'Italy', 'Poland', 
                         'Jamaica', 'Vietnam', 'Mexico', 'Portugal', 'Ireland', 
                         'France', 'Dominican-Republic', 'Laos', 'Ecuador', 
                         'Taiwan', 'Haiti', 'Columbia', 'Hungary', 'Guatemala', 
                         'Nicaragua', 'Scotland', 'Thailand', 'Yugoslavia',
                         'El-Salvador', 'Trinadad&Tobago', 'Peru', 'Hong', 'Holand-Netherlands']


def parse(split_line_array):
    """ each line will be converted to the correct numeric value and will be inserted to a 1xM vector (x vector)
    """
    x = list()
    # Age
    x.append(split_line_array[0])
    # Work-class
    if split_line_array[1] != "?":
        x.append(work_class_values.index(split_line_array[1]))
    else:
        x.append(-1)
    # fnlwgt
    x.append(split_line_array[2])
    # Education
    if split_line_array[3] != "?":
        x.append(education_values.index(split_line_array[3]))
    else:
        x.append(-1)
    # Education-num
    x.append(split_line_array[4])
    # Martial-status
    if split_line_array[5] != "?":
        x.append(marital_status_values.index(split_line_array[5]))
    else:
        x.append(-1)
    # Occupation
    if split_line_array[6] != "?":
        x.append(occupation_values.index(split_line_array[6]))
    else:
        x.append(-1)
    # Relationship
    if split_line_array[7] != "?":
        x.append(relationship_values.index(split_line_array[7]))
    else:
        x.append(-1)
    # Race
    if split_line_array[8] != "?":
        x.append(race_values.index(split_line_array[8]))
    else:
        x.append(-1)
    # Sex
    if split_line_array[9] != "?":
        x.append(sex_values.index(split_line_array[9]))
    else:
        x.append(-1)
    # Capital-gain
    x.append(split_line_array[10])
    # Capital-loss
    x.append(split_line_array[11])
    # Hours-per-week
    x.append(split_line_array[12])
    # Native-country
    if split_line_array[13] != "?":
        x.append(native_country_values.index(split_line_array[13]))
    else:
        x.append(-1)

    y_value = str(split_line_array[14])
    if y_value.__contains__('<=50K'):
        y_value = 0
    else: 
        y_value = 1

    return x, y_value



