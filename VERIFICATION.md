# Verification and delivery

Verified 4 September 2026. This verifies the checklist, not the three applications’ readiness.

## Initial inventory (4 September)

| Project | Included tasks | Deferred / conditional | Total | Linked release gates |
|---|---:|---:|---:|---:|
| Autonomous Tournament | 39 | 9 | 48 | 14 |
| LIVEWELL | 29 | 7 | 36 | 12 |
| RUNWELL | 38 | 8 | 46 | 10 |
| Total | 106 | 24 | 130 | 36 |

19 milestones, including per-project weekend setup and two-week tool reviews. 10 decisions; delivery definition and three Kiro-direction decisions are already resolved from Ian’s instructions. All task owners are Ian. No application task is inferred complete. Original AT/LW/RW numbered plan actions are covered, IDs are unique, and dependency graphs have no cycles. Gate links refer to canonical task IDs.

## Automated checks

14 server-domain tests passed: seed/source coverage, evidence, dependencies, decision prerequisites, one-in-progress and switching, blocker fields, completion/reopening metadata, notes/costs/decisions, stale revision rejection, validated import with definition preservation, reset, circular dependency rejection, signed-evidence rejection, and Frontier escalation rationale.

JavaScript scheduling tests passed: critical decisions, ready next actions, dependency exclusion including doing tasks, lane switching, deferred denominators, completed-project behavior, and evidence-backed gate readiness. JavaScript syntax check passed.

## Deployed checks

- Account 715853571315, region us-west-2.
- Isolated bucket: `three-program-recovery-715853571315-us-west-2`.
- Stack: `three-program-recovery-control`.
- Private signed HTML loads successfully; API without bearer access returns 401.
- S3 versioning, encryption, and all four public-access blocks verified.
- API completion survives reload; reopening clears completion time.
- Invalid evidence, dependency, blocker, and stale-revision updates rejected.
- Notes, decisions, and optional costs persist.
- Import restores state without replacing definitions.
- All temporary edits restored. No completed application work was left behind by testing.

## Browser checks

- Real private deployed page connects and shows shared state.
- Completed AT-601 as a temporary UI test, refreshed, verified persistence, and reopened it.
- Attempted LW-301 completion without evidence: rejected with the correct visible explanation.
- Project selection recalculates metrics and shows exactly one next action for the selected project; All Projects shows three.
- Search, no-result state, release-gate view, and expansion checked.
- JSON exports were downloaded and parsed successfully (130 tasks). The browser automation download event did not report them, so actual files were verified instead.
- Import chooser, confirmation, and successful restoration checked.
- Reset path verified; approved seed restored with no test progress retained.
- Responsive layout checked at 390, 768, 1280, and 1440 pixels. No horizontal overflow at the inspected widths; task editor fits the 390-pixel viewport.
- Focusable semantic controls, native details/dialog patterns, visible focus CSS, and reduced-motion behavior included. Routine checkboxes are labeled. Import is a keyboard-focusable button.
- No JavaScript console errors observed during the inspected interaction sequence.

## Deliberate limitations

The page is protected through private-link possession, not person-level sign-in. A copied bearer capability remains valid until rotation even after the HTML URL expires. Editing requires connectivity. Project-note drafts persist locally; unfinished task forms are not a general offline queue. Cost and evidence entries are manual; there is no GitHub, Kiro, or model billing integration. Cost recording does not configure or enforce external IDE model selection. Full note history is in S3 versions rather than a separate UI. Simple health rules are not forecasts. Original assessment dates can already be overdue and are not silently moved.

Definitions and dependencies are maintained in data.json. Browser updates handle progress, task target dates, evidence, blockers, working notes, decisions, and pilot costs. Original source installation procedures are condensed into task descriptions; this checklist does not install Kiro or modify any application repository.

The next useful increment should follow actual weekend use: adjust overly broad task boundaries and prerequisite links from Ian’s feedback before adding integrations.

## gstack checklist update — 5 September 2026

Added five development-setup tasks per project (AT/LW/RW-631 through -635). New total: 145 tasks, comprising 121 included and 24 deferred; milestones, decisions, and release gates are unchanged. The source reference is ianfmc/gstack revision e23ff280a1c2e517daaee89ccc1a0e415e5aa9bc, checked against its README, setup script, Kiro host config, and official Kiro skill documentation.

Domain validation and scheduling checks passed after the additions. The new tasks use existing project setup phases and weekend milestones; no completed work is inferred. Publication merges definitions and updates the reset seed without installing gstack or changing application repositories.
