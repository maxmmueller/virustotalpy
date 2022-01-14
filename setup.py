from setuptools import find_packages, setup

setup(
    name='virustotalpy',
    version='0.1.0',
    description='library for an easier interaction with the v3 api',
    url='https://github.com/maxmmueller/virustotalpy',
    author='Maximilain Müller',
    license='Apache License 2.0',
    packages=find_packages(include=['virustotalpy']),
    setup_requires=['requests'==2.25],
)