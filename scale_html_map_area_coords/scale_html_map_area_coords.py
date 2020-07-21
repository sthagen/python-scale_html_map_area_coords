#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
"""Reduce integer values in coords attributes comma separated list of html 3.2 map area elements."""

ENCODING = "utf-8"
ENCODING_ERRORS_POLICY = "ignore"


def apply_scaling(reduction_factor:int, text_line: str):
    """Apply the scaling if coords attribute present in line."""
    coords_token_start = ' coords="'
    coords_token_end = '" '
    line = text_line.rstrip()
    if coords_token_start not in line:
        return line
    prefix, rest = line.split(coords_token_start, 1)
    csv, postfix = rest.split(coords_token_end, 1)
    numbers_in = [int(x.strip()) for x in csv.split(',')]
    numbers_out = [n // reduction_factor for n in numbers_in]
    coords = ','.join(str(s) for s in numbers_out)
    return f"{prefix}{coords_token_start}{coords}{coords_token_end}{postfix}"


def scale_html_map_area_coords(reduction_factor: int, html_read_path: str):
    """Naive scaling of the coords attribute values relying on attribute name and values being on the same line."""
    if not html_read_path:  # Early raise
        raise ValueError("path to html file missing")
    scaled = []
    with open(html_read_path, "rt", encoding=ENCODING) as handle:
        for line in handle:
            scaled.append(apply_scaling(reduction_factor, line))
    return '\n'.join(scaled) + '\n'
