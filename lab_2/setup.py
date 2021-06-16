from setuptools import setup, find_packages

setup(
    name='converter',
    version='1.0.0',
    url='https://github.com/JuliaPlahotnikova',
    license='',
    author='Anomie',
    author_email='juliaplakh@gmail.com',
    description='Module for converting to most popular notations (such as JSON, TOML, YAML or Pickle)',
    packages=find_packages('.'),
    entry_points={
        'console_scripts': [
            'converter=Parsers.JSON.main:main',
        ],
    },
)
