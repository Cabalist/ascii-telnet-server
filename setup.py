# coding=utf-8

import setuptools
import os
import pypandoc

here = os.path.abspath(os.path.dirname(__file__))

long_description = pypandoc.convert(os.path.join(here, 'README.md'), 'rst')

setuptools.setup(
        name='ascii-telnet-Server',
        version='1.0',
        author="Martin W. Kirst",
        url="https://github.com/nitram509/ascii-telnet-server",
        packages=setuptools.find_packages(),
        data_files=[('ascii-telnet-server/movies', ['sample_movies/rick_roll.txt',
                                'sample_movies/sw1.txt',
                                'sample_movies/short_intro.txt', ])],
        extra_requires={'test': ['pytest']},
        license='BSD',
        description='ASCII art movie Telnet player',
        long_description=long_description,
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: End Users/Desktop',
            'Natural Language :: English',
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
        ]
)
