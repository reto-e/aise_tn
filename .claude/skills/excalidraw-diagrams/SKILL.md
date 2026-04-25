---
name: excalidraw-diagrams
description: Creates architecture diagrams, UML use case diagrams, and UML data flow diagrams as Excalidraw JSON. Use this skill whenever the user wants to diagram, visualize, or draw a system — architecture, components, services, actors, use cases, or data flows. Triggers on phrases like "draw a diagram", "create an architecture diagram", "use case diagram", "data flow diagram", "visualize the system", "show the components", even if "Excalidraw" is not mentioned. When in doubt, use this skill — it's better to offer a diagram than to describe a system in prose.
---

# Excalidraw Diagram Creator

You create three types of system diagrams as Excalidraw JSON: **architecture diagrams**, **UML use case diagrams**, and **UML data flow diagrams**.

## Workflow

1. **Get a name** — if the user hasn't given a title, ask for one before starting.
2. **Clarify if needed** — for complex diagrams, ask which components/actors/flows to include. For simple requests, make reasonable assumptions and note them.
3. **Plan the layout** — think about grouping, zones, and positions before writing JSON.
4. **Output the Excalidraw JSON** — a complete JSON array the user can paste into Excalidraw.
5. **Offer export** — after the JSON, ask: *"Would you like me to push this to excalidraw.com for a shareable link?"*  If yes, call `mcp__claude_ai_Excalidraw__export_to_excalidraw` with the JSON.

---

## Excalidraw JSON Format

Always begin the elements array with a `cameraUpdate`:
```json
{ "type": "cameraUpdate", "width": 800, "height": 600, "x": 0, "y": 0 }
```

Camera sizes must be exact 4:3 ratios: 400×300 · 600×450 · **800×600 (default)** · 1200×900 · 1600×1200

**Elements:**

```json
// Rectangle (rounded corners)
{ "type": "rectangle", "id": "r1", "x": 100, "y": 100, "width": 200, "height": 80,
  "backgroundColor": "#a5d8ff", "fillStyle": "solid", "roundness": { "type": 3 },
  "label": { "text": "Service A", "fontSize": 18 } }

// Ellipse
{ "type": "ellipse", "id": "e1", "x": 100, "y": 200, "width": 160, "height": 60,
  "backgroundColor": "#d0bfff", "fillStyle": "solid",
  "label": { "text": "Use Case", "fontSize": 16 } }

// Arrow
{ "type": "arrow", "id": "a1", "x": 300, "y": 140, "width": 100, "height": 0,
  "points": [[0,0],[100,0]], "endArrowhead": "arrow" }

// Dashed arrow (UML include/extend)
{ "type": "arrow", "id": "a2", "x": 300, "y": 200, "width": 100, "height": 0,
  "points": [[0,0],[100,0]], "strokeStyle": "dashed", "endArrowhead": "arrow",
  "label": { "text": "<<include>>", "fontSize": 14 } }

// Zone background (use opacity: 30)
{ "type": "rectangle", "id": "z1", "x": 50, "y": 80, "width": 300, "height": 200,
  "backgroundColor": "#dbe4ff", "fillStyle": "solid", "opacity": 30, "strokeColor": "#4a9eed" }

// Title text
{ "type": "text", "id": "t1", "x": 250, "y": 20, "text": "My System", "fontSize": 26 }
```

**Color palette:**

| Fill | Hex | Use |
|------|-----|-----|
| Light Blue | `#a5d8ff` | Inputs, primary nodes, frontend |
| Light Green | `#b2f2bb` | Outputs, success, completed |
| Light Purple | `#d0bfff` | Processing, logic, backend |
| Light Orange | `#ffd8a8` | External, warnings |
| Light Teal | `#c3fae8` | Storage, databases |
| Light Yellow | `#fff3bf` | Notes, decisions |

| Zone | Hex | Layer |
|------|-----|-------|
| `#dbe4ff` | opacity 30 | Frontend / UI |
| `#e5dbff` | opacity 30 | Backend / Logic |
| `#d3f9d8` | opacity 30 | Data / Storage |

**Rules:** minimum font size 16 (titles: 20+); minimum shape size 120×60; IDs must be unique (r1, r2, e1, a1…).

---

## Diagram Types

### Architecture Diagrams

Show system components and their relationships, grouped by layer.

- Layout: left-to-right or top-to-bottom
- Zones: group services by responsibility (frontend / backend / data) using zone background rectangles
- Zone label: small text in the top-left corner of each zone (fontSize 14, muted stroke)
- Title: centered `text` element at the top, fontSize 24–28

Sketch:
```
[Title]
┌── Frontend ──────┐   ┌── Backend ──────────────┐   ┌── Data ──────┐
│  [UI / Client]   │──▶│ [API Gateway]            │──▶│ [Database]   │
└──────────────────┘   │ [Service A]  [Service B] │   └──────────────┘
                       └─────────────────────────┘
```

### UML Use Case Diagrams

Show which actors interact with which use cases in a system.

- System boundary: large rectangle in the center, `label` at top = system name
- Actors: outside the boundary, left and/or right — built from a head ellipse + body rectangle + name text below
- Use cases: ellipses inside the boundary, at least 140×55
- Associations: plain arrows between actors and use cases (no arrowhead style needed — use `"endArrowhead": null` for association lines, or `"arrow"` when directed)
- Include / Extend: dashed arrow between use cases with `<<include>>` or `<<extend>>` label

Actor stick figure (adjust x/y per position):
```json
{ "type": "ellipse",   "id": "ah1", "x": 48, "y": 180, "width": 24, "height": 24,
  "backgroundColor": "#a5d8ff", "fillStyle": "solid", "strokeColor": "#4a9eed" },
{ "type": "rectangle", "id": "ab1", "x": 53, "y": 204, "width": 14, "height": 28,
  "backgroundColor": "#a5d8ff", "fillStyle": "solid", "strokeColor": "#4a9eed",
  "roundness": { "type": 3 } },
{ "type": "text", "id": "an1", "x": 36, "y": 236, "text": "Customer", "fontSize": 16 }
```

Sketch:
```
[Actor] ───── (Use Case 1)
              (Use Case 2) <<include>>──▶ (Use Case 3)
[Actor] ─────────────────╱
```

### UML Data Flow Diagrams

Show how data moves through a system (external entities, processes, data stores, flows).

DFD notation:
- **External entity**: rectangle (plain, no fill or light fill)
- **Process**: ellipse labeled `n.n\nProcess Name` (number + name)
- **Data store**: rectangle labeled `D1: Store Name`, stroke only top/bottom (approximate with a plain labeled rectangle, `fillStyle: "solid"`, `backgroundColor: "#c3fae8"`)
- **Data flow**: arrow labeled with the data being transferred

Layout: external entities on the sides, processes in the center, data stores between processes and entities.

Sketch:
```
[User] ──(login request)──▶ (1.0 Authenticate) ──(token)──▶ [Client]
                                     │
                              (read/write)
                                     │
                                [D1: Users DB]
```

---

## Output

Wrap the JSON in a fenced code block:
````
```json
[ ...elements... ]
```
````

After the block, always ask:
> *Would you like me to push this to excalidraw.com for a shareable link?*
