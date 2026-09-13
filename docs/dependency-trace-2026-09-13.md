# Recovery checklist dependency trace

Historical audit: this records the graph before the approved strategic revision. The live checklist now has separate tracks and reconciled dependencies; consult data.json for current definitions.

Snapshot: 13 September 2026; live revision 132. Read-only audit; no task statuses, dependencies, or dates changed.

All 154 task records were traced recursively. All task and decision references resolve; there are no structural task-dependency cycles. This does not prove that the sequencing matches the intended work.

## How to read this report

- Direct prerequisites are the stored task edges; all listed prerequisites are required.
- Ancestors list every task reachable by following those edges backward, without repetition. Direct prerequisite rows allow every branch to be reconstructed.
- Roots are tasks with no task prerequisites. Decisions are separate gates and are listed alongside task dependencies.
- Milestones and phases group work; they do not add prerequisite edges or enforce milestone order.
- The UI displays only unfinished prerequisites. A missing “Requires” label does not mean a task has no dependencies.
- Deferred tasks are included in the trace but are excluded from active-work recommendations.

## Findings and recommended reconciliation

### LIVEWELL

LW-301 depends only on LW-635 (completed setup). It is intentionally independent of congressional research. Its complete backward ancestry is in the task table. Its stored start date is 2026-10-01, target date 2026-10-16, and milestone LW-W1 ends 2026-09-30. The recommendation function excludes future-start tasks even when doing. These dates conflict with the latest note’s instruction to finish the baseline now.

The research chain currently runs LW-201 → LW-202 → LW-203 → LW-205 → LW-206, with LW-301, LW-107 and LW-108 also required by LW-206. The notebook-first plan instead requires a research spike and ablation before production ingestion. Do not simply make LW-201 depend on LW-206: that would introduce a real cycle. Separate research preparation from production ingestion, connect the research work to LW-206, and make production conditional on an accepted positive ablation result. Completing an ablation alone is not the same as deciding to retain the signal.

LW-103 is done for documenting access and unresolved restrictions, but the latest note requires resolution of the commercial-purpose question before a Track B data pull. That condition has no open decision/task gate in the JSON: LW-D02 is resolved. Preserve the completed research task and represent the remaining specific condition separately. No legal conclusion was reached in this audit.

LW-204 (storage/lineage), LW-207 (user-facing explanation), LW-102 (limitations), and LW-613 (account security) have release-gate coverage but are not ancestors of LW-210. Release-gate coverage is a separate summary; it does not automatically make LW-210 depend on those items. The milestone records still use Discovery contract / Research alpha / Augmented-strategy beta rather than explicit core and research tracks.

The latest LIVEWELL note also contains stale closing text saying LW-102 remains unfinished, although its opening and live status say done. The track-plan document allows bounded wrangling/pulls while the latest note bars a pull until the specific question is resolved; reconcile those instructions. Offline fixture/schema work can remain parallel.

### RUNWELL

Account chain: RW-6001 → RW-6002 → RW-6003 → RW-6004 → RW-6005 → RW-6006 → RW-6007 → RW-6008. RW-103 requires RW-6008. If the deployment needed to verify RW-6006 is RW-103, this creates an operational deadlock even though there is no cycle in the stored graph. Define a bounded setup/test deployment for role verification separately from the production ship gate; preserve RW-6008 as a prerequisite of RW-406.

The main product chain is RW-103/RW-104 → RW-201 → RW-203 → RW-204 → RW-205 → RW-206, joining RW-207 at RW-208, then RW-306 → RW-401 → RW-402/RW-403 → RW-406. Billing, operational hardening, rollback and onboarding feed that chain as shown below.

RW-101/RW-102 (CI), RW-105 (credential boundary), RW-107 (environment reset), and RW-202 (vessel CRUD/orgId verification) are not ancestors of RW-406. Review whether these must block release; their absence is not proof the work is optional. RW-106 architecture reconciliation and RW-108 issue triage are also independent branches. A release regression may cover some areas, but the dependency graph does not establish those checklist tasks as prerequisites.

### AT

AT-101 forks into AT-102 (topology; AT-D02 open) and AT-103 (runtime compatibility; AT-D03 open), joining at AT-105. AT-105 and AT-106 feed AT-201. Golden-path tests lead through AT-401 and AT-403; fallback AT-203 → AT-405 and security AT-307 join at AT-406 → AT-501 → AT-502. The storyboard/deck branch AT-107 → AT-301 also joins the rehearsals.

Final-demo ancestry does not include several separately declared release-gate tasks: AT-104 (development route), AT-205 (multilingual moment), AT-206 (fallback media), AT-306 (claims review), AT-402 (output review), AT-303/AT-305 (roadmap), and AT-504 (limitations). Decide which must be prerequisites of freeze/demo and which are intentionally parallel or follow-up. Narrative tasks AT-302/AT-304, transition work AT-404 and closing narrative AT-503 are also outside the AT-502 ancestry. Do not add a dependency on post-demo follow-up merely to force one linear chain.

## Complete task-by-task trace

### AT — Autonomous Tournament

| Item | Status | Milestone | Direct prerequisites | Direct decisions |
|---|---|---|---|---|
| AT-101 — Define executive audience, decision, and golden demo story | ready | AT-W1 | AT-635 | AT-D01 |
| AT-102 — Select and implement authenticated production topology | ready | AT-W1 | AT-101, AT-635 | AT-D02 |
| AT-103 — Validate AI Core structured output and tool-use compatibility | ready | AT-W1 | AT-101, AT-635 | AT-D03 |
| AT-104 — Configure the authorized SAP Proxy development route | ready | AT-W1 | AT-635 | None |
| AT-105 — Keep model calls and credentials behind the authenticated server | ready | AT-W1 | AT-102, AT-103, AT-635 | None |
| AT-106 — Prepare deterministic demo data and a reset procedure | ready | AT-W1 | AT-635 | None |
| AT-107 — Draft the executive presentation storyboard | ready | AT-W1 | AT-635 | None |
| AT-201 — Stabilize the complete Lessons Learned golden journey | ready | AT-W2 | AT-105, AT-106, AT-635 | None |
| AT-202 — Verify authenticated end-to-end golden-path coverage | ready | AT-W2 | AT-201, AT-635 | None |
| AT-203 — Provide live and deterministic fallback execution | ready | AT-W2 | AT-106, AT-635 | None |
| AT-204 — Verify high-value failure and edge cases | ready | AT-W2 | AT-201, AT-635 | None |
| AT-205 — Validate a meaningful multilingual moment | ready | AT-W2 | AT-201, AT-635 | None |
| AT-206 — Capture presentation fallback screenshots and video | ready | AT-W2 | AT-203, AT-635 | None |
| AT-301 — Complete executive deck and presenter notes | ready | AT-W3 | AT-107, AT-635 | None |
| AT-302 — Explain how observations become institutional learning | ready | AT-W3 | AT-635 | None |
| AT-303 — Define the governed extension opportunity | ready | AT-W3 | AT-635 | None |
| AT-304 — Quantify the opportunity with clearly labeled assumptions | ready | AT-W3 | AT-635 | None |
| AT-305 — Document the productionization roadmap and effort | ready | AT-W3 | AT-303, AT-635 | None |
| AT-306 — Review security and architecture claims for accuracy | ready | AT-W3 | AT-301, AT-635 | None |
| AT-307 — Verify roles, protected actions, logout, and credential boundaries | ready | AT-W3 | AT-105, AT-635 | None |
| AT-401 — Validate the demo with representative sanitized observations | ready | AT-W4 | AT-202, AT-204, AT-635 | None |
| AT-402 — Review report relevance, provenance, and confidence wording | ready | AT-W4 | AT-201, AT-635 | None |
| AT-403 — Complete timed business and technical rehearsals | ready | AT-W4 | AT-301, AT-401, AT-635 | None |
| AT-404 — Refine transitions across presentation and demonstration | ready | AT-W4 | AT-403, AT-635 | None |
| AT-405 — Rehearse failure handling and fallback switching | ready | AT-W4 | AT-203, AT-635 | None |
| AT-406 — Freeze the demo and executive deck | ready | AT-W4 | AT-307, AT-403, AT-405, AT-635 | None |
| AT-501 — Run the final controlled-environment smoke test | ready | AT-W5 | AT-406, AT-635 | None |
| AT-502 — Present the executive context and demonstration | ready | AT-W5 | AT-501, AT-635 | None |
| AT-503 — Close with the roadmap, sponsorship ask, and next milestone | ready | AT-W5 | AT-301, AT-635 | None |
| AT-504 — Publish sanitized limitations and productionization backlog | ready | AT-W5 | AT-305, AT-635 | None |
| AT-601 — Install Kiro and verify access | done | AT-K0 | None | None |
| AT-602 — Review project-specific Kiro steering | done | AT-K0 | AT-601 | None |
| AT-603 — Configure focused project tools and read-only inspection | done | AT-K0 | AT-602, AT-635 | None |
| AT-604 — Add targeted quality hooks and a session handoff | ready | AT-K0 | AT-603, AT-635 | None |
| AT-605 — Complete a bounded Kiro evaluation slice | ready | AT-K0 | AT-604, AT-635 | None |
| AT-606 — Review Kiro efficacy and refine development setup | ready | AT-K0 | AT-605, AT-635 | None |
| AT-607 — Review tool usefulness after two weeks | ready | AT-K1 | AT-635 | None |
| AT-608 — Activate Plan D LLM-router fallback only if needed | deferred | AT-W1 | None | None |
| AT-609 — Evaluate advisory automated PR review later | deferred | AT-W1 | None | None |
| AT-610 — Configure and verify development-only CAP MCP | ready | AT-K0 | AT-602, AT-635 | None |
| AT-611 — Explore a bounded runtime MCP extension | deferred | AT-W1 | AT-202, AT-307 | None |
| AT-620 — Confirm Kiro model choices and a small Qwen trial | done | AT-K0 | AT-602, AT-635 | None |
| AT-900 — Other line-of-business demos | deferred | AT-W1 | None | None |
| AT-901 — Full Work Zone experience | deferred | AT-W1 | None | None |
| AT-902 — Advanced vector similarity | deferred | AT-W1 | None | None |
| AT-903 — Nonessential visual polish | deferred | AT-W1 | None | None |
| AT-904 — Full production operational readiness | deferred | AT-W1 | None | None |
| AT-905 — Runtime MCP extension until core demo is stable | deferred | AT-W1 | None | None |
| AT-631 — Check gstack prerequisites for Kiro | done | AT-K0 | AT-601 | None |
| AT-632 — Install gstack for Kiro from Ian’s fork | done | AT-K0 | AT-631 | None |
| AT-633 — Confirm gstack skill discovery in this Kiro workspace | done | AT-K0 | AT-632 | None |
| AT-634 — Add project-specific gstack usage guidance | done | AT-K0 | AT-602, AT-633 | None |
| AT-635 — Verify Kiro and gstack are ready for AT work | done | AT-K0 | AT-634 | None |

#### Backward ancestry for every item

- **AT-101** — Roots: AT-601. All prerequisite tasks: AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: AT-D01.
- **AT-102** — Roots: AT-601. All prerequisite tasks: AT-101, AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: AT-D01, AT-D02.
- **AT-103** — Roots: AT-601. All prerequisite tasks: AT-101, AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: AT-D01, AT-D03.
- **AT-104** — Roots: AT-601. All prerequisite tasks: AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: None.
- **AT-105** — Roots: AT-601. All prerequisite tasks: AT-101, AT-102, AT-103, AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: AT-D01, AT-D02, AT-D03.
- **AT-106** — Roots: AT-601. All prerequisite tasks: AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: None.
- **AT-107** — Roots: AT-601. All prerequisite tasks: AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: None.
- **AT-201** — Roots: AT-601. All prerequisite tasks: AT-101, AT-102, AT-103, AT-105, AT-106, AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: AT-D01, AT-D02, AT-D03.
- **AT-202** — Roots: AT-601. All prerequisite tasks: AT-101, AT-102, AT-103, AT-105, AT-106, AT-201, AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: AT-D01, AT-D02, AT-D03.
- **AT-203** — Roots: AT-601. All prerequisite tasks: AT-106, AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: None.
- **AT-204** — Roots: AT-601. All prerequisite tasks: AT-101, AT-102, AT-103, AT-105, AT-106, AT-201, AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: AT-D01, AT-D02, AT-D03.
- **AT-205** — Roots: AT-601. All prerequisite tasks: AT-101, AT-102, AT-103, AT-105, AT-106, AT-201, AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: AT-D01, AT-D02, AT-D03.
- **AT-206** — Roots: AT-601. All prerequisite tasks: AT-106, AT-203, AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: None.
- **AT-301** — Roots: AT-601. All prerequisite tasks: AT-107, AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: None.
- **AT-302** — Roots: AT-601. All prerequisite tasks: AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: None.
- **AT-303** — Roots: AT-601. All prerequisite tasks: AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: None.
- **AT-304** — Roots: AT-601. All prerequisite tasks: AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: None.
- **AT-305** — Roots: AT-601. All prerequisite tasks: AT-303, AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: None.
- **AT-306** — Roots: AT-601. All prerequisite tasks: AT-107, AT-301, AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: None.
- **AT-307** — Roots: AT-601. All prerequisite tasks: AT-101, AT-102, AT-103, AT-105, AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: AT-D01, AT-D02, AT-D03.
- **AT-401** — Roots: AT-601. All prerequisite tasks: AT-101, AT-102, AT-103, AT-105, AT-106, AT-201, AT-202, AT-204, AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: AT-D01, AT-D02, AT-D03.
- **AT-402** — Roots: AT-601. All prerequisite tasks: AT-101, AT-102, AT-103, AT-105, AT-106, AT-201, AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: AT-D01, AT-D02, AT-D03.
- **AT-403** — Roots: AT-601. All prerequisite tasks: AT-101, AT-102, AT-103, AT-105, AT-106, AT-107, AT-201, AT-202, AT-204, AT-301, AT-401, AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: AT-D01, AT-D02, AT-D03.
- **AT-404** — Roots: AT-601. All prerequisite tasks: AT-101, AT-102, AT-103, AT-105, AT-106, AT-107, AT-201, AT-202, AT-204, AT-301, AT-401, AT-403, AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: AT-D01, AT-D02, AT-D03.
- **AT-405** — Roots: AT-601. All prerequisite tasks: AT-106, AT-203, AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: None.
- **AT-406** — Roots: AT-601. All prerequisite tasks: AT-101, AT-102, AT-103, AT-105, AT-106, AT-107, AT-201, AT-202, AT-203, AT-204, AT-301, AT-307, AT-401, AT-403, AT-405, AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: AT-D01, AT-D02, AT-D03.
- **AT-501** — Roots: AT-601. All prerequisite tasks: AT-101, AT-102, AT-103, AT-105, AT-106, AT-107, AT-201, AT-202, AT-203, AT-204, AT-301, AT-307, AT-401, AT-403, AT-405, AT-406, AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: AT-D01, AT-D02, AT-D03.
- **AT-502** — Roots: AT-601. All prerequisite tasks: AT-101, AT-102, AT-103, AT-105, AT-106, AT-107, AT-201, AT-202, AT-203, AT-204, AT-301, AT-307, AT-401, AT-403, AT-405, AT-406, AT-501, AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: AT-D01, AT-D02, AT-D03.
- **AT-503** — Roots: AT-601. All prerequisite tasks: AT-107, AT-301, AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: None.
- **AT-504** — Roots: AT-601. All prerequisite tasks: AT-303, AT-305, AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: None.
- **AT-601** — Roots: AT-601. All prerequisite tasks: None. Decisions across the chain: None.
- **AT-602** — Roots: AT-601. All prerequisite tasks: AT-601. Decisions across the chain: None.
- **AT-603** — Roots: AT-601. All prerequisite tasks: AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: None.
- **AT-604** — Roots: AT-601. All prerequisite tasks: AT-601, AT-602, AT-603, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: None.
- **AT-605** — Roots: AT-601. All prerequisite tasks: AT-601, AT-602, AT-603, AT-604, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: None.
- **AT-606** — Roots: AT-601. All prerequisite tasks: AT-601, AT-602, AT-603, AT-604, AT-605, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: None.
- **AT-607** — Roots: AT-601. All prerequisite tasks: AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: None.
- **AT-608** — Roots: AT-608. All prerequisite tasks: None. Decisions across the chain: None.
- **AT-609** — Roots: AT-609. All prerequisite tasks: None. Decisions across the chain: None.
- **AT-610** — Roots: AT-601. All prerequisite tasks: AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: None.
- **AT-611** — Roots: AT-601. All prerequisite tasks: AT-101, AT-102, AT-103, AT-105, AT-106, AT-201, AT-202, AT-307, AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: AT-D01, AT-D02, AT-D03.
- **AT-620** — Roots: AT-601. All prerequisite tasks: AT-601, AT-602, AT-631, AT-632, AT-633, AT-634, AT-635. Decisions across the chain: None.
- **AT-900** — Roots: AT-900. All prerequisite tasks: None. Decisions across the chain: None.
- **AT-901** — Roots: AT-901. All prerequisite tasks: None. Decisions across the chain: None.
- **AT-902** — Roots: AT-902. All prerequisite tasks: None. Decisions across the chain: None.
- **AT-903** — Roots: AT-903. All prerequisite tasks: None. Decisions across the chain: None.
- **AT-904** — Roots: AT-904. All prerequisite tasks: None. Decisions across the chain: None.
- **AT-905** — Roots: AT-905. All prerequisite tasks: None. Decisions across the chain: None.
- **AT-631** — Roots: AT-601. All prerequisite tasks: AT-601. Decisions across the chain: None.
- **AT-632** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631. Decisions across the chain: None.
- **AT-633** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632. Decisions across the chain: None.
- **AT-634** — Roots: AT-601. All prerequisite tasks: AT-601, AT-602, AT-631, AT-632, AT-633. Decisions across the chain: None.
- **AT-635** — Roots: AT-601. All prerequisite tasks: AT-601, AT-602, AT-631, AT-632, AT-633, AT-634. Decisions across the chain: None.

#### Milestones

| ID | Name | Target date |
|---|---|---|
| AT-W1 | Integrated architecture | 2026-09-04 |
| AT-W2 | Reliable golden path | 2026-09-11 |
| AT-W3 | Executive narrative | 2026-09-18 |
| AT-W4 | Rehearsal and freeze | 2026-09-25 |
| AT-W5 | Executive demonstration | 2026-09-30 |
| AT-K0 | Kiro weekend setup and first slice | 2026-09-07 |
| AT-K1 | Development-tool effectiveness review | 2026-09-21 |

#### Declared release gates

| Gate | Required evidence tasks |
|---|---|
| AT-G01 — Audience and ask | AT-101 |
| AT-G02 — Repeated golden journey | AT-201, AT-202 |
| AT-G03 — Deterministic fallback | AT-203, AT-206, AT-405 |
| AT-G04 — Executive deck | AT-301 |
| AT-G05 — Development/runtime distinction | AT-104, AT-306 |
| AT-G06 — Production authentication | AT-102, AT-307 |
| AT-G07 — AI Core runtime | AT-103, AT-105 |
| AT-G08 — Credential boundary | AT-105, AT-307 |
| AT-G09 — Focused E2E | AT-202, AT-204 |
| AT-G10 — Multilingual moment | AT-205 |
| AT-G11 — Representative output | AT-401, AT-402 |
| AT-G12 — Extension roadmap | AT-303, AT-305 |
| AT-G13 — Timed rehearsals | AT-403 |
| AT-G14 — Known limitations | AT-504 |

### LW — LIVEWELL

| Item | Status | Milestone | Direct prerequisites | Direct decisions |
|---|---|---|---|---|
| LW-101 — Write the ADR for Ian’s personal NADEX early-warning workflow | done | LW-W1 | LW-635 | LW-D01 |
| LW-102 — Document disclosure delays and research limitations | done | LW-W1 | LW-635 | None |
| LW-103 — Confirm official-disclosure access method and terms | done | LW-W1 | LW-101, LW-635 | LW-D02 |
| LW-104 — Define canonical disclosure schema and source-document lineage | ready | LW-W1 | LW-101, LW-635 | None |
| LW-105 — Define asset-resolution method, confidence levels, and manual review | ready | LW-W1 | LW-104, LW-635 | None |
| LW-106 — Define aggregation experiments: ticker, sector, market-factor, cross-filer consensus, and purchase/sale imbalance | ready | LW-W1 | LW-101, LW-635 | None |
| LW-107 — Define leakage-safe backtest clock using public filing availability, not transaction date | ready | LW-W1 | LW-104, LW-635 | None |
| LW-108 — Define the join from congressional aggregates to the existing NADEX feature pipeline and the baseline ablation protocol | ready | LW-W1 | LW-107, LW-635 | None |
| LW-201 — Build raw document/index ingestion with idempotency and source snapshots | ready | LW-W2 | LW-103, LW-104, LW-635 | LW-D02 |
| LW-202 — Build parser and canonical normalizer with fixtures for House/Senate variants | ready | LW-W2 | LW-201, LW-635 | None |
| LW-203 — Build asset/ticker resolver and review queue | ready | LW-W2 | LW-105, LW-202, LW-635 | None |
| LW-204 — Add disclosure/transaction tables and lineage keys to DynamoDB/S3 | ready | LW-W2 | LW-104, LW-635 | None |
| LW-205 — Implement versioned time-decay and aggregation features | ready | LW-W3 | LW-106, LW-203, LW-635 | None |
| LW-206 — Extend the existing backtest for leakage-safe baseline-versus-augmented ablation | ready | LW-W3 | LW-107, LW-108, LW-205, LW-301, LW-635 | None |
| LW-207 — Show potential NADEX trades and explain why they were flagged | ready | LW-W4 | LW-205, LW-635 | None |
| LW-208 — Add scheduled pipeline, alarms, replay, and run audit | ready | LW-W4 | LW-201, LW-205, LW-635 | None |
| LW-209 — Add outcome tracker and calibration/performance views | ready | LW-W4 | LW-206, LW-635 | None |
| LW-210 — Security, cost, and reproducibility review | ready | LW-W4 | LW-208, LW-209, LW-635 | None |
| LW-602 — Review project-specific Kiro steering | done | LW-K0 | AT-601 | None |
| LW-603 — Configure focused project tools and read-only inspection | done | LW-K0 | LW-602, LW-635 | None |
| LW-604 — Add targeted quality hooks and a session handoff | ready | LW-K0 | LW-603, LW-635 | None |
| LW-605 — Complete a bounded Kiro evaluation slice | ready | LW-K0 | LW-604, LW-635 | None |
| LW-606 — Review Kiro efficacy and refine development setup | ready | LW-K0 | LW-605, LW-635 | None |
| LW-607 — Review tool usefulness after two weeks | ready | LW-K1 | LW-635 | None |
| LW-608 — Activate Plan D LLM-router fallback only if needed | deferred | LW-W1 | None | None |
| LW-609 — Evaluate advisory automated PR review later | deferred | LW-W1 | None | None |
| LW-610 — Verify AWS documentation and infrastructure context | done | LW-K0 | LW-602, LW-635 | None |
| LW-611 — Establish least-privilege AWS inspection access | done | LW-K0 | LW-602, LW-635 | None |
| LW-612 — Validate the full Kiro project pilot | ready | LW-W3 | LW-206, LW-635 | None |
| LW-620 — Confirm Kiro model choices and a small Qwen trial | done | LW-K0 | LW-602, LW-635 | None |
| LW-301 — Freeze and reproduce the existing NADEX baseline | doing | LW-W1 | LW-635 | None |
| LW-900 — Replacing the existing strategy | deferred | LW-W1 | None | None |
| LW-901 — Standalone trade triggers from congressional activity | deferred | LW-W1 | None | None |
| LW-902 — Offering LIVEWELL to other users or as a commercial product | deferred | LW-W1 | None | None |
| LW-903 — Dedicated GPU hosting | deferred | LW-W1 | None | None |
| LW-904 — Central model gateway before a demonstrated need | deferred | LW-W1 | None | None |
| LW-631 — Check gstack prerequisites for Kiro | done | LW-K0 | AT-601 | None |
| LW-632 — Verify the shared gstack installation for LW | done | LW-K0 | AT-632, LW-631 | None |
| LW-633 — Confirm gstack skill discovery in this Kiro workspace | done | LW-K0 | LW-632 | None |
| LW-634 — Add project-specific gstack usage guidance | done | LW-K0 | LW-602, LW-633 | None |
| LW-635 — Verify Kiro and gstack are ready for LW work | done | LW-K0 | LW-634 | None |
| LW-613 — Complete account security: non-root administration, root MFA and key retirement | done | LW-K0 | LW-611, LW-635 | None |

#### Backward ancestry for every item

- **LW-101** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-602, LW-631, LW-632, LW-633, LW-634, LW-635. Decisions across the chain: LW-D01.
- **LW-102** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-602, LW-631, LW-632, LW-633, LW-634, LW-635. Decisions across the chain: None.
- **LW-103** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-101, LW-602, LW-631, LW-632, LW-633, LW-634, LW-635. Decisions across the chain: LW-D01, LW-D02.
- **LW-104** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-101, LW-602, LW-631, LW-632, LW-633, LW-634, LW-635. Decisions across the chain: LW-D01.
- **LW-105** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-101, LW-104, LW-602, LW-631, LW-632, LW-633, LW-634, LW-635. Decisions across the chain: LW-D01.
- **LW-106** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-101, LW-602, LW-631, LW-632, LW-633, LW-634, LW-635. Decisions across the chain: LW-D01.
- **LW-107** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-101, LW-104, LW-602, LW-631, LW-632, LW-633, LW-634, LW-635. Decisions across the chain: LW-D01.
- **LW-108** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-101, LW-104, LW-107, LW-602, LW-631, LW-632, LW-633, LW-634, LW-635. Decisions across the chain: LW-D01.
- **LW-201** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-101, LW-103, LW-104, LW-602, LW-631, LW-632, LW-633, LW-634, LW-635. Decisions across the chain: LW-D01, LW-D02.
- **LW-202** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-101, LW-103, LW-104, LW-201, LW-602, LW-631, LW-632, LW-633, LW-634, LW-635. Decisions across the chain: LW-D01, LW-D02.
- **LW-203** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-101, LW-103, LW-104, LW-105, LW-201, LW-202, LW-602, LW-631, LW-632, LW-633, LW-634, LW-635. Decisions across the chain: LW-D01, LW-D02.
- **LW-204** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-101, LW-104, LW-602, LW-631, LW-632, LW-633, LW-634, LW-635. Decisions across the chain: LW-D01.
- **LW-205** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-101, LW-103, LW-104, LW-105, LW-106, LW-201, LW-202, LW-203, LW-602, LW-631, LW-632, LW-633, LW-634, LW-635. Decisions across the chain: LW-D01, LW-D02.
- **LW-206** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-101, LW-103, LW-104, LW-105, LW-106, LW-107, LW-108, LW-201, LW-202, LW-203, LW-205, LW-301, LW-602, LW-631, LW-632, LW-633, LW-634, LW-635. Decisions across the chain: LW-D01, LW-D02.
- **LW-207** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-101, LW-103, LW-104, LW-105, LW-106, LW-201, LW-202, LW-203, LW-205, LW-602, LW-631, LW-632, LW-633, LW-634, LW-635. Decisions across the chain: LW-D01, LW-D02.
- **LW-208** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-101, LW-103, LW-104, LW-105, LW-106, LW-201, LW-202, LW-203, LW-205, LW-602, LW-631, LW-632, LW-633, LW-634, LW-635. Decisions across the chain: LW-D01, LW-D02.
- **LW-209** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-101, LW-103, LW-104, LW-105, LW-106, LW-107, LW-108, LW-201, LW-202, LW-203, LW-205, LW-206, LW-301, LW-602, LW-631, LW-632, LW-633, LW-634, LW-635. Decisions across the chain: LW-D01, LW-D02.
- **LW-210** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-101, LW-103, LW-104, LW-105, LW-106, LW-107, LW-108, LW-201, LW-202, LW-203, LW-205, LW-206, LW-208, LW-209, LW-301, LW-602, LW-631, LW-632, LW-633, LW-634, LW-635. Decisions across the chain: LW-D01, LW-D02.
- **LW-602** — Roots: AT-601. All prerequisite tasks: AT-601. Decisions across the chain: None.
- **LW-603** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-602, LW-631, LW-632, LW-633, LW-634, LW-635. Decisions across the chain: None.
- **LW-604** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-602, LW-603, LW-631, LW-632, LW-633, LW-634, LW-635. Decisions across the chain: None.
- **LW-605** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-602, LW-603, LW-604, LW-631, LW-632, LW-633, LW-634, LW-635. Decisions across the chain: None.
- **LW-606** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-602, LW-603, LW-604, LW-605, LW-631, LW-632, LW-633, LW-634, LW-635. Decisions across the chain: None.
- **LW-607** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-602, LW-631, LW-632, LW-633, LW-634, LW-635. Decisions across the chain: None.
- **LW-608** — Roots: LW-608. All prerequisite tasks: None. Decisions across the chain: None.
- **LW-609** — Roots: LW-609. All prerequisite tasks: None. Decisions across the chain: None.
- **LW-610** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-602, LW-631, LW-632, LW-633, LW-634, LW-635. Decisions across the chain: None.
- **LW-611** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-602, LW-631, LW-632, LW-633, LW-634, LW-635. Decisions across the chain: None.
- **LW-612** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-101, LW-103, LW-104, LW-105, LW-106, LW-107, LW-108, LW-201, LW-202, LW-203, LW-205, LW-206, LW-301, LW-602, LW-631, LW-632, LW-633, LW-634, LW-635. Decisions across the chain: LW-D01, LW-D02.
- **LW-620** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-602, LW-631, LW-632, LW-633, LW-634, LW-635. Decisions across the chain: None.
- **LW-301** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-602, LW-631, LW-632, LW-633, LW-634, LW-635. Decisions across the chain: None.
- **LW-900** — Roots: LW-900. All prerequisite tasks: None. Decisions across the chain: None.
- **LW-901** — Roots: LW-901. All prerequisite tasks: None. Decisions across the chain: None.
- **LW-902** — Roots: LW-902. All prerequisite tasks: None. Decisions across the chain: None.
- **LW-903** — Roots: LW-903. All prerequisite tasks: None. Decisions across the chain: None.
- **LW-904** — Roots: LW-904. All prerequisite tasks: None. Decisions across the chain: None.
- **LW-631** — Roots: AT-601. All prerequisite tasks: AT-601. Decisions across the chain: None.
- **LW-632** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-631. Decisions across the chain: None.
- **LW-633** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-631, LW-632. Decisions across the chain: None.
- **LW-634** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-602, LW-631, LW-632, LW-633. Decisions across the chain: None.
- **LW-635** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-602, LW-631, LW-632, LW-633, LW-634. Decisions across the chain: None.
- **LW-613** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, LW-602, LW-611, LW-631, LW-632, LW-633, LW-634, LW-635. Decisions across the chain: None.

#### Milestones

| ID | Name | Target date |
|---|---|---|
| LW-W1 | Discovery contract | 2026-09-30 |
| LW-W2 | Research alpha | 2026-10-16 |
| LW-W3 | Augmented-strategy beta | 2026-10-30 |
| LW-W4 | Personal early-warning system ready | 2026-11-13 |
| LW-K0 | Kiro weekend setup and first slice | 2026-09-07 |
| LW-K1 | Development-tool effectiveness review | 2026-09-21 |

#### Declared release gates

| Gate | Required evidence tasks |
|---|---|
| LW-G01 — Reproducible baseline | LW-301 |
| LW-G02 — Data acquisition method confirmed | LW-103 |
| LW-G03 — Point-in-time lineage | LW-104, LW-204 |
| LW-G04 — Asset confidence and review | LW-203 |
| LW-G05 — Leakage-safe join | LW-107, LW-206 |
| LW-G06 — Ablation completed | LW-206 |
| LW-G07 — Evidence to retain or reject | LW-206 |
| LW-G08 — Scheduled pipeline and replay | LW-208 |
| LW-G09 — Explanation and uncertainty | LW-207 |
| LW-G10 — Outcome tracking | LW-209 |
| LW-G11 — Cost and monitoring | LW-210 |
| LW-G12 — Personal scope and research limitations | LW-101, LW-102 |
| LW-G13 — Personal AWS account access secured | LW-613 |

### RW — RUNWELL

| Item | Status | Milestone | Direct prerequisites | Direct decisions |
|---|---|---|---|---|
| RW-6001 — Create dedicated AWS account | done | RW-K0 | None | None |
| RW-6002 — Create AWS Organization | done | RW-K0 | RW-6001 | None |
| RW-6003 — Secure root user | done | RW-K0 | RW-6002 | None |
| RW-6004 — Create admin role (assumed by ianfmc) | done | RW-K0 | RW-6003 | None |
| RW-6005 — Create runwell-ro read-only identity | done | RW-K0 | RW-6004 | None |
| RW-6006 — Create scoped deploy role | ready | RW-K0 | RW-6005 | None |
| RW-6007 — Establish infrastructure-as-code baseline | ready | RW-K0 | RW-6006 | None |
| RW-6008 — Verify security parity & IaC | ready | RW-K0 | RW-6007 | None |
| RW-101 — Resolve latest landing CI failure and protect `main` with required checks | ready | RW-W1 | RW-635 | None |
| RW-102 — Add CI gates for Business OS and SaaS: install, typecheck, unit, build, selected E2E | ready | RW-W1 | RW-101, RW-635 | None |
| RW-103 — Complete first reproducible SaaS deployment and document environments | blocked | RW-W1 | RW-6008, RW-635 | None |
| RW-104 — Complete per-persona auth fixtures and tenant-isolation tests | blocked | RW-W1 | RW-103, RW-635 | None |
| RW-105 — Move all browser-side GitHub and AI/provider credentials behind Lambda/API boundaries | blocked | RW-W1 | RW-6008, RW-635 | None |
| RW-106 — Reconcile architecture contradiction: CLAUDE.md says Step Functions both required and explicitly excluded; record one decision | doing | RW-W1 | RW-635 | None |
| RW-107 — Establish seed/reset/teardown for test environments | blocked | RW-W1 | RW-103, RW-6008, RW-635 | None |
| RW-108 — Triage open issues into December MVP, post-MVP, and close/duplicate | ready | RW-W1 | RW-635 | None |
| RW-201 — Validate organization provisioning and fleet onboarding end-to-end | ready | RW-W2 | RW-103, RW-104, RW-635 | None |
| RW-202 — Validate vessel CRUD and strict `orgId` enforcement | ready | RW-W2 | RW-201, RW-635 | None |
| RW-203 — Validate task/checklist/workflow builders against real Amplify data | ready | RW-W2 | RW-201, RW-635 | None |
| RW-204 — Validate recurrence generation, assignment, retries, and idempotency | ready | RW-W2 | RW-203, RW-635 | None |
| RW-205 — Validate mobile execution under narrow viewport, intermittent network, and failed upload | ready | RW-W2 | RW-204, RW-635 | None |
| RW-206 — Validate issue-to-service-order path and status lifecycle | ready | RW-W2 | RW-205, RW-635 | None |
| RW-207 — Validate dashboard calculations from real data | ready | RW-W2 | RW-203, RW-635 | None |
| RW-208 — Complete design-partner smoke suite with no mock-only assertions | ready | RW-W2 | RW-206, RW-207, RW-635 | None |
| RW-301 — Decide pilot billing: live Stripe, manually provisioned plan, or time-boxed design-partner entitlement | doing | RW-W3 | RW-635 | RW-D01 |
| RW-302 — Test invites, billing status, cancellation/past-due behavior, and admin support | ready | RW-W3 | RW-201, RW-301, RW-635 | None |
| RW-303 — Add CloudWatch alarms, failure queues/replay where applicable, cost budget, and audit logging | blocked | RW-W3 | RW-103, RW-6008, RW-635 | None |
| RW-304 — Complete privacy/data retention, photo purge, tenant export/deletion, and incident procedures | ready | RW-W3 | RW-635 | None |
| RW-305 — Accessibility and mobile usability pass with charter-domain scenarios | ready | RW-W3 | RW-205, RW-635 | None |
| RW-306 — UAT with one realistic fleet dataset and documented operator workflow | ready | RW-W3 | RW-208, RW-305, RW-635 | None |
| RW-401 — Feature freeze and release candidate | ready | RW-W4 | RW-302, RW-303, RW-304, RW-306, RW-635 | None |
| RW-402 — Clean-environment deployment rehearsal | blocked | RW-W4 | RW-401, RW-6008, RW-635 | None |
| RW-403 — Full critical-path regression and tenant-isolation test | ready | RW-W4 | RW-401, RW-635 | None |
| RW-404 — Backup/restore and rollback rehearsal | blocked | RW-W4 | RW-103, RW-6008, RW-635 | None |
| RW-405 — Design-partner onboarding guide and support process | ready | RW-W4 | RW-306, RW-635 | None |
| RW-406 — Ship / deploy production release by 1 December | blocked | RW-W4 | RW-402, RW-403, RW-404, RW-405, RW-6008, RW-635 | None |
| RW-602 — Review project-specific Kiro steering | done | RW-K0 | AT-601 | None |
| RW-603 — Configure focused project tools and read-only inspection | done | RW-K0 | RW-602, RW-635 | None |
| RW-604 — Add targeted quality hooks and a session handoff | doing | RW-K0 | RW-603, RW-635 | None |
| RW-605 — Complete a bounded Kiro evaluation slice | ready | RW-K0 | RW-604, RW-635 | None |
| RW-606 — Review Kiro efficacy and refine development setup | ready | RW-K0 | RW-605, RW-635 | None |
| RW-607 — Review tool usefulness after two weeks | ready | RW-K1 | RW-635 | None |
| RW-608 — Activate Plan D LLM-router fallback only if needed | deferred | RW-W1 | None | None |
| RW-609 — Evaluate advisory automated PR review later | deferred | RW-W1 | None | None |
| RW-610 — Verify AWS documentation and infrastructure context | ready | RW-K0 | RW-602, RW-635 | None |
| RW-611 — Establish least-privilege AWS inspection access | ready | RW-K0 | RW-6005, RW-602, RW-635 | None |
| RW-612 — Validate the full Kiro project pilot | ready | RW-W2 | RW-208, RW-635 | None |
| RW-620 — Confirm Kiro model choices and a small Qwen trial | done | RW-K0 | RW-602, RW-635 | None |
| RW-900 — Accounting and booking integrations | deferred | RW-W1 | None | None |
| RW-901 — Predictive and cross-tenant analytics | deferred | RW-W1 | None | None |
| RW-902 — Natural-language product interface | deferred | RW-W1 | None | None |
| RW-903 — Communication hub | deferred | RW-W1 | None | None |
| RW-904 — Full autonomous Business OS | deferred | RW-W1 | None | None |
| RW-905 — Broad internationalization | deferred | RW-W1 | None | None |
| RW-631 — Check gstack prerequisites for Kiro | done | RW-K0 | AT-601 | None |
| RW-632 — Verify the shared gstack installation for RW | done | RW-K0 | AT-632, RW-631 | None |
| RW-633 — Confirm gstack skill discovery in this Kiro workspace | done | RW-K0 | RW-632 | None |
| RW-634 — Add project-specific gstack usage guidance | done | RW-K0 | RW-602, RW-633 | None |
| RW-635 — Verify Kiro and gstack are ready for RW work | done | RW-K0 | RW-634 | None |

#### Backward ancestry for every item

- **RW-6001** — Roots: RW-6001. All prerequisite tasks: None. Decisions across the chain: None.
- **RW-6002** — Roots: RW-6001. All prerequisite tasks: RW-6001. Decisions across the chain: None.
- **RW-6003** — Roots: RW-6001. All prerequisite tasks: RW-6001, RW-6002. Decisions across the chain: None.
- **RW-6004** — Roots: RW-6001. All prerequisite tasks: RW-6001, RW-6002, RW-6003. Decisions across the chain: None.
- **RW-6005** — Roots: RW-6001. All prerequisite tasks: RW-6001, RW-6002, RW-6003, RW-6004. Decisions across the chain: None.
- **RW-6006** — Roots: RW-6001. All prerequisite tasks: RW-6001, RW-6002, RW-6003, RW-6004, RW-6005. Decisions across the chain: None.
- **RW-6007** — Roots: RW-6001. All prerequisite tasks: RW-6001, RW-6002, RW-6003, RW-6004, RW-6005, RW-6006. Decisions across the chain: None.
- **RW-6008** — Roots: RW-6001. All prerequisite tasks: RW-6001, RW-6002, RW-6003, RW-6004, RW-6005, RW-6006, RW-6007. Decisions across the chain: None.
- **RW-101** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: None.
- **RW-102** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, RW-101, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: None.
- **RW-103** — Roots: AT-601, RW-6001. All prerequisite tasks: AT-601, AT-631, AT-632, RW-6001, RW-6002, RW-6003, RW-6004, RW-6005, RW-6006, RW-6007, RW-6008, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: None.
- **RW-104** — Roots: AT-601, RW-6001. All prerequisite tasks: AT-601, AT-631, AT-632, RW-103, RW-6001, RW-6002, RW-6003, RW-6004, RW-6005, RW-6006, RW-6007, RW-6008, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: None.
- **RW-105** — Roots: AT-601, RW-6001. All prerequisite tasks: AT-601, AT-631, AT-632, RW-6001, RW-6002, RW-6003, RW-6004, RW-6005, RW-6006, RW-6007, RW-6008, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: None.
- **RW-106** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: None.
- **RW-107** — Roots: AT-601, RW-6001. All prerequisite tasks: AT-601, AT-631, AT-632, RW-103, RW-6001, RW-6002, RW-6003, RW-6004, RW-6005, RW-6006, RW-6007, RW-6008, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: None.
- **RW-108** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: None.
- **RW-201** — Roots: AT-601, RW-6001. All prerequisite tasks: AT-601, AT-631, AT-632, RW-103, RW-104, RW-6001, RW-6002, RW-6003, RW-6004, RW-6005, RW-6006, RW-6007, RW-6008, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: None.
- **RW-202** — Roots: AT-601, RW-6001. All prerequisite tasks: AT-601, AT-631, AT-632, RW-103, RW-104, RW-201, RW-6001, RW-6002, RW-6003, RW-6004, RW-6005, RW-6006, RW-6007, RW-6008, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: None.
- **RW-203** — Roots: AT-601, RW-6001. All prerequisite tasks: AT-601, AT-631, AT-632, RW-103, RW-104, RW-201, RW-6001, RW-6002, RW-6003, RW-6004, RW-6005, RW-6006, RW-6007, RW-6008, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: None.
- **RW-204** — Roots: AT-601, RW-6001. All prerequisite tasks: AT-601, AT-631, AT-632, RW-103, RW-104, RW-201, RW-203, RW-6001, RW-6002, RW-6003, RW-6004, RW-6005, RW-6006, RW-6007, RW-6008, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: None.
- **RW-205** — Roots: AT-601, RW-6001. All prerequisite tasks: AT-601, AT-631, AT-632, RW-103, RW-104, RW-201, RW-203, RW-204, RW-6001, RW-6002, RW-6003, RW-6004, RW-6005, RW-6006, RW-6007, RW-6008, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: None.
- **RW-206** — Roots: AT-601, RW-6001. All prerequisite tasks: AT-601, AT-631, AT-632, RW-103, RW-104, RW-201, RW-203, RW-204, RW-205, RW-6001, RW-6002, RW-6003, RW-6004, RW-6005, RW-6006, RW-6007, RW-6008, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: None.
- **RW-207** — Roots: AT-601, RW-6001. All prerequisite tasks: AT-601, AT-631, AT-632, RW-103, RW-104, RW-201, RW-203, RW-6001, RW-6002, RW-6003, RW-6004, RW-6005, RW-6006, RW-6007, RW-6008, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: None.
- **RW-208** — Roots: AT-601, RW-6001. All prerequisite tasks: AT-601, AT-631, AT-632, RW-103, RW-104, RW-201, RW-203, RW-204, RW-205, RW-206, RW-207, RW-6001, RW-6002, RW-6003, RW-6004, RW-6005, RW-6006, RW-6007, RW-6008, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: None.
- **RW-301** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: RW-D01.
- **RW-302** — Roots: AT-601, RW-6001. All prerequisite tasks: AT-601, AT-631, AT-632, RW-103, RW-104, RW-201, RW-301, RW-6001, RW-6002, RW-6003, RW-6004, RW-6005, RW-6006, RW-6007, RW-6008, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: RW-D01.
- **RW-303** — Roots: AT-601, RW-6001. All prerequisite tasks: AT-601, AT-631, AT-632, RW-103, RW-6001, RW-6002, RW-6003, RW-6004, RW-6005, RW-6006, RW-6007, RW-6008, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: None.
- **RW-304** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: None.
- **RW-305** — Roots: AT-601, RW-6001. All prerequisite tasks: AT-601, AT-631, AT-632, RW-103, RW-104, RW-201, RW-203, RW-204, RW-205, RW-6001, RW-6002, RW-6003, RW-6004, RW-6005, RW-6006, RW-6007, RW-6008, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: None.
- **RW-306** — Roots: AT-601, RW-6001. All prerequisite tasks: AT-601, AT-631, AT-632, RW-103, RW-104, RW-201, RW-203, RW-204, RW-205, RW-206, RW-207, RW-208, RW-305, RW-6001, RW-6002, RW-6003, RW-6004, RW-6005, RW-6006, RW-6007, RW-6008, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: None.
- **RW-401** — Roots: AT-601, RW-6001. All prerequisite tasks: AT-601, AT-631, AT-632, RW-103, RW-104, RW-201, RW-203, RW-204, RW-205, RW-206, RW-207, RW-208, RW-301, RW-302, RW-303, RW-304, RW-305, RW-306, RW-6001, RW-6002, RW-6003, RW-6004, RW-6005, RW-6006, RW-6007, RW-6008, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: RW-D01.
- **RW-402** — Roots: AT-601, RW-6001. All prerequisite tasks: AT-601, AT-631, AT-632, RW-103, RW-104, RW-201, RW-203, RW-204, RW-205, RW-206, RW-207, RW-208, RW-301, RW-302, RW-303, RW-304, RW-305, RW-306, RW-401, RW-6001, RW-6002, RW-6003, RW-6004, RW-6005, RW-6006, RW-6007, RW-6008, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: RW-D01.
- **RW-403** — Roots: AT-601, RW-6001. All prerequisite tasks: AT-601, AT-631, AT-632, RW-103, RW-104, RW-201, RW-203, RW-204, RW-205, RW-206, RW-207, RW-208, RW-301, RW-302, RW-303, RW-304, RW-305, RW-306, RW-401, RW-6001, RW-6002, RW-6003, RW-6004, RW-6005, RW-6006, RW-6007, RW-6008, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: RW-D01.
- **RW-404** — Roots: AT-601, RW-6001. All prerequisite tasks: AT-601, AT-631, AT-632, RW-103, RW-6001, RW-6002, RW-6003, RW-6004, RW-6005, RW-6006, RW-6007, RW-6008, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: None.
- **RW-405** — Roots: AT-601, RW-6001. All prerequisite tasks: AT-601, AT-631, AT-632, RW-103, RW-104, RW-201, RW-203, RW-204, RW-205, RW-206, RW-207, RW-208, RW-305, RW-306, RW-6001, RW-6002, RW-6003, RW-6004, RW-6005, RW-6006, RW-6007, RW-6008, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: None.
- **RW-406** — Roots: AT-601, RW-6001. All prerequisite tasks: AT-601, AT-631, AT-632, RW-103, RW-104, RW-201, RW-203, RW-204, RW-205, RW-206, RW-207, RW-208, RW-301, RW-302, RW-303, RW-304, RW-305, RW-306, RW-401, RW-402, RW-403, RW-404, RW-405, RW-6001, RW-6002, RW-6003, RW-6004, RW-6005, RW-6006, RW-6007, RW-6008, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: RW-D01.
- **RW-602** — Roots: AT-601. All prerequisite tasks: AT-601. Decisions across the chain: None.
- **RW-603** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: None.
- **RW-604** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, RW-602, RW-603, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: None.
- **RW-605** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, RW-602, RW-603, RW-604, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: None.
- **RW-606** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, RW-602, RW-603, RW-604, RW-605, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: None.
- **RW-607** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: None.
- **RW-608** — Roots: RW-608. All prerequisite tasks: None. Decisions across the chain: None.
- **RW-609** — Roots: RW-609. All prerequisite tasks: None. Decisions across the chain: None.
- **RW-610** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: None.
- **RW-611** — Roots: AT-601, RW-6001. All prerequisite tasks: AT-601, AT-631, AT-632, RW-6001, RW-6002, RW-6003, RW-6004, RW-6005, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: None.
- **RW-612** — Roots: AT-601, RW-6001. All prerequisite tasks: AT-601, AT-631, AT-632, RW-103, RW-104, RW-201, RW-203, RW-204, RW-205, RW-206, RW-207, RW-208, RW-6001, RW-6002, RW-6003, RW-6004, RW-6005, RW-6006, RW-6007, RW-6008, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: None.
- **RW-620** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, RW-602, RW-631, RW-632, RW-633, RW-634, RW-635. Decisions across the chain: None.
- **RW-900** — Roots: RW-900. All prerequisite tasks: None. Decisions across the chain: None.
- **RW-901** — Roots: RW-901. All prerequisite tasks: None. Decisions across the chain: None.
- **RW-902** — Roots: RW-902. All prerequisite tasks: None. Decisions across the chain: None.
- **RW-903** — Roots: RW-903. All prerequisite tasks: None. Decisions across the chain: None.
- **RW-904** — Roots: RW-904. All prerequisite tasks: None. Decisions across the chain: None.
- **RW-905** — Roots: RW-905. All prerequisite tasks: None. Decisions across the chain: None.
- **RW-631** — Roots: AT-601. All prerequisite tasks: AT-601. Decisions across the chain: None.
- **RW-632** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, RW-631. Decisions across the chain: None.
- **RW-633** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, RW-631, RW-632. Decisions across the chain: None.
- **RW-634** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, RW-602, RW-631, RW-632, RW-633. Decisions across the chain: None.
- **RW-635** — Roots: AT-601. All prerequisite tasks: AT-601, AT-631, AT-632, RW-602, RW-631, RW-632, RW-633, RW-634. Decisions across the chain: None.

#### Milestones

| ID | Name | Target date |
|---|---|---|
| RW-W1 | Release foundation | 2026-10-09 |
| RW-W2 | Core charter workflow | 2026-11-06 |
| RW-W3 | Operational hardening | 2026-11-20 |
| RW-W4 | Design-partner release | 2026-12-01 |
| RW-K0 | Kiro weekend setup and first slice | 2026-09-07 |
| RW-K1 | Development-tool effectiveness review | 2026-09-21 |

#### Declared release gates

| Gate | Required evidence tasks |
|---|---|
| RW-G01 — Reproducible deployment | RW-103, RW-402 |
| RW-G02 — Tenant isolation | RW-104, RW-403 |
| RW-G03 — Authentication and onboarding | RW-201 |
| RW-G04 — Core charter workflow | RW-208 |
| RW-G05 — Mobile crew acceptance | RW-205, RW-305 |
| RW-G06 — Service orders | RW-206 |
| RW-G07 — Pilot billing | RW-301, RW-302 |
| RW-G08 — Monitoring, backup, rollback | RW-303, RW-304, RW-404 |
| RW-G09 — Design-partner UAT | RW-306 |
| RW-G10 — Onboarding and support | RW-405 |
| RW-G11 — /ship and AWS deploy: security parity & IaC | RW-6008 |

