
``b2_fuzzy_helpers``: Fuzzy basf2 help scripts
===============================================

Basf2 help scripts for easily finding a module or variable description from the
command line with an incremental fuzzy search via fzf_.

Demo session
------------

.. image:: https://asciinema.org/a/zGC6F2TpNmBdXORbgm9d4Me4K.svg
   :target: https://asciinema.org/a/zGC6F2TpNmBdXORbgm9d4Me4K
   :alt: b2help-modules and b2help-variables demo session

Install
-------

First, make sure you have basf2 set up. Then, there are two ways how to install the package:

Easiest: Installation from github

  You can directly install the package with pip from github via

  .. code-block:: bash

      python3 -m pip install --user "git+https://github.com/meliache/b2_fuzzy_helpers"

Developer install

  If you want to install the package locally, you can also clone it and then
  install it with `flit <https://github.com/takluyver/flit>`_.

  .. code-block:: bash

      git clone https://github.com/meliache/b2_fuzzy_helpers
      cd b2_fuzzy_helpers
      flit install --user

  Optionally add the ``-s`` option to install with symbolic links (editable).

Usage
-----

The package installs the scripts

- ``b2help-variables``
- ``b2help-modules``

After installing, you can run these commands from terminal, but rememeber to set
up basf2 first. You will be presented a list of candidates (modules/variables).
Start typing and the list of candidates will be narrowed down with fuzzy
matching to candidates containing the substring. You can provide multipe
substrings, spaces will be interpreted as logical "and". After typing enter, you
will see a description for the current candidate.

See the fzf_ docs for further information how the fuzzy matching works.

Author
------

Michael Eliachevitch

.. _fzf: https://github.com/junegunn/fzf
