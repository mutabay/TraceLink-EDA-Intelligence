from pydantic import BaseModel


class Net(BaseModel, frozen=True):
    net_id: str
    name: str 
    net_type: str   # SIGNAL, POWER, GROUND, CLOCK
    interface: str  # DDR5, PCIe, USB4
    criticality: str  # CRITICAL, HIGH, MEDIUM, LOW
    frequency_mhz: float

class ChipPin(BaseModel, frozen=True):
    pin_id: str
    net_id: str
    x_um: float
    y_um: float

class PackageBall(BaseModel, frozen=True):
    ball_id: str
    net_id: str
    x_mm: float
    y_mm: float

class BoardTrace(BaseModel, frozen=True):
    trace_id: str
    net_id: str
    length_mm: float
    width_um: float
    impedance_ohm: float
    layer: str
