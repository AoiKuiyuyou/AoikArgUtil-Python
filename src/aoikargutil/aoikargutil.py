# coding: utf-8
from __future__ import absolute_import
from argparse import ArgumentTypeError
import re
import sys

#/
__version__ = '0.1.1'

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
def float_lt0(txt):
    try:
        val = float(txt)
        assert val < 0
    except Exception:
        raise ArgumentTypeError('|%s| is not a negative number.' % txt)
    return val

#/
def float_le0(txt):
    try:
        val = float(txt)
        assert val <= 0
    except Exception:
        raise ArgumentTypeError('|%s| is not zero or a negative number.' % txt)
    return val

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
def int_lt0(txt):
    try:
        val = int(txt)
        assert val < 0
    except Exception:
        raise ArgumentTypeError('|%s| is not a negative integer.' % txt)
    return val

#/
def int_le0(txt):
    try:
        val = int(txt)
        assert val <= 0
    except Exception:
        raise ArgumentTypeError('|%s| is not zero or a negative integer.' % txt)
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
        arg_a_spec, arg_b_spec = pair
        
        #/
        if isinstance(arg_a_spec, (list, tuple)):
            arg_a_s = arg_a_spec
        else:
            arg_a_s = [arg_a_spec]
            
        #/
        for arg_a in arg_a_s:
            #/
            arg_a_rec = re.compile('^%s($|=|[0-9])' % arg_a)
            
            #/
            arg_a_exists = any(bool(arg_a_rec.search(arg)) for arg in args)
            
            #/
            if arg_a_exists:
                #/
                if isinstance(arg_b_spec, (list, tuple)):
                    #/
                    arg_b_s = arg_b_spec
                else:
                    #/
                    arg_b_s = [arg_b_spec]
                
                #/
                arg_b_rec_s = [re.compile('^%s($|=|[0-9])' % arg_b) for arg_b in arg_b_s]
                
                #/
                if isinstance(arg_b_spec, list):
                    req_all_arg_bs = True
                else:
                    req_all_arg_bs = False
                    
                #/
                arg_b_exists = False
                
                for arg_b_rec in arg_b_rec_s:
                    #/
                    arg_b_exists = any(bool(arg_b_rec.search(arg)) for arg in args)
                    
                    #/
                    if arg_b_exists:
                        if not req_all_arg_bs:
                            break
                    else:
                        if req_all_arg_bs:
                            break
                
                #/
                if not arg_b_exists:
                    #/
                    if isinstance(arg_b_spec, list):
                        #/
                        msg = 'argument %s: requires all of the arguments %s' % (arg_a, ', '.join(arg_b_spec))
            
                        parser.error(msg)
                        ## raise error
                    #/
                    elif isinstance(arg_b_spec, tuple):
                        #/
                        msg = 'argument %s: requires one of the arguments %s' % (arg_a, ', '.join(arg_b_spec))
            
                        parser.error(msg)
                        ## raise error
                    else:
                        #/
                        msg = 'argument %s: requires argument %s' % (arg_a, arg_b_spec)
            
                        parser.error(msg)
                        ## raise error
                    
                    #/
                    assert False
