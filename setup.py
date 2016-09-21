"""Setup file for itango."""

from setuptools import setup


CLASSIFIERS = """\
Framework :: IPython
Intended Audience :: Developers
Intended Audience :: Science/Research
License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 3
Topic :: System :: Shells
""".splitlines()


setup(
    name='itango',
    version='0.0.1',

    py_modules=['itango'],
    install_requires=[
        'IPython>=0.10,<5',
        'PyTango>=7.2,<9'],

    license='LGPL',
    classifiers=CLASSIFIERS,
    author='Tiago Coutinho',
    author_email="coutinho@esrf.fr",
    description='Compatibility package for itango',
    long_description=open('README.rst').read(),
    url='https://github.com/tango-cs/itango',
    download_url='http://pypi.python.org/pypi/itango',
    platforms=['Linux', 'Windows XP/Vista/7/8'],
    keywords=['PyTango', 'IPython'],
    )
