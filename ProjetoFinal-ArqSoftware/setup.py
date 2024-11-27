from setuptools import setup, find_packages

setup(
    name="Projeto Final Arq Software",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pytest",
        "flake8",
        "mypy",
        "black"
    ],
    extras_require={
        "dev": [
            "pytest",
            "flake8",
            "mypy",
            "black"
        ]
    }
)
