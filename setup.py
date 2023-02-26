from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in alfassam/__init__.py
from alfassam import __version__ as version

setup(
	name="alfassam",
	version=version,
	description="CUstomized app for ERPNext",
	author="sastechnologies",
	author_email="info@sastechnologies.co",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
