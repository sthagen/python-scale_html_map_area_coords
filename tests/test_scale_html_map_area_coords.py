# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pathlib
import pytest  # type: ignore

import scale_html_map_area_coords.scale_html_map_area_coords as do


def test_apply_scaling_ok_string():
    assert do.apply_scaling("imension is implicit") == "imension is implicit"


def test_apply_scaling_ok_empty_string():
    assert do.apply_scaling('') == ''


def test_apply_scaling_nok_list_of_ints():
    message = r"'list' object has no attribute 'rstrip'"
    with pytest.raises(AttributeError, match=message):
        do.apply_scaling([1, 2, 3])


def test_apply_scaling_nok_int():
    message = r"'int' object has no attribute 'rstrip'"
    with pytest.raises(AttributeError, match=message):
        do.apply_scaling(42)


def test_scale_html_map_area_coords_nok_reduction_gibven_but_empty_path():
    message = r"path to html file missing"
    with pytest.raises(ValueError, match=message):
        do.scale_html_map_area_coords(2, '')


def test_scale_html_map_area_coords_nok_reduction_gibven_but_invalid_path():
    sequence_of_ints = [1, 2, 3]
    message = r"expected str, bytes or os.PathLike object, not list"
    with pytest.raises(TypeError, match=message):
        do.scale_html_map_area_coords(2, sequence_of_ints)


def test_scale_html_map_area_coords_nok_reduction_gibven_but_non_existing_path():
    nef = non_existing_folder_path = 'folder_does_not_exist'
    assert pathlib.Path(nef).is_dir() is False, f"Unexpected folder {nef} exists which breaks this test"
    message = f"\\[Errno 2\\] No such file or directory: '{non_existing_folder_path}'"
    with pytest.raises(FileNotFoundError, match=message):
        do.scale_html_map_area_coords(2, non_existing_folder_path)
