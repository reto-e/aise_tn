# Persona — Technician

---

## Profile

**Name:** Marco Ferretti
**Age:** 34
**Background:** Marco grew up around cars — his father ran a small garage and he started as an apprentice mechanic at 17. He completed a dual vocational training programme and has since accumulated 15 years of hands-on experience across independent workshops and a brief stint at a dealership. He is certified in diagnostics and has recently upskilled in electric vehicles. He is not particularly tech-savvy but adapts quickly to tools that save him time on the floor.

---

## Goals and Motivations

- **Get through the day's jobs efficiently** — he wants to know exactly what vehicles are coming in, what needs doing, and have all parts ready before the car arrives.
- **Accurate documentation** — he wants his work recorded correctly so there are no disputes about what was done and what was charged.
- **Recognition and fair attribution** — he wants his completed jobs linked to his name for performance tracking and bonus calculations.
- **Avoid surprises** — no walk-in jobs appearing on his bay without warning, no missing parts when the car is already lifted.

---

## Pain Points

- **Paperwork duplication:** currently fills in a paper job sheet AND has to enter the same data into the system — double effort, frequent transcription errors.
- **Parts availability unknown until too late:** discovers mid-job that a part is out of stock; has to stop work, inform the advisor, and restart later.
- **No visibility on incoming bookings:** learns about new jobs from the advisor verbally or by seeing a key in the rack — the system doesn't push any notification to him.
- **Inspection results not linked to quotes:** after completing a vehicle inspection, his findings are noted on paper; getting them into a formal quote requires the advisor to re-enter everything from scratch.
- **Customer share links are unused:** the system can generate a shareable service record link for the customer, but Marco doesn't know how or when to trigger this — nobody trained him on it.

---

## Typical Day / Workflow Involving the System

| Time | Activity |
|---|---|
| 07:45 | Arrives, checks the physical job board for today's vehicles — does not log in to Torqvoice yet |
| 08:00 | First car arrives; advisor hands him a printed or verbal job sheet |
| 08:05 | Looks up the vehicle in Torqvoice to check prior service history and any open findings |
| 09:30 | During an oil change, notices a worn brake pad — adds a `VehicleFinding` in Torqvoice (if he remembers / has time) |
| 10:15 | Completes inspection on a second vehicle; fills in the Torqvoice `InspectionItem` conditions on a tablet |
| 11:00 | Discovers the air filter needed is out of stock — walks to the counter to ask the parts manager |
| 12:30 | Lunch. Catches up on recording labour hours for the morning jobs |
| 13:00 | Afternoon jobs; updates `ServiceRecord` status to "in progress" |
| 16:30 | Closes out completed jobs in Torqvoice — enters parts used, labour hours, diagnostic notes |
| 17:00 | End of day; marks jobs as complete; prints or sends invoice via advisor |

---

## Quote

> "I don't need the system to be clever — I need it to be fast. If I can update a job in under a minute while my hands are still dirty, I'll use it. If it takes five screens and a password, I won't bother."

---

## System Touchpoints

| Torqvoice Feature | Usage Level | Notes |
|---|---|---|
| Service Record (view) | Daily | Checks history before starting a job |
| Service Record (edit — parts, labour) | Daily | Updates at end of each job |
| Inspection checklist | Several times/week | Uses tablet; often completes it after the fact |
| Vehicle Findings | Occasional | Adds findings when he remembers |
| Inventory / parts lookup | Occasional | Checks stock before ordering manually |
| Status updates | Daily | Moves jobs through workflow |
| Shareable record link | Rarely | Unaware of the feature |
| Notifications | Never | Not currently receiving any push notifications |
