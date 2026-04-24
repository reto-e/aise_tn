---
name: playwright
description: Write and run Playwright browser automation tests
---

# Playwright

Use this skill to create or extend Playwright end-to-end tests.

## Setup (first time only)

Install Playwright and its browsers:

```bash
npm init playwright@latest
```

Or add it to an existing project:

```bash
npm install -D @playwright/test
npx playwright install
```

## Writing a test

Create a file like `tests/<feature>.spec.ts`:

```typescript
import { test, expect } from '@playwright/test';

test('page title is correct', async ({ page }) => {
  await page.goto('https://example.com');
  await expect(page).toHaveTitle(/Example/);
});
```

## Common patterns

| Action | Code |
|---|---|
| Navigate | `await page.goto('https://...')` |
| Click | `await page.click('text=Submit')` |
| Fill input | `await page.fill('#email', 'user@example.com')` |
| Assert text | `await expect(page.locator('h1')).toHaveText('Hello')` |
| Assert URL | `await expect(page).toHaveURL(/dashboard/)` |
| Wait for element | `await page.waitForSelector('.result')` |
| Screenshot | `await page.screenshot({ path: 'screenshot.png' })` |

## Running tests

```bash
# Run all tests (headless)
npx playwright test

# Run with browser visible
npx playwright test --headed

# Run a specific file
npx playwright test tests/login.spec.ts

# Open interactive UI mode
npx playwright test --ui
```

## Steps for a new test

1. Identify the user flow to test (e.g. login, checkout, form submission)
2. Create `tests/<flow>.spec.ts`
3. Use `page.goto()` to start at the relevant URL
4. Chain actions (click, fill, select) to reproduce the flow
5. Add `expect()` assertions at key checkpoints
6. Run with `npx playwright test --headed` to visually verify
7. Run headless in CI with `npx playwright test`
