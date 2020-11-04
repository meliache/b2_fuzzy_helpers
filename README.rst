
Fuzzy basf2 help scripts
========================

Install
-------

Easiest: Installation from github

  You can directly install the package with pip from github via

  .. code-block:: bash

      python3 -m pip install "git+https://github.com/meliache/b2_fuzzy_helpers"

Developer install

  If you want to install the package locally, you can also clone it and then
  install it with `flit <https://github.com/takluyver/flit>`_.

  .. code-block:: bash

      git clone https://github.com/meliache/b2_fuzzy_helpers
      cd b2_fuzzy_helpers
      flit install

  Optionally add the ``-s`` option to install with symbolic links (editable).

Usage
-----

The package installs the script ``b2help-variables``. You can then use the fuzzy
matching (see `fzf <https://github.com/junegunn/fzf>`_) to select the the
candidate that you are interested in and you will be shown the help.

Author
------

Michael Eliachevitch
