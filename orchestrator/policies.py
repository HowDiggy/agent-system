from schemas.critique import Severity
from schemas.decision import Decision, Action


def arbitration_policy(proposals: list, critiques: list) -> Decision:
    """
    Decide what to do given multiple proposals and critiques.
    """

    # For now: pick the first proposal deterministically
    selected_proposal = proposals[0]

    critical_issues = [
        c for c in critiques
        if c.severity == Severity.CRITICAL
        and c.target == selected_proposal["proposer"]
    ]

    if critical_issues:
        return Decision(
            action=Action.REVISE,
            selected_proposer=selected_proposal["proposer"],
            rationale=(
                f"{len(critical_issues)} critical issue(s) "
                "must be addressed before acceptance."
            )
        )

    return Decision(
        action=Action.ACCEPT,
        selected_proposer=selected_proposal["proposer"],
        rationale="No critical issues detected."
    )

