# Specification by Example — Self-Service Booking for Customers

*Feature: Torqvoice self-service portal — customers book a workshop slot online without calling.*

---

## Critical Examples

1. Returning customer + saved vehicle + standard service + valid slot + clear balance → submitted, confirmed, notified.
2. Guest + manual vehicle entry + valid slot → submitted; on confirmation: Customer and Vehicle records created.
3. Any customer + slot < minimum lead time → blocked before submission.
4. Any customer + (start time + service duration) > workshop closing time → blocked before submission.
5. Workshop rejects booking → customer notified with reason and prompt to rebook.
6. Customer with unpaid invoices → warned or blocked (exact policy unresolved).
7. Pre-approval service type → held for manual workshop review, not auto-confirmed.
8. Requested slot at full capacity → blocked with suggestion to choose another slot.

---

## Rules

### Confirmed

1. Customers may book as a guest (name + email + vehicle details) or as a logged-in user.
2. A booking requires: customer identity, vehicle, service type, and a date/time slot.
3. The system must enforce a minimum lead time between now and the requested slot.
4. The system must validate that `requested start time + service duration ≤ workshop closing time` for the selected day.
5. The system must check slot availability; full slots cannot be booked.
6. All bookings go to the workshop for confirmation or rejection — no auto-confirm.
7. On confirmation, the customer receives a notification (email and/or SMS).
8. On rejection, the customer receives a notification with a reason.
9. For guest bookings, a Customer and Vehicle record are created in Torqvoice upon confirmation.

### Assumed (not yet confirmed)

- A. Customers cannot cancel or reschedule via the portal after booking.
- B. A customer's registered vehicles are pre-populated in the booking form when logged in.

---

## Open Questions

1. **Minimum lead time:** how far in advance must a booking be placed — 1 hour, 4 hours, 24 hours?
2. **Open invoice policy:** does an unpaid balance block the booking, trigger a warning, or have no effect?
3. **Service duration source:** where does the system get the expected duration for each service type — fixed catalogue, technician estimate, or workshop-configured?
4. **Opening hours:** are they configured per day per workshop (incl. public holidays)?
5. **Self-service cancellation:** can customers cancel or reschedule after a confirmed booking?
6. **Guest account upgrade:** after a guest booking is confirmed, can the guest convert to a full account?
7. **Slot capacity definition:** is capacity defined by number of simultaneous bookings, number of available technicians, or available bays?
8. **Pre-approval services:** which service types require pre-approval, and who defines this?
9. **Duplicate vehicle detection:** if a guest enters a vehicle already registered under another customer, what happens?
10. **Notification channel:** is notification always email + SMS, or configurable per customer preference?

---

## Attribute Model

| Attribute | What it captures |
|---|---|
| Customer identity | Guest / logged-in / returning with debt |
| Vehicle source | Registered vehicle / manually entered / already in system |
| Service type | Freely bookable / pre-approval required / not self-serviceable |
| Slot timing | Date + start time requested |
| Lead time | Gap between now and requested slot |
| Duration fit | Start time + duration vs. closing time |
| Workshop capacity | Slots available at requested time |
| Customer financial status | Open invoices / unpaid balances |
| Booking outcome | Blocked / Pending / Confirmed / Rejected |
| Post-confirmation actions | Notifications / cancellation / rescheduling |
