import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="agents",
    version="1.0.0",
    author="Aljo",
    author_email="aljo.jo@media.net",
    description="agents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/novasolution-net/agents.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
