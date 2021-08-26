from setuptools import setup

setup(
    name="simple_keyword_clusterer",
    version=0.1,
    description="Extract higher level clusters from keywords",
    py_modules=["simple_keyword_clusterer"],
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python 3.7",
        "Programming Language :: Python 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
