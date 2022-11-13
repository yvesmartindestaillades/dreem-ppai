from distutils.core import setup
from setuptools import find_packages
import os, sys
path = os.path.dirname('/'.join(os.path.abspath(__file__).split('/')[:-1]))
sys.path.append(path)


try:
    with open('/Users/ymdt/src/dreem-ppai/requirements.txt') as f:
        requirements = f.read().splitlines()
except:
    with open('../requirements.txt') as f:
        requirements = f.read().splitlines()

PYTHON_VERSION = (3,10)

if sys.version_info < PYTHON_VERSION:
    sys.exit(f"Python >= {PYTHON_VERSION[0]}.{PYTHON_VERSION[1]} required.")


setup(
   name='dreem-ppai',
   version= '1.1.9',
   license="MIT",
   description='A wrapper for DREEM for the Herschlag lab',
   author='Yves Martin des Taillades',
   author_email='yves@martin.yt',
   long_description= 'TODO',
 #  packages=['dreem-ppai'],  #same as name
   package_dir={'dreem-ppai': 'dreem-ppai'},
   packages=find_packages(),
   package_data={'': ['*.yml']},
   py_modules=[
         'dreem-ppai/sanity_check',
         'dreem-ppai/run_dreem',
         'dreem-ppai/run',
         'dreem-ppai/util',
         'dreem-ppai/template',
         'dreem-ppai/get_info',
         'dreem-ppai/export',
   ],
   include_package_data=True,
   install_requires=requirements, #external packages as dependencies
    entry_points = {
        'console_scripts' : [
            'dreem-ppai = dreem-ppai.run : main'
            ]
    },
    url='https://github.com/yvesmartindestaillades/dreem-ppai'
)