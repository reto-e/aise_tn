# Prompts

Prompts used during the CAS AI workshop. Copy the block between the `EOF` markers.

---

## Demo — Hallucination test (marble & cup)

Use live in class to demonstrate that LLMs predict patterns, not physical reality.

```bash
You place a marble on a table.
You place a cup with the open side facing downwards over this marble.
Then you carry the cup to a chair.
Where is the marble now?
```

---

## 1.1 — Get overview of the platform

Generate an Archimate-style visualisation of the Torqvoice platform to get a quick overview.

```bash
You are an experienced enterprise architect.

Analyse the Torqvoice car workshop management system based on the the docs at https://github.com/Torqvoice/torqvoice 

Generate an Archimate-style overview of the platform. Include:
- The main functional domains (e.g. booking, inventory, customer management)
- Key actors / user roles
- Core system components and their relationships
- External integrations if any

Use your excalidraw-diagrams skill to output the result as a json that can be pasted into Excalidraw. Store it in outputs/archimate_overview.json
```

---

## 2.1 — Create a stakeholder list

```bash

Create a stakeholder list for the torqvoice workshops system. For each stakeholder, provide:
- Name / role
- Primary interest in the system
- Influence (high / medium / low)
- Impact if needs are not met

Consider both internal stakeholders (e.g. workshop staff) and external ones (e.g. car owners, parts suppliers).

Format the result as a markdown table. Store it in outputs/stakeholders.md
```

---

## 2.2 — Create a persona

```bash
Create a detailed persona for the following stakeholder: [STAKEHOLDER ROLE]. You will find infos about this role in outputs/stakeholders.md

Include:
- Name, age, background
- Goals and motivations related to the system
- Pain points with the current process
- A typical day / workflow involving the system
- Quote that captures their attitude

Keep the persona realistic and grounded in the car workshop domain.

Store the output as outputs/persona.md 
Ask me for the [STAKEHOLDER ROLE] first

```

---

## 2.3a — Interview preparation (specs by example)

Prepare rules, examples, and questions before an AI-simulated stakeholder interview.

```bash
You are a requirements engineer preparing to interview a stakeholder about the Torqvoice car workshop system.

Based on the feature "Self service booking for customers" simulate a specs by example workshop using the specs-by-ex skill. 
```

---

## 2.3b — Interview simulation (AI as stakeholder)

Run a dry-run interview with AI playing the stakeholder role.

```bash
You are [STAKEHOLDER NAME], a [STAKEHOLDER ROLE] at a car workshop.

I am a requirements engineer and I will interview you about [TOPIC].
Please stay in character throughout. Answer from your perspective, including frustrations, workarounds, and priorities.
Do not reveal requirements proactively — wait for me to ask.
We will conduct the interview in voice mode.

Persona:
[PASTE PERSONA HERE]

Start by briefly introducing yourself in character. Then wait for my first question.
```

---

## 2.3c — Story map from interview transcript

```bash
You are a requirements engineer. Below is a transcript of a stakeholder interview about Torqvoice.

Extract a user story map from this transcript. Structure the output as:
- Activities (top level, left to right flow)
  - Tasks under each activity
    - User stories under each task (format: "As a [role], I want to [action] so that [benefit]")

Mark stories that seem high-priority with [P1] and those that are uncertain with [?].

Interview transcript:
[PASTE TRANSCRIPT HERE]
```

---

## 2.4 — Find dissatisfiers via code and DB analysis

```bash
You are a requirements engineer analysing the Torqvoice codebase and database schema.

Your goal is to identify "dissatisfiers" — basic requirements that users expect as a minimum but that may be missing, incomplete, or broken in the current system (Kano model: must-be quality).

Analyse the available code and DB structure and provide:
1. A list of inferred basic requirements (what the system currently does)
2. Gaps or weaknesses you detect (what seems missing or fragile)
3. Suggested additions to the story map

Focus on functional behaviour visible to end users.
```

---

## 2.5 — Write a user story

```bash
You are a requirements engineer working on Torqvoice.

Write a user story for the following item from the story map using the story-writer-skill
```

---

## 2.6 — Document screenshots and create a BPMN diagram

```bash
You are a requirements engineer.

I have run through the Torqvoice booking flow using Playwright and captured screenshots.
The screenshots are attached.

1. Describe each screen in one sentence (what the user sees and can do)
2. Identify the sequence of steps as a process flow
3. Output a BPMN-style process description in text form with the following elements:
   - Start event
   - Tasks (with actor: user or system)
   - Gateways (decisions)
   - End event(s)

Highlight any steps where the flow is unclear or where a screenshot seems to be missing.
```

---

## 3.3 — Find lateral traceability between user stories

```bash
You are a requirements engineer working on Torqvoice.

Below is a list of user stories from the Jira backlog.

Identify lateral traceability relationships between these stories. For each pair, state:
- Relationship type: Dependency / Conflict / Refinement
- Direction: Story A → Story B (or bidirectional)
- Reason: one sentence explaining the link

Definitions:
- Dependency: Story A cannot be implemented without Story B being done first
- Conflict: Story A and Story B make contradictory assumptions about the system
- Refinement: Story A is a more detailed version of or derived from Story B

Output a markdown table with columns: Story A | Relationship | Story B | Reason

User stories:
[PASTE YOUR STORIES HERE]
```

---

## 3.4 — Impact analysis for a change request

```bash
You are a requirements engineer working on Torqvoice.

A change request has been raised: the self-service booking flow must support guest users who book without creating an account.

Perform an impact analysis based on the user stories and acceptance criteria below.

For each requirement, state:
- Impact: None / Low / High
- What must change: requirement text, acceptance criterion, or process step
- Lateral dependencies affected: which other requirements are touched

Focus on: authentication assumptions, data model changes, confirmation flow, and GDPR implications.

Requirements:
[PASTE YOUR JIRA STORIES AND ACCEPTANCE CRITERIA HERE]
```

---

## 3.5 — Priority check: backlog alignment with impact map goal

```bash
You are a requirements engineer and product owner for Torqvoice.

Goal from impact map: [INSERT GOAL]
Target behaviour change: [INSERT IMPACT]

Here is the current backlog:
[PASTE YOUR STORIES WITH STATUS: done / in progress / to-do]

For each story, assess:
- Is it aligned with the stated goal? (Yes / Partial / No)
- If partial or no: why does it exist, or is it scope creep?
- MoSCoW priority: Must / Should / Could / Won't (given the goal)

Recommend which stories to reprioritise or drop.
```

---

## 3.x — Devil's advocate (counter anchoring)

Use this after generating any AI output (stakeholder map, requirements list, etc.) to break anchoring bias.

```bash
Review the following [requirements / stakeholder map / user story / ...] and argue against it.

Specifically:
- What is wrong or incomplete?
- Which stakeholders or scenarios are missing?
- Which assumptions are questionable?
- What could go wrong if we implemented this as written?

Be critical. Do not simply validate what is there.

[PASTE OUTPUT TO REVIEW HERE]
```
