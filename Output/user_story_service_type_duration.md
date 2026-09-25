# User Story — Standard Duration per Service Type

## Story
As a workshop owner, I want to define service types with a standard duration for my organisation, so that booking duration estimates are realistic and consistent.

## Acceptance Criteria
1. When a workshop owner opens the service type catalogue, Torqvoice displays all service types belonging to their organisation.
2. When a workshop owner creates a service type, Torqvoice requires both a name and a duration in minutes.
3. When a workshop owner enters a duration, Torqvoice accepts only positive multiples of 15 (e.g. 15, 30, 45, 60 …).
4. If a workshop owner submits a service type without a duration, Torqvoice displays an inline validation error and does not save the record.
5. If a workshop owner enters a duration that is not a positive multiple of 15, Torqvoice displays an inline validation error and does not save the record.
6. When a workshop owner saves a valid service type, Torqvoice stores it scoped to their organisation and shows it in the catalogue list.
7. A workshop owner can edit the name or duration of any service type in their organisation's catalogue.
8. A workshop owner can delete a service type from their organisation's catalogue.
9. Service types and durations of one organisation are not accessible to other organisations.
10. Users without the workshop owner role cannot create, edit, or delete service types.

## Follow-up Stories
- **Self-service booking:** Display the service type's standard duration to the customer at booking time and use it to validate the requested slot fits within opening hours.
- **Buffer time:** As a workshop owner, I want to add a buffer time to each booking slot so that unexpected scope does not cascade into delays.
- **Make/model override:** As a workshop owner, I want to set a duration override per service type and vehicle make/model for jobs whose length depends on the car.

## Lo-fi Prototype

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  body { font-family: sans-serif; font-size: 14px; color: #222; max-width: 680px; margin: 2rem auto; }
  h2 { font-size: 16px; margin-bottom: 1rem; }
  table { width: 100%; border-collapse: collapse; margin-bottom: 1.5rem; }
  th { text-align: left; border-bottom: 2px solid #ccc; padding: 6px 8px; font-size: 12px; color: #555; }
  td { padding: 7px 8px; border-bottom: 1px solid #eee; }
  .actions { display: flex; gap: 8px; }
  .btn { padding: 4px 10px; border: 1px solid #999; border-radius: 3px; background: #f5f5f5; cursor: pointer; font-size: 12px; }
  .btn-primary { background: #222; color: #fff; border-color: #222; }
  fieldset { border: 1px solid #ccc; border-radius: 4px; padding: 1rem; margin-bottom: 1rem; }
  legend { font-weight: bold; font-size: 13px; padding: 0 4px; }
  label { display: block; margin-bottom: 4px; font-size: 12px; color: #444; }
  input { width: 100%; box-sizing: border-box; padding: 6px 8px; border: 1px solid #ccc; border-radius: 3px; font-size: 13px; }
  .hint { font-size: 11px; color: #777; margin-top: 3px; }
  .error { font-size: 11px; color: #c00; margin-top: 3px; }
  .row { display: flex; gap: 1rem; }
  .row > div { flex: 1; }
</style>
</head>
<body>

<h2>Service Types — <em>My Workshop</em></h2>

<table>
  <thead>
    <tr><th>Name</th><th>Duration (min)</th><th></th></tr>
  </thead>
  <tbody>
    <tr><td>Oil Change</td><td>45</td><td class="actions"><button class="btn">Edit</button><button class="btn">Delete</button></td></tr>
    <tr><td>Full Inspection</td><td>90</td><td class="actions"><button class="btn">Edit</button><button class="btn">Delete</button></td></tr>
    <tr><td>Brake Inspection</td><td>60</td><td class="actions"><button class="btn">Edit</button><button class="btn">Delete</button></td></tr>
  </tbody>
</table>

<fieldset>
  <legend>Add service type</legend>
  <div class="row">
    <div>
      <label for="svc-name">Name <span style="color:#c00">*</span></label>
      <input id="svc-name" type="text" placeholder="e.g. Timing Belt Replacement">
    </div>
    <div>
      <label for="svc-dur">Duration (minutes) <span style="color:#c00">*</span></label>
      <input id="svc-dur" type="number" min="15" step="15" placeholder="e.g. 120">
      <div class="hint">Multiples of 15 min only (15, 30, 45 …)</div>
      <div class="error" style="display:none" id="dur-err">Must be a positive multiple of 15.</div>
    </div>
  </div>
  <br>
  <button class="btn btn-primary">Save service type</button>
</fieldset>

</body>
</html>
```
