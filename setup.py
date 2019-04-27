from setuptools import setup, find_packages

setup(
    name='utils',
    version='1.0',
    author='Matheus Melo',
    install_requires=[
        "redis==3.0.1"
    ],
    packages=find_packages()
)
