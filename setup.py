from setuptools import setup

setup(
    name="virustotalpy",
    version="0.2.1",
    description="library for an easier interaction with the v3 api",
    long_description=open('pypi_descr.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/maxmmueller/virustotalpy",
    author="Maximilian Müller",
    license="Apache License 2.0",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    packages=["virustotalpy"],
    include_package_data=True,
    install_requires=["requests"]
)
