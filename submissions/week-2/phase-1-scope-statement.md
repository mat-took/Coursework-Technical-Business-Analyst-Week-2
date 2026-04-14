# Scope Definition

## In Scope

- Identity verification 
    - we are dealing with sensitive information so we need a way to confirm that customers and agents are who they say they are.

- Account summary & eligible actions 
    - customers need to understand what they owe before escalating.
    - stakeholders have different degrees of 'clearance'.
    - option to change details - based on level of clearance.
    - option for agent or customer to flag hardship.
    - display case history.
    - customer optionality to go directly to an agent.

- Promise-to-pay capture 
    - agents have currently capture inconsistently.
    - current difficulty in handovers raised in interviews.
    - case cannot continue without promise-to-pay.
    - risk considered before validation (debt volume, overdraft, frozen funds etc.)

- Portal SMS reminders
    - portal has access to delinquency database
    - sms reminders sent when delinquency stage reaches mid
    - agents spend too much time on this- easy win in terms of time and cost.

- Eligible payment-plan selection 
    - heavily rules-based procedure that fairly assessed customer's data.
    - reduces likelihood of default through generous terms.
    - well defined compliance boundaries.
    - customers less likely to get 'denied' (higher satisfaction).
    - risk of becoming a black-box to agents.

- Rules-based routing to agents
    - current 0.62 non-straightforward case share.
    - special cases to special agents.
    - less handovers, less information lost/altered incorrectly.
    - load balancing.
    - high-complexity cases identified and escalated for review.
        - debt over 10,000
        - monthly payment equal to interest (risk of default)
    - flagged accounts escalated for review.
        - hardship
        - abusive
    - risk of not capturing nuances of cases which an experienced agent may spot.

- Portal outcome reporting
    - current difficult handovers raised in interviews.
    - agents will reject portal if case comes back with no context.
    - reveals pain-points case-wise so business can continually improve.
    - risk of case over-simplification.
    - stage-wise logging.
        - stage outcome.
        - flag where a case is escalated or terminated.
    - key financial changes logged (payment, PTP, delinquency).

- Schedule follow-ups
    - current 0.15 missed follow-up rate.
    - agents save time confirming availability.
    - centralised calendar map.
    - option to manually re-schedule for both agent and customer.

## Out of Scope

- Hardship assessment
    - requires judgement
    - human needed to balance empathy and business requirements.
    - systems can be sycophantic which may increase risk of default.
        - existing data may be misleading (good repayment history despite circumstances)

- Bespoke repayment negotiation
    - requires negotiation
        - convincing and compelling
        - understanding of customer's behaviour
        - mutual trust must be established (customer wont trust a machine, and a machine can be deceived).
    - offer boundaries can be exploited

- Legal escalation workflow
    - requires judgement.
    - high risk process (legal consequences).
    - portal cannot identify abusive behaviour.
        - tone of voice, sarcasm, mean-spiritedness etc.

- Major core-platform replacement
    - this is scope creep.
    - underlying systems are delicate.
        - if replacement goes wrong, so does everything on top of systems.
    - too big of an endeavour for phase 1.

- Advanced personalisation
    - risk of unfairness between customers
    - reintroduces problem of inconsistency between cases

## Assumptions

### Example

- legacy data needed for account summary is accessible enough for Phase 1

- eligibility rules can be agreed without full policy redesign

- operations will support a limited pilot or phased rollout

### Mine

- Case call-ins have a clear structure/ methodology that can be mapped into 'stages' in the portal.

- portal captures context well and completely enough for agents to not reject it.

- payment plan selection and agent routing are completely traceable. The link between data and conclusions drawn should be clear so that agents trust the portal, and can validate it if necessary.

- agents have a model for identifying customer hardship and will consistently flag it in the portal.

- customers will not all opt to go directly to agent- thus making the portal redundant.

## Dependencies and constraints

### Example

- legacy system data availability

- compliance approval for messages and audit trail

- agent workflow alignment for routed cases

### Mine

- Employees calendar data needed for scheduling follow-ups is available.

- What each agent can and cannot do (clearance, expertise) is well-defined.

- procedure for eligible payment plan selection is based on data that exist in a database.

- there are clear escalation policies for different flags.

- clear criteria for when delinquency stage reaches 'mid', with additional criteria used to prioritise cases in that category.

## Credibility

This scope is credible because all in-scope capabilities are rules-driven and high volume. In fact, a simple ROI analysis showed that just automating routine reminders, follow-up scheduling, and promise-to-pay capture can save over 6000 hours, and reveal £550,000 for the business annually. Implementing these is straightforward, software engineering problem that can be achieved in 2 weeks.

The biggest risk was that agents would not use the portal - especially if it returned incomplete contextual information. This is why we have put outcome reporting in our scope. Context thus becomes an acceptance criteria for our phase 1 which mitigates it's biggest risk. Our largest concern is now the possibility that customers themselves opt out of the portal, choosing to phone in or send email requests.

