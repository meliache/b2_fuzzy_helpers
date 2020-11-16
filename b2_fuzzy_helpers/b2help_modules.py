#!/usr/bin/env python3
"""
Helper script to quickly find module descriptions in basf2
"""
from iterfzf import iterfzf
print("Loading basf2…", end="\r")
import basf2


def fuzzy_find_and_describe_module() -> None:
    """Use fzf to find a basf2 module and print module help"""
    module_name = iterfzf(module for module in basf2.list_available_modules().keys())
    basf2.utils.print_params(basf2.register_module(module_name))


if __name__ == '__main__':
    fuzzy_find_and_describe_module()
