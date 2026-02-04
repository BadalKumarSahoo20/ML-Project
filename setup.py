# from setuptools import find_packages, setup
# from typing import List


# def get_requirements(file_path: str) -> List[str]:
#     """
#     This function returns list of requirements
#     """
#     requirements = []

#     with open(file_path) as file_obj:
#         requirements = file_obj.readlines()
#         requirements = [req.replace("\n", "") for req in requirements]

#     return requirements


# setup(
#     name="ml_project",
#     version="0.0.1",
#     author="badal",
#     author_email="badalkumarsahoo.2001@gmail.com",
#     packages=find_packages(),
#     install_requires=get_requirements("requirement.txt")
# )










from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as f:
        return [line.strip() for line in f if line.strip()]


setup(
    name="mlproject",                 # must match folder name
    version="0.0.1",
    author="badal",
    author_email="badalkumarsahoo.2001@gmail.com",

    packages=find_packages(where="src"),   # ✅ critical
    package_dir={"": "src"},               # ✅ critical

    install_requires=get_requirements("requirement.txt"),
)
