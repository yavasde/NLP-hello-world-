Snowball stemming library collection for Python
===============================================

Both Python 2 and Python 3 (>= 3.3) are supported.

How to use library
------------------

The ``snowballstemmer`` module has two functions.

The ``snowballstemmer.algorithms`` function returns a list of available
algorithm names.

The ``snowballstemmer.stemmer`` function takes an algorithm name and returns a
``Stemmer`` object.

``Stemmer`` objects have a ``Stemmer.stemWord(word)`` method and a
``Stemmer.stemWords(word[])`` method.

.. code-block:: python

   import snowballstemmer

   stemmer = snowballstemmer.stemmer('english');
   print(stemmer.stemWords("We are the world".split()));

Automatic Acceleration
----------------------

If `PyStemmer <https://pypi.org/project/PyStemmer/>`_ is installed,
``snowballstemmer.stemmer`` returns a ``PyStemmer`` ``Stemmer`` object
which provides the same ``Stemmer.stemWord()`` and ``Stemmer.stemWords()``
methods.

**PyStemmer** is a wrapper module for Snowball's ``libstemmer_c`` and should
provide results 100% compatible to **snowballstemmer**.

**PyStemmer** is faster because it wraps generated C versions of the stemmers;
**snowballstemmer** uses generate Python code and is slower but offers a pure
Python solution.

Benchmark
~~~~~~~~~

This is a crude benchmark which measures the time for running each stemmer on
every word in its sample vocabulary (10,787,583 words over 26 languages).  It's
not a realistic test of normal use as a real application would do much more
than just stemming.  It's also skewed towards the stemmers which do more work
per word and towards those with larger sample vocabularies.

* Python 2.7 + **snowballstemmer** : 13m00s (15.0 * PyStemmer)
* Python 3.7 + **snowballstemmer** : 12m19s (14.2 * PyStemmer)
* PyPy 7.1.1 (Python 2.7.13) + **snowballstemmer** : 2m14s (2.6 * PyStemmer)
* PyPy 7.1.1 (Python 3.6.1) + **snowballstemmer** : 1m46s (2.0 * PyStemmer)
* Python 2.7 + **PyStemmer** : 52s

For reference the equivalent test for C runs in 9 seconds.

These results are for Snowball 2.0.0.  They're likely to evolve over time as
the code Snowball generates for both Python and C continues to improve (for
a much older test over a different set of stemmers using Python 2.7,
**snowballstemmer** was 30 times slower than **PyStemmer**, or 9 times slower
with **PyPy**).

The message to take away is that if you're stemming a lot of words you should
either install **PyStemmer** (which **snowballstemmer** will then automatically
use for you as described above) or use PyPy.

The TestApp example
-------------------

The ``testapp.py`` example program allows you to run any of the stemmers
on a sample vocabulary.

Usage::

   testapp.py <algorithm> "sentences ... "

.. code-block:: bash

   $ python testapp.py English "sentences... "

License
-------

It is a BSD licensed library.

Copyright (c) 2013, Yoshiki Shibukawa
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

   Redistributions of source code must retain the above copyright notice,
   this list of conditions and the following disclaimer.

   Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

   Neither the name of the <ORGANIZATION> nor the names of its contributors
   may be used to endorse or promote products derived from this software
   without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
