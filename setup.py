from setuptools import setup, find_packages

with open("./requirements.txt", "r") as f:
    requires = f.readlines()

setup(
    name="dg-sdk with pycryptodomex",
    version="1.3.7",
    description="dg-sdk with pycryptodomex",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ironboxer/dg_sdk",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=requires,
)
