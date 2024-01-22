#!/usr/bin/python3
def no_c(my_string):

    new_string = ''.join([ich for ich in my_string if ich.lower() != 'c'])
    return (new_string)
