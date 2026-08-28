from setuptools import setup
from os import path


__version__ = '0.1.0'
__author__ = 'Hezekiah Michael'  # primarily Scott Doucet
__url__ = 'https://github.com/holyspiritomb/YuleLog'

SETUP_DIR = path.abspath(path.dirname(__file__))


__long_description__ = """
``YuleLog`` is an ascii yule log fireplace for your terminal with snowfall and customizable text.
"""

install_requires = [
    'asciimatics == 1.15.0',
    'Pillow == 12.3.0',
    'setuptools < 81',
    'pyfiglet == 1.0.4'
]

setup(
    name='YuleLog',
    version=__version__,
    author=__author__,
    license='MIT License',
    url=__url__,
    packages=['yule_log'],
    package_data={'yule_log': ['yule_log.ico']},
    description='Terminal-based Yule log Fireplace',
    long_description=__long_description__,
    keywords='christmas yule fireplace winter holiday',
    install_requires=install_requires,
    python_requires=">=3.10",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Games/Entertainment',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
    ],
    entry_points={
          'console_scripts': [
              'YuleLog = yule_log.__main__:main'
          ]
      }
)
