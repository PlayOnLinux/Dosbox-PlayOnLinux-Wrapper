#!/usr/bin/python

import sys, os

"""
    This tool transform a long file name into a short one
"""
def _contains_forbidden_chars(name):
    return ' ' in name

def _filter(name):
    return name.replace(' ', '')

def _shortize_component(path_component):
    filename_component = path_component.split(".")
    filename = filename_component[0]
    extension = filename_component[-1] if len(filename_component) > 1 else ''

    is_long_filename = len(filename_component) > 2 or \
        len(filename) > 8 or \
        len(extension) > 3 or \
        _contains_forbidden_chars(filename) or \
        _contains_forbidden_chars(extension)

    if is_long_filename:
        result = "%s~1" % (_filter(filename)[0:6],)  ## Fixme, we should consider the case if there are several files
        if extension:
            result += ".%s" % (_filter(extension)[0:3],)
    else:
        result = filename
        if extension:
            result += ".%s" % (extension,)

    return result.upper()

def shortize(fullpath):
    path = fullpath.split("\\")

    components = [ _shortize_component(path_component) for path_component in path ]

    result = "\\".join(components)
    return(result)

if __name__ == '__main__':
    name = sys.argv[1]
    result = shortize(name)
    print(result)
