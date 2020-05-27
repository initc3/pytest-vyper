pytest-vyper
============
.. image:: https://img.shields.io/badge/ic3-powered-9c2a4c
         :target: https://www.initc3.org/projects.html
         :alt: IC3 Powered

**WORK in PROGRESS**

Pytest plugin for the `vyper`_ smart contract language.

Installation
------------
.. code-block:: shell

    $ pip install git+https://github.com/sbellem/pytest-vyper

License
-------
Distributed under the terms of the `Apache Software License 2.0`_ license,
"pytest-vyper" is free and open source software

Acknowledgements
----------------
A big chunk of the code, meaning most of it at the moment of this writing,
was taken from the `vyper`_ code base, more precisely from:

* ``fixtures``: https://github.com/vyperlang/vyper/blob/master/tests/base_conftest.py
* ``grammar``: https://github.com/vyperlang/vyper/blob/master/tests/grammar

The history for the original `vyper`_ fixture, grammar and test files was preserved
using `git filter-repo`_.

Thanks to `IC3`_ (The Initiative For Cryptocurrencies & Contracts) and Andrew Miller
(`Decentralized Systems Lab <dsl>`_ at `UIUC`_) for supporting this work.


.. _`Apache Software License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`file an issue`: https://github.com/sbellem/pytest-vyper/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project
.. _`git filter-repo`: https://github.com/newren/git-filter-repo/
.. _ic3: https://www.initc3.org/
.. _dsl: https://decentralize.ece.illinois.edu/
.. _uiuc: https://spri.engr.illinois.edu/
.. _vyper: https://github.com/vyperlang/vyper
