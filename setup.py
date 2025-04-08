from setuptools import setup, find_packages

setup(
    name="ariadne",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        
    ],
    entry_points={
        "console_scripts": [
            "ariadne=ariadne.ui.app:main",
        ],
    },
    author="Jose Quiceno",
    author_email="josequiceno000@gmail.com",
    description="Advanced maze generation and solving visualization toolkit",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/josequiceno2000/ariadne",
    keywords="maze algorithms visualization pathfinding tkinter",
    classifiers= [
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    python_requires=">=3.10",
    include_package_data=True
)