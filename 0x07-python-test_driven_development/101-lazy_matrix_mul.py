#!/usr/bin/python3.5
"""

Module is made up of a function that multiplies 2 matrices

"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices

    Arguments:
        m_a: matrix a
        m_b: matrix b

    Returns:
        result of the multiplication


    """

    return (np.matmul(m_a, m_b))
