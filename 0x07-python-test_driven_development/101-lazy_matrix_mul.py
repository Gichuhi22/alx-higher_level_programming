#!/usr/bin/python3
""" Defines a function that multiplies two matrices using numpy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.
        Args:
            m_a (list of lists of ints/floats): The first matrix.
            m_b (list of lists of ints/floats): The second matrix.
    """
    m_c = np.dot(m_a, m_b)

    return m_c
