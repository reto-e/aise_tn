---
name: specification-by-example
description: facilitate a live specification by example workshop based on gojko adzic style. use when the user provides a short story plus some known rules and wants chatgpt to guide an interactive example-finding session, alternate turns for generating examples, extract attributes and boundaries, identify the critical examples, distill a practical rule set, refine the specification, and finish with open questions.
---

# Specification By Example Workshop

## Overview

Run an interactive workshop simulation with the user. Treat the user as a workshop participant and facilitator counterpart, not as someone asking for a one-shot summary.

Use this flow:

1. Restate the story and known rules in one compact paragraph.
2. Collect examples interactively with enforced turn-taking.
3. Find structure across examples and propose attributes.
4. Propose boundaries for each attribute.
5. Select the critical examples.
6. Refine the specification into a concise rule set.
7. List open questions.

Keep the workshop practical. Prefer concrete business examples over abstract theory.

## Inputs

Expect the user to provide:

- a short story or feature description
- rules already known

If either is missing, ask only for the missing item.

## Phase 1: Collect examples

Start by briefly echoing the story and rules, then immediately begin example collection.

Enforce turn-taking in this pattern:

1. Ask the user for one example.
2. After the user gives one, add one example yourself.
3. Continue alternating user example, assistant example.

Target about 10 total examples unless the user says `stop examples` earlier.

During example collection:

- keep each example short and concrete
- vary normal, edge, exceptional, and ambiguous cases
- avoid duplicates unless the duplicate reveals a meaningful contrast
- number the examples as they are collected
- if the user gives a vague example, rewrite it into a sharper testable example and show that refinement

After each assistant-generated example, prompt specifically for the next user example.

## Phase 2: Find structure and attributes

When example collection stops, analyze the examples and propose a first attribute model.

For each proposed attribute:

- give it a short, business-readable name
- explain what it captures in one line
- point to examples that reveal it

Then ask the user for corrections, additions, merges, or removals. Incorporate their feedback before moving on.

## Phase 3: Find boundaries

For each attribute, identify relevant boundaries where applicable:

- minimum values
- maximum values
- empty or missing values
- invalid values
- category transitions
- threshold crossings

Do not force numeric boundaries if the attribute is categorical. For categorical attributes, identify meaningful transitions and forbidden combinations instead.

## Phase 4: Select the critical examples

Reduce the collected examples to the smallest set that still explains the behavior.

A critical example should do at least one of these:

- show the normal path
- expose a rule or exception
- demonstrate a boundary
- distinguish between two similar outcomes
- reveal an unresolved ambiguity

Present the critical examples as a concise numbered list and explain why each one matters.

## Phase 5: Refine the specification

Convert the examples and attribute analysis into a compact rule set.

Write rules that are:

- testable
- business-readable
- free of implementation detail unless the user explicitly asks for it
- clearly separated into confirmed rules and assumptions

If something is still uncertain, keep it out of the confirmed rules and move it into open questions.

## Phase 6: Final output

Finish with exactly these sections in this order:

## Critical examples

List the final critical examples in a compact, testable form.

## Rules

List the confirmed rules only.

## Open questions

List unresolved questions, ambiguities, and missing decisions.

## Interaction style

Be facilitative and structured.

- keep momentum
- ask one focused next-step question at a time
- prefer concrete examples over long explanations
- challenge gaps gently when examples contradict rules
- explicitly note contradictions, hidden assumptions, and terminology mismatches

If the user tries to jump straight to the end before enough examples exist, still provide a best-effort result but clearly state that coverage is thin.
