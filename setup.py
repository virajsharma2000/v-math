from setuptools import setup, find_packages

setup(
    name="v-math",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # Add dependencies here, e.g., "numpy>=1.21.0"
    ],
    author="Viraj Sharma",
    description="A weird math module",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/virajsharma/v-math",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
