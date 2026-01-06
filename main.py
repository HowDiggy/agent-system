from orchestrator.state_machine import Orchestrator
from roles.proposer import SimpleBackupProposer, PhysicalBackupProposer
from roles.critic import ReliabilityCritic


def main():
    proposers = [
        SimpleBackupProposer(),
        PhysicalBackupProposer(),
    ]
    critics = [
        ReliabilityCritic()
    ]

    orchestrator = Orchestrator(
        proposers=proposers,
        critics=critics
    )

    problem = (
        "Design a reliable PostgreSQL backup strategy "
        "for a small production system."
    )

    result = orchestrator.run(problem)

    print("\n=== FINAL RESULT ===\n")

    print("PROPOSAL:")
    print(result["proposal"])

    print("\nCRITIQUES:")
    for critique in result["critiques"]:
        print(f"- [{critique.severity.name}] "
              f"{critique.dimension.name}: "
              f"{critique.issue}")

    print("\nDECISION:")
    print(result["decision"])


if __name__ == "__main__":
    main()
