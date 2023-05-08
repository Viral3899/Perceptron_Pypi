import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

PKG_NAME = "Perceptrone"
USER_NAME = "viral3899"
PROJECT_NAME = "Perceptron_PyPi"
VERSION = '0.0.1'
AUTHOR_NAME = 'Viral Sherathiya'
AUTHOR_EMAIL = 'viralsherathiay1008@gmail.com'
HYPHEN_E_DOT = '-e .'


def get_requirements():
    """
    This Function returns the list of Requirements from requirements.txt & all the Packages.
    """

    with open('./requirements.txt') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setuptools.setup(
    name=f"{PKG_NAME}-{USER_NAME}",
    version="0.0.1",
    author=USER_NAME,
    author_email="viralsherarthiya1008@gmail.com",
    description="A package for perceptron",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{USER_NAME}/{PROJECT_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{USER_NAME}/{PROJECT_NAME}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=['matplotlib==3.5.3', 'seaborn==0.12.2',
                      'pandas==1.3.5', 'numpy==1.21.6',
                      'joblib==1.2.0', 'ipykernel==6.16.2']
)
