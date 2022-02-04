from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in firstu_app/__init__.py
from firstu_app import __version__ as version

setup(
	name="firstu_app",
	version=version,
	description="Fuel app",
	author="sandra thomas",
	author_email="sandrathomass404@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
