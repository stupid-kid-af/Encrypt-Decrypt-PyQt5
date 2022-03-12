
from setuptools import setup





setup(
    name="PyQt5-Encryption",
    author="Ashutosh",
    maintainer="Kyle Altendorf, Bryce Beagle, Florian Bruhin",
    maintainer_email="sda@fstab.net",
    description=" PyQt5 framework",
    data_dir = os.path.join(sys.prefix, "local/lib/python2.7/dist-package/my_module"),
    data_files   = [ ("my_module",  [os.path.join(data_dir, "ui"),
                                 os.path.join(data_dir, "application.py", "cipher.py")])]


    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development"
    ]
)
