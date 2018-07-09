"""
Main python file for the sssdevops example
"""

#import statements go here


def mean(num_list):
    """
    Calculates the mean of a list of numbers

    Parameters
    ---------
    num_list : list
    List of numbers of calculate the average of 

    Returns
    -------
    the average 
    """
    a = 0
    for i in num_list:
        a += i

    return a / len(num_list)
