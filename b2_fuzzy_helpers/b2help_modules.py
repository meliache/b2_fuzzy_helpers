#!/usr/bin/env python3
"""
Helper script to quickly find module descriptions in basf2
"""

from iterfzf import iterfzf
import basf2


def fuzzy_find_and_describe_module() -> None:
    module_name = iterfzf(module for module in basf2.list_available_modules().keys())
    description = basf2.register_module(module_name).description()
    print(f"Module: {module_name}\nDescription: {description}")


if __name__ == '__main__':
    fuzzy_find_and_describe_module()
