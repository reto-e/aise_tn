# User Story Map — Torqvoice (from Technician Interview)

*Extracted from interview with Marco Ferretti, Technician.*  
*[P1] = high priority, [?] = uncertain / needs discussion*

---

## Activity: Start the Working Day

### Task: Get an overview of today's jobs
- As a technician, I want to see today's scheduled jobs in Torqvoice at a glance, so that I don't need to rely on a physical whiteboard. [P1]
- As a technician, I want to be notified when a new booking is added to my day, so that I'm not surprised when a car arrives. [P1]
- As a technician, I want to see jobs added after the day started flagged as late additions, so that I can adjust my schedule. [?]

---

## Activity: Prepare for a Job

### Task: Check vehicle history
- As a technician, I want to view a vehicle's full service history before the job starts, so that I know about prior findings and work done. [P1]

### Task: Check parts availability
- As a technician, I want to see whether the parts needed for a job are in stock before the car arrives, so that I can flag missing parts in advance. [P1]
- As a technician, I want to raise a parts request directly in the system, so that I don't have to chase the parts manager verbally or via WhatsApp. [P1]
- As a technician, I want the inventory to reflect real stock levels, so that I can trust what the system shows me. [P1]

---

## Activity: Execute a Job

### Task: Update job status
- As a technician, I want to move a job through statuses (pending → in progress → done) quickly, so that the advisor and customer have an up-to-date view. [P1]

### Task: Record findings during inspection
- As a technician, I want to add vehicle findings mid-job on a mobile device, so that I don't lose information before I get back to a desk. [P1]
- As a technician, I want findings I record to automatically generate a quote request, so that I don't have to relay information verbally to the advisor. [?]

### Task: Record parts and labour
- As a technician, I want to log parts used and labour hours against a job in under a minute, so that I don't skip it because it takes too long. [P1]

---

## Activity: Manage Unexpected Scope

### Task: Handle jobs that run over their booked time
- As a service advisor, I want the system to alert me when a job is running over its booked time, so that I can proactively contact the customer. [P1]
- As a workshop owner, I want standard durations defined per service type (and optionally per vehicle make/model), so that booking estimates are realistic. [P1]
- As a service advisor, I want a buffer time added automatically to each booking slot, so that unexpected findings don't cascade into delays for the next job. [?]

---

## Activity: Close Out the Day

### Task: Confirm completed jobs
- As a technician, I want to mark all jobs as complete at end of day and see a summary, so that nothing falls through the cracks. [P1]

---

## Key Process Gaps Identified

1. **Whiteboard dependency** — daily job overview lives on a physical whiteboard, not in Torqvoice. A technician-facing daily view would eliminate this.
2. **Parts ordering is off-system** — all parts requests go through verbal communication or WhatsApp. No traceability, no confirmation loop.
3. **Inventory accuracy** — technicians don't trust the stock levels in Torqvoice because updates are inconsistent.
4. **Booking-to-technician gap** — online bookings don't reach the technician directly; they go through the service advisor and then the whiteboard.
5. **Duration estimation** — no standard job durations in the system; customers set unrealistic expectations at booking time.
