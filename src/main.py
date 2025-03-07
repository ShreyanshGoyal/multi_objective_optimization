# G40_Real_World_Experiments.py

import numpy as np
import math
from pymoo.core.problem import Problem
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.optimize import minimize
import networkx as nx

# Define Gaussian Function
def gaussian(x, mean, var):
    return np.exp(-(x-mean)**2 / (2*var))

# Student class
class Student:
    def __init__(self, student_id, num_obj, objs):
        self.student_id = student_id
        self.num_obj = num_obj
        self.objectives = objs
        self.acads = None
        self.sports = None
        self.research = None
        self.pors = None
        self.tech_team = None
        self.tech_club = None
        self.nc_club = None
        self.cult = None
        self.leisure = None
        self.sleep = None

# Objective Functions
def job(s):  
    return (9*(s.acads)**2 + 4*(s.research)**2 + 3*(s.pors)**2 + 5*(s.tech_team)**2 + 5*(s.tech_club)**2) * gaussian(s.sleep, 49, 14**2)

def gradstudy(s):
    return gaussian(s.sleep, 49, 14**2)*(8*(s.acads)**2+10*(s.research)**2+5*(s.tech_team)**2+5*(s.tech_club)**2)

def health(s): 
    return gaussian(s.sleep, 49, 7**2)*(1 + s.sports**2/5 + (1 - np.exp(-s.leisure/15)))

def social(s):
    return gaussian(s.sleep, 49, 14**2)*((s.sports**2)+7*(s.pors**2)+3*(s.tech_team)**2+3*(s.tech_club)**2+7*(s.nc_club**2)+7*(s.cult**2))

def explore(s):
    return gaussian(s.sleep, 49, 14**2)*(5*(s.sports**2)+5*(s.pors**2)+5*(s.tech_team)**2+5*(s.tech_club)**2 +5*(s.nc_club**2)+5*(s.cult**2)+5*(s.acads**2)+5*(s.research**2))

# List of Students
student_list = [
    Student(student_id=0, num_obj=1, objs=[job]),
    Student(student_id=1, num_obj=1, objs=[gradstudy]),
    Student(student_id=2, num_obj=1, objs=[health]),
    Student(student_id=3, num_obj=1, objs=[social]),
    Student(student_id=4, num_obj=2, objs=[explore, social])
]

# Influence Graph class
class InfluenceGraph:
    def __init__(self):
        self.graph = nx.DiGraph()
    
    def add_influence(self, influencer, influenced, weight):
        self.graph.add_edge(influencer, influenced, weight=weight)

# NSGA-II Setup
class StudentOptimizationProblem(Problem):
    def __init__(self, students):
        super().__init__(n_var=10,
                         n_obj=sum(s.num_obj for s in students),
                         n_constr=6,
                         xl=[18,0,0,0,0,0,0,0,10,35],
                         xu=[54,50,50,50,50,50,50,50,60,70])
        self.students = students

    def _evaluate(self, x, out, *args, **kwargs):
        results = []
        constraints = []

        for s in student_list:
            s.acads, s.sports, s.research, s.pors, s.tech_team, s.tech_club, s.nc_club, s.cult, s.leisure, s.sleep = x
            for obj_func in s.objs:
                results.append(obj_func(s))
        
        constraints = [
            168 - sum(x),
            sum(x) - 120,
            x[0] - 18,
            54 - x[0],
            50 - sum(x[3:7]),
            x[9] - 35,
        ]
        out["F"] = results
        out["G"] = constraints

# NSGA-II Execution Logic
def run_optimization():
    problem = StudentOptimizationProblem(student_list)
    algorithm = NSGA2(pop_size=100)

    res = minimize(problem,
                   algorithm,
                   ('n_gen', 200),
                   verbose=True)

    return res

if __name__ == '__main__':
    result = run_optimization()
    print(result.X, result.F)
