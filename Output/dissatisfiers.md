# Dissatisfiers Analysis — Torqvoice

*Analysis based on the Prisma schema, repository structure, and feature surface.*
*Kano model: must-be quality — things users expect as a minimum, whose absence causes dissatisfaction.*

---

## 1. Inferred Basic Requirements (what the system currently does)

| # | Requirement | Evidence in Codebase |
|---|---|---|
| R1 | Customer and vehicle records management | `Customer`, `Vehicle` models with rich fields |
| R2 | Work order lifecycle (open → in-progress → closed) | `ServiceRecord.status`, `startDateTime`, `endDateTime` |
| R3 | Quote and invoice generation with PDF export | `Quote`, `ServiceRecord`, PDF generator component noted in src |
| R4 | Inventory tracking with stock levels and min-quantity alerts | `InventoryPart.quantity`, `InventoryPart.minQuantity` |
| R5 | Technician assignment and tracking | `ServiceRecord.technicianId`, `Technician` model |
| R6 | Customer notifications (SMS, Telegram) | `SmsMessage`, `TelegramMessage` models |
| R7 | Role-based access control | `Role`, `Permission`, `OrganizationMember` models |
| R8 | Multi-organisation / multi-workshop support | `Organization` model, `OrganizationMember` |
| R9 | Inspection checklists with condition ratings | `Inspection`, `InspectionTemplate`, `InspectionItem.condition` |
| R10 | Payment recording and tracking | `Payment` model with method, amount, date |
| R11 | Recurring invoices (subscription-style jobs) | `RecurringInvoice`, `RecurringPart`, `RecurringLabor` |
| R12 | Audit logging | `AuditLog` model |
| R13 | Customer self-service portal session management | `CustomerSession` model |
| R14 | Two-factor authentication and passkey support | `TwoFactor`, `Passkey` models |
| R15 | Service reminders for vehicles | `Reminder` model |
| R16 | Vehicle findings/defects tracking | `VehicleFinding` with severity and status |
| R17 | Analytics and scheduled reporting | `ReportSchedule`, notes in src |
| R18 | Webhooks for external integrations | `Webhook` model |
| R19 | Fuel log tracking per vehicle | `FuelLog` model |
| R20 | Stripe-based subscription management | `Subscription`, `SubscriptionPlan` models |

---

## 2. Gaps and Weaknesses Detected

| # | Gap / Weakness | Risk | Suggested Fix |
|---|---|---|---|
| G1 | **No explicit online booking/appointment model** — `ServiceRequest` is lightweight (title, description, status only); there is no slot-based booking with time, confirmation, or cancellation workflow | High — customers expect to book online and receive confirmations | Add a `Booking` entity with slot, confirmation token, status, and link to `ServiceRecord` |
| G2 | **No currency field on financial records** — `ServiceRecord`, `Quote`, and `Payment` store amounts but no currency code; breaks multi-country or multi-currency workshops | High for international use | Add `currency` field (ISO 4217) to all financial models |
| G3 | **No GDPR / right-to-be-forgotten support** — `Customer` has no `deletedAt` or anonymisation flag; `Vehicle` has `isArchived` but `Customer` doesn't | High — legal requirement in EU | Add soft delete / anonymisation flag to `Customer`; add a data-erasure workflow |
| G4 | **No email notification model** — SMS and Telegram are first-class entities; email is mentioned as a feature but has no dedicated model for sent/received tracking or bounces | Medium — no audit trail for email comms | Add `EmailMessage` model analogous to `SmsMessage` |
| G5 | **Service request has no time/slot field** — `ServiceRequest.status` exists but no scheduling metadata; advisors cannot see when a job is expected | Medium | Add `scheduledAt`, `estimatedDuration` to `ServiceRequest` or to a new `Booking` model |
| G6 | **No dispute / void mechanism for invoices** — once a `ServiceRecord` is invoiced there is no `voidedAt` or credit note concept | Medium — incorrect invoices cannot be formally reversed | Add `invoiceVoidedAt`, `creditNoteNumber` to `ServiceRecord` |
| G7 | **No purchase order system for parts** — `InventoryPart` tracks stock and suppliers but there is no `PurchaseOrder` entity to formalise restocking | Low-Medium — manual reorder process is error-prone | Add `PurchaseOrder` model linked to `InventoryPart` and supplier |
| G8 | **Customer portal authentication is session-only** — `CustomerSession` exists but no customer-facing login/signup model (no password, OAuth, or magic link for customers); unclear how customers authenticate | High — self-service portal cannot function without customer auth | Add `CustomerAccount` with auth method (magic link / OAuth) |
| G9 | **No SLA / priority field on work orders** — `ServiceRecord` has no urgency or priority flag; all jobs are treated equally | Medium — high-value or time-sensitive jobs get no preferential handling | Add `priority` enum to `ServiceRecord` |
| G10 | **No multi-location support within an organisation** — `Organization` is a single entity with no `Location` or `Workshop` sub-entity; a chain with multiple physical shops cannot differentiate | Medium for chains | Add `Location` model under `Organization` |
| G11 | **`minQuantity` alerts not surfaced in schema** — `InventoryPart.minQuantity` exists but there is no `StockAlert` or notification model; unclear if low-stock triggers any action | Medium | Add stock alert mechanism / `Notification` entry for low stock |
| G12 | **No warranty claim workflow** — `ServiceRecord` has warranty fields (`warrantyMonths`, `warrantyExpiresAt`) but no model for warranty claims or customer-initiated warranty requests | Low-Medium | Add `WarrantyClaim` model |

---

## 3. Suggested Additions to the Story Map

Based on the gaps above, add the following user stories to the backlog:

1. **As a customer, I want to book a service slot online** so that I don't need to call during business hours. *(G1, G5)*
2. **As a workshop owner, I want invoices to store a currency code** so that I can operate across currencies without ambiguity. *(G2)*
3. **As a data protection officer, I want to anonymise a customer's data on request** so that we comply with GDPR right-to-erasure. *(G3)*
4. **As a service advisor, I want an audit trail of all emails sent to customers** so that I can confirm what was communicated. *(G4)*
5. **As a workshop owner, I want to void or credit an incorrect invoice** so that I can correct billing errors formally. *(G6)*
6. **As an inventory manager, I want to raise a purchase order for low-stock parts** so that restocking is traceable. *(G7)*
7. **As a customer, I want to log in to the self-service portal securely** so that I can view my vehicle history without calling the workshop. *(G8)*
8. **As a service advisor, I want to mark a job as urgent** so that technicians know to prioritise it. *(G9)*
