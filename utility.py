#function to swap keys and values of a dictionary
def invert_dictionary(dictionary):
  inv_dict = {}
  for el in dictionary.items():
    inv_dict.update({el[1]:el[0]})

  return inv_dict
