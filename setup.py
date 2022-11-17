from setuptools import setup

setup(
   name='planprogenerator',
   version='1.0',
   description='A simple toolkit to generate planpro files',
   author='OSM@HPI',
   packages=['planprogenerator', 'planprogenerator.model', 'planprogenerator.planproxml'],  # would be the same as name
   install_requires=["planpro-python-model @ git+ssh://git@github.com/arneboockmeyer/planpro-python-model.git"],
)
