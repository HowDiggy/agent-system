# Agent System (Minimal, Principled Multi-Agent Orchestration)

This repository is an experimental but disciplined exploration of **agent system architecture**.

The goal is not to build a flashy “AI agent”, but to **understand and implement the minimal structural pieces** required for a robust, extensible, multi-agent reasoning system — starting from first principles.

We deliberately began with **mental models and control flow**, not tools, GPUs, frameworks, or hype.

---

## Motivation

Most “agent frameworks” jump straight to:
- Tool calling
- Memory systems
- Vector databases
- Parallel execution
- Complex abstractions

This project asks a simpler, deeper question:

> *What is the smallest possible system that deserves to be called an agent system?*

To answer that, we focused on:
- Clear role boundaries
- Explicit control flow
- Deterministic orchestration
- Structured communication
- Observable state transitions

Only once the loop is structurally sound do we add complexity.

---

## Core Mental Model

At its heart, this system is a **controlled reasoning loop**.

It consists of:

1. **Proposers**  
   Generate candidate solutions to a problem.

2. **Critics**  
   Analyze proposals and produce structured critiques.
   - Critics may *only* critique.
   - They may not propose or revise solutions.

3. **Arbitration Policy**  
   Decides what to do given proposals and critiques.
   - Accept
   - Revise
   - Reject
   - Select which proposer continues

4. **Orchestrator (State Machine)**  
   The “brain stem” of the system.
   - Decides which role runs next
   - Tracks state across iterations
   - Enforces constraints
   - Determines stopping conditions

> **Important:**  
> The orchestrator does *not* generate content.  
> It only routes control and data.

---

## What This System Is *Not*

- Not a chatbot
- Not an LLM wrapper
- Not a tool-calling framework
- Not tied to any model, provider, or API

Everything here can run:
- Without GPUs
- Without network access
- Without external dependencies

This is intentional.

---

## Current Architecture (v0.2)
```
agent-system/
├── orchestrator/
│ ├── state_machine.py # Core control loop (explicit FSM)
│ ├── guards.py # Loop guards & termination logic
│ └── policies.py # Arbitration logic (decision making)
│
├── roles/
│ ├── proposer.py # Proposer base + concrete proposers
│ ├── critic.py # Critic base + concrete critics
│ └── comparator.py # (Planned) comparative critics
│
├── schemas/
│ ├── critique.py # Structured critique outputs
│ └── decision.py # Structured arbitration decisions
│
├── memory/
│ └── bias_memory.py # (Planned) long-lived bias tracking
│
├── examples/
│ └── postgres_backup.py # Example problem domain
│
└── main.py # Entry point: runs one full loop
```
---

## Orchestrator as a State Machine

The orchestrator is implemented as an **explicit finite state machine**:
```
START
↓
PROPOSE
↓
CRITIQUE
↓
ARBITRATE
↓
REVISE (optional, bounded)
↓
END
```
Key properties:
- All transitions are explicit
- Loop guards prevent infinite execution
- State is observable and traceable
- Behavior is deterministic given inputs

This makes debugging and extension straightforward.

---

## Current Capabilities (v0.2)

- Multiple independent proposers
- Multiple critics
- Structured critiques (severity, proposer attribution)
- Principled arbitration
- Revision loop with hard stop
- Full debug trace of the orchestration loop

Example run output shows:
- Which proposals were generated
- Which critiques were raised
- Why arbitration chose revision or acceptance
- When and why the system stopped

---

## Example Domain

The included example explores:

> **“How should PostgreSQL backups be designed?”**

This domain was chosen because:
- It is concrete
- It has multiple valid approaches
- Tradeoffs are real and critique-worthy

The architecture is domain-agnostic.

---

## Design Principles

This project follows a few non-negotiable principles:

### 1. Separation of Concerns
Each role has a single responsibility.

### 2. Explicit Control Flow
No hidden magic. No implicit recursion.

### 3. Structured Outputs
Free-form text is avoided at role boundaries.

### 4. Minimalism First
Complexity is added only when forced by real needs.

### 5. Debuggability
If you cannot trace a run, the system is not done.

---

## Roadmap

### v0.1 — Single proposer loop
- One proposer
- One critic
- Accept / revise loop

### v0.2 — Multiple proposers + arbitration
- Independent proposers
- Selection via policy
- Revision routing

### v0.3 — Comparative Criticism (Next)
- Critics that can see *multiple proposals at once*
- Relative evaluation instead of isolated critique
- Arbitration informed by comparison, not just severity

### v0.4 — Proposal Pools
- Keep multiple proposals alive
- Parallel refinement tracks

### v0.5 — Memory & Bias Tracking
- Persistent preferences
- Learned arbitration tendencies

---

## Why This Matters

Most failures in agent systems come from:
- Entangled responsibilities
- Implicit control flow
- Unbounded loops
- Uninspectable decisions

This project treats **architecture itself as the first problem**.

If the system works with:
- Hardcoded logic
- No models
- No tools

Then it will scale cleanly *with* them later.

---

## Status

Current version: **v0.2**

The system is:
- Structurally sound
- Actively evolving
- Designed for learning, not hype

---

## Next Step

Implement **comparative critics**:
- Define what they are allowed to see
- Define what they may output
- Integrate them into arbitration *without breaking the loop*
