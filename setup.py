from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='dicegame',
    version='0.1.5',
    packages=find_packages(),
    install_requires=[],
    long_description=readme,
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': ['dicegame = dicegame.main:main'],
    },
)
