#!/usr/bin/python3
'''defines matrix multiplying function'''


def matrix_mul(m_a, m_b):
    """Miltiplies two matrices
    Args:
        mattrix m_a and matrix m_b
    Return:
        Returns the resulting matrix after multiplication
    Raises:
        TypeError: raised if passed arguments not a list of lists
            values in lists not integers or floats
            rows in each passed argument not same

        ValueError: raised if passed list is empty
        two matrices cannot be multiplied

    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not (all(type(i) == list for i in m_a)):
        # if isinstance(lst, list) and all(isinstance(i, list) for i in m_a):
        raise TypeError("m_a must be a list of lists")
    if not (all(type(i) == list for i in m_b)):
        # if isinstance(lst, list) and all(isinstance(i, list) for i in m_b):
        raise TypeError("m_b must be a list of lists")

    if not m_a or len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if not m_b or len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    for items in m_a:
        for item in items:
            if not isinstance(item, (int, float)):
                raise TypeError("m_a should only contain integers or floats")
    for items in m_b:
        for item in items:
            if not isinstance(item, (int, float)):
                raise TypeError("m_b should only contain integers or floats")

    for i in range(len(m_a)):
        if len(m_a[i]) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for i in range(len(m_b)):
        if len(m_b[i]) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    rows_A = len(m_a)
    cols_A = len(m_a[0])
    rows_B = len(m_b)
    cols_B = len(m_b[0])

    # Create the result matrix
    # Dimensions would be rows_A x cols_B
    m_c = [[0 for row in range(cols_B)] for col in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                m_c[i][j] += m_a[i][k] * m_b[k][j]
    return m_c
