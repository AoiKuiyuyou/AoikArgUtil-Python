# AoikArgUtil-Python
Argparse utility and best practices.

Tested working with:
- Python 2.7, 3.2+

## Table of Contents
- [Setup](#setup)
  - [Setup via pip](#setup-via-pip)
    - [pip from Github](#pip-from-github)
  - [Setup via git](#setup-via-git)
- [Usage](#usage)
  - [Argument be str nonempty](#argument-be-str-nonempty)
  - [Argument be str nonempty after strip](#argument-be-str-nonempty-after-strip)
  - [Argument be either 0 or 1](#argument-be-either-0-or-1)
  - [Argument be int greater than 0](#argument-be-int-greater-than-0)
  - [Argument be int greater than or equal to 0](#argument-be-int-greater-than-or-equal-to-0)
  - [Argument be float greater than 0](#argument-be-float-greater-than-0)
  - [Argument be float greater than or equal to 0](#argument-be-float-greater-than-or-equal-to-0)
  - [Specify mutually exclusive argument pairs](#specify-mutually-exclusive-argument-pairs)
  - [Specify one of a list of arguments is required](#specify-one-of-a-list-of-arguments-is-required)
  - [Specify one argument requires another](#specify-one-argument-requires-another)
- [Argparse Best Practices](#argparse-best-practices)
  - [Separate an *argpsr* module from main module](#separate-an-argpsr-module-from-main-module)
  - [Separate an *argpsr_const* module from *argpsr* module](#separate-an-argpsr_const-module-from-argpsr-module)
  - [Use constants to synthesize depending values](#use-constants-to-synthesize-depending-values)
  - [Use *dest* constants to get argument values](#use-dest-constants-to-get-argument-values)
  - [How to specify complex exclusive/inclusive of arguments](#how-to-specify-complex-exclusiveinclusive-of-arguments)

## Setup

### Setup via pip

#### pip from Github
```
pip install git+https://github.com/AoiKuiyuyou/AoikArgUtil-Python
```

### Setup via git
Clone this repo to local
```
git clone https://github.com/AoiKuiyuyou/AoikArgUtil-Python
```

You can run the **setup.py** file in the local repo dir
```
python setup.py install
```
The effect is equivalent to installation via pip.

## Usage

### Argument be str nonempty
E.g.
```
from aoikargutil import str_nonempty
from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument(
        '-x',
        type=str_nonempty,
    )

    parser.parse_args(['-x', ''])
    ## main.py: error: argument -x: Empty value is not allowed.
```
- ```str_nonempty``` is defined [here](/src/aoikargutil/aoikargutil.py#L11)

### Argument be str nonempty after strip
E.g.
```
from aoikargutil import str_strip_nonempty
from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument(
        '-x',
        type=str_strip_nonempty,
    )

    parser.parse_args(['-x', '   '])
    ## main.py: error: argument -x: Empty value is not allowed.
```
- ```str_strip_nonempty``` is defined [here](/src/aoikargutil/aoikargutil.py#L18)

### Argument be either 0 or 1
E.g.
```
from aoikargutil import bool_0or1
from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument(
        '-x',
        type=bool_0or1,
    )

    parser.parse_args(['-x', '2'])
    ## main.py: error: argument -x: |2| is not 0 or 1.
```
- ```bool_0or1``` is defined [here](/src/aoikargutil/aoikargutil.py#L29)

### Argument be int greater than 0
E.g.
```
from aoikargutil import int_gt0
from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument(
        '-x',
        type=int_gt0,
    )

    parser.parse_args(['-x', '0'])
    ## main.py: error: argument -x: |0| is not a positive integer.
```
- ```int_gt0``` is defined [here](/src/aoikargutil/aoikargutil.py#L56)

### Argument be int greater than or equal to 0
E.g.
```
from aoikargutil import int_ge0
from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument(
        '-x',
        type=int_ge0,
    )

    parser.parse_args(['-x', '-1'])
    ## main.py: error: argument -x: |-1| is not zero or a positive integer.
```
- ```int_ge0``` is defined [here](/src/aoikargutil/aoikargutil.py#L65)

### Argument be float greater than 0
E.g.
```
from aoikargutil import float_gt0
from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument(
        '-x',
        type=float_gt0,
    )

    parser.parse_args(['-x', '0.0'])
    ## main.py: error: argument -x: |0.0| is not a positive number.
```
- ```float_gt0``` is defined [here](/src/aoikargutil/aoikargutil.py#L38)

### Argument be float greater than or equal to 0
E.g.
```
from aoikargutil import float_ge0
from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument(
        '-x',
        type=float_ge0,
    )

    parser.parse_args(['-x', '-1.0'])
    ## main.py: error: argument -x: |-1.0| is not zero or a positive number.
```
- ```float_ge0``` is defined [here](/src/aoikargutil/aoikargutil.py#L47)

### Specify mutually exclusive argument pairs
Take program **AoikFuncit** for exmaple.  
[Here](https://github.com/AoiKuiyuyou/AoikFuncit-Python/tree/28dd658a370dabe2574a7c472f05fb34f8936024/src/aoikfuncit/argpsr_const.py#L92),
defines a list of mutually exclusive argument pairs.  
[Here](https://github.com/AoiKuiyuyou/AoikFuncit-Python/tree/28dd658a370dabe2574a7c472f05fb34f8936024/src/aoikfuncit/main_imp.py#L68),
calls [ensure_exc_pairs](/src/aoikargutil/aoikargutil.py#L74) to enforce the rule.

**itertools**'s **combinations** and **product** are good tools for generating these pairs.

### Specify one of a list of arguments is required
Take program **AoikFuncit** for exmaple.  
[Here](https://github.com/AoiKuiyuyou/AoikFuncit-Python/tree/28dd658a370dabe2574a7c472f05fb34f8936024/src/aoikfuncit/argpsr_const.py#L104),
defines a list of arguments, one of which is required to be present.  
[Here](https://github.com/AoiKuiyuyou/AoikFuncit-Python/tree/28dd658a370dabe2574a7c472f05fb34f8936024/src/aoikfuncit/main_imp.py#L70),
calls [ensure_req_one](/src/aoikargutil/aoikargutil.py#L100) to enforce the rule.

### Specify one argument requires another
Take program **AoikFuncit** for exmaple.  
[Here](https://github.com/AoiKuiyuyou/AoikFuncit-Python/tree/28dd658a370dabe2574a7c472f05fb34f8936024/src/aoikfuncit/argpsr_const.py#L113),
defines a list of dependent argument pairs, the left requiring the right.  
[Here](https://github.com/AoiKuiyuyou/AoikFuncit-Python/tree/28dd658a370dabe2574a7c472f05fb34f8936024/src/aoikfuncit/main_imp.py#L72),
calls [ensure_req_pairs](/src/aoikargutil/aoikargutil.py#L128) to enforce the rule.

## Argparse Best Practices
Below are best practices I recommend when using **argparse**.

### Separate an *argpsr* module from main module
Put **argparse**-related code in an **argpsr** module.
This keeps your main module from being bloated.

Take program **AoikFuncit** for exmaple.  
The **argpsr** module provides a [parser_make](https://github.com/AoiKuiyuyou/AoikFuncit-Python/tree/28dd658a370dabe2574a7c472f05fb34f8936024/src/aoikfuncit/argpsr.py#L61) function.  
The main module simply imports and [uses this function](https://github.com/AoiKuiyuyou/AoikFuncit-Python/tree/28dd658a370dabe2574a7c472f05fb34f8936024/src/aoikfuncit/main_imp.py#L65).

### Separate an *argpsr_const* module from *argpsr* module
Define constants in an **argpsr_const** module for values fed to
 **add_argument** calls in **argpsr** module. This makes adjusting of these
 values much easier, and makes code using these values more resilient to
 changes.

Take program **AoikFuncit** for exmaple.  
The **argpsr_const** module is [here](https://github.com/AoiKuiyuyou/AoikFuncit-Python/tree/28dd658a370dabe2574a7c472f05fb34f8936024/src/aoikfuncit/argpsr_const.py).  
These constants are used in **argpsr** module [this way](https://github.com/AoiKuiyuyou/AoikFuncit-Python/tree/28dd658a370dabe2574a7c472f05fb34f8936024/src/aoikfuncit/argpsr.py#L66).

### Use constants to synthesize depending values
This makes depending values resilient to changes of dependent values.

Take program **AoikFuncit** for exmaple.  
[Here](https://github.com/AoiKuiyuyou/AoikFuncit-Python/tree/28dd658a370dabe2574a7c472f05fb34f8936024/src/aoikfuncit/argpsr_const.py#L39),
 the argument's help message ```ARG_TIMEIT_ON_H``` is synthesized according to the
 argument's default value ```ARG_TIMEIT_ON_D```.

### Use *dest* constants to get argument values
This makes code resilient to changes of **dest** values.  

Take program **AoikFuncit** for exmaple.  
[Here](https://github.com/AoiKuiyuyou/AoikFuncit-Python/tree/28dd658a370dabe2574a7c472f05fb34f8936024/src/aoikfuncit/argpsr_const.py#L10)
 defines constant ```ARG_EXPR_K``` for **dest** value.  
[Here](https://github.com/AoiKuiyuyou/AoikFuncit-Python/tree/28dd658a370dabe2574a7c472f05fb34f8936024/src/aoikfuncit/argpsr.py#L68)
 the constant is fed to ```add_argument```.  
[Here](https://github.com/AoiKuiyuyou/AoikFuncit-Python/tree/28dd658a370dabe2574a7c472f05fb34f8936024/src/aoikfuncit/main_imp.py#L81)
 the constant is used to get argument value.

You can go futher by using [garbled characters](https://github.com/AoiKuiyuyou/AoikFuncit-Python/tree/28dd658a370dabe2574a7c472f05fb34f8936024/src/aoikfuncit/argpsr_const.py#L10)
 for **dest** values, making it impossible to hardcode them.

### How to specify complex exclusive/inclusive of arguments
**argparse**'s [add_mutually_exclusive_group](https://docs.python.org/2/library/argparse.html#argparse.ArgumentParser.add_mutually_exclusive_group) makes arguments within a group
 mutually exclusive. If there are more than one group, however, it requires
 that one argument can only be in one of the groups.

Attempts have been made to support more complex exclusive/inclusive cases:
- [http://bugs.python.org/issue10984](http://bugs.python.org/issue10984)
- [http://bugs.python.org/issue11588](http://bugs.python.org/issue11588)

My solution has been provided in this repo, see
- [Specify mutually exclusive argument pairs](#specify-mutually-exclusive-argument-pairs)
- [Specify one of a list of arguments is required](#specify-one-of-a-list-of-arguments-is-required)
- [Specify one argument requires another](#specify-one-argument-requires-another)
