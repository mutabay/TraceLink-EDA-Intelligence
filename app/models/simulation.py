from datetime import datetime
from pydantic import BaseModel

class Violation(BaseModel, frozen=True):
    violation_id: str
    violation_type: str  # IMPEDANCE, CROSSTALK, TIMING_SETUP, EYE_HEIGHT, IR_DROP
    severity: str  # CRITICAL, HIGH, MEDIUM, LOW
    net_id: str
    simulation_id: str
    measured_value: float
    threshold: float
    unit: str

class Contraint(BaseModel, frozen=True):
    constraint_id: str
    constraint_type: str 
    net_id: str
    min_value: float | None
    max_value: float | None
    unit: str

class SimulationRun(BaseModel, frozen=True):
    simulation_id: str
    run_type: str  # SIGNAL_INTEGRITY, POWER_INTEGRITY, TIMING
    timestamp: datetime