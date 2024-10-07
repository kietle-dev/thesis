from setuptools import setup, find_packages

setup(
    name="web-observer",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # Add your project dependencies here
    ],
)
