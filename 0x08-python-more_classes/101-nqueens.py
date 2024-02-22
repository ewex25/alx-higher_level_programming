#!/usr/bin/python3
"""
This module contains an algorithm that resolves the N-Queen puzzle
using backtracking
"""


def isSafe(m_queen, nqueen):
    """ Method that determines if the queens can or can't kill each other
    Args:
        m_queen: array that has the queens positions
        nqueen: queen number
    Returns:
        True: when queens can't kill each other
        False: when some of the queens can kill
    """

    for i in range(nqueen):

        if m_queen[i] == m_queen[nqueen]:
            return False

        if abs(m_queen[i] - m_queen[nqueen]) == abs(i - nqueen):
            return False

    return True


def print_result(m_queen, nqueen):
    """ Method that prints the list with the Queens positions
    Args:
        m_queen: array that has the queens positions
        nqueen: queen number
    """

    res = []

    for i in range(nqueen):
        res.append([i, m_queen[i]])
