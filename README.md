# Grant Accord Escrow

- **Repo:** [Synthesis-Arkhai](https://github.com/CrystallineButterfly/Synthesis-Arkhai)
- **Primary track:** Arkhai
- **Category:** agreements
- **Primary contract:** `GrantAccordEscrow`
- **Primary module:** `arkhai_accord`
- **Submission status:** audited and offline-demo ready; optional live partner credentials unlock network execution.

## What this repo does

An escrow-ready agreement layer that turns natural-language grant or service terms into verifiable release checkpoints.

## Why this build matters

The repo models natural-language agreements and escrow checkpoints for public-goods or service deals. A contract stores agreement hashes and release policies while Python scripts turn negotiation state into verifiable escrow actions.

## Submission fit

- **Primary track:** Arkhai
- **Overlap targets:** Octant, ENS, Filecoin, SelfProtocol, PayWithLocus, Markee
- **Partners covered:** Arkhai, Octant, ENS, Filecoin, SelfProtocol, PayWithLocus, Markee

## Idea shortlist

1. Natural-Language Grant Agreements
2. Git-Commit Trading for Public Goods
3. Escrowed Octant Deliverables

## System graph

```mermaid
flowchart TD
    Signals[Discover signals]
    Planner[Agent runtime]
    DryRun[Dry-run artifact]
    Contract[GrantAccordEscrow policy contract]
    Verify[Verify and render submission]
    Signals --> Planner --> DryRun --> Contract --> Verify
    Contract --> arkhai[Arkhai]
    Contract --> octant[Octant]
    Contract --> ens[ENS]
    Contract --> filecoin[Filecoin]
    Contract --> selfprotocol[SelfProtocol]
    Contract --> paywithlocus[PayWithLocus]
```

## Repository contents

| Path | What it contains |
| --- | --- |
| `src/` | Shared policy contracts plus the repo-specific wrapper contract. |
| `script/Deploy.s.sol` | Foundry deployment entrypoint for the policy contract. |
| `agents/` | Python runtime, project spec, env handling, and partner adapters. |
| `scripts/` | Terminal entrypoints for run, demo planning, and submission rendering. |
| `docs/` | Architecture, credentials, security notes, and demo steps. |
| `submissions/` | Generated `synthesis.md` snippet for this repo. |
| `test/` | Foundry tests for the Solidity control layer. |
| `tests/` | Python tests for runtime and project context. |
| `agent.json` | Submission-facing agent manifest. |
| `agent_log.json` | Local execution log and status trail. |

## Autonomy loop

1. Discover signals relevant to the repo track and its overlap targets.
2. Build a bounded plan with per-action and compute caps.
3. Persist a dry-run artifact before any live execution.
4. Enforce onchain policy through the guarded contract wrapper.
5. Verify outputs, update receipts, and render submission material.

## Current readiness

- **Latest verification:** `verified` at `2026-03-19T03:52:08+00:00`
- **Execution mode:** `offline_prepared`
- **Offline-prepared partners:** ENS (prepared_contract_call), Filecoin (prepared_filecoin_bundle)
- **Live credential blockers:** Arkhai, Octant, SelfProtocol, PayWithLocus, Markee
- **Audit docs:** `docs/audit.md`, `docs/live_readiness.md`

## Most sensitive actions

- `selfprotocol_zk_verify` (SelfProtocol, high)

## Live blocker details

- **Arkhai** — ARKHAI_API_KEY, ARKHAI_ESCROW_URL — https://arkhai.ai/
- **Octant** — OCTANT_SIGNAL_URL — https://octant.app/
- **SelfProtocol** — SELF_PROTOCOL_API_KEY, SELF_VERIFICATION_URL — https://docs.self.xyz/
- **PayWithLocus** — LOCUS_API_KEY, LOCUS_PAYMENT_URL — https://docs.locus.finance/
- **Markee** — MARKEE_API_KEY, MARKEE_MESSAGE_URL — https://markee.xyz/

## Latest evidence artifacts

- `artifacts/onchain_intents/ens_ens_publish.json`
- `artifacts/filecoin/0x9cdddc8730546aa1e6e811e634dd306a3072dd5303c97b69700e34a5d7e1e0b2.json`

## Security controls

- Admin-managed allowlists for targets and selectors.
- Per-action caps, daily caps, cooldown windows, and a principal floor.
- Reporter-only receipt anchoring and proof attachment.
- Env-only secrets; no committed private keys or partner tokens.
- Pause switch plus dry-run-first execution flow.

## Action catalog

| Action | Partner | Purpose | Max USD | Sensitivity |
| --- | --- | --- | --- | --- |
| `arkhai_agreement_stage` | Arkhai | Use Arkhai for a bounded action in this repo. | $30 | medium |
| `octant_signal_publish` | Octant | Use Octant for a bounded action in this repo. | $25 | medium |
| `ens_ens_publish` | ENS | Use ENS for a bounded action in this repo. | $5 | low |
| `filecoin_proof_store` | Filecoin | Use Filecoin for a bounded action in this repo. | $20 | medium |
| `selfprotocol_zk_verify` | SelfProtocol | Use SelfProtocol for a bounded action in this repo. | $3 | high |
| `paywithlocus_subaccount_pay` | PayWithLocus | Use PayWithLocus for a bounded action in this repo. | $120 | medium |
| `markee_repo_message` | Markee | Use Markee for a bounded action in this repo. | $5 | low |

## Local terminal flow (Anvil + Sepolia)

```bash
export SEPOLIA_RPC_URL=https://sepolia.infura.io/v3/YOUR_KEY
anvil --fork-url "$SEPOLIA_RPC_URL" --chain-id 11155111
cp .env.example .env
# keep private keys only in .env; TODO.md stays local-only too
forge script script/Deploy.s.sol --rpc-url "$RPC_URL" --broadcast
python3 scripts/run_agent.py
python3 scripts/render_submission.py
```

## Commands

```bash
python3 -m unittest discover -s tests
forge test
python3 scripts/run_agent.py
python3 scripts/plan_live_demo.py
python3 scripts/render_submission.py
```

## Credentials

| Partner | Variables | Docs |
| --- | --- | --- |
| Arkhai | ARKHAI_API_KEY, ARKHAI_ESCROW_URL | https://arkhai.ai/ |
| Octant | OCTANT_SIGNAL_URL | https://octant.app/ |
| ENS | ENS_NAME | https://docs.ens.domains/ |
| Filecoin | FILECOIN_API_TOKEN, FILECOIN_UPLOAD_URL | https://docs.filecoin.cloud/ |
| SelfProtocol | SELF_PROTOCOL_API_KEY, SELF_VERIFICATION_URL | https://docs.self.xyz/ |
| PayWithLocus | LOCUS_API_KEY, LOCUS_PAYMENT_URL | https://docs.locus.finance/ |
| Markee | MARKEE_API_KEY, MARKEE_MESSAGE_URL | https://markee.xyz/ |

## Live demo plan

1. Copy .env.example to .env and fill the required keys.
2. Deploy the contract with forge script script/Deploy.s.sol --broadcast for GrantAccordEscrow.
3. Run python3 scripts/run_agent.py to produce a dry run for arkhai_accord.
4. Set LIVE_MODE=true and rerun python3 scripts/run_agent.py with real credentials.
5. Run python3 scripts/render_submission.py and attach TxIDs plus repo links.
