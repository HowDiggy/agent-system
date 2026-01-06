# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-01-05

### Added
- **Orchestrator**: Implemented `Orchestrator` class with a state machine to manage the flow between proposing, critiquing, and arbitrating.
- **Proposers**:
  - `SimpleBackupProposer`: Suggests basic local backup strategies using `pg_dump`.
  - `RobustBackupProposer`: Suggests compressed, object-storage backed strategies with checksum verification.
- **Critics**:
  - `ReliabilityCritic`: Evaluates proposals for integrity verification (checksums) and redundancy (avoiding single local disk storage).
- **Policies**:
  - `arbitration_policy`: Logic to reject proposals containing `CRITICAL` severity issues and accept those without.
- **Schemas**:
  - `Critique`: Data model for feedback including severity (INFO, WARNING, CRITICAL) and dimensions (RELIABILITY, etc.).
  - `Decision`: Data model for the orchestrator's final action (ACCEPT, REVISE, REJECT).
- **Entry Point**: `main.py` script to demonstrate the interaction between a simple proposer and a reliability critic.