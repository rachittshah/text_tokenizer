from setuptools import setup, find_packages

setup(
    name="text_tokenizer",
    version="0.1",
    author='Rachitt Shah',
    author_email='rachitt01@gmail.com',
    packages=find_packages(),
    install_requires=[
        "nltk",
        "requests"
    ],
)
