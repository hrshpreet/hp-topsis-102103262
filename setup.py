from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="hp-toposis",
    version="1.0.0",
    description="A Python package to get toposis rankings for any table.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/hrshpreet",
    author="Harshpreet Singh",
    author_email="harshpreetny@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "Programming Language :: Python :: 3.7",
    ],
    packages=["hp_toposis"],
    include_package_data=True,
    install_requires=["numpy","pandas"],
    entry_points={
        "console_scripts": [
            "hp-toposis=hp_toposis.topsis:main",
        ]
    },
)