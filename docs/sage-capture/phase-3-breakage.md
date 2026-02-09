---
parent: ./index.md
---

# Phase 3: The Breakage (10 July 2024)

**Event:** Rynette Farrar reports that the Sage user switch has broken the Stock2Shop integration, preventing e-commerce orders from syncing to the accounting system.

**Date:** 10 July 2024

**Significance:** This is the immediate, predictable consequence of the fraudulent ownership transfer. It provides a direct causal link between the takeover and the disruption of critical business operations. Rynette's own words serve as an admission that the switch she orchestrated was the cause of the failure.

---

## The "It Broke" Email

The morning after the successful user switch, Rynette sends an urgent email to Sage support and Peter Faucitt, admitting the integration is no longer working.

| Attribute | Value |
| :--- | :--- |
| **Date** | `2024-07-10 06:42:00+00:00` |
| **From** | `rynette@regima.zone` |
| **To** | `Sibongile.Ndhlovu@sage.com`, `PETE@REGIMA.COM` |
| **Subject** | `RE: Invited user switch` |

> "Good morning
> 
> **Remember I asked you if this switch would affect our Shopify shop, and you said no. This morning, I can see the orders coming in on the Shopify portal, but it is not sinking with SAGE.**
> 
> I am awaiting a call from the Stock2shop technician."


## The Panic and Backpedal Attempt

Minutes later, realizing the severity of the issue, Rynette sends a follow-up email attempting to reverse the change, implicitly admitting the connector is tied to Kayla's credentials.

| Attribute | Value |
| :--- | :--- |
| **Date** | `2024-07-10 06:46:00+00:00` |
| **From** | `rynette@regima.zone` |
| **To** | `Sibongile.Ndhlovu@sage.com`, `PETE@REGIMA.COM` |
| **Subject** | `RE: Invited user switch` |

> "Good morning
> 
> Just one question, **is it possible that we can leave Kayla as the owner for now, as apparently all sorts of connectors are connected to her email address?** Then, can we add Pete as an Administrator for now?"

---

## Analysis

These two emails are critically important:

1.  **Direct Admission of Consequence:** Rynette explicitly states that the "switch" caused the Shopify-Sage sync to fail. This is not a technical guess; it is a statement of cause and effect.
2.  **Proof of API Dependency:** Her request to revert ownership back to "Kayla" because "all sorts of connectors are connected to her email address" is a direct admission that the Stock2Shop API key and integration were tied to the original, legitimate owner's credentials.
3.  **Foreknowledge of Risk:** Her first email, "Remember I asked you if this switch would affect our Shopify shop...", indicates she was aware of the potential for disruption but proceeded anyway.
4.  **Confirmation from Sage:** Sage support agent Sibongile later confirms that while Sage's internal changes don't affect third-party apps, Rynette *will* have to consult with Stock2Shop about the two different API connections now in play.

This event provides a clear, time-stamped link between the fraudulent administrative action and its tangible, negative impact on the business's core e-commerce operations.

**[Raw Email Evidence](./raw_emails/invited_user_switch_thread.md)**
