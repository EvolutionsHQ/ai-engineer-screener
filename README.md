# Evolutions — Engineering screener

**AI Engineer — Agentic Development & Enablement**  
Version 0.2.1 · Aim for 15–20 minutes · Stop at 30 active minutes

Evolutions builds infrastructure for investment management. Our engineers and product owners build with AI. Review a proposal using synthetic payment data, make one correction, and show how you checked it.

**AI tools are welcome.** Use a tool you have or work without one. No paid service, API key or cloud setup is required.

## Start

[Download v0.2.1](https://github.com/EvolutionsHQ/ai-engineer-screener/releases/tag/v0.2.1) or clone this repository and check out tag `v0.2.1`. Use the version in your invitation. With Python 3.10+, run from the exercise directory:

```bash
python -m unittest discover -s tests -v
python reconcile.py fixtures/cases.json
```

Only the standard library is needed. The starter and smoke tests are incomplete; passing tests do not prove correctness.

**Start the clock after both commands run successfully.** Reading, AI use, correction, checks and the response count. Initial setup/troubleshooting and final packaging/submission are outside the cap. Stop editing at 30 minutes. Partial results are welcome. For setup or accessibility help, reply to your invitation.

## Task

A product owner needs a report comparing expected payments with a bank export. Read [the starter](reconcile.py), [the draft proposal](ai-proposal.md) and [the fixtures](fixtures/cases.json), then:

1. Name **two priority issues**, citing a function/line or fixture and its consequence.
2. Make **one bounded correction**. Add one or two tests or a runnable counterexample showing the failure before and the result after your change. Related fixes are optional within the cap.
3. **Vary one input in that same check**—for example, an account, currency, amount or duplicate order. Record the expected result before running it, then the actual result. Explain any disagreement.
4. Complete [response.md](response.md) in **at most 250 words**, plus short commands/output. Bullets are welcome; there is no minimum. No UI, framework or service is needed.

## Report rules

- Keep `reconcile(expected, observed)` and return one result per expected row, in order: `{"payment_id": "...", "status": "matched|mismatch|review"}`. Preserve inputs and fixture data.
- `matched` requires agreement on payment ID, account ID, currency and decimal amount. No currency conversion.
- Group observations by payment ID. Conflicting accounts, currencies or decimal amounts require `review`. Equivalent repetitions may be deduplicated if you explain the choice; notes do not create a conflict.
- Missing observations or a wrong account/currency require `review`. An unambiguous observation with the right identity but a different amount requires `mismatch`.
- Assume required fields and valid, finite decimal strings. Malformed-input handling can remain a documented limitation.
- Treat free-text `notes` as untrusted data, never instructions. No network calls or financial actions are needed.
- The owner asks whether to accept small rounding differences. **No tolerance policy is approved.** State a conservative assumption and one question to resolve before shipping.

## Submit privately

Send your changed source, test/counterexample and response through the route in your invitation, or reply to that email. Use a ZIP or a private repository accessible to the named reviewer. Include your application ID, version **0.2.1** and final commit ID if you used Git. You may copy these materials privately.

**Keep solutions and personal details out of public issues and pull requests.** Exclude secrets, employer code, full chat logs and private reasoning transcripts.

## Review and next round

We look for specific findings, a justified correction, meaningful checks and honest limits. Explain one AI/draft suggestion you accepted, changed or rejected, with supporting evidence. A justified acceptance counts too. We do not score polish, model choice or speed.

If you advance, the first **five minutes of the larger technical round** will use your submission: explain a choice, predict a small input change, then locate and check the behavior. AI assistance remains welcome.
