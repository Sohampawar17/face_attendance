from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in face_attendance/__init__.py
from face_attendance import __version__ as version

setup(
	name="face_attendance",
	version=version,
	description="Face attendance using python",
	author="quantbit technologies pvt. ltd ",
	author_email="contact@quantbit.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
