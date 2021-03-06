#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
"""Scale coords attribute values of html map area elements."""
import sys

from scale_html_map_area_coords.scale_html_map_area_coords import scale_html_map_area_coords


# pylint: disable=expression-not-assigned
def main(argv=None):
    """Test driver for the scaling of coords attributes in map > area htmle elements of file from argv or stdin and writing to stdout."""
    reduction = int(sys.argv[1]) if argv is None else int(argv[0])
    read_path = sys.argv[2] if argv is None else argv[1]
    sys.stdout.write(scale_html_map_area_coords(reduction, read_path))
