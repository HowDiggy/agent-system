class Proposer:
    def __init__(self, name: str):
        self.name = name

    def propose(self, problem: str) -> dict:
        raise NotImplementedError


class SimpleBackupProposer(Proposer):
    def __init__(self):
        super().__init__(name="simple_backup_proposer")

    def propose(self, problem: str) -> dict:
        return {
            "proposer": self.name,
            "solution": (
                "Use pg_dump to create a daily logical backup "
                "stored on local disk via cron."
            )
        }


class RobustBackupProposer(Proposer):
    def __init__(self):
        super().__init__(name="robust_backup_proposer")

    def propose(self, problem: str) -> dict:
        return {
            "proposer": self.name,
            "solution": (
                "Use pg_dump with compression, store backups in "
                "object storage, and verify integrity with checksums."
            )
        }
