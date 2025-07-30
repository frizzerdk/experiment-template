from setuptools import setup, find_packages

setup(
    name="EXPERIMENT_NAME_PLACEHOLDER",
    version="1.0.0",
    description="EXPERIMENT_DESCRIPTION_PLACEHOLDER",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy>=1.21.0",
        "matplotlib>=3.5.0",
        "pyyaml>=6.0",
    ],
    python_requires=">=3.8",
) 