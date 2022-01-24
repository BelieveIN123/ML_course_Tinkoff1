import numpy as np
from typing import Optional, Union, Tuple


def euclidean_distance(x: np.array, y: np.array) -> float:
    """
    Calculate euclidean distance between points x and y
    Args:
        x, y: two points in Euclidean n-space
    Returns:
        Length of the line segment connecting given points
    """
    return (np.sum((x - y)**2))**(1/2)
    pass


def euclidean_similarity(x: np.array, y: np.array) -> float:
    """
    Calculate euclidean similarity between points x and y
    Args:
        x, y: two points in Euclidean n-space
    Returns:
        Similarity between points x and y
    """
    # drop 0
    count_obj = x.shape(0)
    not_zero_x = np.where(np.x != 0)
    x = x[not_zero_x]
    y = y[not_zero_x]
    # оставшиеся не оцененные фильмы
    not_zero_y = np.where(np.y != 0)
    x = x[not_zero_y]
    y = y[not_zero_y]

    corr = 1/(1 - euclidean_distance(x, y))

    if corr != corr:
        return 0 
    else:
        return corr 
    # if x.shape < 1:
    #     return 0
    # print(x, y)

    pass


def pearson_similarity(x: np.array, y: np.array) -> float:
    """
    Calculate a Pearson correlation coefficient given 1-D data arrays x and y
    Args:
        x, y: two points in n-space
    Returns:
        Pearson correlation between x and y
    """
    x_mean = np.mean(x[x != 0])
    y_mean = np.mean(y[y != 0])

    if x_mean != x_mean:
        x_mean = 3
    if y_mean != y_mean:
        y_mean = 3
    print(x_mean, y_mean)

    # drop 0
    count_obj = x.shape(0)
    not_zero_x = np.where(x != 0)
    x = x[not_zero_x]
    y = y[not_zero_x]
    # оставшиеся не оцененные фильмы
    not_zero_y = np.where(y != 0)
    x = x[not_zero_y]
    y = y[not_zero_y]

    if x.shape < 1:
        return 0



    print(x, y)
    corr = np.sum((x - x_mean)@(y - y_mean)) / (np.sum((x - x_mean)**2) * np.sum((y - y_mean)**2))**(1/2)
    if corr != corr:
        return 0
    else:
        return corr
    
    pass


def apk(actual: np.array, predicted: np.array, k: int = 10) -> float:
    """
    Compute the average precision at k
    Args:
        actual: a list of elements that are to be predicted (order doesn't matter)
        predicted: a list of predicted elements (order does matter)
        k: the maximum number of predicted elements
    Returns:
        The average precision at k over the input lists
    """



    act_set = set(actual.flatten())
    pred_set = set(predicted[:k].flatten())
    result = len(act_set & pred_set) / float(k)
    return result



def mapk(actual: np.array, predicted: np.array, k: int = 10) -> float:
    """
    Compute the mean average precision at k
    Args:
        actual: a list of lists of elements that are to be predicted
        predicted: a list of lists of predicted elements
        k: the maximum number of predicted elements
    Returns:
        The mean average precision at k over the input lists
    """
    act_set = set(actual.flatten())
    pred_set = set(predicted[:k].flatten())
    result = len(act_set & pred_set) / float(len(act_set))
    return result
