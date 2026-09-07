# ERD — Community Cooking Rota

## Entities

### User (Django built-in)
- id
- username, email, password
- (standard Django auth fields)

### Profile (1—1 with User)
- id
- user (OneToOneField → User)
- role (choices: "organiser" / "cook")
- created_at

### Rota (organiser owns; 1—N from User as organiser)
- id
- organiser (ForeignKey → User)
- recipient_name
- occasion
- dietary_notes
- address
- start_date
- end_date
- created_at
- updated_at

### Slot (1—N from Rota; optionally claimed by a cook)
- id
- rota (ForeignKey → Rota)
- date
- cook (ForeignKey → User, null=True, blank=True — unclaimed until a cook claims it)
- notes
- claimed_at
- created_at

## Relationships

```
User 1───1 Profile
User 1───N Rota        (as organiser)
Rota 1───N Slot
User 1───N Slot         (as cook, nullable until claimed)
```

## Notes

- A Slot's `cook` field starts empty (unclaimed). A cook claiming a slot is an UPDATE on Slot, not a new model.
- Only the Rota's organiser can create/edit/delete that Rota and its Slots.
- Only a Slot's claimant (or the Rota's organiser) can un-claim (clear `cook` on) a Slot.
- Anonymous users can view nothing beyond the public marketing pages.
