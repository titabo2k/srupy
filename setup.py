from setuptools import setup

setup(
    name = "srupy",
    version = "0.0.45",
    description = "A Python client for fetching data from SRU endpoints",
    authors = ["Andreas Lüschow"],
    license = "MIT",
    packages=["srupy"],
    package_dir={"srupy": "srupy"},
    python_requires=">=3.7",
    install_requires=[
        'requests>=1.1.0',
        'lxml>=3.2.3'],
    classifiers=[
        'Development Status :: 3 - Alpha',],
    keywords="SRU Search-Retrieve-via-URL",)
