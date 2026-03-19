# Live readiness

- **Project:** Grant Accord Escrow
- **Track:** Arkhai
- **Latest verification:** `verified`
- **Execution mode:** `offline_prepared`
- **Generated at:** `2026-03-19T03:52:08+00:00`

## Trust boundaries

- **Arkhai** — `rest_json` — Stage natural-language agreements and escrow checkpoints.
- **Octant** — `rest_json` — Publish scored public-goods signals and DPI artifacts.
- **ENS** — `contract_call` — Publish human-readable coordination and identity receipts.
- **Filecoin** — `file_upload` — Persist proofs, logs, and evidence bundles offchain.
- **SelfProtocol** — `rest_json` — Gate sensitive actions behind privacy-preserving proofs.
- **PayWithLocus** — `rest_json` — Create bounded subaccounts and controlled spend flows.
- **Markee** — `rest_json` — Publish GitHub-adjacent build stories and repo messages.

## Offline-ready partner paths

- **ENS** — prepared_contract_call
- **Filecoin** — prepared_filecoin_bundle

## Live-only partner blockers

- **Arkhai**: ARKHAI_API_KEY, ARKHAI_ESCROW_URL — https://arkhai.ai/
- **Octant**: OCTANT_SIGNAL_URL — https://octant.app/
- **SelfProtocol**: SELF_PROTOCOL_API_KEY, SELF_VERIFICATION_URL — https://docs.self.xyz/
- **PayWithLocus**: LOCUS_API_KEY, LOCUS_PAYMENT_URL — https://docs.locus.finance/
- **Markee**: MARKEE_API_KEY, MARKEE_MESSAGE_URL — https://markee.xyz/

## Highest-sensitivity actions

- `selfprotocol_zk_verify` — SelfProtocol — Use SelfProtocol for a bounded action in this repo.

## Exact next steps

- Copy .env.example to .env and fill the required keys.
- Deploy the contract with forge script script/Deploy.s.sol --broadcast for GrantAccordEscrow.
- Run python3 scripts/run_agent.py to produce a dry run for arkhai_accord.
- Set LIVE_MODE=true and rerun python3 scripts/run_agent.py with real credentials.
- Run python3 scripts/render_submission.py and attach TxIDs plus repo links.
