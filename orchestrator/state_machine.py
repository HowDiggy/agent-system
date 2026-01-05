from enum import Enum, auto
from typing import List

from orchestrator.policies import arbitration_policy
from schemas.decision import Action
from roles.proposer import Proposer
from roles.critic import Critic


class OrchestratorState(Enum):
    START = auto()
    PROPOSE = auto()
    CRITIQUE = auto()
    ARBITRATE = auto()
    END = auto()


class Orchestrator:
    def __init__(
        self,
        proposer: Proposer,
        critics: List[Critic],
    ):
        self.proposer = proposer
        self.critics = critics

        self.state = OrchestratorState.START

        self.proposal = None
        self.critiques = []
        self.decision = None

    def run(self, problem: str):
        while self.state != OrchestratorState.END:

            if self.state == OrchestratorState.START:
                self.state = OrchestratorState.PROPOSE

            elif self.state == OrchestratorState.PROPOSE:
                self.proposal = self.proposer.propose(problem)
                self.state = OrchestratorState.CRITIQUE

            elif self.state == OrchestratorState.CRITIQUE:
                self.critiques = []
                for critic in self.critics:
                    self.critiques.extend(
                        critic.critique(self.proposal)
                    )
                self.state = OrchestratorState.ARBITRATE

            elif self.state == OrchestratorState.ARBITRATE:
                self.decision = arbitration_policy(
                    self.proposal,
                    self.critiques
                )

                if self.decision.action == Action.ACCEPT:
                    self.state = OrchestratorState.END

                elif self.decision.action == Action.REVISE:
                    self.state = OrchestratorState.END

                else:
                    self.state = OrchestratorState.END

        return {
            "proposal": self.proposal,
            "critiques": self.critiques,
            "decision": self.decision,
        }
