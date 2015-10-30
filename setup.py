from setuptools import setup, find_packages
import os


setup(
    name='designstandards',
    version="0.0",
    description='Open source UI components and visual style guide to create consistency and beautiful user experiences across U.S. federal government websites',
    author='Paul Tagliamonte',
    author_email='paul.tagliamonte@va.gov',
    url='',
    packages=find_packages(),
    package_data={
        'usa': [
            'static/*/css/*',
            'static/*/fonts/*',
            'static/*/js/*',
            'static/*/img/*',
            'templates/*/*/*',
        ]
    },
    license='',
    platforms=["any"],
)
