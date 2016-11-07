[:var_set('', """
# Compile command
aoikdyndocdsl -s README.src.md -n aoikdyndocdsl.ext.all::nto -g README.md
""")
]\
[:HDLR('heading', 'heading')]\
# AoikArgUtil-Python
Python **argparse** library's utility library.

Tested working with:
- Python 2.7 and 3.5
- Linux
- MacOS
- Windows

## Table of Contents
[:toc(beg='next', indent=-1)]

## Setup
[:tod()]

### Setup via pip
Run:
```
pip install git+https://github.com/AoiKuiyuyou/AoikArgUtil-Python
```

### Setup via git
Run:
```
git clone https://github.com/AoiKuiyuyou/AoikArgUtil-Python

cd AoikArgUtil-Python

python setup.py install
```

## Usage
[:tod()]

### Ensure argument is nonempty
Code:
```
from argparse import ArgumentParser
from aoikargutil import str_nonempty


parser = ArgumentParser()

parser.add_argument(
    '-a',
    type=str_nonempty,
)

args = parser.parse_args(['-a', 'value'])
print(args)
# Namespace(a='value')

args = parser.parse_args(['-a', ' '])
print(args)
# Namespace(a=' ')

args = parser.parse_args(['-a', ''])
# Error: Expected a non-empty string. Got: ''.
```

### Ensure argument is nonempty after strip
Code:
```
from argparse import ArgumentParser
from aoikargutil import str_strip_nonempty


parser = ArgumentParser()

parser.add_argument(
    '-a',
    type=str_strip_nonempty,
)

args = parser.parse_args(['-a', 'value'])
print(args)
# Namespace(a='value')

args = parser.parse_args(['-a', ' '])
# Error: Expected a non-empty and non-whitespace-only string. Got: ' '.
```

### Ensure argument is boolean
Code:
```
from argparse import ArgumentParser
from aoikargutil import bool_0or1


parser = ArgumentParser()

parser.add_argument(
    '-a',
    type=bool_0or1,
)

args = parser.parse_args(['-a', '0'])
print(args)
# Namespace(a=False)

args = parser.parse_args(['-a', '1'])
print(args)
# Namespace(a=True)

args = parser.parse_args(['-a', '2'])
# Error: Expected '0' or '1'. Got: '2'.
```

### Ensure argument is int
Code:
```
from argparse import ArgumentParser
from aoikargutil import int_ge0
from aoikargutil import int_gt0
from aoikargutil import int_le0
from aoikargutil import int_lt0


parser = ArgumentParser()

parser.add_argument(
    '-a',
    type=int_ge0,
)

args = parser.parse_args(['-a', '0'])
print(args)
# Namespace(a=0)

args = parser.parse_args(['-a', '1'])
print(args)
# Namespace(a=1)

args = parser.parse_args(['-a', '-1'])
# Expected an integer >=0. Got: '-1'.
```

### Ensure argument is float
Code:
```
from argparse import ArgumentParser
from aoikargutil import float_ge0
from aoikargutil import float_gt0
from aoikargutil import float_le0
from aoikargutil import float_lt0


parser = ArgumentParser()

parser.add_argument(
    '-a',
    type=float_ge0,
)

args = parser.parse_args(['-a', '0'])
print(args)
# Namespace(a=0)

args = parser.parse_args(['-a', '0.1'])
print(args)
# Namespace(a=0.1)

args = parser.parse_args(['-a', '-0.1'])
# Expected a float >=0. Got: '-0.1'.
```

### Ensure one of arguments is given
Code:
```
from argparse import ArgumentParser
from aoikargutil import ensure_spec
from aoikargutil import OneOf


ensure_spec(spec=OneOf('-a', '-b'), args=['-a'])
# OK

ensure_spec(spec=OneOf('-a', '-b'), args=['-b'])
# OK

ensure_spec(spec=OneOf('-a', '-b'), args=[])
# Error: Require exact one of arguments ['-a', '-b']. Got none.

ensure_spec(spec=OneOf('-a', '-b'), args=['-a', '-b'])
# Error: Require exact one of arguments ['-a', '-b']. Got '-a' and '-b'.
```

### Ensure all of arguments are given
Code:
```
from argparse import ArgumentParser
from aoikargutil import AllOf
from aoikargutil import ensure_spec


ensure_spec(spec=AllOf('-a', '-b'), args=['-a', '-b'])
# OK

ensure_spec(spec=AllOf('-a', '-b'), args=[])
# Error: Require all of arguments ['-a', '-b'].

ensure_spec(spec=AllOf('-a', '-b'), args=['-a'])
# Error: Require all of arguments ['-a', '-b'].

ensure_spec(spec=AllOf('-a', '-b'), args=['-b'])
# Error: Require all of arguments ['-a', '-b'].
```

### Ensure argument dependency
Code:
```
from argparse import ArgumentParser
from aoikargutil import AllOf
from aoikargutil import Argument
from aoikargutil import ensure_spec
from aoikargutil import OneOf
from aoikargutil import Option


ensure_spec(spec=Argument('-a', '-b'), args=['-a', '-b'])
# OK

ensure_spec(spec=Argument('-a', '-b'), args=['-a'])
# Error: Argument '-a' requires argument '-b'.

ensure_spec(spec=Argument('-a', Argument('-b', '-c')), args=['-a', '-b'])
# Error: Argument '-b' requires argument '-c'.

ensure_spec(spec=Argument('-a', OneOf('-b', '-c')), args=['-a'])
# Error: Argument '-a' requires exact one of arguments ['-b', '-c']. Got none.

ensure_spec(spec=Argument('-a', AllOf('-b', '-c')), args=['-a'])
# Error: Argument '-a' requires all of arguments ['-b', '-c'].

ensure_spec(spec=Option('-a', '-b'), args=['-a', '-b'])
# OK

ensure_spec(spec=Option('-a', '-b'), args=[])
# OK

ensure_spec(spec=Option('-a', '-b'), args=['-a'])
# Error: Argument '-a' requires argument '-b'.

ensure_spec(spec=Option('-a', Option('-b', '-c')), args=['-a'])
# OK

ensure_spec(spec=Option('-a', Option('-b', '-c')), args=['-b'])
# OK

ensure_spec(spec=Option('-a', Option('-b', '-c')), args=['-a', '-b'])
# Error: Argument '-b' requires argument '-c'.

ensure_spec(spec=Option('-a', OneOf('-b', '-c')), args=[])
# OK

ensure_spec(spec=Option('-a', OneOf('-b', '-c')), args=['-a'])
# Error: Argument '-a' requires exact one of arguments ['-b', '-c']. Got none.

ensure_spec(spec=Option('-a', AllOf('-b', '-c')), args=[])
# OK

ensure_spec(spec=Option('-a', AllOf('-b', '-c')), args=['-a'])
# Error: Argument '-a' requires all of arguments ['-b', '-c'].
```
