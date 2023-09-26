from setuptools import setup, find_packages
from typing import List

E_dot = "-e ."
def get_requirements(f_path:str)->List[str]:

    requirements = []
    with open(f_path) as f_obj:
        requirements = f_obj.readlines()
        requirements = [x.replace("\n", " ") for x in requirements]

        if E_dot in requirements:
            requirements.remove(E_dot)
    
    return requirements

setup(     
    name='mlproejct',
    version='0.0.1',
    author='Kabir Singla',
    author_email='Kabir18singla@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)