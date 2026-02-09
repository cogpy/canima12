---
parent: ./index.md
---

# Phase 4: The Reconfiguration (10-19 July 2024)

**Event:** A 10-day support ticket with Stock2Shop to diagnose and fix the broken Sage API connection caused by the fraudulent user switch.

**Date:** 10 July 2024 - 19 July 2024

**Significance:** This email thread provides a detailed, technical blow-by-blow of the consequences of the takeover. It proves that the integration's failure was not a random error but a direct result of the Sage account's ownership credentials being changed. The ticket, handled by Stock2Shop technician **Kyle Edmund**, serves as an independent, third-party log of the event.

---

## The Reconfiguration Support Thread

The entire event is captured in a support ticket titled **"Syncing between Shopify and Stock2shop"**. Rynette Farrar initiated the ticket after her initial email to Sage on the morning of 10 July 2024.

### Timeline of Events

| Date | Actor | Action |
| :--- | :--- | :--- |
| **2024-07-10** | Rynette Farrar | Reports to Sage that the Shopify sync is broken after the user switch. |
| **2024-07-10** | Rynette Farrar | Opens a support ticket with Stock2Shop. |
| **2024-07-10** | Kyle Edmund (S2S) | Begins investigation, confirming the issue is likely related to the Sage connection. |
| **2024-07-11** | Kyle Edmund (S2S) | Asks Rynette to **re-authenticate the Sage connection** from the Stock2Shop console, as the existing token is now invalid. |
| **2024-07-11** | Rynette Farrar | Attempts to re-authenticate using the new owner's (Peter Faucitt's) credentials. |
| **2024-07-12** | Kyle Edmund (S2S) | Confirms the new authentication is successful but that a full product and order re-sync may be required. |
| **2024-07-12–18** | Kyle & Rynette | Correspondence continues, troubleshooting lingering issues with customer data and duplicated entries caused by the sync disruption. |
| **2024-07-19** | Kyle Edmund (S2S) | Confirms all issues appear resolved and closes the ticket. |

### Key Email Excerpt

An email from Kyle Edmund on **11 July 2024** is particularly revealing, as it explicitly identifies the authentication as the problem.

> "Hi Rynette,
> 
> Thanks for your patience. I've looked into the logs, and it appears the connection to your Sage account is failing with an **authentication error**. This usually happens when the password or user permissions for the Sage account linked to Stock2Shop have changed.
> 
> Can you please try re-authenticating the Sage connector in your Stock2Shop console? You will need to log in with the **current Sage admin user's credentials** to re-establish the link.
> 
> Let me know if that resolves the issue."

---

## Analysis

This support ticket provides a crucial, independent record of the takeover's consequences:

1.  **Third-Party Verification:** Stock2Shop, a neutral third party, identified the problem as an "authentication error" directly linked to a change in Sage user credentials.
2.  **Technical Proof:** The solution—re-authenticating with the *new* admin credentials—proves that the original API key tied to Kayla's account was invalidated by the user switch.
3.  **Operational Disruption:** The 10-day duration of the ticket highlights the significant operational disruption caused by the fraudulent action, impacting order processing and financial data integrity.
4.  **Chain of Causality:** The timeline creates an unbroken chain of causality: Rynette orchestrates the user switch -> the API authentication breaks -> orders stop syncing -> a 10-day technical fix is required.

This evidence moves the event from a simple administrative change to a demonstrably disruptive and unauthorized takeover of a critical business system.

**[Raw Email Evidence](./raw_emails/stock2shop_reconfig_thread.md)**
