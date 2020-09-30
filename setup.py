import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dViz",
    version="1.0",
    author="Umashankar",
    author_email="umashanks99@gmail.com",
    description="A Visualization Library for Deep Learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Shanks0465/dViz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)