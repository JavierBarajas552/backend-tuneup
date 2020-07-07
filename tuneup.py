#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment

Use the timeit and cProfile libraries to find bad code.
"""

__author__ = "???"

import cProfile
import pstats
import functools
import timeit
from pstats import SortKey


def profile(func):
    """A cProfile decorator function that can be used to
    measure performance.
    """
    # Be sure to review the lesson material on decorators.
    # You need to understand how they are constructed and used.
    def wrapper(*args, **kwargs):
        prof = cProfile.Profile()
        prof.enable()
        ret = prof.runcall(func, *args, **kwargs)
        prof.disable()
        p = pstats.Stats(prof)
        p.strip_dirs().sort_stats(SortKey.CUMULATIVE).print_stats()
        return ret
    return wrapper


def read_movies(src):
    """Returns a list of movie titles."""
    #print(f'Reading file: {src}')
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """Returns True if title is within movies list."""
    # for movie in movies:
    #    if movie.lower() == title.lower():
    if movies:
        if title == movies[-1]:
            return True
    return False


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list."""
    movies = read_movies(src)
    movies.sort()
    duplicates = []
    while movies:
        movie = movies.pop()
        if is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates


def timeit_helper():
    """Part A: Obtain some profiling measurements using timeit."""
    # YOUR CODE GOES HERE
    t = timeit.Timer(stmt=main)
    res = t.repeat(repeat=7, number=5)
    res.sort()
    print('Best time across 7 repeats of 5 runs ' + str(res[0]) + ' sec')
    pass


def main():
    """Computes a list of duplicate movie entries."""
    result = find_duplicate_movies('movies.txt')
    print(f'Found {len(result)} duplicate movies:')
    print('\n'.join(result))


timeit_helper()


if __name__ == '__main__':
    main()
