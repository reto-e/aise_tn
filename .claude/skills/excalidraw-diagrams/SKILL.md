---
name: excalidraw-diagrams
description: Creates architecture diagrams, UML use case diagrams, and UML data flow diagrams as Excalidraw JSON. Use this skill whenever the user wants to diagram, visualize, or draw a system — architecture, components, services, actors, use cases, or data flows. Triggers on phrases like "draw a diagram", "create an architecture diagram", "use case diagram", "data flow diagram", "visualize the system", "show the components", even if "Excalidraw" is not mentioned. When in doubt, use this skill — it's better to offer a diagram than to describe a system in prose.
---

# Excalidraw Diagram Creator

You create three types of system diagrams as valid Excalidraw JSON: **architecture diagrams**, **UML use case diagrams**, and **UML data flow diagrams**.

## Workflow

1. **Get a name** — if the user hasn't given a diagram title, ask for one.
2. **Clarify if needed** — for complex diagrams, ask which components/actors/flows to include. For simple requests, make reasonable assumptions and note them.
3. **Plan the layout** — think about grouping, zones, and element positions before writing JSON.
4. **Output the Excalidraw JSON** — a complete `.excalidraw` file the user can open directly in Excalidraw.
5. **Offer export** — after the JSON, ask: *"Would you like me to push this to excalidraw.com for a shareable link?"* If yes, call `mcp__claude_ai_Excalidraw__export_to_excalidraw` with the JSON.

---

## Excalidraw JSON Format

### Top-level file structure

Every output must be a complete `.excalidraw` file, not just an elements array:

```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [ ...elements... ],
  "appState": {
    "gridSize": null,
    "viewBackgroundColor": "#ffffff"
  },
  "files": {}
}
```

### Required base fields on every element

All element types share these fields. Never omit them:

```json
{
  "id": "r1",
  "type": "rectangle",
  "x": 100,
  "y": 100,
  "width": 200,
  "height": 80,
  "angle": 0,
  "strokeColor": "#1e1e1e",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "strokeStyle": "solid",
  "roughness": 1,
  "opacity": 100,
  "roundness": null,
  "groupIds": [],
  "frameId": null,
  "boundElements": [],
  "link": null,
  "locked": false,
  "seed": 100001,
  "version": 1,
  "versionNonce": 0,
  "isDeleted": false,
  "updated": 1700000000000
}
```

Use sequential seeds (100001, 100002, …). Use the same `updated` timestamp throughout one diagram.

### Element types

**Rectangle / Diamond / Ellipse** — use the base fields above with the appropriate `type`. For rounded corners on rectangles: `"roundness": {"type": 3}`.

**Text** — standalone text for titles and zone labels:

```json
{
  "type": "text",
  "id": "t1",
  "x": 150,
  "y": 30,
  "width": 300,
  "height": 35,
  "text": "My Diagram",
  "fontSize": 28,
  "fontFamily": 1,
  "textAlign": "left",
  "verticalAlign": "top",
  "containerId": null,
  "originalText": "My Diagram",
  "autoResize": true,
  "lineHeight": 1.25,
  ...base fields...
}
```

fontFamily: `1` = Virgil (hand-drawn), `2` = Helvetica, `3` = Cascadia Code

**Text inside a shape** — requires TWO elements: the shape with `boundElements`, and a text element with `containerId`:

```json
{
  "type": "rectangle",
  "id": "r1",
  ...base fields...,
  "boundElements": [{"type": "text", "id": "r1_text"}]
},
{
  "type": "text",
  "id": "r1_text",
  "x": 110,
  "y": 125,
  "width": 180,
  "height": 30,
  "text": "Service A",
  "fontSize": 18,
  "fontFamily": 1,
  "textAlign": "center",
  "verticalAlign": "middle",
  "containerId": "r1",
  "originalText": "Service A",
  "autoResize": true,
  "lineHeight": 1.25,
  ...base fields (backgroundColor: "transparent", strokeColor: "#1e1e1e")...
}
```

Position text at the center of the shape: `x = shape.x + shape.width/2 - text.width/2`, `y = shape.y + shape.height/2 - text.height/2`.

**Arrow**:

```json
{
  "type": "arrow",
  "id": "a1",
  "x": 300,
  "y": 140,
  "width": 150,
  "height": 0,
  "points": [[0, 0], [150, 0]],
  "startArrowhead": null,
  "endArrowhead": "arrow",
  "startBinding": null,
  "endBinding": null,
  "elbowed": false,
  "roundness": {"type": 2},
  ...base fields...
}
```

`endArrowhead`: `"arrow"` | `"triangle"` | `"bar"` | `"dot"` | `null`

For dashed arrows (UML include/extend): add `"strokeStyle": "dashed"` to the base fields.

Arrow bindings (optional but recommended for connected arrows):
```json
"startBinding": { "elementId": "r1", "focus": 0, "gap": 1, "fixedPoint": null },
"endBinding":   { "elementId": "r2", "focus": 0, "gap": 1, "fixedPoint": null }
```

---

## Color palette

| Fill | Hex | Use |
|------|-----|-----|
| Light Blue | `#a5d8ff` | Inputs, primary nodes, frontend |
| Light Green | `#b2f2bb` | Outputs, success, completed |
| Light Purple | `#d0bfff` | Processing, logic, backend |
| Light Orange | `#ffd8a8` | External, warnings |
| Light Teal | `#c3fae8` | Storage, databases |
| Light Yellow | `#fff3bf` | Notes, decisions, business layer |

For zone backgrounds, set `"opacity": 30` and use a light fill. Zone rectangles have no text; use a separate `text` element for the zone label.

Stroke colors that pair with fills: `#f59e0b` (amber), `#4a9eed` (blue), `#22c55e` (green), `#8b5cf6` (purple), `#ef4444` (red).

---

## Diagram types

### Architecture Diagrams

Left-to-right or top-to-bottom. Group services by layer using low-opacity zone rectangles. Each zone gets a small text label (fontSize 14–16) in its top-left corner. Services are filled rectangles with rounded corners and a bound text element.

```
[Title]
┌── Frontend ──┐   ┌── Backend ────────────┐   ┌── Data ──┐
│  [Client UI] │──▶│ [API GW]  [Service A] │──▶│ [DB]     │
└──────────────┘   └──────────────────────┘   └──────────┘
```

### UML Use Case Diagrams

- **System boundary**: large rectangle, label at top-left inside the boundary
- **Actors**: outside the boundary — head (ellipse ~24×24) + body (narrow rectangle ~14×30) + name text below
- **Use cases**: ellipses inside the boundary, minimum 140×55, with bound text
- **Association**: arrow with `"endArrowhead": null` (plain line)
- **Include / Extend**: dashed arrow with `"strokeStyle": "dashed"`, labeled with a text element showing `<<include>>` or `<<extend>>`

### UML Data Flow Diagrams

DFD notation:
- **External entity**: rectangle, light fill
- **Process**: ellipse, labeled `1.0\nProcess Name`
- **Data store**: rectangle with `"backgroundColor": "#c3fae8"`, labeled `D1: Store Name`
- **Data flow**: arrow labeled with a small text element near the midpoint

Layout: external entities on edges, processes in centre, data stores between.

---

## Output

Wrap the full JSON in a fenced code block:

````
```json
{
  "type": "excalidraw",
  ...
}
```
````

If the user did not provide a name ask for a file name and store the output as json file.
