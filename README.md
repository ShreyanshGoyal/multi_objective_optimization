
# Multi Objective Multi Agent Optimization (MOMA Optimization)

This repository hosts the implementation of the Multi Objective Multi Agent Optimization (MOMA) project, developed at IIT Bombay.

---

## Overview

The objective of this project is to address optimization problems involving multiple agents, each with their own set of objectives and influenced by interactions among agents. It employs Genetic Algorithms (specifically NSGA-II) for obtaining Pareto-optimal solutions.

---

## Project Structure

```
moma_optimization/
│
├── docs/
│   ├── notebook.ipynb
│   └── Presentation.pdf
├── moma/
│   ├── __init__.py
│   ├── agents.py
│   ├── objectives.py
│   ├── optimization.py
│   ├── influence.py
│   └── utils.py
│
├── examples/
│   └── run_experiment.py
│
├── setup.py
└── requirements.txt
```

- `moma`: Core library with modular components for agents, objectives, influence analysis, and optimization.
- `examples`: Practical examples demonstrating how to use the library.
- `docs`: Contains executable jupyter notebook and a presentation outlining the approach and results
---

## Installation

Clone the repository:

```bash
git clone https://github.com/ShreyanshGoyal/multi_objective_optimization.git
cd multi_objective_optimization
```

Set up the Python environment:

```bash
pip install -r requirements.txt
pip install -e .
```

---

## Usage

Run the optimization example:

```bash
python examples/run_experiment.py
```

This will output optimized decision variables and objective function values.

---

## Key Concepts

- **Multi-objective Optimization**: Solving problems with several conflicting objectives simultaneously.
- **Genetic Algorithms (GA)**: Evolution-inspired algorithms to find optimal or near-optimal solutions.
- **NSGA-II**: A fast elitist multi-objective genetic algorithm that emphasizes Pareto optimal solutions and diversity.

---

## Dependencies

- `numpy`
- `matplotlib`
- `pymoo`
- `networkx`

Install these via:

```bash
pip install -r requirements.txt
```

---
## Contributors
- Shreyansh Goyal
---

## License

Distributed under the MIT License. See `LICENSE` for more information.
