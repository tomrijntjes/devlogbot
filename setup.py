from setuptools import setup, find_packages

setup(
    name='devlogbot',
    version='1.0',
    description='Query development logs',
    packages=find_packages(),
    install_requires=['chromadb', 'openai'],
    entry_points={
        'console_scripts': [
            'devlogbot=devlogbot.main:main',  # Adjust if `main.py` has a different function
        ],
    },
)

