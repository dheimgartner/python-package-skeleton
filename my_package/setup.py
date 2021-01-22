# This setup.py file tells setuptools about your package (s.a. name and version) and
# as well as code files to include. Similar to Description file in R.

# There are many more element which can be included - following only the basic basics ...
# See guides for more info: https://packaging.python.org/guides/distributing-packages-using-setuptools/

import setuptools

# Contains the long_description - referenced below
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# help(setuptools.setup)
setuptools.setup(
    name="my-package-dheim",                        # does not need to correspond to root directory name
    version="0.0.1",                                # 10 x 10 x 10 version possibilities
    author="Daniel Heimgartner",
    author_email="author@example.com",
    description="A small example package",          # short one-sentence summary
    long_description=long_description,              # in this case read from the README.md
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",    # just the URL for the homepage of the project -> can be your own GitHub page
    packages=setuptools.find_packages(),            # finds all packages required automatically
    classifiers=[                                   # Always at least include these elements!
        "Programming Language :: Python :: 3",
        "Licence :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)