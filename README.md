# AoikArgUtil-Python
Argparse utility and best practices.

Tested working with:
- Python 2.7+, 3.2+

## Table of Contents
- [Setup](#setup)
  - [Setup via pip](#setup-via-pip)
  - [Setup via git](#setup-via-git)
- [Usage](#usage)
  - [Argument be str nonempty](#argument-be-str-nonempty)
  - [Argument be str nonempty after strip](#argument-be-str-nonempty-after-strip)
  - [Argument be either 0 or 1](#argument-be-either-0-or-1)
  - [Argument be int greater than 0](#argument-be-int-greater-than-0)
  - [Argument be int greater than or equal to 0](#argument-be-int-greater-than-or-equal-to-0)
  - [Argument be float greater than 0](#argument-be-float-greater-than-0)
  - [Argument be float greater than or equal to 0](#argument-be-float-greater-than-or-equal-to-0)
  - [Specify one of arguments is required](#specify-one-of-arguments-is-required)
  - [Specify one argument requires another](#specify-one-argument-requires-another)
  - [Specify mutually exclusive arguments](#specify-mutually-exclusive-arguments)
- [Argparse Best Practices](#argparse-best-practices)
  - [Separate an *argpsr* module from main module](#separate-an-argpsr-module-from-main-module)
  - [Separate an *argpsr_const* module from *argpsr* module](#separate-an-argpsr_const-module-from-argpsr-module)
  - [Use constants to synthesize depending values](#use-constants-to-synthesize-depending-values)
  - [Use *dest* constants to get argument values](#use-dest-constants-to-get-argument-values)
  - [Specify complex exclusive/inclusive of arguments](#specify-complex-exclusiveinclusive-of-arguments)

## Setup

### Setup via pip
Run
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
- ```str_nonempty``` is defined [here](/src/aoikargutil/aoikargutil.py#L12)

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
- ```str_strip_nonempty``` is defined [here](/src/aoikargutil/aoikargutil.py#L19)

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
- ```bool_0or1``` is defined [here](/src/aoikargutil/aoikargutil.py#L30)

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
- ```int_gt0``` is defined [here](/src/aoikargutil/aoikargutil.py#L57)

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
- ```int_ge0``` is defined [here](/src/aoikargutil/aoikargutil.py#L66)

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
- ```float_gt0``` is defined [here](/src/aoikargutil/aoikargutil.py#L39)

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
- ```float_ge0``` is defined [here](/src/aoikargutil/aoikargutil.py#L48)

### Specify one of arguments is required
Take program **AoikFuncit** for exmaple.  
[Here](https://github.com/AoiKuiyuyou/AoikFuncit-Python/blob/0.1.1/src/aoikfuncit/argpsr_const.py#L107),
uses `SPEC_DI_K_ONE` to specify required arguments.  
[Here](https://github.com/AoiKuiyuyou/AoikFuncit-Python/blob/0.1.1/src/aoikfuncit/main_imp.py#L75),
calls [ensure_spec](/src/aoikargutil/aoikargutil.py#L364) to ensure the rules.

`SPEC_DI_K_ONE`'s value can be tuple or list.  
If it's a tuple, it's considered one argument group. E.g.
```
SPEC_DI_K_ONE: ('-a', '-b')
# means
SPEC_DI_K_ONE: [
    ('-a', '-b'),
]
```

If it's a list, it's considered a list of argument groups. E.g.
```
SPEC_DI_K_ONE: [
    ('-a', '-b'),
    ('-c', '-d'),
]
```

Required arguments are checked within each argument group, not among groups.

Argument group's value can be tuple or list.  
If it's a tuple, it means "one and only one" argument in the group is required. E.g.
```
('-a', '-b')
```
If it's a list, it means "one or more" arguments in the group are required. E.g.
```
['-a', '-b']
```

### Specify one argument requires another
Take program **AoikFuncit** for exmaple.  
[Here](https://github.com/AoiKuiyuyou/AoikFuncit-Python/blob/0.1.1/src/aoikfuncit/argpsr_const.py#L116),
uses `SPEC_DI_K_TWO` to specify argument pairs, the left requiring the right.  
[Here](https://github.com/AoiKuiyuyou/AoikFuncit-Python/blob/0.1.1/src/aoikfuncit/main_imp.py#L75),
calls [ensure_spec](/src/aoikargutil/aoikargutil.py#L364) to ensure the rules.

`SPEC_DI_K_TWO`'s value can be tuple or list.  
If it's a tuple, it's considered one argument pair. E.g.
```
SPEC_DI_K_TWO: ('-a', '-b')
# means
SPEC_DI_K_TWO: [
    ('-a', '-b'),
]
```

If it's a list, it's considered a list of argument pairs. E.g.
```
SPEC_DI_K_TWO: [
    ('-a', '-b'),
    ('-c', '-d'),
]
```

### Specify mutually exclusive arguments
Take program **AoikFuncit** for exmaple.  
[Here](https://github.com/AoiKuiyuyou/AoikFuncit-Python/blob/0.1.1/src/aoikfuncit/argpsr_const.py#L124),
uses `SPEC_DI_K_EXC` to specify mutually exclusive arguments.  
[Here](https://github.com/AoiKuiyuyou/AoikFuncit-Python/blob/0.1.1/src/aoikfuncit/main_imp.py#L75),
calls [ensure_spec](/src/aoikargutil/aoikargutil.py#L364) to ensure the rules.

`SPEC_DI_K_EXC`'s value can be tuple or list.  
If it's a tuple, it's considered one argument group. E.g.
```
SPEC_DI_K_EXC: ('-a', '-b')
# means
SPEC_DI_K_EXC: [
    ('-a', '-b'),
]
```

If it's a list, it's considered a list of argument groups. E.g.
```
SPEC_DI_K_EXC: [
    ('-a', '-b'),
    ('-c', '-d'),
]
```

Mutually exclusive arguments are checked within each argument group, not among
 groups.

Argument group's value can be tuple or list (no difference). E.g.
```
# argument group
['-a', '-b', '-c']
# transforms to mutually exclusive pairs
[('-a', '-b'), ('-a', '-c'), ('-b', '-c')]
```

If an argument group has two arguments, and the second is a tuple or list, it's
 considered as special syntax. E.g.
```
# argument group
['-a', ['-b', '-c']]
# transforms to mutually exclusive pairs
[('-a', '-b'), ('-a', '-c')]
```

## Argparse Best Practices
Below are best practices I recommend when using **argparse**.

### Separate an *argpsr* module from main module
Put **argparse**-related code in an **argpsr** module.
This keeps your main module from being bloated.

Take program **AoikFuncit** for exmaple.  
The **argpsr** module provides a [parser_make](https://github.com/AoiKuiyuyou/AoikFuncit-Python/blob/0.1.1/src/aoikfuncit/argpsr.py#L69) function.  
The main module simply imports and [uses this function](https://github.com/AoiKuiyuyou/AoikFuncit-Python/blob/0.1.1/src/aoikfuncit/main_imp.py#L69).

### Separate an *argpsr_const* module from *argpsr* module
Define constants in an **argpsr_const** module for values fed to
 **add_argument** calls in **argpsr** module. This makes adjusting of these
 values much easier, and makes code using these values more resilient to
 changes.

Take program **AoikFuncit** for exmaple.  
The **argpsr_const** module is [here](https://github.com/AoiKuiyuyou/AoikFuncit-Python/blob/0.1.1/src/aoikfuncit/argpsr_const.py).  
These constants are used in **argpsr** module [this way](https://github.com/AoiKuiyuyou/AoikFuncit-Python/blob/0.1.1/src/aoikfuncit/argpsr.py#L75).

### Use constants to synthesize depending values
This makes depending values resilient to changes of dependent values.

Take program **AoikFuncit** for exmaple.  
[Here](https://github.com/AoiKuiyuyou/AoikFuncit-Python/blob/0.1.1/src/aoikfuncit/argpsr_const.py#L49),
 the argument's help message ```ARG_TIMEIT_ON_H``` is synthesized according to the
 argument's default value ```ARG_TIMEIT_ON_D```.

### Use *dest* constants to get argument values
This makes code resilient to changes of **dest** values.  

Take program **AoikFuncit** for exmaple.  
[Here](https://github.com/AoiKuiyuyou/AoikFuncit-Python/blob/0.1.1/src/aoikfuncit/argpsr_const.py#L12)
 defines constant ```ARG_EXPR_K``` for **dest** value.  
[Here](https://github.com/AoiKuiyuyou/AoikFuncit-Python/blob/0.1.1/src/aoikfuncit/argpsr.py#L76)
 the constant is fed to ```add_argument```.  
[Here](https://github.com/AoiKuiyuyou/AoikFuncit-Python/blob/0.1.1/src/aoikfuncit/main_imp.py#L92)
 the constant is used to get argument value.

You can go futher by using [garbled characters](https://github.com/AoiKuiyuyou/AoikFuncit-Python/blob/0.1.1/src/aoikfuncit/argpsr_const.py#L13)
 for **dest** values, making it impossible to hardcode them.

### Specify complex exclusive/inclusive of arguments
**argparse**'s [add_mutually_exclusive_group](https://docs.python.org/2/library/argparse.html#argparse.ArgumentParser.add_mutually_exclusive_group) makes arguments within a group
 mutually exclusive. If there are more than one group, however, it requires
 that one argument can only be in one of the groups.

Attempts have been made to support more complex exclusive/inclusive cases:
- [http://bugs.python.org/issue10984](http://bugs.python.org/issue10984)
- [http://bugs.python.org/issue11588](http://bugs.python.org/issue11588)

My solution has been provided in this repo, see
- [Specify one of arguments is required](#specify-one-of-arguments-is-required)
- [Specify one argument requires another](#specify-one-argument-requires-another)
- [Specify mutually exclusive arguments](#specify-mutually-exclusive-arguments)
