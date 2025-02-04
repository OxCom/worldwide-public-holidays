from setuptools import setup, find_packages

setup(
    name='world public holidays',
    version='1.0.0',
    description='API to fetch list of public holidays',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/OxCom/wwph',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'fastapi'
        'holidays'
        'uvicorn'
        'asyncio',
    ],
    extras_require={
        'dev': ['pytest'],
    },
    tests_require=['pytest'],
    test_suite='tests',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)