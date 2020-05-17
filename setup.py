import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xbot", # Replace with your own username
    version="0.0.1",
    author="Alessandro Solbiati",
    author_email="alessandro.solbiati@gmail.com",
    description="code generator for messaging bot in multiple platforms ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SolbiatiAlessandro/xbot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)