# GraphArmor-Net // Zero-Trust Network Topology Mapper

An engineering tool designed to map enterprise internal network infrastructure layouts, tracing the algorithmic blast radius of lateral malware movements using highly performant graph structures.

## Core Capabilities
- **Adjacency List Matrix Structures (C Backend):** Implements dynamic memory nodes and edges to model internal connectivity routes without $O(V^2)$ storage constraints.
- **Blast-Radius Calculations (BFS):** Utilizes full **Breadth-First Search** to efficiently evaluate network compromises, computing exposure limits in direct $O(V + E)$ processing timelines.
- **Automation Pipeline Infrastructure:** Bridges structural pointer data arrays out of C memory spaces straight into structured runtime scripts for security modeling.

## File Map
- `network_graph.c`: Native Adjacency List building blocks and functions.
- `blast_radius.c`: Traversal algorithms and system-level matrix logic.
- `blast_radius.h`: Declarations and structures matching memory boundaries.
- `graph_bridge.py`: Automated compilation layer and type handler.
- `visualizer.py`: The deployment runtime test platform.

## Execution Requirements
Run the orchestration platform with:
```bash
python visualizer.py
