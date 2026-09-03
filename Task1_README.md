# FINOVA Blockchain Management Committee: Task 1

## Approach

I chose decentralized traceability for agricultural supply chains, verifying where
produce came from as it moves from farmer to consumer, because it's a problem I could
reason through end to end without leaning on advanced blockchain features I don't
actually use daily. Rather than reaching for every advanced concept I knew of, I tried
to keep the design to only what the problem genuinely needed:

- A record on-chain for each handoff of a batch of produce.
- An off-chain app and database for everything that doesn't need blockchain guarantees.
- A basic step to bridge a real-world action (a QR scan) into a transaction.

I picked Polygon over Ethereum mainnet for one concrete reason, transaction cost at
volume, rather than listing every possible chain. And in the challenges section, I
tried to be honest about what the design doesn't fully solve (verifying that input data
is true in the first place) rather than presenting it as a solved problem.

