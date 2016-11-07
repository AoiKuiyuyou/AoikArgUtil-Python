# coding: utf-8
"""
This module contains utility functions for Python built-in module `argparse`.
"""
from __future__ import absolute_import

# Standard imports
from argparse import ArgumentTypeError
import re


__version__ = '0.3.0'


__all__ = (
    '__version__',
    'str_nonempty',
    'str_strip_nonempty',
    'bool_0or1',
    'int_ge0',
    'int_gt0',
    'int_le0',
    'int_lt0',
    'float_ge0',
    'float_gt0',
    'float_le0',
    'float_lt0',
    'SpecViolationError',
    'Argument',
    'Option',
    'OneOf',
    'AllOf',
    'ensure_spec',
)


def str_nonempty(text):
    """
    Ensure given argument text is not empty.

    Used as `type` argument of `argparse.ArgumentParser.add_argument`.

    :param text: Argument text.

    :return: Argument text.
    """
    # If given argument text is not empty
    if text != '':
        # Return given argument text
        return text

    # If given argument text is empty
    else:
        # Get error message
        msg = 'Expected a non-empty string. Got: {0}.'.format(repr(text))

        # Raise error
        raise ArgumentTypeError(msg)


def str_strip_nonempty(text):
    """
    Strip whitespace on both sides of given argument, and ensure the result \
        is not empty.

    Used as `type` argument of `argparse.ArgumentParser.add_argument`.

    :param text: Argument text.

    :return: Stripped argument text.
    """
    # Strip given argument text
    stripped_text = text.strip()

    # If the stripped text is not empty
    if stripped_text != '':
        # Return the stripped text
        return stripped_text

    # If the stripped text is empty
    else:
        # Get error message
        error_msg = 'Expected a non-empty and non-whitespace-only string.'\
            ' Got: {0}.'.format(repr(text))

        # Raise error
        raise ArgumentTypeError(error_msg)


def bool_0or1(text):
    """
    Convert given argument text '0' and '1' to False and True, respectively.

    Used as `type` argument of `argparse.ArgumentParser.add_argument`.

    :param text: Argument text.

    :return: False for '0', True for '1'.
    """
    # If given argument text is '0'
    if text == '0':
        # Return False
        return False

    # If given argument text is '1'
    elif text == '1':
        # Return True
        return True

    # If given argument text is not '0' or '1'
    else:
        # Get error message
        error_msg = "Expected '0' or '1'. Got: {0}.".format(repr(text))

        # Raise error
        raise ArgumentTypeError(error_msg)


def int_lt0(text):
    """
    Convert given argument text to integer and ensure the integer is <0.

    Used as `type` argument of `argparse.ArgumentParser.add_argument`.

    :param text: Argument text.

    :return: Integer <0.
    """
    try:
        # Convert given argument text to integer.
        # May raise error.
        value = int(text)

        # Assert the value is <0.
        # May raise error.
        assert value < 0

    # If have error
    except Exception:
        # Get error message
        error_msg = 'Expected an integer <0. Got: {0}.'.format(repr(text))

        # Raise error
        raise ArgumentTypeError(error_msg)

    # If not have error
    else:
        # Return the value
        return value


def int_le0(text):
    """
    Convert given argument text to integer and ensure the integer is <=0.

    Used as `type` argument of `argparse.ArgumentParser.add_argument`.

    :param text: Argument text.

    :return: Integer <=0.
    """
    try:
        # Convert given argument text to integer.
        # May raise error.
        value = int(text)

        # Assert the value is <=0.
        # May raise error.
        assert value <= 0

    # If have error
    except Exception:
        # Get error message
        error_msg = 'Expected an integer <=0. Got: {0}.'.format(repr(text))

        # Raise error
        raise ArgumentTypeError(error_msg)

    # If not have error
    else:
        # Return the value
        return value


def int_gt0(text):
    """
    Convert given argument text to integer and ensure the integer is >0.

    Used as `type` argument of `argparse.ArgumentParser.add_argument`.

    :param text: Argument text.

    :return: Integer >0.
    """
    try:
        # Convert given argument text to integer.
        # May raise error.
        value = int(text)

        # Assert the value is >0.
        # May raise error.
        assert value > 0

    # If have error
    except Exception:
        # Get error message
        error_msg = 'Expected an integer >0. Got: {0}.'.format(repr(text))

        # Raise error
        raise ArgumentTypeError(error_msg)

    # If not have error
    else:
        # Return the value
        return value


def int_ge0(text):
    """
    Convert given argument text to integer and ensure the integer is >=0.

    Used as `type` argument of `argparse.ArgumentParser.add_argument`.

    :param text: Argument text.

    :return: Integer >=0.
    """
    try:
        # Convert given argument text to integer.
        # May raise error.
        value = int(text)

        # Assert the value is >=0.
        # May raise error.
        assert value >= 0

    # If have error
    except Exception:
        # Get error message
        error_msg = 'Expected an integer >=0. Got: {0}.'.format(repr(text))

        # Raise error
        raise ArgumentTypeError(error_msg)

    # If not have error
    else:
        # Return the value
        return value


def float_lt0(text):
    """
    Convert given argument text to float and ensure the float is <0.

    Used as `type` argument of `argparse.ArgumentParser.add_argument`.

    :param text: Argument text.

    :return: Float <0.
    """
    try:
        # Convert given argument text to float.
        # May raise error.
        value = float(text)

        # Assert the value is <0.
        # May raise error.
        assert value < 0

    # If have error
    except Exception:
        # Get error message
        error_msg = 'Expected a float <0. Got: {0}.'.format(repr(text))

        # Raise error
        raise ArgumentTypeError(error_msg)

    # If not have error
    else:
        # Return the value
        return value


def float_le0(text):
    """
    Convert given argument text to float and ensure the float is <=0.

    Used as `type` argument of `argparse.ArgumentParser.add_argument`.

    :param text: Argument text.

    :return: Float <=0.
    """
    try:
        # Convert given argument text to float.
        # May raise error.
        value = float(text)

        # Assert the value is <=0.
        # May raise error.
        assert value <= 0

    # If have error
    except Exception:
        # Get error message
        error_msg = 'Expected a float <=0. Got: {0}.'.format(repr(text))

        # Raise error
        raise ArgumentTypeError(error_msg)

    # If not have error
    else:
        # Return the value
        return value


def float_gt0(text):
    """
    Convert given argument text to float and ensure the float is >0.

    Used as `type` argument of `argparse.ArgumentParser.add_argument`.

    :param text: Argument text.

    :return: Float >0.
    """
    try:
        # Convert given argument text to float.
        # May raise error.
        value = float(text)

        # Assert the value is >0.
        # May raise error.
        assert value > 0

    # If have error
    except Exception:
        # Get error message
        error_msg = 'Expected a float >0. Got: {0}.'.format(repr(text))

        # Raise error
        raise ArgumentTypeError(error_msg)

    # If not have error
    else:
        # Return the value
        return value


def float_ge0(text):
    """
    Convert given argument text to float and ensure the float is >=0.

    Used as `type` argument of `argparse.ArgumentParser.add_argument`.

    :param text: Argument text.

    :return: Float >=0.
    """
    try:
        # Convert given argument text to float.
        # May raise error.
        value = float(text)

        # Assert the value is >=0.
        # May raise error.
        assert value >= 0

    # If have error
    except Exception:
        # Get error message
        error_msg = 'Expected a float >=0. Got: {0}.'.format(repr(text))

        # Raise error
        raise ArgumentTypeError(error_msg)

    # If not have error
    else:
        # Return the value
        return value


class BaseSpec(object):
    """
    Base class for spec.
    """

    def ensure_spec(self, args, depending):
        """
        Ensure this spec. Raise SpecViolationError if violated.

        :param args: Argument list.

        :param depending: Depending argument name.

        :return: None.
        """
        # Implemented in subclass
        raise NotImplementedError()


class Argument(BaseSpec):
    """
    Argument spec that requires given argument name exists, and given sub \
        spec is ensured.
    """

    def __init__(self, arg_name, sub_spec=None):
        """
        Constructor.

        :param arg_name: Argument name.

        :param sub_spec: Sub spec.

        :return: None.
        """
        # Store argument name
        self.arg_name = arg_name

        # Store sub spec
        self.sub_spec = sub_spec

    def __repr__(self):
        """
        Convert to string representation.

        :return: String.
        """
        # Return string representation
        return 'Argument({0}, {1})'.format(
            repr(self.arg_name),
            repr(self.sub_spec),
        )

    def ensure_spec(self, args, depending):
        """
        Ensure this spec. Raise SpecViolationError if violated.

        :param args: Argument list.

        :param depending: Depending argument name.

        :return: None.
        """
        # Get argument name
        arg_name = self.arg_name

        # Ensure the argument name exists
        ensure_argument_name(arg_name, args, depending=depending)

        # Get sub spec
        sub_spec = self.sub_spec

        # If have sub spec
        if sub_spec is not None:
            # Ensure the sub spec
            ensure_spec(spec=sub_spec, args=args, depending=arg_name)


class Option(BaseSpec):
    """
    Argument spec that requires given sub spec is ensured only if given \
        argument name exists.
    """

    def __init__(self, arg_name, sub_spec=None):
        """
        Constructor.

        :param arg_name: Argument name.

        :param sub_spec: Sub spec.

        :return: None.
        """
        # Store argument name
        self.arg_name = arg_name

        # Store sub spec
        self.sub_spec = sub_spec

    def __repr__(self):
        """
        Convert to string representation.

        :return: String.
        """
        # Return string representation
        return 'Option({0}, {1})'.format(
            repr(self.arg_name),
            repr(self.sub_spec),
        )

    def ensure_spec(self, args, depending):
        """
        Ensure this spec. Raise SpecViolationError if violated.

        :param args: Argument list.

        :param depending: Depending argument name.

        :return: None.
        """
        # Get argument name
        arg_name = self.arg_name

        # If the argument name exists
        if argument_exists(arg_name, args):
            # Get sub spec
            sub_spec = self.sub_spec

            # If have sub spec
            if sub_spec is not None:
                # Ensure the sub spec
                ensure_spec(spec=sub_spec, args=args, depending=arg_name)


class OneOf(BaseSpec):
    """
    Argument spec that requires exact one of given sub specs is ensured.
    """

    def __init__(self, *sub_specs):
        """
        Constructor.

        :param sub_specs: Sub spec list.

        Each sub spec must be argument name string, or Argument object. \
            Otherwise raise TypeError.

        :return: None.
        """
        # For each sub spec
        for sub_spec in sub_specs:
            # If the sub spec is not argument name string or Argument object
            if not isinstance(sub_spec, (str, Argument)):
                # Get error message
                msg = 'Expected string or Argument object. Got {0}.'.format(
                    repr(sub_spec)
                )

                # Raise error
                raise TypeError(msg)

        # Store sub specs
        self._sub_specs = list(sub_specs)

    def __iter__(self):
        """
        Get sub spec iterator.

        :return: Sub spec iterator.
        """
        # Return sub spec iterator
        return iter(self._sub_specs)

    def __repr__(self):
        """
        Convert to string representation.

        :return: String.
        """
        # Return string representation
        return 'OneOf({0})'.format(', '.join(repr(x) for x in self))

    def ensure_spec(self, args, depending):
        """
        Ensure this spec. Raise SpecViolationError if violated.

        :param args: Argument list.

        :param depending: Depending argument name.

        :return: None.
        """
        # Found argument's name
        found_arg_name = None

        # Found argument's spec
        found_sub_spec = None

        # Argument name list
        arg_name_s = []

        # This loop aims to collect given OneOf spec's all argument names.
        #
        # For this OneOf spec's each sub spec.
        for sub_spec in self._sub_specs:
            # If the sub spec is string
            if isinstance(sub_spec, str):
                # Use the string as argument name
                arg_name = sub_spec

            # If the sub spec is Argument spec
            elif isinstance(sub_spec, Argument):
                # Get the Argument spec's argument name
                arg_name = sub_spec.arg_name

            # If the sub spec is not string or Argument spec
            else:
                # Get error message
                msg = 'Expected string or Argument object. Got {0}.'.format(
                    repr(sub_spec)
                )

                # Raise error
                raise TypeError(msg)

            # Add the argument name to the argument name list
            arg_name_s.append(arg_name)

        # For this OneOf spec's each sub spec
        for sub_spec in self._sub_specs:
            # If the sub spec is string
            if isinstance(sub_spec, str):
                # Use the string as argument name
                arg_name = sub_spec

            # If the sub spec is Argument spec
            elif isinstance(sub_spec, Argument):
                # Get the Argument spec's argument name
                arg_name = sub_spec.arg_name

            # If the sub spec is not string or Argument spec
            else:
                # Get error message
                msg = 'Expected string or Argument object. Got {0}.'.format(
                    repr(sub_spec)
                )

                # Raise error
                raise TypeError(msg)

            # If the argument name exists
            if argument_exists(arg_name, args=args):
                # If have not found argument before
                if found_arg_name is None:
                    # Store the found argument's name
                    found_arg_name = arg_name

                    # Store the found argument's spec
                    found_sub_spec = sub_spec

                # If have found argument before.
                # This means the OneOf spec is violated.
                else:
                    # If depending argument name is given
                    if depending:
                        # Get error message
                        msg = (
                            'Argument {0} requires exact one of arguments {1}.'
                            ' Got {2} and {3}.'
                        ).format(
                            repr(depending),
                            repr(arg_name_s),
                            repr(found_arg_name),
                            repr(arg_name),
                        )
                    # If depending argument name is not given
                    else:
                        # Get error message
                        msg = (
                            'Require exact one of arguments {0}. Got {1} and'
                            ' {2}.'
                        ).format(
                            repr(arg_name_s),
                            repr(found_arg_name),
                            repr(arg_name),
                        )

                    # Raise error
                    raise SpecViolationError(msg, self)

        # If given OneOf spec has sub specs
        if arg_name_s:
            # If have not found argument name.
            # This means the OneOf spec is violated.
            if found_arg_name is None:
                # If depending argument name is given
                if depending:
                    # Get error message
                    msg = (
                        'Argument {0} requires exact one of arguments {1}.'
                        ' Got none.'
                    ).format(
                        repr(depending),
                        repr(arg_name_s),
                        repr(found_arg_name),
                        repr(arg_name),
                    )

                # If depending argument name is not given
                else:
                    # Get error message
                    msg = (
                        'Require exact one of arguments {0}. Got none.'
                    ).format(
                        repr(arg_name_s),
                        repr(found_arg_name),
                        repr(arg_name),
                    )

                # Raise error
                raise SpecViolationError(msg, self)

            # If have found argument name
            else:
                # Assert the found argument's spec is not None
                assert found_sub_spec is not None

                # Ensure the found argument's spec
                ensure_spec(
                    spec=found_sub_spec, args=args, depending=depending
                )


class AllOf(BaseSpec):
    """
    Argument spec that requires all given sub specs are ensured.
    """

    def __init__(self, *sub_specs):
        """
        Constructor.

        :param sub_specs: Sub spec list.

        :return: None.
        """
        # Store sub specs
        self._sub_specs = list(sub_specs)

    def __iter__(self):
        """
        Get sub spec iterator.

        :return: Sub spec iterator.
        """
        # Return sub spec iterator
        return iter(self._sub_specs)

    def __repr__(self):
        """
        Convert to string representation.

        :return: String.
        """
        # Return string representation
        return 'AllOf({0})'.format(', '.join(repr(x) for x in self))

    def ensure_spec(self, args, depending):
        """
        Ensure this spec. Raise SpecViolationError if violated.

        :param args: Argument list.

        :param depending: Depending argument name.

        :return: None.
        """
        # Argument name list
        arg_name_s = []

        # This loop aims to collect the AllOf spec's all argument names.
        #
        # For this AllOf spec's each sub spec.
        for sub_spec in self._sub_specs:
            # If the sub spec is string
            if isinstance(sub_spec, str):
                # Use the string as argument name
                arg_name = sub_spec

            # If the sub spec is Argument spec
            elif isinstance(sub_spec, Argument):
                # Get the Argument spec's argument name
                arg_name = sub_spec.arg_name

            # If the sub spec is not string or Argument spec
            else:
                # Get error message
                msg = 'Expected string or Argument object. Got {0}.'.format(
                    repr(sub_spec)
                )

                # Raise error
                raise TypeError(msg)

            # Add the argument name to the argument name list
            arg_name_s.append(arg_name)

        # For this AllOf spec's each sub spec
        for sub_spec in self._sub_specs:
            try:
                # Ensure the sub spec
                ensure_spec(spec=sub_spec, args=args, depending=depending)

            # If have error
            except SpecViolationError as exc:
                # Get violated spec
                violated_spec = exc.args[1]

                # If the violated spec is string or Argument spec
                if isinstance(violated_spec, (str, Argument)):
                    # For given AllOf spec's each sub spec
                    for sub_spec in self._sub_specs:
                        # If the sub spec is the violated spec
                        if sub_spec is violated_spec:
                            # If depending argument name is given
                            if depending:
                                # Get error message
                                msg = (
                                    'Argument {0} requires all of arguments'
                                    ' {1}.'
                                ).format(
                                    repr(depending),
                                    repr(arg_name_s),
                                )

                            # If depending argument name is not given
                            else:
                                # Get error message
                                msg = (
                                    'Require all of arguments {0}.'
                                ).format(
                                    repr(arg_name_s),
                                )

                            # Raise error
                            raise SpecViolationError(msg, self)

                # Raise original error
                raise


class SpecViolationError(Exception):
    """
    Error raised when an argument spec violation is detected.
    """


def argument_exists(arg_name, args):
    """
    Test whether given argument name exists in given argument list.

    :param arg_name: Argument name.

    :param args: Argument list.

    :return: Whether given argument name exists in given argument list.
    """
    # Create regular expression object that matches `^_ARG_$` or `^_ARG_=`
    re_obj = re.compile('^%s(?:$|=)' % arg_name)

    # For given argument list's each argument
    for arg in args:
        # If the argument matches the regular expression
        if re_obj.search(arg):
            # Return True
            return True

    # If none of the arguments matches the regular expression.
    else:
        # Return False
        return False


def ensure_argument_name(arg_name, args, depending=None):
    """
    Ensure given argument name exists in given argument list. Raise \
        SpecViolationError if violated.

    :param arg_name: Argument name.

    :param args: Argument list.

    :param depending: Depending argument name.

    :return: None.
    """
    # If given argument name not exists in given argument list
    if not argument_exists(arg_name, args):
        # If depending argument name is given
        if depending:
            # Get error message
            msg = 'Argument {0} requires argument {1}.'.format(
                repr(depending), repr(arg_name)
            )

        # If depending argument name is not given
        else:
            # Get error message
            msg = 'Require argument {0}.'.format(repr(arg_name))

        # Raise error
        raise SpecViolationError(msg, arg_name)


def ensure_spec(spec, args, depending=None):
    """
    Ensure given spec. Raise SpecViolationError if violated.

    :param spec: Spec.

    Can be:
        - String
        - Argument spec
        - Option spec
        - OneOf spec
        - AllOf spec

    :param args: Argument list.

    :param depending: Depending argument name.

    :return: None.
    """
    # If given spec is None
    if spec is None:
        # Return
        return

    # If given argument list is None
    if args is None:
        # Get error message
        msg = 'Expected argument list. Got None.'

        # Raise error
        raise TypeError(msg)

    # If given spec is string
    if isinstance(spec, str):
        # Ensure argument name
        ensure_argument_name(arg_name=spec, args=args, depending=depending)

    # If given spec is BaseSpec instance
    elif isinstance(spec, BaseSpec):
        # Ensure the spec
        spec.ensure_spec(args=args, depending=depending)

    # If given spec is none of above
    else:
        # Get error message
        msg = (
            'Expected string, Argument, Option, OneOf, or AllOf.'
            ' Got {0}.'
        ).format(repr(spec))

        # Raise error
        raise TypeError(msg)
