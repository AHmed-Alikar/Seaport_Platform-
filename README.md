# Seaport Platform (earlier snapshot)

An earlier snapshot of the same project now continued at
[`import_export_seaport_platforms_2026`](https://github.com/AHmed-Alikar/import_export_seaport_platforms_2026)
— this repo's backend is a strict subset of that one (it's missing the
`shipment` model and the `dashboard` routes that exist there). Treat
that repository as the current one; this one is kept for history.

## Security note

This repo had the same issue as the current one: a committed `.env`
file and a hardcoded database credential in `backend/app/config.py`.
Both are fixed here too — config now requires `SECRET_KEY` and
`DATABASE_URI` from the environment. **If those committed values were
ever real credentials, rotate them** — removing the file from the
latest commit doesn't remove it from git history.

See the [current repo's README](https://github.com/AHmed-Alikar/import_export_seaport_platforms_2026#readme)
for the actual tech stack, setup steps, and API docs.
