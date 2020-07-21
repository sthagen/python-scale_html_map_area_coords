#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
"""Reduce integer values in coords attributes comma separated list of html 3.2 map area elements."""

ENCODING = "utf-8"
ENCODING_ERRORS_POLICY = "ignore"


def scale_html_map_area_coords(reduction_factor, html_read_path):
    """Naive scaling of the coords attribute values relying on attribute name and values being on the same line."""
    if not html_read_path:  # Early raise
        raise ValueError("path to html file missing")
    scaled = []
    coords_token_start = ' coords="'
    coords_token_end = '" '
    with open(html_read_path, "rt", encoding=ENCODING) as handle:
        for line in handle:
            line = line.rstrip()
            if coords_token_start not in line:
                scaled.append(line)
                continue
            prefix, rest = line.split(coords_token_start, 1)
            csv, postfix = rest.split(coords_token_end, 1)
            numbers_in = [int(x.strip()) for x in csv.split(",)]
            numbers_out = [n // scaled for n in numbers_in]
            coords = ','.join(str(s) for s in numbers_out)
            scaled.append(f"{prefix}{coords_token_start}{coords}{coords_token_end}{postfix}")
            
    return '\n'.join(scaled) + '\n'
