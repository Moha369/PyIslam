import setuptools

def long_desc():
    with open('README.md', 'r') as desc:
        return desc.read()

setuptools.setup(
    name = 'pyislam',
    version = '0.1.1',
    author = 'Mohammed Shaawa',
    author_email = 'mshaawa963@gmail.com',
    description = 'An Islamic Python Package',
    long_description = long_desc(),
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/moha369/pyislam',
    packages = setuptools.find_packages(),
    install_requires = ['requests'],
    license = 'MIT',
    keywords = 'islam quran sunnah',
    classifiers = [
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
    ],
    python_requires = '>=3.6'
)
