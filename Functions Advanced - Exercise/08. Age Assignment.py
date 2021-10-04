def age_assignment(*args, **kwargs):
    dict = {}
    for arg in args:
        letter = arg[0]
        dict[arg] = kwargs[letter]
    return dict


print(age_assignment("Peter", "George", G=26, P=19))