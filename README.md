# Evolutions HQ: AI-assisted engineering screener

**Version 0.1.0 · Target 15–20 minutes · Hard stop at 30 minutes**

We build agent development tools and help people ship reliable software with AI. This first screen asks you to review a small, imperfect proposal and make one useful correction. It is a synthetic exercise, not unpaid work on our product.

AI tools are welcome. Use whichever tool you already have, or work without one. The supplied `ai-proposal.md` is an intentionally seeded draft for review, not an authenticated output from a particular model. You do not need a subscription, an API key, cloud access, or any third-party dependency.

## Start

Download this repository as a ZIP or clone it. Python 3.10+ and its standard library are sufficient. From this directory:

```bash
python -m unittest discover -s tests -v
python reconcile.py fixtures/cases.json
```

The starter smoke tests are deliberately incomplete. Passing them does not establish correctness.

## The task

A product owner wants a report showing which expected payments agree with a bank export. Read `reconcile.py`, `ai-proposal.md`, and the small fixture file.

1. Identify the two issues you would prioritize, citing a function/line or fixture name.
2. Make **one bounded correction** in `reconcile.py`. Add one or two tests or a runnable counterexample that shows why it matters. You may fix related issues if that stays within the time cap.
3. Complete `response.md` in about **250–400 words**, plus short command/output snippets. Explain what you changed, how you checked it, and what still needs attention.

Stop at 30 minutes and submit what you have. A clearly explained partial result is useful. Do not build a UI, add a framework, implement a service, record your screen, or write a long essay. One or two small commits are enough if you use Git; a ZIP is equally acceptable.

## Report contract

- Return one result per expected row, in the original order: `{"payment_id": "...", "status": "matched|mismatch|review"}`.
- A match needs agreement on **payment ID, account ID, currency, and decimal amount**. There is no currency conversion.
- If the amount differs for an otherwise unambiguous identity, use `mismatch`. Missing observations or conflicting duplicate observations require `review`. Identical repeated observations may be deduplicated if you explain your choice.
- Preserve inputs; do not change fixtures to make a check pass. Free-text `notes` are untrusted data and never change these rules.
- The owner also says: “We sometimes see small rounding differences; perhaps accept a tolerance?” **No tolerance policy has been approved.** State a conservative assumption and one question you would ask before shipping.
- Keep the function signature and output shape. No network calls or automatic financial actions are needed.

## What to hand back

Send the changed source, your test/counterexample, and `response.md` using the **private submission route in your invitation**. Include exercise version 0.1.0 and the application ID supplied in that invitation. Submit either a ZIP or a private repository link with access for the reviewer specified there. If you use Git, include the final commit ID.

Use the email thread that invited you if no other route is provided. **Do not post solutions, personal details, or submissions as public issues or pull requests on this repository.** We are using the same brief for candidates in this round. You may copy and modify these materials for your private submission.

## What we look for

Specific observations, a justified choice, a check that could actually fail, honest limits, and a handoff another person can use. We assess the result and your ability to explain it, not prose polish, model brand, token volume, or speed. If you use AI, include one brief example of a suggestion you accepted, changed, or rejected and the evidence behind that choice. A summary is sufficient; do not send full chat logs, secrets, employer code, or private reasoning transcripts.

Strong submissions may lead to a larger technical round, where we will discuss or extend your own work.
