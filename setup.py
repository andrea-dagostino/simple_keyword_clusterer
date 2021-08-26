from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description=f.read()


setup(
    name="simple_keyword_clusterer",
    version=0.13,
    url="https://github.com/Tangelus/simple_keyword_clusterer",
    author="Andrea D'Agostino",
    author_email="andrea@andreadagostino.com",
    description="Extract higher level clusters from keywords",
    keywords = ['keyword-extraction', 'keyword-clustering'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    license="MIT",
    py_modules=["simple_keyword_clusterer", "preprocessing", "clustering"],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
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
