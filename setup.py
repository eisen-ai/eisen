from setuptools import setup, find_packages


VERSION = '0.1.8'

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

setup(
    name='eisen',
    version=VERSION,
    description='Eisen Meta Package (installs all components of Eisen)',
    packages=find_packages(),
    install_requires=install_requires,
    python_requires='>=3.6',
)