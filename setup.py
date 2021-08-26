from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description=f.read()


setup(
    name="simple_keyword_clusterer",
    version=1.1,
    url="https://github.com/Tangelus/simple_keyword_clusterer",
    author="Andrea D'Agostino",
    author_email="andrea@andreadagostino.com",
    description="Extract higher level clusters from keywords",
    keywords = ['keyword-extraction', 'keyword-clustering'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    package_dir={"":"src"},
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6",
    install_requires=[
        "scikit-learn",
        "tqdm",
        "seaborn",
        "numpy",
        "nltk",
        "matplotlib",
        "pandas",
    ],
)
