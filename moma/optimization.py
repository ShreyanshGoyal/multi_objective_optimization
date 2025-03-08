from pymoo.core.problem import Problem
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.optimize import minimize
from .agents import Student
from .objectives import *
from .utils import gaussian
import numpy as np

class StudentOptimizationProblem(Problem):
    def __init__(self, students):
        super().__init__(n_var=10,
                         n_obj=sum(s.num_obj for s in students),
                         n_constr=6,
                         xl=[18,0,0,0,0,0,0,0,10,35],
                         xu=[54,50,50,50,50,50,50,50,60,70])
        self.students = students

    def _evaluate(self, x, out, *args, **kwargs):
        results, constraints = [], []

        for s in self.students:
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

def run_optimization(student_list, generations=200):
    problem = StudentOptimizationProblem(student_list)
    algorithm = NSGA2(pop_size=100)

    res = minimize(problem, algorithm, ('n_gen', generations), verbose=True)
    return res
