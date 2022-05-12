import setuptools

# readme.md = github readme.md

with open('README.md', 'r') as fr:
    long_description = fr.read()

setuptools.setup(
    name="CDKBlueprint",
    version="0.0.1",
    author="Vunk Lai",
    author_email="vunk.lai@gmail.com",
    description="Declarative Attribute for CDKv2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VunkLai/cdk-blueprint",
    packages=['blueprint', ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
