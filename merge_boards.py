#!/usr/bin/env python3
"""
Merge board_00.excalidraw and board_01.excalidraw into clean_board.excalidraw.

Strategy:
- Use known coordinate regions to carve out distinct diagrams.
- Classify each region as story_map, archimate, dependency_map, wireframe, or other.
- Re-layout in a clean grid: story maps, then archimate, then dependency, then other.
- Write merged JSON.
"""

import json
import sys
from collections import defaultdict


def load(path):
    with open(path) as f:
        return json.load(f)


def bounding_box(elements):
    if not elements:
        return (0, 0, 0, 0)
    xs_min = min(e["x"] for e in elements)
    ys_min = min(e["y"] for e in elements)
    xs_max = max(e["x"] + e.get("width", 0) for e in elements)
    ys_max = max(e["y"] + e.get("height", 0) for e in elements)
    return (xs_min, ys_min, xs_max, ys_max)


def translate_elements(elements, dx, dy):
    """Translate all elements by dx, dy."""
    result = []
    for e in elements:
        ne = dict(e)
        ne["x"] = e["x"] + dx
        ne["y"] = e["y"] + dy
        # Shift line/arrow start/end points if stored as absolute coords
        if "points" in ne:
            ne["points"] = [[p[0] + dx, p[1] + dy] for p in ne["points"]]
        result.append(ne)
    return result


def elements_in_region(elements, x1, y1, x2, y2, partial=False):
    """Return elements whose centre (or bbox) falls within the region."""
    result = []
    for e in elements:
        cx = e["x"] + e.get("width", 0) / 2
        cy = e["y"] + e.get("height", 0) / 2
        if x1 <= cx <= x2 and y1 <= cy <= y2:
            result.append(e)
    return result


def classify_text(elements):
    """Return category string based on text heuristics."""
    all_text = " ".join(
        (e.get("text", "") or e.get("originalText", "")).lower()
        for e in elements
        if e["type"] == "text"
    )

    # Mermaid
    if any(kw in all_text for kw in
           ["graph ", "flowchart", "sequencediagram", "classdiagram", "erdiagram"]):
        return "mermaid"

    # Dependency map
    dep_count = all_text.count("dependency") + all_text.count("refinement") + all_text.count("conflict")
    if dep_count >= 5:
        return "dependency_map"

    # Story map
    story_score = sum(1 for kw in [
        "user story map", "story map", "[p1]", "[?]", "activity 1", "activity 2",
        "1. access", "1. service", "2. describe", "receive & respond", "as a ",
        "as tech", "as customer", "as mgmt"
    ] if kw in all_text)
    if story_score >= 2:
        return "story_map"

    # Archimate
    arch_score = sum(1 for kw in [
        "archimate", "motivation layer", "business layer", "technology layer",
        "implementation layer", "presentation layer", "business actors",
        "application layer", "data & infrastructure", "functional domains",
        "archimate-style", "archimate 3.2", "actors / roles",
        "torqvoice platform overview", "workshop management platform",
        "enterprise architecture"
    ] if kw in all_text)
    if arch_score >= 2:
        return "archimate"

    # Wireframe
    if any(kw in all_text for kw in
           ["wireframe", "low fidelity", "screen", "portal\n/auth", "1. portal", "book service"]):
        return "wireframe"

    # KAN stories = dependency_map / story extension
    if all_text.count("kan-") >= 3:
        return "dependency_map"

    return "other"


def main():
    print("Loading files…")
    b00 = load("/home/teig/Projects/aise_tn/board_00.excalidraw")
    b01 = load("/home/teig/Projects/aise_tn/board_01.excalidraw")

    e00 = [e for e in b00["elements"] if not e.get("isDeleted", False)]
    e01 = [e for e in b01["elements"] if not e.get("isDeleted", False)]
    print(f"  board_00: {len(b00['elements'])} total, {len(e00)} non-deleted")
    print(f"  board_01: {len(b01['elements'])} total, {len(e01)} non-deleted")

    # ── board_00 regions ──────────────────────────────────────────────────────
    # Identified from coordinate analysis:
    # Region A: Workshop notes/brainstorm (sticky notes, top area)
    #   x ~ -900 to 1600,  y ~ -300 to 700
    # Region B: Small archimate sketch (top left area with "Torqvoice Workshop Management System")
    #   x ~ -900 to -100, y ~ -300 to 1300 (overlaps with A - use tighter box)
    #   Actually: x ~ -900 to -100, y ~ -300 to 1250
    # Region C: Archimate full (Motivation/Business/Technology layers)
    #   x ~ 2500 to 3700, y ~ 196 to 1250
    # Region D: Archimate v0 mini (Presentation/Business Logic/Data layers)
    #   x ~ 1300 to 2300, y ~ 710 to 1250
    # Region E: Archimate v1 full  (x ~ -950 to 2600, y ~ 1300-1950)
    # Region F: Stakeholder table  (x ~ -2450 to -2200, y ~ 1850-1960)
    # Region G: Archimate v2       (x ~ -970 to 5960, y ~ 1938-3000)
    # Region H: Archimate v3       (x ~ -970 to 6600, y ~ 3013-3900)
    # Region I: Archimate v4 extended (x ~ -1130 to 7300, y ~ 3894-5813)
    # Region J: "marble on table" / stray text  (x ~ 1540, y ~ 820-930)
    # Region K: stray lone rectangle (x ~ -6802, y ~ 426)

    # board_01 regions:
    # Region L: Customer Portal Story Map (y ~ -7450 to -7080)
    # Region M: Self-Service Booking Story Map (x ~ 1880-4350, y ~ 0-900)
    # Region N: Wireframe (x ~ 8680-10800, y ~ 0-900)
    # Region O: Service Quality Story Map (x ~ 522-4250, y ~ 900-2800)
    # Region P: KAN stories / story extension (x ~ 4250-13000, y ~ 1700-2800)
    # Region Q: Dependency / story dependency map (y ~ 2800-6300)
    # Region R: Stray 2 elements (y ~ -2270 to -2190)

    INF = 1e9

    # Carve out regions with element_in_region using centre-point test
    regions_00 = [
        {
            "name": "00-A: Workshop brainstorm sticky notes",
            "category": "other",
            "bbox": (-900, -400, 1750, 1280),
        },
        {
            "name": "00-C: Archimate full layers (Motivation/Biz/Tech)",
            "category": "archimate",
            "bbox": (2490, 150, 3700, 1280),
        },
        {
            "name": "00-D: Presentation/Biz/Data layers mini",
            "category": "archimate",
            "bbox": (1720, 710, 2490, 1280),
        },
        {
            "name": "00-E: Archimate v1 mini + full (y~1280-1960)",
            "category": "archimate",
            "bbox": (-970, 1280, 2700, 1970),
        },
        {
            "name": "00-F: Stakeholder analysis Markdown",
            "category": "other",
            # wide text element: x=-2396, w=3179 → centre x=-806; y=1882, h=600 → centre y=2182
            "bbox": (-2500, 1870, 1000, 2500),
        },
        {
            "name": "00-G: Archimate v2 (ArchiMate-style full)",
            "category": "archimate",
            "bbox": (-970, 1970, 6100, 3020),
        },
        {
            "name": "00-H: Archimate v3 (simplified v2)",
            "category": "archimate",
            "bbox": (-990, 3000, 6700, 3910),
        },
        {
            "name": "00-I: Archimate v4 extended annotated",
            "category": "archimate",
            "bbox": (-1140, 3890, 7400, 5900),
        },
    ]

    regions_01 = [
        {
            "name": "01-L: Customer Portal Story Map",
            "category": "story_map",
            "bbox": (1400, -7500, 2500, -7050),
        },
        {
            "name": "01-J: Maria Customer Journey Storyboard",
            "category": "story_map",
            "bbox": (650, 200, 1860, 820),
        },
        {
            "name": "01-M: Self-Service Booking Story Map",
            "category": "story_map",
            "bbox": (1860, -50, 4600, 920),
        },
        {
            "name": "01-N: Wireframe (Self-Service Booking UX)",
            "category": "wireframe",
            "bbox": (8640, -50, 11000, 920),
        },
        {
            "name": "01-O: Service Quality Story Map + Screenshots",
            "category": "story_map",
            "bbox": (490, 880, 8700, 2850),
        },
        {
            "name": "01-Q: KAN user stories grid",
            "category": "dependency_map",
            "bbox": (8700, 1650, 13200, 2900),
        },
        {
            "name": "01-R: Story dependency map",
            "category": "dependency_map",
            "bbox": (490, 2800, 21000, 6400),
        },
        {
            "name": "01-S: Stray elements (y~-2200)",
            "category": "other",
            "bbox": (2700, -2300, 3200, -2100),
        },
    ]

    # We'll use a simpler approach: assign each element to the first matching region
    # and collect unassigned elements into "other".
    # Process board_00 and board_01 separately.

    def assign_regions(elements, region_specs, source_label):
        assigned = defaultdict(list)  # region_name -> elements
        unassigned = []

        for e in elements:
            cx = e["x"] + e.get("width", 0) / 2
            cy = e["y"] + e.get("height", 0) / 2
            matched = None
            for r in region_specs:
                x1, y1, x2, y2 = r["bbox"]
                if x1 <= cx <= x2 and y1 <= cy <= y2:
                    matched = r["name"]
                    break
            if matched:
                assigned[matched].append(e)
            else:
                unassigned.append(e)

        return assigned, unassigned

    print("\nAssigning board_00 elements to regions…")
    assigned_00, unassigned_00 = assign_regions(e00, regions_00, "board_00")
    print(f"  Assigned: {sum(len(v) for v in assigned_00.values())} elements")
    print(f"  Unassigned: {len(unassigned_00)} elements")
    for r in regions_00:
        n = len(assigned_00.get(r["name"], []))
        print(f"    {r['name']}: {n} elements")

    print("\nAssigning board_01 elements to regions…")
    # board_01 has overlapping regions (P is subset of O), so order matters.
    # We want the more specific region to win — put it first.
    # Actually our regions don't overlap for board_01 — let's verify.
    assigned_01, unassigned_01 = assign_regions(e01, regions_01, "board_01")
    print(f"  Assigned: {sum(len(v) for v in assigned_01.values())} elements")
    print(f"  Unassigned: {len(unassigned_01)} elements")
    for r in regions_01:
        n = len(assigned_01.get(r["name"], []))
        print(f"    {r['name']}: {n} elements")

    # ── classify and label clusters ────────────────────────────────────────────
    # Build a flat list of (label, category, elements)
    all_region_specs = regions_00 + regions_01
    all_assigned = {**assigned_00, **assigned_01}

    clusters = []
    for r in all_region_specs:
        elems = all_assigned.get(r["name"], [])
        if not elems:
            continue
        # Trust the explicit category from the region spec.
        # Auto-infer is only used for the unassigned bucket below.
        cat = r["category"]
        inferred = classify_text(elems)
        clusters.append({
            "name": r["name"],
            "category": cat,
            "inferred": inferred,
            "elements": elems,
        })

    # Add unassigned elements — auto-classify them
    all_unassigned = unassigned_00 + unassigned_01
    if all_unassigned:
        inferred_cat = classify_text(all_unassigned)
        clusters.append({
            "name": "unassigned / stray elements",
            "category": inferred_cat if inferred_cat != "other" else "other",
            "inferred": inferred_cat,
            "elements": all_unassigned,
        })

    print("\nAll clusters:")
    for c in clusters:
        bb = bounding_box(c["elements"])
        w = bb[2] - bb[0]
        h = bb[3] - bb[1]
        print(f"  [{c['category']:15s}] {c['name']:55s}  {len(c['elements']):4d} elems  "
              f"size=({w:.0f}x{h:.0f})")

    # ── layout ────────────────────────────────────────────────────────────────
    # Sections in order; within each section, lay clusters out horizontally
    # with CLUSTER_H_GAP between them. Then SECTION_V_GAP between sections.
    CLUSTER_H_GAP = 2500    # horizontal gap between clusters in same section
    SECTION_V_GAP = 3000    # vertical gap between sections
    SECTION_PADDING = 200   # extra top padding within each section

    category_order = [
        "story_map",
        "wireframe",
        "archimate",
        "dependency_map",
        "mermaid",
        "other",
    ]

    # Group clusters by category
    by_cat = defaultdict(list)
    for c in clusters:
        by_cat[c["category"]].append(c)

    print("\nLayout:")
    final_elements = []
    current_y = 0

    for category in category_order:
        cat_clusters = by_cat.get(category, [])
        if not cat_clusters:
            continue

        print(f"\n  === {category.upper()} ({len(cat_clusters)} clusters) ===")

        # Sort by element count descending (largest first)
        cat_clusters = sorted(cat_clusters, key=lambda c: len(c["elements"]), reverse=True)

        cursor_x = 0
        max_h_in_row = 0

        for c in cat_clusters:
            elems = c["elements"]
            bb = bounding_box(elems)
            w = bb[2] - bb[0]
            h = bb[3] - bb[1]

            dx = cursor_x - bb[0]
            dy = current_y + SECTION_PADDING - bb[1]

            moved = translate_elements(elems, dx, dy)
            final_elements.extend(moved)

            print(f"    {c['name'][:60]:60s}  "
                  f"{len(elems):4d} elems  "
                  f"({w:.0f}x{h:.0f})  "
                  f"→ placed at ({cursor_x:.0f}, {current_y+SECTION_PADDING:.0f})")

            cursor_x += w + CLUSTER_H_GAP
            max_h_in_row = max(max_h_in_row, h)

        current_y += max_h_in_row + SECTION_PADDING + SECTION_V_GAP

    # ── merge files dict ───────────────────────────────────────────────────────
    merged_files = {}
    merged_files.update(b00.get("files", {}))
    merged_files.update(b01.get("files", {}))

    # ── write output ──────────────────────────────────────────────────────────
    out = {
        "type": b00["type"],
        "version": b00["version"],
        "source": b00.get("source", "https://excalidraw.com"),
        "elements": final_elements,
        "appState": {
            **b00.get("appState", {}),
            "scrollX": 0,
            "scrollY": 0,
            "zoom": {"value": 0.5},
        },
        "files": merged_files,
    }

    out_path = "/home/teig/Projects/aise_tn/clean_board.excalidraw"
    with open(out_path, "w") as f:
        json.dump(out, f, ensure_ascii=False)

    import os
    size_mb = os.path.getsize(out_path) / 1e6
    print(f"\nWrote {len(final_elements)} elements to {out_path}  ({size_mb:.2f} MB)")

    # Summary stats
    print("\nSummary by category:")
    for category in category_order:
        cat_clusters = by_cat.get(category, [])
        total_elems = sum(len(c["elements"]) for c in cat_clusters)
        if total_elems:
            print(f"  {category:20s}: {len(cat_clusters):2d} clusters, {total_elems:5d} elements")


if __name__ == "__main__":
    main()
