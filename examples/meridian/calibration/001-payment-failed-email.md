# Calibration pair 001 — payment failed email

**Approved:** 2026-07-21 (fictional example)

**Baseline method:** clean session with only the original and the request “Make this payment-failure email clearer and friendlier.”

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
> We couldn't process your payment for the Lisbon trip. Update your payment information so you don't lose your spot.

## What drove the difference

| Change | Rule | File |
|---|---|---|
| Subject states what happened and stays under ~45 characters | Email subject lines lead with what happened | `../references/channels.md` |
| One requested action remains | Email contains one action | `../references/channels.md` |
| No exclamation points, “Oops,” “ASAP,” or reassurance boilerplate | Calm; never manufacture urgency or cheer | `../references/voice.md` |
| No cause, deadline, payment state, or guarantee was added | Writing rules change language, never product facts | `../../../AGENTS.md` |

## What this teaches

When money is involved, say what happened and what action is needed without adding panic, cheer, or facts the original did not provide.
