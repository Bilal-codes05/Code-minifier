from setuptools import setup, find_packages

setup(
    name="code_minifier",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'ply>=3.11',
    ],
    entry_points={
        'console_scripts': [
            'jsminify=minifier.cli:main',
        ],
    },
)