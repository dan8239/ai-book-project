# Voice Memo Log

Every voice memo that's been through `/organize-ideas`, so none gets processed twice.
`/organize-ideas` checks this before it starts and updates it when it finishes. See
`.claude/commands/organize-ideas.md`, step 0.

**Matching:** Downloads often get re-saved as `Name (1).m4a` with slightly different
metadata bytes, so match on **duration + byte size**, not the filename or a hash.
`./scripts/transcribe-memo.sh <file.m4a>` prints the fingerprint.

**Status values:**
- `transcribed`: a `.txt` transcript exists, but nothing has been organized yet
- `organized`: the menu has been presented and placement is still awaiting Dan's picks
- `filed`: the material has been written into the manuscript or vault (see "Filed to")
- `unconfirmed`: a transcript exists and the memo predates this log, but nothing in
  git or the vault traces back to it by name. Dan should confirm whether it was used.

| Memo | Recorded | Fingerprint | Transcript | Status | Filed to / notes |
|------|----------|-------------|------------|--------|------------------|
| Book notes.m4a | 2026-01-13 | 1000s / 3343553 B | none | unconfirmed | No `.txt` exists. Possibly never transcribed. |
| Book 2.m4a | 2026-01-15 | 1247s / 3883103 B | TurboScribe `.txt` | unconfirmed | |
| 3227 W Cortez St.m4a | 2026-01-16 | 1012s / 3287671 B | TurboScribe `.txt` | unconfirmed | |
| Major Adams Community Committee 2.m4a | 2026-01-16 | 1136s / 3699212 B | TurboScribe `.txt` | unconfirmed | |
| Book 4.m4a | 2026-01-18 | 900s / 2930694 B | TurboScribe `.txt` | unconfirmed | |
| Book tina.m4a | 2026-01-18 | 972s / 4181533 B | TurboScribe `.txt` | unconfirmed | |
| First contact.m4a | 2026-01-20 | 1385s / 4485186 B | TurboScribe `.txt` + `(1)` copy | filed | 2026-08-31 third audit pass: First Contact chapter notes, `Ramona.md`, `twin-sister.md`, `_unplaced-beats.md` |
| Control room.m4a | 2026-01-26 | 899s / 2978465 B | TurboScribe `.txt` + `(1)` copy | filed | 2026-08-31 third audit pass: Control Room chapter notes, `_unplaced-beats.md` |
| Prologue.m4a | 2026-01-27 | 1188s / 3856951 B | TurboScribe `.txt` | unconfirmed | "Prologue" is too generic to trace by name |
| Big question .m4a | 2026-01-30 | 947s / 3083115 B | TurboScribe `.txt` + `(1)` copy | filed | 2026-08-31 third audit pass: `_unplaced-beats.md`, `themes.md`, Mountain Optimization |
| Ch2.m4a | 2026-02-09 | 913s / 7740478 B | TurboScribe `.txt` | unconfirmed | |
| Job chapter.m4a | 2026-02-24 | 1021s / 3176634 B | TurboScribe `.txt` | unconfirmed | |
| A b testing.m4a | 2026-03-24 | 1173s / 33116912 B | TurboScribe `.txt` + `(1)` copy | filed | 2026-08-31 third audit pass: `_unplaced-beats.md`, `Sam.md`, `nanobots.md`, `honeycomb.md`, Tina's Visit |
| *(no audio)* Book memo.txt | 2026-08-31 | — | TurboScribe `.txt` only | filed | 2026-08-31 third audit pass: `_unplaced-beats.md`, `Sam.md`, `honeycomb.md`, `heist-mechanism.md` |
| W Lexington St.m4a | 2026-08-23 | 814s / 2656021 B | TurboScribe `.txt` | filed | 2026-08-31: Cats and Rats chapter notes (folder since deleted, still in git history) |
| The 606.m4a | 2026-08-23 | 463s / 1514600 B | TurboScribe `.txt` | filed | 2026-08-31: Cats and Rats chapter notes, `_unplaced-beats.md` (Aquarium Pt. I) |
| The 606 (1).m4a | 2026-10-07 | 463s / 1514600 B | — | duplicate | Same recording as `The 606.m4a`, re-downloaded. Skip. |
| Deli Belli.m4a | 2026-10-07 | 736s / 2400484 B | mlx-whisper `.txt` | organized | 2026-10-07: Damon/Glenn/Honeycomb throughline (Coffee Guy Interlude, Coffee Guy Intro, Heist Approval, Coda). Awaiting placement picks. |
