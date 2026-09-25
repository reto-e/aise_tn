# Lateral Traceability — User Story Relationships

> **Definitions**
> - **Dependency**: Story A cannot be implemented without Story B being done first (A → B)
> - **Conflict**: Story A and B make contradictory assumptions about the system (↔)
> - **Refinement**: Story A is a more detailed version of or derived from Story B (A → B)

| Story A | Relationship | Direction | Story B | Reason |
|---------|-------------|-----------|---------|--------|
| KAN-39 Create work order | Dependency | KAN-39 → KAN-33 | KAN-33 Register customer | A work order must be linked to an existing customer record |
| KAN-39 Create work order | Dependency | KAN-39 → KAN-22 | KAN-22 Add new car | A work order requires a vehicle to be already registered in the system |
| KAN-46 Generate invoice | Dependency | KAN-46 → KAN-45 | KAN-45 Close work order | An invoice can only be generated from a completed/closed work order |
| KAN-41 Add parts to work order | Dependency | KAN-41 → KAN-52 | KAN-52 Add new part to inventory | Parts added to a work order must already exist in the inventory catalogue |
| KAN-40 Add services to work order | Dependency | KAN-40 → KAN-29 | KAN-29 Define labour rates | Service line items on a work order are priced using configured labour rates |
| KAN-42 Assign technician to work order | Dependency | KAN-42 → KAN-28 | KAN-28 Manage employee profiles | Technicians must be registered as employees before they can be assigned |
| KAN-42 Assign technician to work order | Dependency | KAN-42 → KAN-30 | KAN-30 Set up service bays | Technician assignment involves allocating a service bay, which must be configured first |
| KAN-50 Mark invoice as paid | Dependency | KAN-50 → KAN-46 | KAN-46 Generate invoice from work order | An invoice must exist before it can be marked as paid |
| KAN-47 Apply discount to invoice | Dependency | KAN-47 → KAN-46 | KAN-46 Generate invoice from work order | A discount can only be applied to an already-generated invoice |
| KAN-48 Send invoice by email | Dependency | KAN-48 → KAN-46 | KAN-46 Generate invoice from work order | The invoice must exist before it can be sent by email |
| KAN-49 Preview invoice before sending | Dependency | KAN-49 → KAN-46 | KAN-46 Generate invoice from work order | There must be an invoice to preview |
| KAN-51 Issue credit note | Dependency | KAN-51 → KAN-46 | KAN-46 Generate invoice from work order | A credit note is issued against an existing invoice |
| KAN-68 Issue refund | Dependency | KAN-68 → KAN-50 | KAN-50 Mark invoice as paid | A refund can only be processed against a previously paid invoice |
| KAN-69 Send payment receipt | Dependency | KAN-69 → KAN-50 | KAN-50 Mark invoice as paid | A receipt is generated upon successful payment confirmation |
| KAN-55 Configure low-stock alerts | Dependency | KAN-55 → KAN-52 | KAN-52 Add new part to inventory | Alerts can only be set for parts that already exist in the inventory |
| KAN-53 Update part stock level | Dependency | KAN-53 → KAN-52 | KAN-52 Add new part to inventory | Stock levels can only be updated for parts already registered in the catalogue |
| KAN-57 View stock history | Dependency | KAN-57 → KAN-56 | KAN-56 Record stock adjustment | Stock history is built from recorded adjustments; no adjustments means no history |
| KAN-58 Send appointment reminder | Dependency | KAN-58 → KAN-24 | KAN-24 Schedule a service appointment | A reminder can only be sent for a previously scheduled appointment |
| KAN-77 Sync appointments to Google Calendar | Dependency | KAN-77 → KAN-24 | KAN-24 Schedule a service appointment | Calendar sync requires appointments to already exist in the system |
| KAN-59 Notify customer when vehicle is ready | Dependency | KAN-59 → KAN-45 | KAN-45 Close and complete work order | The "vehicle ready" notification is triggered by work order completion |
| KAN-63 Configure notification templates | Dependency | KAN-63 → KAN-58 | KAN-58 Send appointment reminder | Templates govern the content of reminder notifications and must be set up first |
| KAN-25 View service history for a vehicle | Dependency | KAN-25 → KAN-22 | KAN-22 Add new car | Service history can only be viewed for a vehicle that is registered in the system |
| KAN-25 View service history for a vehicle | Dependency | KAN-25 → KAN-45 | KAN-45 Close and complete work order | Service history is populated by completed work orders |
| KAN-82 Confirm booking with one tap | Dependency | KAN-82 → KAN-79 | KAN-79 Self-service booking | The one-tap confirmation is a step within the self-service booking flow |
| KAN-81 Book Car Inspection | Dependency | KAN-81 → KAN-22 | KAN-22 Add new car | Booking an inspection requires the vehicle to be registered first |
| KAN-76 Export report to PDF | Dependency | KAN-76 → KAN-71 | KAN-71 View revenue summary report | PDF export presupposes at least one report type being available to export |
| KAN-76 Export report to PDF | Dependency | KAN-76 → KAN-72 | KAN-72 View work orders by status report | PDF export presupposes at least one report type being available to export |
| KAN-34 Edit customer details | Dependency | KAN-34 → KAN-33 | KAN-33 Register new customer | A customer record must exist before it can be edited |
| KAN-35 View customer history | Dependency | KAN-35 → KAN-33 | KAN-33 Register new customer | Customer history is only accessible for registered customers |
| KAN-36 Search and filter customers | Dependency | KAN-36 → KAN-33 | KAN-33 Register new customer | There must be customer records in the system before search is meaningful |
| KAN-37 Archive customer record | Dependency | KAN-37 → KAN-33 | KAN-33 Register new customer | Only an existing customer record can be archived |
| KAN-38 Merge duplicate customer records | Dependency | KAN-38 → KAN-33 | KAN-33 Register new customer | Merging requires at least two existing customer records |
| KAN-29 Define labour rates | Dependency | KAN-29 → KAN-27 | KAN-27 Configure workshop settings | Labour rates are a sub-configuration within the broader workshop settings module |
| KAN-30 Set up service bays | Dependency | KAN-30 → KAN-27 | KAN-27 Configure workshop settings | Service bays are a sub-configuration within the broader workshop settings module |
| KAN-31 Manage workshop closures | Dependency | KAN-31 → KAN-27 | KAN-27 Configure workshop settings | Closure management is a sub-configuration within the broader workshop settings module |
| KAN-67 Split payment across methods | Dependency | KAN-67 → KAN-64 | KAN-64 Accept cash payment | Split payment relies on individual payment methods being implemented |
| KAN-67 Split payment across methods | Dependency | KAN-67 → KAN-65 | KAN-65 Accept card payment | Split payment relies on individual payment methods being implemented |
| KAN-13 Add new part to inventory | Conflict | KAN-13 ↔ KAN-23 | KAN-23 Add new part to inventory | Both stories have identical summaries — one is a duplicate and they cannot coexist as separate backlog items |
| KAN-13 Add new part to inventory | Conflict | KAN-13 ↔ KAN-52 | KAN-52 Add new part to inventory | Three stories share the exact same title, implying contradictory scope boundaries across sprints |
| KAN-66 Record partial payment | Conflict | KAN-66 ↔ KAN-50 | KAN-50 Mark invoice as paid | A partial payment contradicts the binary "paid/unpaid" assumption in KAN-50; the payment status model must reconcile these states |
| KAN-37 Archive customer record | Conflict | KAN-37 ↔ KAN-35 | KAN-35 View customer history | Archiving may restrict access to customer history, contradicting the expectation that history remains viewable |
| KAN-68 Issue refund | Conflict | KAN-68 ↔ KAN-50 | KAN-50 Mark invoice as paid | A refund reverses the "paid" state, requiring reconciliation of invoice status logic |
| KAN-79 Self-service booking | Refinement | KAN-79 → KAN-24 | KAN-24 Schedule a service appointment | Self-service booking is a customer-facing, detailed realisation of the general appointment scheduling story |
| KAN-81 Book Car Inspection | Refinement | KAN-81 → KAN-79 | KAN-79 Self-service booking | Inspection booking is a specific service-type instance of the generic self-service booking flow |
| KAN-82 Confirm booking with one tap | Refinement | KAN-82 → KAN-79 | KAN-79 Self-service booking | One-tap confirmation is a UX-level detail refining the self-service booking confirmation step |
| KAN-71 View revenue summary report | Refinement | KAN-71 → KAN-26 | KAN-26 Generate monthly revenue report | Revenue summary is a more granular and generalisable version of the monthly revenue report story |
| KAN-78 Acknowledge complaint via email | Refinement | KAN-78 → KAN-61 | KAN-61 Log communication history | Email complaint acknowledgement is a specific channel and trigger for the general communication logging story |
| KAN-64 Accept cash payment | Refinement | KAN-64 → KAN-46 | KAN-46 Generate invoice from work order | Cash payment is a specific realisation of the general invoice settlement concept |
| KAN-65 Accept card payment | Refinement | KAN-65 → KAN-46 | KAN-46 Generate invoice from work order | Card payment is a specific realisation of the general invoice settlement concept |
