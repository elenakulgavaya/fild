from setuptools import setup
from setuptools import find_packages


__version__ = ''
packages = [module for module in find_packages()]


setup(
    name='fild',
    version=__version__,
    classifiers=[
        'Intended Audience :: AQAs',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
    ],
    packages=packages,
    author='Elena Kulgavaya',
    author_email='elena.kulgavaya@gmail.com',
    include_package_data=True,
    install_requires=[
        'Faker==11.3.0',
        'pytz==2021.3',
    ],
    dependency_links=[],
)
