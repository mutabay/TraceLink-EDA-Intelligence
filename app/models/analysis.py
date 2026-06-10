from pydantic import BaseModel

from app.models.simulation import Violation

class ViolationCluster(BaseModel, frozen=True):
    cluster_id: str
    root_net_id: str
    net_ids: list[str]
    violations: list[Violation]
    score: float


class ImpactResult(BaseModel, frozen=True):
    source_net_id: str
    affected_net_ids: list[str]
    affected_traces: list[str]
    affected_balls: list[str]
    violations: list[Violation]
    simulation_ids: list[str]

class SimulationRecommendation(BaseModel, frozen=True):
    simulation_id: str
    run_type: str
    priority: str          # HIGH, MEDIUM, LOW
    reason: str
    affected_nets: list[str]