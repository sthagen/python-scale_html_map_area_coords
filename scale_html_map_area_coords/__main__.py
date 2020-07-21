# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring
import sys

from scale_html_map_area_coords.cli import main

if __name__ == "__main__":  # pragma: no cover
    sys.exit(main(sys.argv[1:] if sys.argv[1:] else None))
