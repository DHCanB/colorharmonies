# -*- coding: utf-8 -*-
from setuptools import setup

setup(name='test',
      version='1.0',
      description='Library to generate all your color harmonies with simplicity!',
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
      ],
      keywords='color management RGB harmonies complementary monochromatic analogous',
      url='https://github.com/DHCanB/colorharmonies',
      author=' ',
      author_email=' ',
      license='MIT',
      packages=['test'],
      python_requires='>=3',
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)