# coding: utf-8
"""
This module contains tests.
"""
from __future__ import absolute_import

# Standard imports
from argparse import ArgumentTypeError

# External imports
import pytest

# Local imports
from .aoikargutil import AllOf
from .aoikargutil import Argument
from .aoikargutil import OneOf
from .aoikargutil import Option
from .aoikargutil import SpecViolationError
from .aoikargutil import argument_exists
from .aoikargutil import bool_0or1
from .aoikargutil import ensure_argument_name
from .aoikargutil import ensure_spec
from .aoikargutil import float_ge0
from .aoikargutil import float_gt0
from .aoikargutil import float_le0
from .aoikargutil import float_lt0
from .aoikargutil import int_ge0
from .aoikargutil import int_gt0
from .aoikargutil import int_le0
from .aoikargutil import int_lt0
from .aoikargutil import str_nonempty
from .aoikargutil import str_strip_nonempty


def test_str_nonempty():
    """
    Test `str_nonempty`.
    """
    #
    assert str_nonempty(' ') == ' '

    #
    assert str_nonempty('123') == '123'

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        str_nonempty('')

    assert exc_info.value.args[0] == "Expected a non-empty string. Got: ''."


def test_str_strip_nonempty():
    """
    Test `str_strip_nonempty`.
    """
    #
    assert str_nonempty('123') == '123'

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        str_strip_nonempty('')

    assert exc_info.value.args[0] == \
        "Expected a non-empty and non-whitespace-only string. Got: ''."

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        str_strip_nonempty('  ')

    assert exc_info.value.args[0] == \
        "Expected a non-empty and non-whitespace-only string. Got: '  '."

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        str_strip_nonempty('\t\t')

    assert exc_info.value.args[0] == \
        r"Expected a non-empty and non-whitespace-only string. Got: '\t\t'."

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        str_strip_nonempty('\n\n')

    assert exc_info.value.args[0] == \
        r"Expected a non-empty and non-whitespace-only string. Got: '\n\n'."

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        str_strip_nonempty('\r\r')

    assert exc_info.value.args[0] == \
        r"Expected a non-empty and non-whitespace-only string. Got: '\r\r'."


def test_bool_0or1():
    """
    Test `bool_0or1`.
    """
    #
    assert bool_0or1('0') is False

    #
    assert bool_0or1('1') is True

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        bool_0or1('')

    assert exc_info.value.args[0] == "Expected '0' or '1'. Got: ''."

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        bool_0or1('-1')

    assert exc_info.value.args[0] == "Expected '0' or '1'. Got: '-1'."

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        bool_0or1('2')

    assert exc_info.value.args[0] == "Expected '0' or '1'. Got: '2'."

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        bool_0or1('True')

    assert exc_info.value.args[0] == "Expected '0' or '1'. Got: 'True'."

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        bool_0or1('False')

    assert exc_info.value.args[0] == "Expected '0' or '1'. Got: 'False'."


def test_int_lt0():
    """
    Test `int_lt0`.
    """
    #
    assert int_lt0('-1') == -1

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        int_lt0('0')

    assert exc_info.value.args[0] == "Expected an integer <0. Got: '0'."

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        int_lt0('1')

    assert exc_info.value.args[0] == "Expected an integer <0. Got: '1'."

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        int_lt0('NaN')

    assert exc_info.value.args[0] == "Expected an integer <0. Got: 'NaN'."


def test_int_le0():
    """
    Test `int_le0`.
    """
    #
    assert int_le0('-1') == -1

    #
    assert int_le0('0') == 0

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        int_le0('1')

    assert exc_info.value.args[0] == "Expected an integer <=0. Got: '1'."

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        int_le0('NaN')

    assert exc_info.value.args[0] == "Expected an integer <=0. Got: 'NaN'."


def test_int_gt0():
    """
    Test `int_gt0`.
    """
    #
    assert int_gt0('1') == 1

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        int_gt0('0')

    assert exc_info.value.args[0] == "Expected an integer >0. Got: '0'."

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        int_gt0('-1')

    assert exc_info.value.args[0] == "Expected an integer >0. Got: '-1'."

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        int_gt0('NaN')

    assert exc_info.value.args[0] == "Expected an integer >0. Got: 'NaN'."


def test_int_ge0():
    """
    Test `int_ge0`.
    """
    #
    assert int_ge0('1') == 1

    #
    assert int_ge0('0') == 0

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        int_ge0('-1')

    assert exc_info.value.args[0] == "Expected an integer >=0. Got: '-1'."

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        int_ge0('NaN')

    assert exc_info.value.args[0] == "Expected an integer >=0. Got: 'NaN'."


def test_float_lt0():
    """
    Test `float_lt0`.
    """
    #
    assert float_lt0('-1') == -1

    #
    assert float_lt0('-0.1') == -0.1

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        float_lt0('0')

    assert exc_info.value.args[0] == "Expected a float <0. Got: '0'."

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        float_lt0('0.1')

    assert exc_info.value.args[0] == "Expected a float <0. Got: '0.1'."

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        float_lt0('1')

    assert exc_info.value.args[0] == "Expected a float <0. Got: '1'."

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        float_lt0('NaN')

    assert exc_info.value.args[0] == "Expected a float <0. Got: 'NaN'."


def test_float_le0():
    """
    Test `float_le0`.
    """
    #
    assert float_le0('-1') == -1

    #
    assert float_le0('-0.1') == -0.1

    #
    assert float_le0('0') == 0

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        float_le0('0.1')

    assert exc_info.value.args[0] == "Expected a float <=0. Got: '0.1'."

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        float_le0('1')

    assert exc_info.value.args[0] == "Expected a float <=0. Got: '1'."

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        float_le0('NaN')

    assert exc_info.value.args[0] == "Expected a float <=0. Got: 'NaN'."


def test_float_gt0():
    """
    Test `float_gt0`.
    """
    #
    assert float_gt0('1') == 1

    #
    assert float_gt0('0.1') == 0.1

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        float_gt0('0')

    assert exc_info.value.args[0] == "Expected a float >0. Got: '0'."

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        float_gt0('-0.1')

    assert exc_info.value.args[0] == "Expected a float >0. Got: '-0.1'."

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        float_gt0('-1')

    assert exc_info.value.args[0] == "Expected a float >0. Got: '-1'."

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        float_gt0('NaN')

    assert exc_info.value.args[0] == "Expected a float >0. Got: 'NaN'."


def test_float_ge0():
    """
    Test `float_ge0`.
    """
    #
    assert float_ge0('1') == 1

    #
    assert float_ge0('0.1') == 0.1

    #
    assert float_ge0('0') == 0

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        float_ge0('-0.1')

    assert exc_info.value.args[0] == "Expected a float >=0. Got: '-0.1'."

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        float_ge0('-1')

    assert exc_info.value.args[0] == "Expected a float >=0. Got: '-1'."

    #
    with pytest.raises(ArgumentTypeError) as exc_info:
        float_ge0('NaN')

    assert exc_info.value.args[0] == "Expected a float >=0. Got: 'NaN'."


def test_argument_exists():
    """
    Test `argument_exists`.
    """
    assert argument_exists('-a', []) is False

    assert argument_exists('-a', ['-b']) is False

    assert argument_exists('-a', ['--a']) is False

    assert argument_exists('--a', ['-a']) is False

    assert argument_exists('-a', ['-a']) is True

    assert argument_exists('--a', ['--a']) is True


def test_ensure_argument_name():
    """
    Test `ensure_argument_name`.
    """
    #
    ensure_argument_name(arg_name='-a', args=['-a'])

    #
    with pytest.raises(SpecViolationError) as exc_info:
        ensure_argument_name(arg_name='-a', args=[])

    assert exc_info.value.args[0] == "Require argument '-a'."

    #
    with pytest.raises(SpecViolationError) as exc_info:
        ensure_argument_name(arg_name='-a', args=[], depending='-b')

    assert exc_info.value.args[0] == "Argument '-b' requires argument '-a'."


def test_ensure_string_spec():
    """
    Test ensure string spec.
    """
    #
    ensure_spec(spec='-a', args=['-a'])

    #
    with pytest.raises(SpecViolationError) as exc_info:
        ensure_spec(spec='-a', args=[])

    assert exc_info.value.args[0] == "Require argument '-a'."

    #
    with pytest.raises(SpecViolationError) as exc_info:
        ensure_spec(spec='-a', args=[], depending='-b')

    assert exc_info.value.args[0] == "Argument '-b' requires argument '-a'."


def test_ensure_argument_spec():
    """
    Test ensure Argument spec.
    """
    #
    ensure_spec(spec=Argument('-a'), args=['-a'])

    ensure_spec(spec=Argument('-a', '-b'), args=['-a', '-b'])

    #
    with pytest.raises(SpecViolationError) as exc_info:
        ensure_spec(spec=Argument('-a'), args=[])

    assert exc_info.value.args[0] == "Require argument '-a'."

    #
    with pytest.raises(SpecViolationError) as exc_info:
        ensure_spec(spec=Argument('-a', '-b'), args=['-a'])

    assert exc_info.value.args[0] == "Argument '-a' requires argument '-b'."

    #
    with pytest.raises(SpecViolationError) as exc_info:
        ensure_spec(
            spec=Argument('-a', Argument('-b', '-c')), args=['-a', '-b']
        )

    assert exc_info.value.args[0] == "Argument '-b' requires argument '-c'."

    #
    with pytest.raises(SpecViolationError) as exc_info:
        ensure_spec(spec=Argument('-a', OneOf('-b', '-c')), args=['-a'])

    assert exc_info.value.args[0] == \
        "Argument '-a' requires exact one of arguments ['-b', '-c']. Got none."

    #
    with pytest.raises(SpecViolationError) as exc_info:
        ensure_spec(spec=Argument('-a', AllOf('-b', '-c')), args=['-a'])

    assert exc_info.value.args[0] == \
        "Argument '-a' requires all of arguments ['-b', '-c']."


def test_ensure_option_spec():
    """
    Test ensure Option spec.
    """
    #
    ensure_spec(spec=Option('-a'), args=[])

    #
    ensure_spec(spec=Option('-a'), args=['-a'])

    #
    ensure_spec(spec=Option('-a', '-b'), args=[])

    #
    ensure_spec(spec=Option('-a', '-b'), args=['-a', '-b'])

    #
    with pytest.raises(SpecViolationError) as exc_info:
        ensure_spec(spec=Option('-a', '-b'), args=['-a'])

    assert exc_info.value.args[0] == "Argument '-a' requires argument '-b'."

    #
    ensure_spec(spec=Option('-a', Option('-b', '-c')), args=['-a'])

    #
    ensure_spec(spec=Option('-a', Option('-b', '-c')), args=['-b'])

    #
    with pytest.raises(SpecViolationError) as exc_info:
        ensure_spec(spec=Option('-a', Option('-b', '-c')), args=['-a', '-b'])

    assert exc_info.value.args[0] == "Argument '-b' requires argument '-c'."

    #
    ensure_spec(spec=Option('-a', OneOf('-b', '-c')), args=[])

    #
    with pytest.raises(SpecViolationError) as exc_info:
        ensure_spec(spec=Option('-a', OneOf('-b', '-c')), args=['-a'])

    assert exc_info.value.args[0] == \
        "Argument '-a' requires exact one of arguments ['-b', '-c']. Got none."

    #
    ensure_spec(spec=Option('-a', AllOf('-b', '-c')), args=[])

    #
    with pytest.raises(SpecViolationError) as exc_info:
        ensure_spec(spec=Option('-a', AllOf('-b', '-c')), args=['-a'])

    assert exc_info.value.args[0] == \
        "Argument '-a' requires all of arguments ['-b', '-c']."


def test_ensure_oneof_spec():
    """
    Test ensure OneOf spec.
    """
    #
    ensure_spec(spec=OneOf('-a', Argument('-b')), args=['-a'])

    ensure_spec(spec=OneOf('-a', Argument('-b')), args=['-b'])

    #
    with pytest.raises(SpecViolationError) as exc_info:
        ensure_spec(spec=OneOf('-a', '-b'), args=['-c'])

    assert exc_info.value.args[0] == \
        "Require exact one of arguments ['-a', '-b']. Got none."

    #
    with pytest.raises(SpecViolationError) as exc_info:
        ensure_spec(spec=OneOf('-a', '-b'), args=['-a', '-b'])

    assert exc_info.value.args[0] == \
        "Require exact one of arguments ['-a', '-b']. Got '-a' and '-b'."

    #
    with pytest.raises(TypeError) as exc_info:
        ensure_spec(spec=OneOf(OneOf('-a')), args=[])

    assert exc_info.value.args[0] == \
        "Expected string or Argument object. Got OneOf('-a')."

    #
    with pytest.raises(TypeError) as exc_info:
        ensure_spec(spec=OneOf(AllOf('-a')), args=[])

    assert exc_info.value.args[0] == \
        "Expected string or Argument object. Got AllOf('-a')."


def test_ensure_allof_spec():
    """
    Test ensure AllOf spec.
    """
    #
    ensure_spec(spec=AllOf('-a', '-b'), args=['-a', '-b'])

    #
    with pytest.raises(SpecViolationError) as exc_info:
        ensure_spec(spec=AllOf('-a', '-b'), args=[])

    assert exc_info.value.args[0] == "Require all of arguments ['-a', '-b']."

    #
    with pytest.raises(SpecViolationError) as exc_info:
        ensure_spec(spec=AllOf('-a', '-b'), args=['-a'])

    assert exc_info.value.args[0] == "Require all of arguments ['-a', '-b']."

    #
    with pytest.raises(SpecViolationError) as exc_info:
        ensure_spec(spec=AllOf('-a', '-b'), args=['-b'])

    assert exc_info.value.args[0] == "Require all of arguments ['-a', '-b']."
