POP = [4e5, 4.2e5, 6e5, 12e5, 8e5, 3.1e5, 2e5, 1e5]
MASS = [14, 12.2, 4]


def normalised_list(value_list):
    """Nomalise abd return the input list values"""
    return [value / sum(value_list) for value in value_list]


print(normalised_list(POP))
print(normalised_list(MASS))
