# TraceLink EDA Intelligence

TraceLink EDA Intelligence is a graph-based engineering analysis platform for simulated chip-package-board co-design workflows.

The project demonstrates how fragmented design data, simulation results, constraints, and violations can be connected through a knowledge graph to support violation correlation, change impact analysis, and verification planning.

The goal is to explore how modern software engineering, graph technologies, and AI-assisted analysis can improve design and verification efficiency in complex semiconductor development environments.

---

## Problem

Chip-package-board co-design involves multiple tools, simulations, and engineering domains.

When a violation occurs, engineers often need to manually answer questions such as:

* Which nets are affected?
* Which chip pins, package balls, and board traces are involved?
* Which simulations produced these violations?
* Are multiple violations related?
* What is the impact of changing a design object?
* Which verification simulations should be rerun?

As systems become more complex, understanding relationships between design objects and simulation results becomes increasingly difficult.

---

## Solution

TraceLink EDA Intelligence transforms fragmented EDA-style data into connected engineering knowledge.

The platform:

* Ingests design and simulation data.
* Builds a knowledge graph representing chip-package-board relationships.
* Correlates related violations.
* Performs impact analysis for design changes.
* Recommends verification reruns.
* Generates AI-assisted engineering reports using a multi-agent architecture.

---

## Architecture

```text
Synthetic EDA Data
        ↓
Data Ingestion and Validation
        ↓
Knowledge Graph Construction
        ↓
Violation Correlation
        ↓
Impact Analysis
        ↓
Verification Recommendation
        ↓
Multi-Agent Report Generation
        ↓
Flask Dashboard
```

---

## Core Features

### Knowledge Graph Construction

Represent relationships between:

* Chips
* Pins
* Nets
* Package balls
* Board traces
* Constraints
* Simulations
* Violations

---

### Violation Correlation

Group related violations instead of treating them independently.

Example:

```text
Cluster #3

Root Object:
DDR_DQ_17

Related:
- Timing violations
- Signal integrity warnings
- Impedance violations

Affected Objects:
- Package Ball B17
- Board Trace T001
```

---

### Impact Analysis

Analyze the consequences of changing:

* Nets
* Package balls
* Board traces
* Simulation configurations

The system determines affected design objects and recommends verification reruns.

---

### Verification Planning

Recommend which simulations should be rerun based on affected objects and violation types.

Examples:

* Signal integrity simulation
* Timing verification
* Power integrity analysis
* Connectivity checks

---

### Multi-Agent Engineering Reports

Specialized agents generate structured engineering reports:

* Graph Investigator Agent
* Violation Correlation Agent
* Verification Planner Agent
* Report Writer Agent
* Validation Agent

Agents operate on structured analysis results rather than replacing deterministic logic.

---

## Technology Stack

### Backend

* Python
* Flask
* Pandas
* Pydantic
* Neo4j

### AI

* OpenAI API / Ollama
* Multi-Agent Architecture

### Engineering

* Docker
* Pytest
* GitHub Actions

---

## Project Structure

```text
tracelink-eda-intelligence/
│
├── app/
├── data/
├── docs/
├── scripts/
├── tests/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Current Status

The project is currently under active development.

Planned capabilities include:

* Synthetic EDA project generation
* Knowledge graph construction
* Violation clustering
* Impact analysis
* Verification recommendation
* Multi-agent report generation
* Flask-based engineering dashboard

---

## Motivation

This project explores how graph technologies, software engineering, and AI can be combined to support complex semiconductor design workflows and improve design and verification efficiency.
