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
    REVISE = auto()
    END = auto()


class Orchestrator:
    def __init__(
        self,
        proposers: List[Proposer],
        critics: List[Critic],
    ):
        self.proposers = proposers
        self.critics = critics

        self.state = OrchestratorState.START

        self.proposals = []
        self.active_proposal = None
        self.selected_proposer_name = None
        self.critiques = []
        self.decision = None
        self.max_iterations = 3
        self.iteration = 0

    def run(self, problem: str):
        while self.state != OrchestratorState.END:

            if self.state == OrchestratorState.START:
                self.state = OrchestratorState.PROPOSE

            elif self.state == OrchestratorState.PROPOSE:
                self.proposals = [
                    proposer.propose(problem)
                    for proposer in self.proposers
                ]

                self.state = OrchestratorState.CRITIQUE

            elif self.state == OrchestratorState.CRITIQUE:
                self.critiques = []

                for proposal in self.proposals:
                    for critic in self.critics:
                        self.critiques.extend(
                            critic.critique(proposal)
                        )

                print("Proposals:")
                for p in self.proposals:
                    print(f" - {p['proposer']}")

                print("Critiques:")
                for c in self.critiques:
                    print(f" - {c.target}: {c.severity}")


                self.state = OrchestratorState.ARBITRATE


            elif self.state == OrchestratorState.ARBITRATE:
                self.decision = arbitration_policy(
                    self.proposals,
                    self.critiques
                )

                self.selected_proposer_name = self.decision.selected_proposer

                if self.decision.action == Action.ACCEPT:
                    self.state = OrchestratorState.END

                elif self.decision.action == Action.REVISE:
                    if self.iteration >= self.max_iterations:
                        self.state = OrchestratorState.END
                    else:
                        self.state = OrchestratorState.REVISE

                else:
                    self.state = OrchestratorState.END

            elif self.state == OrchestratorState.REVISE:
                self.iteration += 1

                winning_proposer = next(
                    p for p in self.proposers
                    if p.name == self.selected_proposer_name
                )

                self.active_proposal = winning_proposer.revise(
                    problem,
                    self.active_proposal,
                    self.critiques
                )

                self.proposals = [self.active_proposal]
                self.state = OrchestratorState.CRITIQUE

        return {
            "proposal": self.selected_proposer_name,
            "critiques": self.critiques,
            "decision": self.decision,
        }

