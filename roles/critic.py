from schemas.critique import Critique, Severity, Dimension


class Critic:
    def __init__(self, name: str):
        self.name = name

    def critique(self, proposal: dict) -> list[Critique]:
        raise NotImplementedError


class ReliabilityCritic(Critic):
    def __init__(self):
        super().__init__(name="reliability_critic")

    def critique(self, proposal: dict) -> list[Critique]:
        critiques = []

        solution = proposal.get("solution", "").lower()

        if "verify" not in solution and "checksum" not in solution:
            critiques.append(
                Critique(
                    target=proposal["proposer"],
                    issue="No verification of backup integrity",
                    severity=Severity.CRITICAL,
                    dimension=Dimension.RELIABILITY,
                    resolvable=True,
                    rationale=(
                        "Backups may succeed but be corrupted "
                        "without verification."
                    )
                )
            )

        if "local disk" in solution:
            critiques.append(
                Critique(
                    target=proposal["proposer"],
                    issue="Single storage location",
                    severity=Severity.WARNING,
                    dimension=Dimension.RELIABILITY,
                    resolvable=True,
                    rationale=(
                        "Storing backups only on local disk "
                        "risks data loss if the host fails."
                    )
                )
            )

        return critiques
