# Calibration pair 001 — payment failed email

**Approved:** 2026-07-21 (fictional example)

## Original

> Subject: Payment Failure Notification!
>
> Oops! Unfortunately your payment for the Lisbon trip could not be processed at this time. Please update your payment information ASAP so you don't lose your spot! Don't worry — this happens all the time!

## Without the system

> Subject: Payment issue with your Lisbon trip
>
> We couldn't process your payment for the Lisbon trip. Please update your payment method soon to keep your reservation. We apologize for any inconvenience.

## With the system

> Subject: Your payment didn't go through
>
> Your card for "Lisbon in October" was declined — no one was charged, and your spot is safe for now. Update your payment method by Friday and you're set. You can change cards any time.

## What drove the difference

| Change | Rule | File |
|---|---|---|
| "didn't go through… no one was charged" | Calm; say what happened, release pressure | `references/voice.md` |
| Trip named as "Lisbon in October" | Trips are named objects, not generic "the trip" | `references/terminology.md` |
| "by Friday" replaces "ASAP" | Promises carry a time or they don't ship | `references/channels.md` (email) |
| One action, subject states what happened | Email: one action per email; subject under ~45 chars | `references/channels.md` (email) |
| No exclamation points, no "Oops" | Calm: never add urgency the situation doesn't have | `references/voice.md` |

## What this teaches

When something goes wrong with money, say what happened and what's safe before what's needed — calm is stating facts in order, not adding reassurance.
