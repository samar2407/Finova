# Task 1: Decentralized Agricultural Supply Chain Traceability

## The problem

As produce moves farmer → distributor → retailer → consumer, each handoff is recorded
separately (paper, spreadsheets, private systems). No one downstream can verify claims
like "organic," catch mislabeling, or trace a contamination issue back to one batch
instead of recalling an entire product line.

## 1. Solution: architecture and workflow

See `diagrams/architecture.svg`.

Core idea: every handoff of a batch gets written to the blockchain as a transaction.
Since that record can't be edited afterward, everyone in the chain can trust it without
trusting each other directly.

**On-chain:** batch details (crop, farmer ID, timestamp) and a hash of the
certification document; one entry per handoff (who received it, when). Only small data
and hashes — no bulky files.

**Off-chain:** the farmer/distributor app, a normal database for search and history,
the actual certificate files/photos (stored on IPFS), and a small "oracle" that turns a
real-world action (a QR scan) into an on-chain transaction — the blockchain has no way
to know what happened physically without something telling it.

**Workflow:**
1. Farmer logs a harvest in the app → creates the first on-chain record for that batch.
2. Each handoff triggers a QR scan → writes a new custody-transfer record on-chain.
3. Consumer scans the final QR code → sees the full history pulled from the chain.

## 2. Why blockchain, and why this chain

**Why blockchain:** the real issue isn't storage, it's that no party fully trusts
another to keep an honest record. A normal shared database still requires trusting
whoever runs it. Blockchain removes that single point of trust — once written, no one
party (including the app's own creator) can quietly change a record.

**Why Polygon:** mainly cost. Recording thousands of small handoffs a day would be too
expensive on Ethereum mainnet; Polygon charges a fraction of a cent per transaction and
is compatible with the same tools and smart-contract language (Solidity), so nothing
has to be built from scratch.

## 3. Challenges

- **Trusting the input, not just the record.** Blockchain guarantees a record wasn't
  altered after the fact — not that it was true to begin with. A false scan becomes
  permanent. Not fully solvable; can be reduced with basic sanity checks (implausible
  location/time flags).
- **Getting farmers to actually use it.** Most won't want to manage crypto wallets or
  fees. The app needs to hide this — normal login, blockchain handled in the background.
- **Cost at scale.** Manageable for a pilot, but high daily volume would need planning
  (e.g. batching multiple updates into one transaction) as it grows.
- **Legal weight.** An on-chain record isn't automatically legally binding — needs
  clear agreements that participants treat it as the official record between them.
