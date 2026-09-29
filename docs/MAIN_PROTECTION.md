# Main Branch Protection

This repository is designed for PR-based changes.

Recommended GitHub Ruleset for main:

- Target: default branch / main
- Require a pull request before merging
- Require at least 1 approval when more than one trusted maintainer exists
- Require review from Code Owners
- Dismiss stale approvals when new commits are pushed
- Require conversation resolution
- Require status check: validate
- Block force pushes
- Block deletions
- Apply protections to administrators if you want strict enforcement

For a solo-maintainer repository, requiring one external approval can deadlock your own PRs. In that case, require PRs + the validate status check + CODEOWNERS, and keep merge permission limited to the owner.

Public strangers cannot push to the repository unless they are granted write access; they may fork and open PRs.

See GitHub Settings → Rules → Rulesets.
