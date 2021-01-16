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


#  def find_version():
#      with open("afitop100/__init__.py") as fp:
#          for line in fp:
#              match = re.search(r"__version__\s*=\s*'([^']+)", line)
#              if match is not None:
#                  return match.group(1)
#      assert False, "cannot find version"


setuptools.setup(
    name="afitop100",
    version=get_version("afitop100/__init__.py"),
    packages=setuptools.find_packages(),
    install_requires=["beautifulsoup4", "requests"],
    license="Creative Commons Attribution-Noncommercial-Share Alike license",
)