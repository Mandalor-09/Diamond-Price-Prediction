from setuptools import find_packages,setup
from typing import List 
import os
#print(os.getcwd(),'<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
cwd = os.getcwd()
def get_pakages(filename):
    with open(filename) as f:
        requirenment = f.readlines()
        requirenment = [i.replace('/n','') for i in requirenment ]
        if '-e .' in requirenment:
            requirenment.remove('-e .')
            return requirenment

        
setup(
    name = 'Diamond Price Prediction',
    author='Mandalor09',
    author_email='oms42162@gmail.com',
    version="0.0.1",
    description= "Predicting Diamonds Prices using Machine Learning Algorithms.",
    install_requires=get_pakages(cwd + '/requirements.txt'),
    packages=find_packages()
)