# Releasing Rose Blush

## Before publishing

- [ ] Confirm the public author name, MIT license, and rights to distribute the theme and embedded chevron. Add any required third-party attribution before release.
- [ ] Confirm that **Rose Blush** is available in the Community directory. Obsidian requires a unique name and keeps the theme name fixed after submission. [Manifest reference](https://docs.obsidian.md/Reference/Manifest)
- [ ] Run `python3 scripts/validate.py` from the repository root. Check the stylesheet in Obsidian as well.
- [ ] Test a clean desktop vault with snippets and community plugins disabled. In both schemes, check Reading View and Live Preview with tables, checklists, properties, code, and long lines. Confirm the first body row uses the editor background, headers match the alternating tint and have normal weight, and table editing handles remain usable.
- [ ] Use Tab to check visible keyboard focus on settings filters, switches, and checkboxes. Inspect active and inactive pinned tabs, including a community plugin tab with a supplied icon and native stacked tabs.
- [ ] Test at least one real phone and, if available, a tablet. Check settings, the navigation drawers, long tables, and orientation changes on the minimum supported Obsidian version. Record platform, app version, and issues before claiming support.
- [ ] Try Focus Mode separately. Check that its toggle and command still operate and that leaving Focus Mode restores the interface. Test the core Slides presentation with arrow keys, Escape, and code and tables in light mode. Also check native dark-mode Slides.
- [ ] Capture the store image from a throwaway vault with example notes, a table, and tasks. Use `screenshots/light.png` as the store path, at Obsidian’s recommended 512 × 288. Capture matching dark and optional mobile views. Check readability at the store size and remove any personal filenames, accounts, or notes from the frame. [Theme submission guide](https://docs.obsidian.md/themes/app-themes/submit-theme)

## After approval to publish

1. Push the repository to GitHub with `README.md`, `LICENSE`, `manifest.json`, `theme.css`, and the store screenshot on the default branch.
2. Create the GitHub release with a tag that exactly matches the manifest version, currently `1.0.0`. Attach the two individual files `manifest.json` and `theme.css` from that same revision.
3. Sign into the Obsidian Community directory and link the GitHub account that owns the repository. Add a theme with the GitHub repository URL, directory owner, relative screenshot path `screenshots/light.png`, and the verified supported modes.
4. Review the automated scan and address any errors with a new version and matching release. Use the directory’s publish control when the entry is ready. [Set up and claim](https://docs.obsidian.md/community-directory/set-up-and-claim)

Keep the CSS source and both release assets readable and offline. [Developer policies](https://docs.obsidian.md/community-directory/developer-policies) · [Theme guidelines](https://docs.obsidian.md/Themes/App%20themes/Theme%20guidelines)
