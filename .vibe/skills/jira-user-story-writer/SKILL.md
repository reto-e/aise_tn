---
name: jira-user-story-writer
description: write concise english jira-ready user stories from short chat notes or bullet points. use when the user describes a requirement informally and wants a story they can copy into jira with a fixed template, iso 29148-style acceptance criteria, invest-oriented wording, clarification questions first, and a lo-fi html prototype for new ui elements. after presenting the story, open a canvas and place the story content there for further editing.
---

Use this skill to turn rough requirement notes into a Jira-ready story.

Follow this workflow exactly:

1. Read the user's notes and identify the requested behavior, actor, business value, affected function, data changes, rules, validation impacts, integration/display impacts, and UI implications.
2. Before drafting any story, ask only the relevant clarification questions as a short checklist. Do not write the story yet. Number the questions so that the user can use those numbers to refer to the questions when answering.
3. After the user answers, write one concise story in English using the exact template below.
4. Check the result against the review checklist before finalizing.
5. If the story introduces new UI elements, append a lo-fi HTML prototype directly in the chat after the story.

## Clarification-first rule
Always ask clarification questions first.

Output the questions as a short numbered list. Keep them terse. Ask only the items that are relevant to the described change.

Use and adapt this checklist:
- Does the search index need to be extended?
- for new input fields: how should they be validated, required or not?
- What exact data fields, business rules, edge cases, and permissions apply?

If critical information is still missing after one round of answers, ask only the remaining blocking questions.

## Output template
When enough information is available, produce exactly this structure:

#### Story
[As a x I want x so that x.]

#### Acceptance Criteria
1. [acceptance criterion]
2. [acceptance criterion]


## Story-writing rules
- Write in English.
- Keep the story short.
- Make the story easy to copy into Jira.
- Use the canonical story form: `As a ... I want ... so that ...`
- Keep one story focused on one vertical slice whenever possible.
- Follow INVEST:
  - independent
  - negotiable
  - valuable
  - estimable
  - small
  - testable
- Prefer a single clear affected function entry. Use a short bullet list only if multiple functions are unavoidable.
- Do not add commentary outside the requested structure unless you need a separate section for follow-up stories or the HTML prototype.

## Acceptance criteria rules
Write numbered acceptance criteria only. Do not use subheadings or labels between them.

Use ISO 29148 sentence logic:
`[<condition>] <subject> <action> <object> [<constraint>]`

Guidance:
- Start each acceptance criterion with `If`, `When`, or `Unless` when a condition exists.
- Name the acting subject explicitly, such as `Workshop Manager`, `Technician`, `Torqvoice`, etc
- State one observable action and object.
- Avoid modal verbs: Instead of `Torqvoice shall display the link` write `Torqvoice displays the link`
- End with a constraint or result when needed.
- Keep each criterion testable and unambiguous.
- Cover ideal flow first, then alternative flows, then postconditions.
- Include relevant data and business rules.
- Cover validation, permissions, empty states, and error states when applicable.
- Split broad behavior into multiple criteria instead of writing compound sentences.

## Review checklist before final answer
Silently verify that:
- the acceptance criteria are ordered as ideal flow, alternative flows, then postconditions
- all relevant data aspects are covered
- all relevant rules are covered
- the story is concise and still testable
- the result follows INVEST well enough for a Jira refinement draft
- the wording stays specific and avoids implementation noise unless the user asked for it

## Follow-up stories
If the user confirms that additional surfaces are affected, add a short section after the main story:

#### Follow-up stories
- [surface]: [short follow-up story summary]

Only include this section when clearly needed.

## Lo-fi HTML prototype rule
If the change introduces a new UI element, append a compact lo-fi HTML prototype directly in the chat after the story.

Requirements for the prototype:
- Use plain HTML with minimal inline CSS.
- Keep it lightweight and monochrome.
- Show only the essential layout, fields, labels, buttons, states, and hints.
- Include read-only representation if the clarified requirements say it is needed.
- Do not use JavaScript unless a tiny inline script is necessary to demonstrate a core state.
- Put the code in a fenced `html` block.

## Default response pattern
If information is still missing:
1. output `#### Clarification questions`
2. list the short checklist questions
3. stop

If information is sufficient:
1. output the Jira-ready story using the template
2. optionally output `#### Follow-up stories`
3. optionally output the lo-fi HTML prototype in a fenced `html` block
