from setuptools import setup, find_packages
setup(
    name='remotepython',
    version='1.0',
    author='john snow',
    description='Job listing crawler for remotepython.com website',
    packages=find_packages(),
    install_requires=[
        'click',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            f'remotepython=remotepython.cli:main'
        ],
    },
)
