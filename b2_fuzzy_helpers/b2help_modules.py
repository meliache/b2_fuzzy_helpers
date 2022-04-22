#!/usr/bin/env python3
"""
Helper script to quickly find module descriptions in basf2
"""


from typing import List

import basf2
from iterfzf import iterfzf
from joblib import Memory
from xdg import xdg_cache_home

from b2_fuzzy_helpers.utils import get_basf2_git_hash

memory = Memory(location=xdg_cache_home() / "b2_fuzzy_helpers")
from joblib import Memory


# make cached version of basf2.list_available_modules, i.e. save module list for a specific release
@memory.cache
def get_modules(
    _basf2_release: str,
) -> List[str]:  # release parameter only used as cache key
    print("Loading basf2 modules…", end="\r")
    return [m for m in basf2.list_available_modules().keys()]


def fuzzy_find_and_describe_module() -> None:
    """Use fzf to find a basf2 module and print module help"""
    modules = get_modules(get_basf2_git_hash())
    module_name = iterfzf(modules)
    basf2.utils.print_params(basf2.register_module(module_name))


if __name__ == "__main__":
    fuzzy_find_and_describe_module()
