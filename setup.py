from setuptools import setup, find_packages

setup(
	author="Matt Triano",
	description="A barebones package.",
	name="mypkg",
	version="0.1.0",
	packages=find_packages(include=["mypkg", "mypkg.*"]),
)