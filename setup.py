from setuptools import setup

setup(
    name="virustotalpy",
    version="1.0.1",
    description="library for an easier interaction with the VirusTotal v3 API",
    long_description=open('README.md').read(),
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
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent"
    ],
    packages=["virustotalpy"],
    include_package_data=True,
    install_requires=["requests"]
)