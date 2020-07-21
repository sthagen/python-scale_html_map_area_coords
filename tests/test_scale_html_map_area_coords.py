# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import scale_html_map_area_coords.scale_html_map_area_coords as do


def test_apply_scaling_ok_string():
    assert do.apply_scaling("imension is implicit") == "imension is implicit"


def test_apply_scaling_ok_empty_string():
    assert do.apply_scaling('') == ''
