from schemas.critique import Severity
from schemas.decision import Decision, Action


def arbitration_policy(proposal: dict, critiques: list) -> Decision:
    """
    Decide what to do with a proposal given its critiques.
    """

    critical_issues = [
        c for c in critiques if c.severity == Severity.CRITICAL
    ]

    if critical_issues:
        return Decision(
            action=Action.REVISE,
            target=proposal["proposer"],
            rationale=(
                f"{len(critical_issues)} critical issue(s) "
                "must be addressed before acceptance."
            )
        )

    return Decision(
        action=Action.ACCEPT,
        target=None,
        rationale="No critical issues detected."
    )
