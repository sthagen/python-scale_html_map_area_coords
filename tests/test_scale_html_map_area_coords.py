# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import scale_html_map_area_coords.scale_html_map_area_coords as do


def test_apply_scaling_ok_string():
    assert do.apply_scaling("imension is implicit") == "imension is implicit"


def test_apply_scaling_ok_empty_string():
    assert do.apply_scaling('') == ''


def test_apply_scaling_nok_ints():
    message = r"'list' object has no attribute 'rstrip'"
    with pytest.raises(AttributeError, match=message):
        do.apply_scaling([1, 2, 3])
