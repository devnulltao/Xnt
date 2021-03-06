Running Xnt
===========

Invoking Xnt from the command line is very simple and very similar to how other
build tools are invoked (this was intentional).

.. _defaultUse:

Default Use
-----------

The most simplistic use of Xnt is as follows::

    $ xnt

This will attempt to invoke the `default` target in the current directory's
`build.py`.

.. _invokeTarget:

Invoke a Target
---------------

To invoke a particular target, use::

    $ xnt {target}

Where the value of `{target}` is dependent on your particular `build.py` file.

Invoke MORE Targets
~~~~~~~~~~~~~~~~~~~

Xnt now supports executing multiple targets in one go. That is, if you want to
chain targets together, you now can *without* separate executions of Xnt. For
example::

    $ xnt {target1} {target2} ... {targetN}

Will execute `target1` through `targetN` in order of listing.

.. _otherCommands:

Other Commands
--------------

Xnt has a number of other commands that can be invoked besides those defined in
the current directory's `build.py` file. One will need a build file to run. The
others, however, do not.

* ``-h`` or ``--help`` prints a summary message, including information about
  the version of Xnt, license, and usage.

Usage::

    $ xnt --help


* ``-l`` or ``--list-targets`` does exactly what the name should suggest: it
  prints a list of the targets found in the current directory's `build.py`
  script, along with any docstrings that may be defined with them.

Usage::

    $ xnt --list-targets

* ``--version`` prints Xnt's installed version.

Usage::

    $ xnt --version

.. _xntOptions:

Options
-------

Xnt also has a few "options" that may be provided along with a regular targets.

Usage::

    $ xnt [options] [target]

Where options can be any and all of the following (unless otherwise specified):

* ``-v`` or ``--verbose``: add verbose output to the execution of Xnt

* ``-b BUILDFILE`` or ``--build-file BUILDFILE``: use the given buildfile

.. _xntPropertiesParameters:

Properties and Parameter Passing
--------------------------------

Xnt now has the ability to accept command line parameters and forward them to
your `build.py` file. This can be useful for a number of reasons: flipping
debug flags, deployment flags and the like or whatever else you can imagine.

The general semantic for passing the parameters is as follows::

    $ xnt [-D{name}={value}]+ [options] [target]

*Notice:* the `-D` is used to distinguish values to be passed to the `build`
file from regular options. You may specify as many parameters as you like and
there is no other real ordering required to be parsed correctly. Just know,
spaces are used to delimit arguments; if your passed value *must* have a space,
remember to quote it.

Please see :ref:`buildProperties` to see how this works on the `build.py` side.
