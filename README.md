
# Multi-Objective Multi-Agent Optimization Project

### Overview
This project implements Multi-Objective Multi-Agent (MOMA) optimization using evolutionary algorithms (NSGA-II) and influence analysis methods. Specifically, it optimizes multiple conflicting objectives for a group of interacting agents (students) considering realistic constraints and mutual influences.

---

### Project Structure
```
MULTI_OBJECTIVE_OPTIMIZATION/
├── docs/
│   ├── ME_308_G40_Presentation.pdf
│   └── ME308_G40_Report.pdf
├── src/
│   └── main.py
├── LICENSE
└── README.md
```

---

### Dependencies
- Python 3.8+
- pymoo (`pip install pymoo`)
- networkx (`pip install networkx`)
- numpy

Install dependencies using:
```bash
pip install pymoo networkx numpy
```

---

### Running the Experiments
Navigate to the `src` directory and execute:
```bash
python main.py
```

This will run the optimization and display Pareto-optimal solutions and corresponding decision variables.

---

### Key Components
- **NSGA-II Algorithm:** Used for multi-objective optimization to obtain Pareto optimal solutions.
- **Influence Graph:** Models how agents' decisions influence each other.
- **Objective Functions:** Include job opportunities, graduate studies, health, social interactions, and exploration.

---

### Constraints
- Total available time per week is bounded between 120 and 168 hours.
- Specific time constraints for academics, sleep, leisure, and extracurricular activities.

---

### Results
The script provides optimal decision variables (time allocation per activity) and their corresponding objective function values (job, grad study, health, social life, etc.) after execution.

---

### Further Reading
For detailed explanations and experimental insights, refer to the documents in the `docs` folder:
- **ME_308_G40_Presentation.pdf**
- **ME308_G40_Report.pdf**

---

### Contributions & Extensions
- Explore additional clustering methods for state abstraction.
- Extend analysis methods to other neural network types.
- Improve computational efficiency and scalability.

---

### License
This project is licensed under the terms specified in the LICENSE file.
