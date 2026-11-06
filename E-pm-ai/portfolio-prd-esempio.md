# Sample PRD: Smart appointment reminders

> Portfolio sample. The product **CareSlot** is fictional; all numbers are illustrative assumptions, labeled as such.

**Author:** [Manu] · **Status:** Draft for review · **Last updated:** 2026-11-06

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
