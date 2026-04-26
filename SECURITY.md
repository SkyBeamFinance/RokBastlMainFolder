# Security & Incident Response

## Reporting Vulnerabilities

If you discover a security vulnerability in any document, tool, or workflow in this repository, please open a GitHub Issue labeled **security** or contact the repository owner directly. Do not include sensitive credential or exploit details in public issues.

---

## Emergency Checklist — Repository Disappearance / Account Takeover

> **Use this checklist if repositories suddenly become invisible, inaccessible, or are reported as deleted, especially across an entire organisation.**

Work through each section in order. Preserve evidence at every step before taking corrective action.

---

### 1. Verify Account and Organisation Ownership

- [ ] Go to **github.com** and confirm you can still sign in to your personal account.
- [ ] Navigate to **github.com/orgs/\<org-name\>** and confirm you still appear as an Owner under *People → Owners*.
- [ ] If you cannot sign in, use the **Forgot password** flow on the email address registered to the account.
- [ ] If your email address itself was changed by an attacker, check for a **GitHub "your primary email address was changed"** notification in the old inbox and use the reversal link it contains (valid for a limited time).
- [ ] Check **Settings → Organizations** to verify you are still a member/owner of every organisation you expect.

---

### 2. Check GitHub Audit Log (Organisations)

Audit logs record every admin event (repo deletions, transfers, member changes).

- [ ] Go to **github.com/organizations/\<org-name\>/settings/audit-log**.
- [ ] Filter by `action:repo.destroy` or `action:repo.transferred` to find deletion or transfer events.
- [ ] Note the actor, IP address, and timestamp of every suspicious event.
- [ ] Export the log (CSV) and store it offline as evidence.
- [ ] Check `action:org.remove_member` and `action:org.update_member` for unexpected membership changes.
- [ ] Check `action:protected_branch.*` and `action:hook.*` for backdoor additions.

> Personal (non-org) accounts do not have an audit log. Use the Security Log instead (step 3).

---

### 3. Check GitHub Security Log and Email Notices

- [ ] Go to **github.com/settings/security-log** for your personal account.
- [ ] Look for events such as `repo.destroy`, `user.login` from unfamiliar IPs/devices, `oauth_access.create`, `personal_access_token.create`.
- [ ] Review your **email inbox** for GitHub notifications about:
  - Password or email changes
  - New SSH key added
  - New OAuth application authorized
  - Billing changes
  - Repository visibility changes
  - Account suspension notices
- [ ] Check your **spam/junk folder** — attackers sometimes try to suppress these emails.
- [ ] Note all timestamps and forward relevant emails to yourself as evidence.

---

### 4. Restore Deleted Repositories (within 90 days)

GitHub retains deleted repositories for **90 days** and owners can restore them.

- [ ] Go to **github.com/settings/repositories** (personal) or **github.com/organizations/\<org\>/settings/deleted_repositories** (org).
- [ ] Identify deleted repositories and click **Restore**.
- [ ] Verify restored content against any local clone you have.
- [ ] If the 90-day window has passed or the button is absent, contact GitHub Support immediately (see step 8) — they may be able to assist within a longer internal window.

> **Important:** Restore repositories *before* taking other destructive cleanup actions (e.g., revoking tokens), so you do not accidentally lose evidence of who performed the deletion.

---

### 5. Check Billing and Plan Status

A lapsed payment or plan downgrade can make private repositories inaccessible (they are not deleted, just hidden).

- [ ] Go to **github.com/settings/billing** (personal) or **github.com/organizations/\<org\>/settings/billing**.
- [ ] Confirm the current plan is active and no payment has failed.
- [ ] Check for recent plan downgrades that may have reduced the number of allowed private repositories.
- [ ] If a payment failed, update the payment method and retry — repositories should reappear promptly.
- [ ] Review any emails from GitHub about billing failures or plan changes.

---

### 6. Check for Policy Violations or Account Suspension

GitHub may disable or restrict accounts/organisations that violate their Terms of Service.

- [ ] Look for a banner on **github.com** indicating your account or organisation has been flagged or suspended.
- [ ] Check your registered email for a **GitHub Trust & Safety** or **Support** message explaining the reason.
- [ ] Review **github.com/github/site-policy** to understand which policy may have been triggered.
- [ ] If you believe the suspension is in error, contact GitHub Support (step 8) immediately with your explanation and any supporting evidence.

---

### 7. Review and Rotate Credentials

If any unauthorised access is confirmed or suspected, revoke and rotate everything.

#### Access Tokens (PATs)
- [ ] Go to **github.com/settings/tokens** and revoke all tokens you do not recognise.
- [ ] Rotate (delete and re-create) any token that may have been exposed.

#### OAuth Apps and GitHub Apps
- [ ] Go to **github.com/settings/applications** → *Authorized OAuth Apps* and *Installed GitHub Apps*.
- [ ] Revoke any application you do not recognise or no longer use.
- [ ] For orgs: **github.com/organizations/\<org\>/settings/oauth_application_policy**.

#### SSH Keys
- [ ] Go to **github.com/settings/keys**.
- [ ] Remove every SSH key you do not recognise.
- [ ] Generate a new SSH key pair on a trusted machine and add the new public key.

#### Two-Factor Authentication (2FA)
- [ ] Verify 2FA is enabled: **github.com/settings/security** → *Two-factor authentication*.
- [ ] Switch to an authenticator app (TOTP) or hardware key if you are currently using SMS-based 2FA.
- [ ] Regenerate and securely store new recovery codes.
- [ ] If your 2FA device was compromised, use a recovery code to regain access, then disable and re-enable 2FA on a clean device.

#### Secrets in Repositories / Actions
- [ ] Go to **Settings → Secrets and variables → Actions** for every affected repository.
- [ ] Rotate any secret that may have been exposed (API keys, deploy keys, cloud credentials).

---

### 8. Contact GitHub Support and Preserve Evidence

- [ ] Open a support ticket at **support.github.com** (logged in, to associate it with your account).
- [ ] Choose the category that best matches: *Account security / Account access / Organisation management*.
- [ ] Include in your ticket:
  - Your GitHub username and organisation name(s)
  - Timestamps and descriptions of suspicious events (from the audit/security log)
  - Whether you believe credentials were compromised
  - Which repositories are missing and when they disappeared
- [ ] Do **not** share passwords or 2FA codes with support staff — they will not ask for them.
- [ ] Keep a local copy of all audit log exports, email screenshots, and any other evidence.
- [ ] If you suspect a criminal intrusion, also file a report with your local cybercrime authority and preserve all digital evidence in its original form.

---

### Quick-Reference Summary

| Priority | Action |
|----------|--------|
| **Immediate** | Change password, enable/verify 2FA |
| **Within minutes** | Revoke unrecognised tokens, SSH keys, OAuth apps |
| **Within the hour** | Check audit log, restore deleted repos |
| **Same day** | Rotate all secrets, open GitHub Support ticket, preserve evidence |
| **Follow-up** | Review billing, check for policy suspension, harden org security settings |

---

*Last updated: 2026-04-26*
