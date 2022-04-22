
``b2_fuzzy_helpers``: Fuzzy basf2 help scripts
===============================================

Basf2 help scripts for easily finding a module or variable description from the
command line with an incremental fuzzy search via fzf_.

Demo session
------------

.. image:: https://asciinema.org/a/HyiOhmQB0EKFs6kSpDuac1dVJ.svg
   :target: https://asciinema.org/a/HyiOhmQB0EKFs6kSpDuac1dVJ
   :alt: b2fuzzy-modules and b2fuzzy-variables demo session

   Demo session. Note: In the latest version I renamed the fuzzy helper scripts
   from `b2help-...` to `b2fuzzy-variables` and `b2fuzzy-modules` to avoid name
   conflicts with the new built-in basf2 help scripts starting with `b2help-`.

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

  Optionally add the ``-s`` option to install via symbolic links (editable).

If the scripts are still not found after installation, make sure that your ``~/.local/bin`` directory is in the ``PATH``. If not, you can add it by adding the following line to your shell init file (e.g. ``~/.bashrc``):

.. code-block:: bash

    export PATH=$HOME/.local/bin:$PATH

and ``source`` the file again or open a new terminal.

Usage
-----

The package installs the scripts

- ``b2fuzzy-variables``
- ``b2fuzzy-modules``

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
