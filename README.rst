Various geometric decorations are provided:

- Hatch marks for lines
- The angular analogue

  + A "corner" variant of the arc markings is available for the familiar
    right-angle signifiers, but generalizes to any angle.

- Labels for lines and angles.

----

A length-2 mathtuple type ``Point`` is provided, and some geometric functions:

- ``dist(pt1, pt2)``
- ``midpoint(pt1, pt2)``
- ``between(pt1, pt2, pos)``

  + ``pos`` specifies a distance from ``pt1`` towards ``pt2`` scaled such
    that zero corresponds to ``pt1`` and one to ``pt2``.
  + ``pos`` is not restricted to this range: it can be any real number, but
    this is the range "between" the points.

Several bindings from the standard library module ``math`` are passed through:
functions ``sqrt()``, ``sin()``, ``cos()``, ``atan2()``, as well as the constant ``pi``.

----

`SimpleSVG`_, `mathtuple`_, and `attrs`_ are dependencies

.. _SimpleSVG: https://github.com/sfaleron/SimpleSVG
.. _mathtuple: https://github.com/sfaleron/mathtuple
.. _attrs: https://www.attrs.org/
