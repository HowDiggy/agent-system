class Proposer:
    def __init__(self, name: str):
        self.name = name

    def propose(self, problem: str) -> dict:
        raise NotImplementedError
    
    def revise(
        self,
        problem: str,
        prior_proposal: dict,
        critiques: list
    ) -> dict:
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
    def revise(self, problem: str, prior_proposal: dict, critiques: list) -> dict:
        return {
            "proposer": self.name,
            "solution": (
                "Use pg_dump to create daily logical backups, "
                "store them off-host, and verify integrity using checksums."
            )
        }



class PhysicalBackupProposer(Proposer):
    def __init__(self):
        super().__init__(name="physical_backup_proposer")
        
    def propose(self, problem: str) -> dict:
        return {
            "proposer": self.name,
            "solution": (
                "Use pg_basebackup to take physical backups, "
                "store WAL archives, and enable point-in-time recovery."
            )
        }

    def revise(self, problem: str, prior_proposal: dict, critiques: list) -> dict:
        return {
            "proposer": self.name,
            "solution": (
                "Use pg_basebackup with WAL archiving, "
                "store backups off-host, and regularly test restores."
            )
        }
