from setuptools import setup, find_packages

setup(
    name='pyobjectid',
    version='0.1.4',
    packages=find_packages(),
    description='A package to generate, validate, and deal with MongoDB ObjectIds.',
    author='Zifo',
    author_email='ahmedshaban.sh10@Gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=["bson", "pydantic"]
)
