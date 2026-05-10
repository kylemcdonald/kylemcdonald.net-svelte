# Agent Notes

## Project Link Text Style

When editing links in `src/routes/projects.json`, preserve the old link text style:

- Use short lowercase labels.
- Use bare nouns or compact phrases for project-owned links, like `site`, `code`, `video`, `photos`, `extension page`, or `podcast interview`.
- Use `on publication` for press/article links, with the publication name lowercased, like `on gizmodo`, `on wired`, `on the verge`, `on nytimes`, or `on the times`.
- Prefer the established shorthand already present in the older entries over official masthead capitalization.
- Do not use article titles, title case, or all-caps brand styling for press links unless the older corpus already uses a specific acronym form.
- `src/routes/projects.json` may be regenerated from Google Sheets by `update.sh`; after regenerating, verify that new press links still follow this style.
