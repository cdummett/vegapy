from setuptools import setup, find_packages

setup(
    name="vegapy",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "vegapy.visualisations.styles": ["theme-dark.mplstyle"],
    },
)
