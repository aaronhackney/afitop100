import setuptools
import codecs
import os


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setuptools.setup(
    name="afitop100",
    version=get_version("afitop100/__init__.py"),
    packages=setuptools.find_packages(),
    install_requires=["beautifulsoup4", "requests", "flask", "uwsgi"],
    license="Creative Commons Attribution-Noncommercial-Share Alike license",
    entry_points={"console_scripts": ["afitop100 = afitop100.__main__:main"]},
)