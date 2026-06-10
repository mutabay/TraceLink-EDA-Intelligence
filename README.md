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

Group related violations across nets, simulation types, and physical layers.

The correlator uses graph traversal (not simple grouping) to find clusters that span adjacent nets, different simulation domains, and multiple physical layers.

Example:

```text
Cluster #1 (score: 24)

Root: DDR_DQ[17]

Violations:
- DDR_DQ[17]: Crosstalk (SI simulation)
- DDR_DQ[17]: Timing setup failure (Timing simulation)
- DDR_DQ[18]: Eye height degraded (SI simulation)  ← adjacent net
- Board Trace T001: Impedance mismatch (SI simulation)  ← physical path

Correlation:
  Impedance discontinuity on T001 → signal reflections →
  crosstalk into adjacent DQ[18] → timing margin lost on DQ[17]
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

Three specialized agents generate structured engineering reports:

* **Investigator Agent** — Translates natural language questions into Cypher queries against the knowledge graph. Executes queries, observes results, and retries if needed.
* **Analysis Agent** — Reasons about root causes and explains why violations are correlated using domain knowledge.
* **Report Agent** — Synthesizes findings into a structured engineering report with recommendations.

The pipeline uses deterministic algorithms for correlation, impact analysis, and verification planning. LLM agents operate at the end of the pipeline — they explain and report, they don't replace the logic.

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

## Quick Start

```bash
docker-compose up
```

Open `http://localhost:5000`. Demo data is loaded automatically.

Or run manually:

```bash
make setup
make pipeline
make dashboard
```

---

## Project Structure

```text
tracelink-eda-intelligence/
│
├── app/
│   ├── models/          # Pydantic domain models
│   ├── ingestion/       # Data loading and parsing
│   ├── graph/           # Neo4j client and queries
│   ├── analysis/        # Correlator, impact, verification
│   ├── agents/          # LLM agents (investigator, analysis, report)
│   └── dashboard/       # Flask app
├── data/
├── scripts/
├── tests/
├── Dockerfile
├── docker-compose.yml
├── Makefile
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
