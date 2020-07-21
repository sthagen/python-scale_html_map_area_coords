# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pathlib
import pytest  # type: ignore

import scale_html_map_area_coords.cli as cli


def test_main_nok_reduction_gibven_but_non_existing_path():
    nef = non_existing_file_path = 'file_does_not_exist'
    assert pathlib.Path(nef).is_file() is False, f"Unexpected file {nef} exists which breaks this test"
    message = f"\\[Errno 2\\] No such file or directory: '{non_existing_file_path}'"
    with pytest.raises(FileNotFoundError, match=message):
        cli.main([2, non_existing_file_path])
