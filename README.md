# party-pages

Welcome pages for guest photo uploads at weddings and parties.
Each event has its own folder with an `index.html`; the button links to that event's Synology Photos "Photo Request" upload link.

| Event | Page | Expires |
|---|---|---|
| Marko & Ana | `/marko-ana/` | 2026-11-19 |
| Ivana 40! (demo, vrtna zabava) | `/ivana-40/` | upload link not set yet |

To add an event: copy `marko-ana/` to a new folder, change the names, text and upload link.

## Card styles
- **Floral** – weddings and formal occasions (used for Marko & Ana)
- **Party** – birthdays and parties (`tools/example-party-card.pdf`)

`tools/build_cards.py` generates both A6 cards as HTML (render to PDF with headless Chrome).
