from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in internal_insurances/__init__.py
from internal_insurances import __version__ as version

setup(
	name="internal_insurances",
	version=version,
	description="Internal insurance for company employees",
	author="osamahmutawakel@gmail.com",
	author_email="osamahmutawakel@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
