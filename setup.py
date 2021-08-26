from setuptools import setup

setup(
    name="job_title_extractor",
    version=0.1,
    description="Extract job titles and cluster them in high level groups",
    py_modules=["job_title_extractor"],
    package_dir={"": "src"},
)
