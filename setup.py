from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='A short description of the project.',
    author='Your name (or your organization/company/team)',
    license='',
)
setup(
    name='utils',
    version='1.0.0',
    packages=find_packages(),
    install_requires=['numpy', 'pandas','scikit-learn'],
    author='Nikul Nayi',
    author_email='nikulnayi97@gmail.com',
    description='Function and Classes to support preprocessing Pipeline',
)