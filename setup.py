from setuptools import setup, find_packages

setup(
    name="Ariadne",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "tkinter>=8.6",
    ],
    entry_points={
        "console_scripts": [
            "ariadne=ariadne.ui.app:main",
        ],
    },
    author="Jose Quiceno",
    author_email="josequiceno000@gmail.com",
    description="Advanced maze generation and solving visualization toolkit",
    keywords="maze, algorithms, visualization, pathfinding",
    python_requires=">=3.10.12",
)