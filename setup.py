
from setuptools import setup



long_description = read('README.md')


setup(
    name="PyQt5-Encryption",
    url="https://github.com/python-qt-tools/PyQt5-stubs",
    author="Stefan Lehmann",
    maintainer="Kyle Altendorf, Bryce Beagle, Florian Bruhin",
    maintainer_email="sda@fstab.net",
    description="PEP561 stub files for the PyQt5 framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["PyQt5-stubs"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development"
    ]
)
