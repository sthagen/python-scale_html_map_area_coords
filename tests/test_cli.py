# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pathlib
from unittest import mock  # pylint: disable=no-name-in-module

import pytest  # type: ignore

import scale_html_map_area_coords.cli as cli


def test_main_nok_reduction_given_but_non_existing_path():
    nef = non_existing_file_path = 'file_does_not_exist'
    assert pathlib.Path(nef).is_file() is False, f"Unexpected file {nef} exists which breaks this test"
    message = f"\\[Errno 2\\] No such file or directory: '{non_existing_file_path}'"
    with pytest.raises(FileNotFoundError, match=message):
        cli.main([2, non_existing_file_path])


def test_main_nok_reduction_wrong_type_and_non_existing_path():
    nef = non_existing_file_path = 'file_does_not_exist'
    assert pathlib.Path(nef).is_file() is False, f"Unexpected file {nef} exists which may break other tests"
    message = f"unsupported operand type\(s\) for //: 'int' and 'NoneType'"
    with pytest.raises(TypeError, match=message):
        cli.main([None, non_existing_file_path])


@mock.patch('builtins.open', mock.mock_open(read_data=' coords="0,0" no_rstrip'))
def test_main_ok_with_file_mock(capsys):
    assert cli.main([2, '/call/me/mock.html']) is None
    out, err = capsys.readouterr()
    assert out == ' coords="0,0" no_rstrip\n'


@mock.patch('builtins.open', mock.mock_open(read_data=' coords="1,3" no_rstrip'))
def test_main_ok_with_file_mock_and_non_zero_coords(capsys):
    assert cli.main([2, '/call/me/mock.html']) is None
    out, err = capsys.readouterr()
    assert out == ' coords="0,1" no_rstrip\n'
