EBMDataLab bigquery utils
=========================

Useful, common utilities for working with bigquery.

This is currently a moving target and subject to fast, breaking
changes... in particular, our dataset and project names are hard-coded
here.


Development notes
-----------------

To run tests and check packaging, run tox::

  $ tox

Note that the functional tests expect `GOOGLE_APPLICATION_CREDENTIALS`
to be set in your environment.

To push to PyPI::

  $ python setup.py sdist upload -r pypi
