# Community Cooking Rota

**Live app:** _add your Heroku link here once deployed_
**Repository:** https://github.com/sarahjhill/community-cooking-rota

## Introduction

Community Cooking Rota is a Django web app that helps a support network organise home-cooked meals for someone going through a hard patch — new parents, a household recovering from surgery or bereavement, or an elderly neighbour who could use the help. An organiser creates a rota for the recipient, sets the dates, and invites cooks; each cook registers, claims an open slot, and can see delivery and dietary details, cancelling if their plans change. It replaces the ad-hoc spreadsheet-and-WhatsApp approach with a simple, accountable, full CRUD web app built around one real, everyday problem.

This is a Full-Stack Individual Capstone Project for the Code Institute AI Augmented Full-Stack Bootcamp.

## The idea

A Django rebuild of the rota concept from the `cardiff-community-meals` project, reworked as a full account-based CRUD app (rather than a static link-and-access-code page) so it satisfies the auth, CRUD and testing requirements of this assessment.

- **Organiser** — creates a rota for a recipient, sets the date range, invites cooks, edits or deletes the rota and its slots.
- **Cook** — registers/logs in, browses open slots on rotas they've been invited to (or that are public), claims a slot, can cancel their own claim, sees dietary notes and delivery details.

## MVP scope

- User registration/login/logout with a role (Organiser or Cook) chosen at signup.
- Organiser: create, view, edit, delete a Rota (recipient, occasion, dietary notes, address, dates).
- Organiser: create, edit, delete Slots (cooking dates) within a Rota.
- Cook: view a Rota's open slots; claim a slot via a form (no admin panel); cancel their own claimed slot.
- Access control: only the organiser can edit/delete their own rota and its slots; only a slot's claimant (or the organiser) can un-claim it; anonymous users can't reach any of the above.
- On-page notifications (Django messages) for every create/update/delete/claim action.
- Responsive, accessible front end (Bootstrap 5 + custom CSS).
- Automated tests for models, views and permissions, plus a manual test log.
- Deployed to Heroku with `DEBUG=False` and secrets in environment variables.

## Data model (ERD)

`User 1—1 Profile` · `User 1—N Rota` (as organiser) · `Rota 1—N Slot` · `User 1—N Slot` (as cook, nullable until claimed)

See `docs/erd.md` for the full breakdown.

## Future features

- Recipe/dish attached to a slot, with its own CRUD (what's being cooked, allergens).
- Comment/update thread on a rota so cooks can leave notes for each other.
- Swap requests between cooks.
- Email reminders a day before a claimed slot.
- Public invite link + join code layered on top of accounts.
- iCal export / calendar view.
- Photo/confirmation upload when a meal is delivered.
- Search/filter rotas by dietary tag or date range.

## Tech stack

- Django 5 + Python 3
- SQLite locally, PostgreSQL in production
- Bootstrap 5 + custom CSS
- Django's built-in auth (`User` + a `Profile` model with a role field)
- Heroku for deployment

## Local setup

```bash
git clone https://github.com/sarahjhill/community-cooking-rota.git
cd community-cooking-rota
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Testing

_To be completed as the app is built — manual test table, automated test summary, and validator results (HTML, CSS, PEP8, Lighthouse) will go here._

## Deployment

_Step-by-step Heroku deployment instructions will go here once deployed._

## AI usage

_A brief, honest reflection on where AI assistance helped with planning, scaffolding, code generation, debugging and testing will go here._

## Credits

Planning document and this MVP scope were developed with Claude (Anthropic) as a planning aid, working from the Code Institute assessment guide and Sarah Hill's own project brief.
