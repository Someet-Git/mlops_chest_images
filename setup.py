import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "mlops_chest_images"
AUTHOR_USER_NAME = "Someet-Git"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "someetsahoo654@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A CNN Classifier for Chest Disease Classification from Chest CT Scan Images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"http://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"http://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)