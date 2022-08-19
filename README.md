![gnutools Logo](imgs/gnutools-python.png)

--------------------------------------------------------------------------------

Cheking is a Python package that provides scheduled checkin/checkout for remote work. It includes:
- Click on button.
- Input of clipboard/input text in a text field.

### Code structure
```python
from setuptools import setup
from checkin import __version__
setup(
    name='checkin',
    version=__version__,
    long_description="",
    packages=[
        "checkin",
    ],
    include_package_data=True,
    url='https://github.com/JeanMaximilienCadic/checkin',
    license='MIT',
    author='Jean Maximilien Cadic',
    python_requires='>=3.6',
    install_requires=[r.rsplit()[0] for r in open("requirements.txt")],
    author_email='git@cadic.jp',
    description='Checkin tool for python',
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
    ]
)

```

### How to

#### Install the wheel
```
pip install dist/*.whl
```

### Run the main file
```
python -m checkin "2020/08/19 11:34"
```
