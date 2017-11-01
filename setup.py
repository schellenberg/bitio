from setuptools import setup
import os.path
import sys

setupdir = os.path.dirname(__file__)

requirements = []
for line in open(os.path.join(setupdir, 'requirements.txt'), encoding="UTF-8"):
    if line.strip() and not line.startswith('#'):
        requirements.append(line)

setup(
      name="cs20-microbitio",
      version="0.1",
      description="Use Micro:bit as an I/O device in Python.",
      long_description="""This is just a package containing David Whaley's 
      bitio module, so that it can be easily installed in Thonny using
      Manage Packages (pip install). This simplifies the install process
      for the students, so they don't need to worry about where to save files.""",
      url="https://github.com/schellenberg/bitio",
      author="Dan Schellenberg",
	    author_email="schellenberg@gmail.com",
      license="MIT",
      classifiers=[
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
        "Environment :: X11 Applications",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "License :: Freeware",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Education",
        "Topic :: Software Development",
      ],
      keywords="IDE education programming microbit",
      platforms=["Windows", "macOS", "Linux"],
      python_requires=">=3.4",
      package_dir={'microbit': 'microbit'},
	    package_data={'microbit': ['drivescan/*', 'portscan/*', 'repl/*', 'serial/*']},
      install_requires=requirements,
      packages=["microbit"],
)