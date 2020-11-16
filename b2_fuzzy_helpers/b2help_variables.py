#!/usr/bin/env python3
"""
Helper script to quickly find variable descriptions in basf2
"""

from iterfzf import iterfzf
from variables import variables as vm


def fuzzy_find_and_describe_variable() -> None:
    variable_name = iterfzf(vm.getNames())
    description = vm.getVariable(variable_name).description
    print(f"Variable: {variable_name}\nDescription: {description}")


if __name__ == '__main__':
    fuzzy_find_and_describe_variable()
