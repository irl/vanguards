"""setup.py: setuptools control."""

import io
import os

from setuptools import find_packages
from setuptools import setup

# Read version and other info from package's __init.py file
module_info = {}
init_path = os.path.join(os.path.dirname(__file__), "src", 'vanguards',
                         '__init__.py')
with open(init_path) as init_file:
    exec(init_file.read(), module_info)


def read(*names, **kwargs):
    return io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ).read()

setup(
    name="vanguards",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        "console_scripts": [
            'vanguards = vanguards.vanguards:main',
        ]},
    description="Vanguards help guard you from getting vanned...",
    long_description=read('README.md'),
    include_package_data=True,
    version=module_info.get('__version__'),
    author=module_info.get('__author__'),
    author_email=module_info.get('__contact__'),
    url=module_info.get('__url__'),
    license=module_info.get('__license__'),
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    keywords='tor',
    install_requires=[
        'setuptools',
        'stem>=1.2.2',
        ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License (MIT)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ]
)
