# coding: utf-8
from setuptools import find_packages
from setuptools import setup

setup(
    name='AoikArgUtil',

    version='0.1.1',

    description="""Argparse utility and best practices.""",

    long_description="""`Documentation on Github
<https://github.com/AoiKuiyuyou/AoikArgUtil-Python>`_""",

    url='https://github.com/AoiKuiyuyou/AoikArgUtil-Python',

    author='Aoi.Kuiyuyou',

    author_email='aoi.kuiyuyou@google.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='argparse utility best practices',

    package_dir={'':'src'},

    packages=find_packages('src'),
)
