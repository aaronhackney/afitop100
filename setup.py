import setuptools
import re

def find_version():
    with open("afitop100/__init__.py") as fp:
        for line in fp:
            match = re.search(r"__version__\s*=\s*'([^']+)", line)
            if match is not None:
                return match.group(1)
    assert False, 'cannot find version'

setuptools.setup(
    name='afitop100',
    version=find_version(),
    packages=['afitop100',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
)