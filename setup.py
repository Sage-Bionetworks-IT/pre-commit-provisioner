import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

install_requirements = [
    'gitpython>=3.1,<4',
    'pyyaml>=5.3.1,<6',
    'Jinja2>=2.11.2,<3',
]

setuptools.setup(
    name='pre-commit-provisioner-sage-bionetworks',
    version='0.0.4',
    author='Sage Bionetworks IT Dept.',
    author_email='it@sagebionetworks.org',
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=install_requirements,
    license='Apache Software License',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url='https://github.com/Sage-Bionetworks-IT/pre-commit-provisioner',
    entry_points={
        'console_scripts': [
            'compare-stack-and-file-names = linters.check_file_names:compare_file_and_stack_names'
        ]
    },
    python_requires = '>=3.6'
)