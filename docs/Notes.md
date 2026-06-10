# EDA Learning Notes

## Chip-Package-Board Co-Design

### The Physical Stack

A semiconductor product has three layers:

1. **Chip (Die)** — silicon with transistors. Has I/O pads/bumps on its surface.
2. **Package** — houses the chip. Has a substrate with routing layers. Connects chip bumps to BGA solder balls on the bottom.
3. **Board (PCB)** — the package is soldered onto this. Traces connect the package to other components (memory, connectors, power).

A signal travels: **chip pad → package routing → BGA ball → board trace → destination**

Each transition (chip-to-package, package-to-board) is where problems happen — impedance discontinuities, parasitic inductance, reflections.

### Why Co-Design Matters

Each layer is designed by a different team, often using different tools. But the signal path spans all three. A timing problem might be caused by package routing. A signal integrity ("Is the signal arriving cleanly?") issue might be caused by board trace spacing. You can't debug one layer in isolation.

---

## Key Concepts

### Net

A named electrical connection that spans the entire stack. Example: `DDR_DQ[17]` is one data bit of a DDR5 bus. It starts at a chip bump, goes through package routing, exits via a BGA ball, and reaches a board trace.

Graph: Net is the central node. Everything connects through it.

### Interface

A group of nets that share a protocol. Examples: DDR5 (memory), PCIe Gen5 (high-speed serial), USB4. Each interface has specific electrical requirements (impedance targets, timing margins, crosstalk limits).

### Impedance

The "resistance" a signal sees at high frequency. Target is typically 50Ω (single-ended) or 85-100Ω (differential). If the impedance changes along the path (e.g., 50Ω on board but 60Ω in package), the signal partially reflects back. This causes violations.

### Crosstalk

When two parallel traces are too close, a switching signal on one (aggressor) induces noise on the other (victim). Gets worse with: closer spacing, longer parallel run, higher frequency.

This is why project groups adjacent nets — if DDR_DQ[17] has crosstalk, DDR_DQ[16] and DDR_DQ[18] are likely involved.

### S-Parameters

Describe how a signal behaves passing through an interconnect. Measured across frequency.

- **S11 (Return Loss):** How much reflects back. Want < -15 dB (less reflection is better).
- **S21 (Insertion Loss):** How much passes through. Want close to 0 dB (less loss is better).
- **S31/S41 (Crosstalk):** Coupling to adjacent channels. Want < -25 dB.

### Eye Diagram

Overlays thousands of signal transitions to visualize quality:
- **Eye height (mV):** Voltage margin. Higher = cleaner signal.
- **Eye width (ps):** Timing margin. Wider = more timing slack.

When eye closes → signal integrity failure → violation.

### Timing (Setup/Hold)

- **Setup time:** Data must be stable BEFORE the clock edge arrives.
- **Hold time:** Data must stay stable AFTER the clock edge.
- **Slack:** How much margin is left. Negative slack = violation.

Timing connects to SI: if signal quality degrades (reflections, crosstalk), the receiver might sample wrong data → timing violation.

### Power Integrity "Is the power supply clean and stable?"

- **IR Drop:** Voltage drop across the power network. If too much, logic doesn't get enough voltage.
- **PDN Impedance:** Power distribution network must be low-impedance across frequency.
- **Decoupling capacitors:** Filter noise at different frequency ranges.

---

## EDA Tools (What the Job Posting Mentions)

### Cadence

- **Allegro** — PCB/Package design tool
- **Sigrity** — SI/PI simulation for packages and boards
- **Skill** — Lisp-based scripting language for Cadence tools

### Keysight

- **ADS (Advanced Design System)** — Signal integrity simulation
- **AEL** — ADS scripting language
- **Python API** — Python automation for ADS

### What These Tools Produce

All these tools output files: simulation results, violation lists, S-parameter data, timing reports. The project represents the next step — taking those outputs and connecting them for cross-domain analysis.

### Touchstone Format (.s2p, .s4p)

S-parameter file format. Contains frequency points and S-parameter matrices. You don't need to parse these, but know they exist and represent frequency-domain signal behavior.

---

## Compute Farms

EDA simulations are computationally expensive. Companies run them on compute farms:

- **Job scheduler:** LSF, SLURM, or SGE manages a cluster of compute nodes
- **Workflow:** Engineer submits job → scheduler assigns to a node → tool runs → outputs to shared filesystem (NFS)
- **Batch mode:** Tools run headless, produce output files

---

## What Synthetic Data Should Look Like

### Violation example (CSV):
```
violation_id,violation_type,severity,net_id,simulation_id,measured_value,threshold,unit
V001,CROSSTALK,HIGH,NET_DDR_DQ17,SIM_SI_003,92.0,70.0,mV
V002,IMPEDANCE,HIGH,NET_DDR_DQ17,SIM_SI_003,61.0,50.0,ohm
V003,TIMING_SETUP,HIGH,NET_DDR_DQ17,SIM_TIM_001,-35.0,0.0,ps
V004,EYE_HEIGHT,MEDIUM,NET_DDR_DQ17,SIM_SI_003,180.0,200.0,mV
```

### Simulation log example (mimics ADS):
```
================================================================
  Channel Simulation Report
  Tool: MockKeysightADS
  Configuration: DDR5_4800MT_SI
  Nets: 72
  Status: COMPLETED WITH WARNINGS
================================================================
NET          | IL@4GHz | RL@4GHz | Xtalk | Eye_H | Eye_W | STATUS
DDR_DQ[0]    | -3.2dB  | -18.5dB | 45mV  | 250mV | 65ps  | PASS
DDR_DQ[17]   | -5.8dB  | -12.1dB | 92mV  | 180mV | 42ps  | FAIL
DDR_DQ[18]   | -4.9dB  | -14.3dB | 78mV  | 195mV | 48ps  | WARNING

[ERROR] DDR_DQ[17]: Crosstalk 92mV exceeds limit 70mV
[ERROR] DDR_DQ[17]: Eye height 180mV below minimum 200mV
[WARNING] DDR_DQ[18]: Eye height 195mV marginal (minimum 200mV)
================================================================
```

---

## How Concepts Map to Project

| EDA Concept | Project Implementation |
|------------|---------------------------|
| Net | Central graph node, links everything |
| Signal path (chip→pkg→board) | Graph traversal: ChipPin → Net → PackageBall → BoardTrace |
| Crosstalk / adjacency | ADJACENT_TO relationship, cluster expansion |
| SI violation | Violation node with type=IMPEDANCE/CROSSTALK/EYE_HEIGHT |
| Timing violation | Violation node with type=TIMING_SETUP/TIMING_HOLD |
| PI violation | Violation node with type=IR_DROP |
| Constraint (from spec) | Constraint node with APPLIES_TO → Net |
| Simulation run | SimulationRun node with CHECKS → Net, PRODUCED → Violation |
| Tool output parsing | Log parser in ingestion layer |
| Cross-domain correlation | Correlator groups violations across simulation types |
| Design change impact | Impact analyzer traverses graph from changed object |
| Verification rerun | Planner finds simulations covering affected nets |
