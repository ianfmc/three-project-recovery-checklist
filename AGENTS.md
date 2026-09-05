# Recovery checklist
Use plain HTML, CSS, JavaScript and a minimal Python Lambda save service. No frameworks, databases, or build tooling.
All changing checklist definitions and initial state belong in data.json. Live shared state is authoritative in the isolated S3 bucket's data.json; never overwrite it with local seed data.
Normal ./deploy.sh publishes layout only after initial setup. PUBLISH_DETAILS=1 merges definitions while preserving task progress, notes, decisions, and costs. PUBLISH_SERVICE=1 deliberately updates the save service and reset seed.
Keep application repositories untouched. All tasks belong to Ian, with AT-, LW-, RW- prefixes. Do not copy SAP source, internal implementation details, customers, credentials, signed URLs, or proprietary prompts here.
Never commit .private or tokens. Read README.md before deployment/service changes.
Use Lato typography for this personal checklist; do not apply SAP Brand 72.
Use bundled Google Material Symbols for interface icons. Ian dislikes emoji-style or standalone Unicode icon characters; do not use them as UI icons.
LIVEWELL is Ian’s personal early-warning system for potential NADEX trades. Assume no multi-user scenario or commercial product unless Ian explicitly changes that scope.
