from setuptools import setup


with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name="DungeonGenerator",
    author="Robert Sharp",
    author_email="webmaster@sharpdesigndigital.com",
    install_requires=["Fortuna"],
    packages=["DungeonGenerator"],
    version="0.1.10",
    description="D&D 5e Dungeon Generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Free for non-commercial use",
    platforms=["Darwin", "Linux"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.6",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=["D&D", "Random Dungeon", "Monster", "Treasure", "Traps"],
    python_requires='>=3.6',
)
