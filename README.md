# Three-Program Recovery · Execution Control

Ian’s private checklist for Autonomous Tournament (AT), LIVEWELL (LW), and RUNWELL (RW). All tasks belong to Ian. The application repositories are separate and are never modified by this checklist.

## Use

Open the private link in `.private/url.txt` after deployment. Anyone with the page can read and edit the shared checklist. Select a project to recalculate its metrics and next action. Expand a project to see context, notes, decisions, tasks, release gates, and optional pilot costs.

Routine completion is one click. A release task needs a concise evidence statement. Required task/decision prerequisites must be complete. One task can be in progress per project; Update offers an explicit switch. Blocked work requires a reason and next unblocking action. Reopening preserves evidence and notes; reopen dependent completed work first.

The top metrics reflect the selected projects. Work view, search, and hide-completed narrow detailed tasks without changing the project’s completion denominator or hiding its next action. Deferred work is excluded from general completion. Linked release gates reuse canonical tasks and never create duplicate counts. General progress and release readiness are separate.

This weekend’s Kiro setup is bounded for all three projects. AT is the September primary lane; LIVEWELL discovery is secondary; RUNWELL remains foundation-only until October. A future start date affects recommendation, not permission to work ahead. An unresolved critical decision may be the next action. Router fallback remains deferred until deliberately activated. Model names in the plan are candidates, not verified service availability. Cost tracking is manual and optional, with no assumed personal budget.

## Sources and reconciliation

Seed derived from Ian’s `three-program-recovery-plan.md`, assessment 30 August 2026, and the subsequent planning conversation. The actual project task lists govern IDs; sample schemas do not. Every numbered AT/LW/RW action is retained. DEV work is split into project-specific tasks, with source references retained. One-time Kiro installation is AT-601; each project has its own setup and evaluation. Long installation procedures are condensed into task descriptions rather than copied as commands. CP construction tasks are excluded. AT task descriptions are sanitized.

Unverified application work is open. Historical assessment percentages are contextual only. The known delivery and Kiro-direction decisions are recorded as resolved; no application task is inferred complete. Original milestones are retained; September RUNWELL work is limited to CI repair, credential boundaries, backlog triage, and bounded setup/evaluation. RW billing is due October 16 ahead of implementation. Dates are evaluated in America/Los_Angeles.

The business plan informs RUNWELL’s outcome (design-partner real use and a path to payment); its broader roadmap does not silently expand the approved release scope.

## Local preview

Run `python3 -m http.server 8769` in this directory, then open `http://localhost:8769`. Static preview reads `data.json`. Shared edits require the private deployed page. No framework, database, or asset build is required. Brand 72 is preferred if installed; Arial is the fallback.

## Shared persistence and security

Private, versioned, encrypted S3 `data.json` is authoritative. A dedicated API Gateway HTTP API and Python Lambda enforce evidence, prerequisite, status, WIP, import, and conflict rules. IAM grants the function only GetObject/PutObject on this checklist’s exact JSON key. There is no access to Tournament data or the application repositories.

Every update carries a document revision and uses S3 conditional writes. Conflicts return a visible error rather than overwrite another device. Polling runs every 15 seconds while the page is visible and on focus; it pauses for open editors and unsaved note drafts. Unsaved note text is retained in browser storage. Saved progress is never presented as successful offline. Full note history is available through S3 version history; the UI displays only the latest note.

The HTML embeds a long random bearer capability generated during deployment. Link holders can read/edit all three projects. Expiry of an S3 link does not revoke a token already copied from the page. Names are self-reported. To revoke access, rotate the stack’s AccessToken, then republish the page. No personal sign-in is provided by design. Never commit tokens, rendered private HTML, or presigned links. `.private` is ignored by Git and restricted to the local user. No external scripts, fonts, analytics, or resources are loaded by the published page.

Do not enter credentials, SAP implementation details, customer data, proprietary prompts, or signed URLs as evidence. AT evidence accepts sanitized text labels only. Simple token-pattern checks are guardrails, not comprehensive content classification.

## Deploy and update

Account: 715853571315. Region: us-west-2 (explicit; CLI defaults are ignored). Bucket: `three-program-recovery-715853571315-us-west-2`. Stack: `three-program-recovery-control`.

`./deploy.sh` uses the installed AWS SAM Python runtime’s SDK. It verifies identity and the isolated bucket tag, enables public-access blocking, encryption, versioning, and TLS-only access, initializes absent state once, and publishes the self-contained HTML. On later runs it publishes layout without replacing shared progress. It stores a seven-day presigned link in `.private/url.txt`; `./deploy.sh --print-url` prints it. Temporary AWS sessions can shorten a presigned link’s effective life.

- Layout: edit HTML/CSS/JS and run `./deploy.sh`.
- Task definitions: edit `data.json`, retain IDs, run `PUBLISH_DETAILS=1 PUBLISH_SERVICE=1 ./deploy.sh`. This preserves existing statuses, user-edited task dates, evidence, notes, decisions, costs, and omitted records; it updates the service’s approved reset seed too. Validation rejects changes that invalidate current completed work.
- Service: read this README, run tests, then `PUBLISH_SERVICE=1 ./deploy.sh`.

No bucket-wide sync or deletion occurs during deployment.

## Verification

Run `python3 -m unittest -v test_domain.py`, `node test_logic.js`, and `node --check app.js`. The source-coverage test optionally reads Ian’s source plan if still available, without modifying it. Browser verification and deployed API checks are recorded in VERIFICATION.md.

## Backup, import, reset, rollback

Export JSON downloads a full snapshot without credentials. Import accepts progress only for the current exact IDs; definitions cannot be overwritten. The server validates the entire imported result. Reset requires confirmation, exports the currently loaded state, and returns to the approved seed. S3 versions preserve the immediately preceding authoritative state as well. Reset affects all devices.

For page rollback, use the S3 console in us-west-2 → bucket above → Show versions → `index.html` → select a prior version → copy it over the current key, then generate a new link. For state rollback, first export the current JSON, download the desired older `data.json` version, and use Import progress after review. Import validates the old state against current definitions. Do not upload local seed over live state.

For service rollback, use CloudFormation stack parameters to select the prior `service/<hash>.zip` CodeKey, retain the existing AccessToken, and deploy the same template. Service archives are retained in the isolated bucket. Do not roll back state merely to roll back code.

## Exact removal scope

1. Export the checklist and save it outside this repository if wanted.
2. Run `aws cloudformation delete-stack --stack-name three-program-recovery-control --region us-west-2`, then `aws cloudformation wait stack-delete-complete --stack-name three-program-recovery-control --region us-west-2`.
3. In the S3 console, select only `three-program-recovery-715853571315-us-west-2`, empty all versions and delete markers, then delete that bucket. Confirm its name before deletion. The bucket is deliberately retained outside the stack for recovery.
4. Delete the local `.private` directory if removing saved links.

No other bucket, stack, checklist, or application resource should be removed.

## Resource and cost summary

Dedicated private S3 bucket (HTML, JSON versions, service archives), one Lambda, one HTTP API, one IAM role, and a log group with 14-day retention. No provisioned database, compute instance, or NAT gateway. Charges depend on API calls, Lambda execution, S3 requests/storage/version retention, and logs. While open and idle, one visible tab polls up to 240 times/hour; hidden tabs pause. This is request-based infrastructure, not a quoted monthly price. Application runtime and Kiro usage are separate costs.
