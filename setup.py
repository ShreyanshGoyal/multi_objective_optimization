from setuptools import setup, find_packages
setup(
    name='moma_optimization',
    version='0.1',
    packages=find_packages(),
    install_requires=['numpy', 'matplotlib', 'pymoo', 'networkx'],
    author='Shreyansh Goyal',
    description='Multi Objective Multi Agent Optimization',
    url='https://github.com/ShreyanshGoyal/multi_objective_optimization',
)
