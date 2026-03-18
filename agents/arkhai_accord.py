"""Project-specific context module."""

from __future__ import annotations

PROJECT_CONTEXT = {
  "project_name": "Grant Accord Escrow",
  "track": "Arkhai",
  "pitch": "An escrow-ready agreement layer that turns natural-language grant or service terms into verifiable release checkpoints.",
  "overlap_targets": [
    "Octant",
    "ENS",
    "Filecoin",
    "SelfProtocol",
    "PayWithLocus",
    "Markee"
  ],
  "goals": [
    "discover a bounded opportunity",
    "plan a dry-run-first action",
    "verify receipts and proofs"
  ]
}


def seed_targets() -> list[str]:
    """Return the first batch of overlap targets for planning."""
    return list(PROJECT_CONTEXT['overlap_targets'])
