import os
import sys

try:
    from setuptools import setup
    setup
except ImportError:
    from distutils.core import setup

from radosgw import __version__


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='radosgw-admin',
    version=__version__,
    author='Valery Tschopp',
    author_email='valery.tschopp@switch.ch',
    include_package_data=True,
    install_requires = ['boto'],
    py_modules=['radosgw'],
    url='https://github.com/valerytschopp/python-radosgw-admin',
    license='Apache2, see LICENCE',
    description='Ceph RADOS Gateway admin operations REST API',
    long_description=open('README.md').read(),
)
