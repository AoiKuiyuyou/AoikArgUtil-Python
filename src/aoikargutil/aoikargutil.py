# coding: utf-8
from __future__ import absolute_import
from argparse import ArgumentTypeError
import re
import sys

#/
__version__ = '0.1'

#/
def str_nonempty(txt):
    if txt != '':
        return txt
    else:
        raise ArgumentTypeError('Empty value is not allowed.')

#/
def str_strip_nonempty(txt):
    #/
    txt = txt.strip()

    #/
    if txt != '':
        return txt
    else:
        raise ArgumentTypeError('Empty value is not allowed.')

#/
def bool_0or1(txt):
    if txt == '0':
        return False
    elif txt == '1':
        return True
    else:
        raise ArgumentTypeError('|%s| is not 0 or 1.' % txt)

#/
def float_gt0(txt):
    try:
        val = float(txt)
        assert val > 0
    except Exception:
        raise ArgumentTypeError('|%s| is not a positive number.' % txt)
    return val

#/
def float_ge0(txt):
    try:
        val = float(txt)
        assert val >= 0
    except Exception:
        raise ArgumentTypeError('|%s| is not zero or a positive number.' % txt)
    return val

#/
def int_gt0(txt):
    try:
        val = int(txt)
        assert val > 0
    except Exception:
        raise ArgumentTypeError('|%s| is not a positive integer.' % txt)
    return val

#/
def int_ge0(txt):
    try:
        val = int(txt)
        assert val >= 0
    except Exception:
        raise ArgumentTypeError('|%s| is not zero or a positive integer.' % txt)
    return val

#/
def ensure_exc_pairs(parser, pairs, args=None):
    #/
    if args is None:
        args = sys.argv[1:]

    #/
    for pair in pairs:
        #/
        arg_a, arg_b = pair

        arg_a_rec = re.compile('^%s($|=|[0-9])' % arg_a)

        arg_b_rec = re.compile('^%s($|=|[0-9])' % arg_b)

        #/
        if any(map(lambda x: bool(arg_a_rec.search(x)), args))\
        and any(map(lambda x: bool(arg_b_rec.search(x)), args)):
            #/
            msg = 'argument %s: not allowed with argument %s' % (arg_a, arg_b)

            parser.error(msg)
            ## raise error

            assert False

#/
def ensure_req_one(parser, names, args=None):
    #/
    if args is None:
        args = sys.argv[1:]

    #/
    arg_name_exists = False

    for arg_name in names:
        #/
        arg_name_rec = re.compile('^%s($|=|[0-9])' % arg_name)

        #/
        arg_name_exists = any(map(lambda x: bool(arg_name_rec.search(x)), args))

        if arg_name_exists:
            return

    #/
    if not arg_name_exists:
        msg = """one of the arguments %s is required""" % (', '.join(names))

        parser.error(msg)
        ## raise error

        assert False

#/
def ensure_req_pairs(parser, pairs, args=None):
    #/
    if args is None:
        args = sys.argv[1:]

    #/
    for pair in pairs:
        #/
        arg_a, arg_b = pair

        arg_a_rec = re.compile('^%s($|=|[0-9])' % arg_a)

        arg_b_rec = re.compile('^%s($|=|[0-9])' % arg_b)

        #/
        if any(map(lambda x: bool(arg_a_rec.search(x)), args))\
        and not any(map(lambda x: bool(arg_b_rec.search(x)), args)):
            #/
            msg = 'argument %s: requires argument %s' % (arg_a, arg_b)

            parser.error(msg)
            ## raise error

            assert False
