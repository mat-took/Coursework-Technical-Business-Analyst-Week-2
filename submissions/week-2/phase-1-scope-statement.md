# Scope Definition

## In Scope

- Identity verification 
    - we are dealing with sensitive information so we need a way to confirm that customers and agents are who they say they are.

- Account summary & eligible actions 
    - customers need to understand what they owe before escalating.
    - stakeholders have different degrees of 'clearance'.
    - option to change details - based on level of clearance.
    - option to flag hardship
    - display case history

- Promise-to-pay capture 
    - agents have currently capture inconsistently.
    - current difficulty in handovers raised in interviews.
    - risk considered before validation (debt volume, overdraft, frozen funds etc.)

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

    

