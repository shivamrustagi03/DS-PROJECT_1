# This Setup.py is responsibe in creating my machine learning applications as a package.
# You can also use this package in your project or you can also use it .

# So with the help of Setup.py , You will be able to build you entire applications as a project.

# Why we are doing so?
# Because of this anybody can install the code or project and install it. It is very useful in Coding.

from setuptools import find_packages , setup
# This will automatically find out all the packages that are available in the entire machine learning application that we have created. Setup will setup all this.
from typing import List

HYPEN_E_DOT = '-e .' # Created Constant Value
def get_requirements(file_path:str)->List[str]: # This Function will return the List of Requirements
    requirements=[] # This bracket symbolizes List
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() # Now lines will get read which is written in Requirement.txt
        requirements=[req.replace("\n", "")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements  


setup(
    
    # Here you will see all the parameters that are basically required.
    name = 'dsproject_1', # This is my Project Name
    version='0.0.1', # This is Version , Whenever your next version will come you just keep on updating it.
    author='Shivam',
    author_email='shivam@gmail.com',
    packages = find_packages(), # This is very important and powerful.
    #install_requires=['pandas','numpy','seaborn','matplotlib'] # Installing required Libraries.
    #But this is not possible everytime in big projects
    install_requires=get_requirements('requirements.txt')
) 