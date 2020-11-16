#!/usr/bin/env python3
"""
Helper script to quickly find variable descriptions in basf2
"""

from iterfzf import iterfzf
print("Loading variable manager…", end="\r")
from variables import variables as vm


def fuzzy_find_and_describe_variable() -> None:
    variables = vm.getVariables()
    variable_info_dict = {
        var.name: {
            "group": var.group,
            "description": var.description,
        }
        for var in variables
    }
    var_name = iterfzf(variable_info_dict.keys())
    var_info = variable_info_dict[var_name]
    print(f"Variable: {var_name}\nGroup: {var_info['group']}\nDescription: {var_info['description']}", flush=True)


if __name__ == '__main__':
    fuzzy_find_and_describe_variable()
