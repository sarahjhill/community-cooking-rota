# Low-fi wireframes — Community Cooking Rota

Rough layout notes for the MVP screens. Sketch these properly (Balsamiq/Figma/pen & paper photo) before Day 62 build work — this is the structural placeholder so nothing gets missed.

## Mobile (base breakpoint)

```
┌───────────────────────┐
│  ☰   Community         │
│      Cooking Rota      │
├───────────────────────┤
│ [ Log in ] [ Sign up ] │
├───────────────────────┤
│  Hero: one-line pitch  │
│  + CTA button          │
├───────────────────────┤
│  How it works (3 steps)│
├───────────────────────┤
│  Footer / credits      │
└───────────────────────┘
```

### Organiser — Rota list (logged in)
```
┌───────────────────────┐
│ Nav (role: Organiser)  │
├───────────────────────┤
│ [ + New rota ]         │
├───────────────────────┤
│ Rota card              │
│  recipient · dates     │
│  [ View ] [ Edit ] [x] │
├───────────────────────┤
│ Rota card ...          │
└───────────────────────┘
```

### Rota detail — Slot list
```
┌───────────────────────┐
│ Rota: recipient name   │
│ dietary notes / address│
├───────────────────────┤
│ [ + Add slot ]  (org.) │
├───────────────────────┤
│ Slot: date              │
│  status: open/claimed  │
│  [ Claim ] or [ Cancel]│
├───────────────────────┤
│ Slot: date  ...         │
└───────────────────────┘
```

## Desktop (≥768px)

Same content, two-column layout: rota list / detail side-by-side once a rota is selected; slot cards in a responsive grid rather than a single column.

## Notes

- Every create/update/delete/claim action shows a Django `messages` banner at the top of the page.
- No admin-only actions — every CRUD action above has a front-end form or button.
- Buttons/links get real focus states and sufficient contrast (WCAG AA) — see the accessibility pass task later in the plan.
