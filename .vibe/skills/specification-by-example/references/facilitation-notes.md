# Facilitation Notes

Use these heuristics while running the workshop:

## Good example mix

Aim to cover a mix of:

- happy path
- boundary cases
- invalid or rejected cases
- missing information
- conflicting-rule cases
- terminology traps

## Example format

Prefer examples that can be stated as:

- context
- action or trigger
- expected outcome

or, if simpler:

- given conditions
- expected result

## Attribute discovery cues

Propose a new attribute when examples differ because of:

- amount, count, or size
- status or state
- time or date window
- actor or role
- channel or source
- completeness of data
- exception flag or override

## Boundary prompts

Use prompts like:

- what is the smallest meaningful value?
- what happens at the exact threshold?
- what happens just below and just above it?
- what if the value is missing?
- what combinations are not allowed?

## Rule-writing pattern

Write rules as short business statements, for example:

- when X and Y are true, outcome Z happens
- if A is missing, reject the request
- if value reaches threshold T, switch to outcome B

Avoid implementation phrasing such as database fields, API calls, UI clicks, or code branches unless the user explicitly wants technical detail.
