#!/usr/bin/env python3
"""
Helper script to quickly find variable descriptions in basf2
"""

from typing import List

from iterfzf import iterfzf
from joblib import Memory
from xdg import xdg_cache_home

memory = Memory(location=xdg_cache_home() / "b2_fuzzy_helpers")

from b2_fuzzy_helpers.utils import get_basf2_git_hash


# make cached version of basf2 get_variables, i.e. save variable list for a specific release
@memory.cache
def get_variables(
    _basf2_release: str,
) -> List[str]:  # release parameter only used as cache key
    print("Loading variable manager…", end="\r")
    from variables import variables as vm

    return list(vm.getVariables())


def fuzzy_find_and_describe_variable() -> None:
    variables = get_variables(get_basf2_git_hash())
    variable_info_dict = {
        var.name: {
            "group": var.group,
            "description": var.description,
        }
        for var in variables
    }
    var_name = iterfzf(variable_info_dict.keys())
    var_info = variable_info_dict[var_name]
    print(
        f"Variable: {var_name}\nGroup: {var_info['group']}\nDescription: {var_info['description']}",
        flush=True,
    )

if __name__ == "__main__":
    fuzzy_find_and_describe_variable()
