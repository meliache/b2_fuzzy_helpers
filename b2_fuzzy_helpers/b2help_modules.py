#!/usr/bin/env python3
"""
Helper script to quickly find module descriptions in basf2
"""
from subprocess import run
from iterfzf import iterfzf
import basf2


def fuzzy_find_and_describe_module() -> None:
    """Use fzf to find a basf2 module and print module help"""
    module_name = iterfzf(module for module in basf2.list_available_modules().keys())
    cmd = ["basf2", "-m", module_name]
    run(cmd, check=True)


if __name__ == '__main__':
    fuzzy_find_and_describe_module()
