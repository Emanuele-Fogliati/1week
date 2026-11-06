# Content of the "PM AI Toolkit": templates + prompts for Product Managers (English).

TEMPLATES = [
("One-page product brief", "Use it before anyone writes a PRD: it forces the team to agree on the problem first.", """# [Product / feature name] — One-pager
**Owner:** [name] · **Date:** [date] · **Status:** Draft / In review / Approved

## Problem
Who has the problem, how often, and what it costs them today. One paragraph, no solution yet.

## Evidence
- [Data point, e.g. "38% of tickets in Q3 mention X"]
- [Customer quote, with source]
- [What we don't know yet]

## Goal and success metric
We will know this worked when [metric] moves from [baseline] to [target] by [date].
Guardrail: [metric that must not get worse].

## Proposed direction (not a spec)
[2-4 sentences]

## Not doing
- [Explicitly out of scope]

## Biggest risk
[Value / usability / feasibility / viability] — and the cheapest way to test it: [test]."""),

("Product Requirements Document (PRD)", "The full spec engineers and designers build from. A worked example follows at the end of the templates.", """# PRD: [Feature name]
**Author:** · **Reviewers:** · **Last updated:** · **Status:**

## 1. Problem and context
What is broken today, for whom, and how we know (data, quotes). Link the one-pager.
## 2. Goals and success metrics
| Goal | Metric | Baseline | Target | Deadline |
|---|---|---|---|---|
| [Outcome] | [How measured] | [Today] | [Target] | [Date] |
Guardrail metrics: what must not get worse.
## 3. Users and use cases
Primary user, secondary users, top 3 use cases in one line each.
## 4. Scope
**In scope (v1):** the smallest version that can move the metric.
**Out of scope:** said explicitly, to stop scope creep.
**Later (v2+):** good ideas parked on purpose.
## 5. Requirements
| ID | Requirement | Priority (Must/Should/Could) | Notes |
|---|---|---|---|
| R1 | [What the system must do, testable] | Must | |
## 6. User stories and acceptance criteria
Link the tickets, or list the key stories with Given/When/Then.
## 7. UX notes and open design questions
## 8. Analytics and events to track
Which product question each event answers.
## 9. Risks, dependencies and mitigations
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
## 10. Rollout plan
Pilot group, % rollout, success threshold to go to 100%, kill switch.
## 11. Open questions
| Question | Owner | Due |
|---|---|---|"""),

("User story with acceptance criteria", "One story per ticket. If you can't write the acceptance criteria, the story isn't ready.", """**Title:** [Short, user-facing]

**As a** [type of user]
**I want** [capability]
**so that** [outcome / value].

**Acceptance criteria**
- *Given* [context], *when* [action], *then* [observable result].
- *Given* [edge case], *when* [action], *then* [result].
- *Given* [error case], *when* [action], *then* [result and message shown].

**Out of scope for this story:** [ ]
**Design:** [link] · **Analytics event:** [event_name] · **Dependencies:** [ ]
**Definition of Ready check:** value clear ☐ · AC testable ☐ · design attached ☐ · estimated ☐ · fits in a sprint ☐"""),

("Customer interview script", "45 minutes, problem-focused. Never pitch your idea during discovery.", """**Intro (3 min)** Thanks, purpose, no right answers, permission to record.

**Context (7 min)**
- Tell me about your role and a typical week.
- Where does [problem area] fit in your work?

**Story of the last time (20 min)**
- Tell me about the last time you [did the task / hit the problem]. Walk me through it step by step.
- What did you try first? What happened?
- What was the hardest part? Why?
- What did it cost you (time, money, stress)?
- What do you use today to deal with it? What do you like and dislike about it?

**Wrap-up (10 min)**
- If you could wave a magic wand, what would change?
- Is there anyone else I should talk to?

**Rules:** ask about the past, not the future · ask "why" and "tell me more" · no leading questions · write down exact words."""),

("Interview synthesis grid", "Fill it within 24 hours of each interview, then look for patterns across 5+ interviews.", """| Interview | Segment | Job to be done | Pains (exact quotes) | Current workaround | Willingness to pay signal | Surprises |
|---|---|---|---|---|---|---|
| #1 | | | | | | |

**Patterns after [N] interviews**
- Pain mentioned by ≥ 60% of people:
- Segment where pain is strongest:
- Hypotheses invalidated:
- Next questions:"""),

("Worked example: a complete PRD", "A full PRD for a realistic feature, to show the level of detail that works.", """# Sample PRD: Smart appointment reminders

> Worked example. The product **CareSlot** is fictional; all numbers are illustrative assumptions, labeled as such.

**Author:** Product team · **Status:** Draft for review · **Last updated:** 2026-11-06

## 1. Problem
CareSlot is a booking app for small physiotherapy and dental clinics (1-10 practitioners). Clinics tell us no-shows are their biggest avoidable loss: an empty 45-minute slot cannot be resold at short notice.
Today CareSlot sends one fixed email 24h before the appointment. Patients often miss it, and there is no easy way to cancel or reschedule from the reminder, so they simply don't show up.

**Assumption to validate:** no-show rate in our clinics is ~8-12% of appointments (industry figures vary; we will measure our own baseline first, see §8).

## 2. Goals and success metrics
| Goal | Metric | Target (90 days after launch) |
|---|---|---|
| Fewer no-shows | No-show rate per clinic | -30% vs. baseline |
| Freed slots get reused | % of cancelled slots rebooked before start | ≥ 25% |
| Clinics see the value | Clinics that keep reminders enabled after 30 days | ≥ 85% |

**Guardrail:** patient opt-out from reminders stays under 5%.

## 3. Users
- **Clinic owner / receptionist:** wants a full calendar and zero manual phone calls.
- **Patient:** wants a reminder at the right time, on the right channel, and a one-tap way to say "I can't make it".

## 4. Scope
**In scope (v1)**
- Reminders via SMS and email, at times set by the clinic (default: 48h and 3h before).
- One-tap **Confirm / Cancel / Reschedule** links in every reminder, no login needed.
- When a patient cancels, the slot is reopened and offered to the clinic's waitlist.
- Dashboard tile for the clinic: confirmed, cancelled, no-show this week.

**Out of scope (v1)**
- WhatsApp channel (pending provider evaluation and cost).
- Automatic no-show fees or deposits.
- AI-predicted no-show risk (candidate for v2 once we have data).

## 5. Requirements
| ID | Requirement | Priority |
|---|---|---|
| R1 | Clinic can enable/disable reminders and choose up to 2 send times | Must |
| R2 | Reminder contains date, time, practitioner, address, and Confirm/Cancel/Reschedule links | Must |
| R3 | Links work without login, are unique per appointment and expire at appointment start | Must |
| R4 | Cancelling frees the slot within 1 minute and notifies the clinic | Must |
| R5 | Freed slot is offered to waitlisted patients, first to accept gets it | Should |
| R6 | Patient can opt out of SMS reminders; email remains as fallback | Must |
| R7 | Reminders respect quiet hours (no SMS 21:00-08:00 local time) | Should |

## 6. Example user stories
**US-1** As a patient, I want to cancel from the reminder in one tap, so that I don't have to call the clinic.
- *Given* I received a reminder for an upcoming appointment, *when* I tap "Cancel" and confirm, *then* the appointment is cancelled, I see a confirmation screen, and the clinic is notified.
- *Given* the appointment has already started, *when* I open the link, *then* I see "This appointment can no longer be changed online" and the clinic's phone number.

**US-2** As a receptionist, I want freed slots offered to the waitlist automatically, so that I don't have to phone patients one by one.

## 7. Risks and mitigations
| Risk | Mitigation |
|---|---|
| SMS cost erodes margin for small clinics | SMS on paid plan only; email free; show cost estimate in settings |
| Reminder links forwarded to others | Links only allow cancel/reschedule of that appointment, no personal data beyond what's in the message |
| GDPR: health-related data in SMS | No treatment type in reminder text, only "appointment at [clinic]" |

## 8. Rollout and measurement
1. Two weeks measuring baseline no-show rate across pilot clinics (no feature change).
2. Pilot with 10 clinics, 4 weeks, compare to baseline.
3. General release if no-show reduction ≥ 15% and opt-out < 5%.

## 9. Open questions
- Do clinics want to customise the reminder text, or does that create support load?
- Should rescheduling show all free slots or only those of the same practitioner?
"""),

("Experiment canvas", "Turn every assumption into a cheap test with a decision rule decided upfront.", """**We believe that** [assumption]
**To verify, we will** [experiment: landing page, fake door, concierge, prototype test...]
**And measure** [metric]
**We are right if** [threshold, decided BEFORE running]
**Cost / time:** [ ] · **Owner:** [ ] · **Decision date:** [ ]

**Result:** [ ] · **Decision:** persevere / pivot / kill · **What we learned:** [ ]"""),

("Release notes", "Write for users, not for the team. Lead with the benefit.", """## [Month Year] — What's new

### [Benefit-led headline, e.g. "Cancel appointments in one tap"]
[1-2 sentences: what changed and why it helps you.] [Link / GIF]

### Improvements
- [Thing] is now [faster/easier] — [one-line why it matters]

### Fixes
- Fixed an issue where [symptom users noticed].

Questions or feedback? [contact]"""),

("Sprint retrospective", "45 minutes. End with max 2 actions, each with an owner.", """**Check-in (5 min):** one word for this sprint.
**What went well (10 min):**
**What was hard (10 min):**
**What we learned (5 min):**
**Actions (15 min):** max 2, each with owner and due date.
| Action | Owner | Due | Done? |
|---|---|---|---|
**Last retro's actions — did we do them?**"""),
]

PROMPTS = {
"Discovery and research": [
 ("Turn raw notes into an interview summary", "You are a senior product researcher. Here are my raw notes from a customer interview: [paste]. Summarise in: (1) context of the person, (2) the job they are trying to get done, (3) pains with exact quotes, (4) current workarounds, (5) surprises. Do not invent anything that is not in the notes; mark anything uncertain."),
 ("Find patterns across interviews", "Here are summaries of [N] customer interviews: [paste]. Group the pains into themes. For each theme give: how many interviews mention it, the strongest quote, and which customer segment it affects most. End with the 3 riskiest assumptions these interviews do NOT yet answer."),
 ("Write a non-leading interview script", "I want to understand how [user type] deal with [problem area]. Write a 45-minute interview script focused on past behaviour, not opinions about the future. Flag any question that could be leading and rewrite it."),
 ("Competitor teardown", "Act as a product strategist. For [competitor 1], [competitor 2], [competitor 3] in the [market] market, compare: target customer, core promise, pricing model, onboarding, key features, and the obvious gaps. Use only what I paste below from their websites: [paste]. Then list 3 positioning opportunities for us."),
 ("Jobs-to-be-done statements", "Based on this research [paste], write 5 jobs-to-be-done statements in the format 'When [situation], I want to [motivation], so I can [expected outcome]'. Rank them by how often they appear in the evidence."),
],
"Strategy and prioritisation": [
 ("Opportunity solution tree", "Our desired outcome is [metric and target]. From these customer insights [paste], build an opportunity solution tree: outcome → 3-5 opportunities (customer needs) → 2-3 solution ideas each → one cheap experiment per idea."),
 ("RICE scoring with reasoning", "Score these initiatives with RICE (Reach, Impact, Confidence, Effort): [list with any data I have]. Show your assumptions for each number, flag where confidence is low, and tell me which 2 scores would change the ranking if they were wrong."),
 ("Pre-mortem", "Imagine it is 6 months after launching [feature] and it failed. Write the 8 most likely reasons why, grouped into value, usability, feasibility and business viability risks. For each, suggest an early warning signal and a mitigation."),
 ("Define a North Star metric", "Our product is [description] for [users]. Propose 3 candidate North Star metrics. For each: why it reflects customer value, how it could be gamed, and 3 input metrics teams can influence directly."),
 ("Say no to a stakeholder", "A stakeholder asked for [request] because [reason]. It doesn't fit our current goal [goal]. Draft a short, respectful message that acknowledges the need, explains the trade-off with data, and offers an alternative or a date to revisit."),
],
"Specs and delivery": [
 ("PRD first draft from a brief", "You are an experienced product manager. Write a PRD for [feature] using this structure: problem, goals and metrics (table), users, in/out of scope, requirements table with MoSCoW priority, risks, rollout, open questions. Context: [paste]. Mark every assumption as [ASSUMPTION] so I can verify it."),
 ("Break an epic into user stories", "Break this epic into vertical user stories that each deliver user value and fit in one sprint: [epic]. Use 'As a / I want / so that'. Add Given/When/Then acceptance criteria including at least one edge case and one error case per story."),
 ("Find gaps in a spec", "Review this spec as a sceptical senior engineer and a QA lead: [paste]. List missing edge cases, unclear requirements, untestable acceptance criteria, and questions the team will ask in refinement. Be specific."),
 ("Write analytics events", "For this feature [description], propose the tracking plan: event names (snake_case), when they fire, properties with types, and which product question each event answers. Keep it under 10 events."),
 ("Estimate risk, not just effort", "For each of these stories [paste], identify the biggest unknown (technical, design, or dependency) and suggest a spike or prototype that would reduce it in under 2 days."),
],
"Communication": [
 ("Stakeholder update", "Turn these notes [paste] into a 150-word weekly update for leadership: headline status (on track / at risk / off track), what shipped, metric movement, top risk and what we need from them. No jargon."),
 ("Release notes for users", "Rewrite these internal changelog items [paste] as user-facing release notes. Lead each with the benefit, max 2 sentences each, friendly but not cheesy."),
 ("Explain a trade-off", "Explain to a non-technical audience why we chose [option A] over [option B] for [decision]. Include what we gain, what we give up, and when we would revisit. Max 200 words."),
 ("Meeting to decisions", "Here is a meeting transcript [paste]. Extract: decisions made, open questions with owner, action items with owner and due date. If a decision is ambiguous, list it under 'needs confirmation'."),
 ("Customer email for a sunset", "Draft an email telling customers we are retiring [feature] on [date]. Explain why in one sentence, what they can use instead, how to export their data, and where to get help. Empathetic and clear."),
],
}
