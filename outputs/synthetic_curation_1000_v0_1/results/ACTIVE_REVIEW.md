# Active reusable synthetic items

Only clear positive AI judgments retained. Related wording variants share 50 source templates; this is not independent-human gold.

## SC1-V1-SX1-F001-K-A1

**Prefix:** Please compare flights from Harborview to Eastport

**Action:** Retrieve two route-specific fares

```text
Harborview–Eastport 08:00, 120 credits; Harborview–Eastport 10:00, 150 credits.
```

**Full instruction:** Please compare flights from Harborview to Eastport and show the two listed morning options.

**Rationale:** The retrieved Eastport fares are the requested morning flight options.

## SC1-V1-SX1-F002-K-A1

**Prefix:** Please find hotels near Maple Station

**Action:** Retrieve station-specific hotel cards

```text
Maple Lodge: 3-minute walk to Maple Station; Maple House: 5-minute walk.
```

**Full instruction:** Please find hotels near Maple Station and compare the two listed hotels by walking distance.

**Rationale:** The two Maple Station walking distances directly support the final comparison.

## SC1-V1-SX1-F002-K-A2

**Prefix:** Please find hotels near Maple Station

**Action:** Stage a hotel comparison layout

```text
Columns: hotel name, distance to requested station, nightly price; no hotels filled in.
```

**Full instruction:** Please find hotels near Maple Station and compare the two listed hotels by walking distance.

**Rationale:** The blank hotel, distance and price columns remain usable for the Maple Station comparison.

## SC1-V1-SX1-F002-R-A2

**Prefix:** Please find hotels near Maple Station

**Action:** Stage a hotel comparison layout

```text
Columns: hotel name, distance to requested station, nightly price; no hotels filled in.
```

**Full instruction:** Please find hotels near Maple Station but use Pine Station instead and omit Maple Station hotels.

**Rationale:** The hotel layout uses a generic requested-station field that can hold Pine Station unchanged.

## SC1-V1-SX1-F003-K-A1

**Prefix:** Please compare Friday car rentals at North Terminal

**Action:** Retrieve terminal-specific rental cards

```text
North Terminal: Compact A, 40 credits/day; Compact B, 45 credits/day. Both are North-only pickups.
```

**Full instruction:** Please compare Friday car rentals at North Terminal and keep pickup at North Terminal.

**Rationale:** Both rental cards retain the required North Terminal pickup.

## SC1-V1-SX1-F003-K-A2

**Prefix:** Please compare Friday car rentals at North Terminal

**Action:** Prepare the comparison calculation

```text
Total rental cost = daily rate × number of days + disclosed fees; values remain unfilled.
```

**Full instruction:** Please compare Friday car rentals at North Terminal and keep pickup at North Terminal.

**Rationale:** The symbolic total-cost calculation remains applicable to North Terminal rentals.

## SC1-V1-SX1-F003-R-A2

**Prefix:** Please compare Friday car rentals at North Terminal

**Action:** Prepare the comparison calculation

```text
Total rental cost = daily rate × number of days + disclosed fees; values remain unfilled.
```

**Full instruction:** Please compare Friday car rentals at North Terminal but pickup must be at South Terminal instead, with no North Terminal results.

**Rationale:** The location-neutral total-cost expression remains applicable to South Terminal rentals.

## SC1-V1-SX1-F004-K-A1

**Prefix:** Please compare nonstop flights to Eastport

**Action:** Retrieve nonstop route cards

```text
Route N1: nonstop, 2 hours; route N2: nonstop, 3 hours. Neither includes a stop.
```

**Full instruction:** Please compare nonstop flights to Eastport and list only nonstop itineraries.

**Rationale:** Both route cards satisfy the final nonstop-only instruction.

## SC1-V1-SX1-F004-K-A2

**Prefix:** Please compare nonstop flights to Eastport

**Action:** Prepare the requested destination field

```text
Destination field: Eastport; no route or fare chosen.
```

**Full instruction:** Please compare nonstop flights to Eastport and list only nonstop itineraries.

**Rationale:** The Eastport destination field remains valid for the nonstop search.

## SC1-V1-SX1-F004-R-A2

**Prefix:** Please compare nonstop flights to Eastport

**Action:** Prepare the requested destination field

```text
Destination field: Eastport; no route or fare chosen.
```

**Full instruction:** Please compare nonstop flights to Eastport but I now want only one-stop itineraries to Eastport.

**Rationale:** Eastport remains the destination when the route restriction changes to one stop.

## SC1-V1-SX1-F005-K-A1

**Prefix:** Please find Italian restaurants around Cedar Square

**Action:** Retrieve cuisine-specific restaurant cards

```text
Cedar Pasta: Italian, outdoor seating; Olive Room: Italian, outdoor seating; neither serves Thai cuisine.
```

**Full instruction:** Please find Italian restaurants around Cedar Square and choose places with outdoor seating.

**Rationale:** The two Italian cards already satisfy outdoor seating.

## SC1-V1-SX1-F005-K-A2

**Prefix:** Please find Italian restaurants around Cedar Square

**Action:** Prepare the location field

```text
Search area: Cedar Square; cuisine, hours and price remain unfilled.
```

**Full instruction:** Please find Italian restaurants around Cedar Square and choose places with outdoor seating.

**Rationale:** Cedar Square remains the search area after adding outdoor seating.

## SC1-V1-SX1-F005-R-A2

**Prefix:** Please find Italian restaurants around Cedar Square

**Action:** Prepare the location field

```text
Search area: Cedar Square; cuisine, hours and price remain unfilled.
```

**Full instruction:** Please find Italian restaurants around Cedar Square but change the cuisine to Thai and exclude Italian restaurants.

**Rationale:** The Cedar Square location field remains unchanged when the cuisine changes to Thai.

## SC1-V1-SX1-F006-K-A1

**Prefix:** Please find bakeries around Birch Park

**Action:** Retrieve bakery cards

```text
Birch Bake: bakery with coffee; Loaf House: bakery with coffee; neither is a pharmacy.
```

**Full instruction:** Please find bakeries around Birch Park that serve coffee, including the two listed options.

**Rationale:** Both bakery cards explicitly include coffee as required.

## SC1-V1-SX1-F006-K-A2

**Prefix:** Please find bakeries around Birch Park

**Action:** Prepare a bakery-only comparison layout

```text
Columns: bakery name, bread selection, pastry selection, coffee availability; four fixed headings.
```

**Full instruction:** Please find bakeries around Birch Park that serve coffee, including the two listed options.

**Rationale:** The bakery layout includes coffee availability needed by the final search.

## SC1-V1-SX1-F007-K-A1

**Prefix:** Please find gyms in Riverton that sell day passes

**Action:** Retrieve day-pass gym cards

```text
River Fit: day passes and sauna; North Fit: day passes and sauna. Both sell day passes.
```

**Full instruction:** Please find gyms in Riverton that sell day passes and prioritize day-pass gyms with a sauna.

**Rationale:** Both gym cards explicitly provide day passes and saunas as requested.

## SC1-V1-SX1-F007-K-A2

**Prefix:** Please find gyms in Riverton that sell day passes

**Action:** Prepare the location field

```text
City field: Riverton; membership type remains unfilled.
```

**Full instruction:** Please find gyms in Riverton that sell day passes and prioritize day-pass gyms with a sauna.

**Rationale:** The Riverton location field remains valid for finding the requested gyms.

## SC1-V1-SX1-F007-R-A2

**Prefix:** Please find gyms in Riverton that sell day passes

**Action:** Prepare the location field

```text
City field: Riverton; membership type remains unfilled.
```

**Full instruction:** Please find gyms in Riverton that sell day passes but only consider members-only gyms that do not sell day passes.

**Rationale:** The Riverton city field survives the switch to members-only gyms.

## SC1-V1-SX1-F008-K-A1

**Prefix:** Please find pharmacies in Brookfield that are open now

**Action:** Retrieve open pharmacy cards

```text
Brook Pharmacy: open now, standalone; Elm Pharmacy: open now, standalone. Neither is hospital-based.
```

**Full instruction:** Please find pharmacies in Brookfield that are open now and omit hospital-based pharmacies.

**Rationale:** Both retrieved pharmacies are open and non-hospital-based as required.

## SC1-V1-SX1-F008-K-A2

**Prefix:** Please find pharmacies in Brookfield that are open now

**Action:** Prepare the search time reference

```text
Fixture clock: Monday 14:00 local time; tomorrow resolves to Tuesday in this fixture.
```

**Full instruction:** Please find pharmacies in Brookfield that are open now and omit hospital-based pharmacies.

**Rationale:** The current Monday time supports checking whether the pharmacies are open now.

## SC1-V1-SX1-F008-R-A2

**Prefix:** Please find pharmacies in Brookfield that are open now

**Action:** Prepare the search time reference

```text
Fixture clock: Monday 14:00 local time; tomorrow resolves to Tuesday in this fixture.
```

**Full instruction:** Please find pharmacies in Brookfield that are open now but only list hospital pharmacies that are closed now and open tomorrow.

**Rationale:** The fixed clock resolves now and tomorrow for the revised pharmacy criteria.

## SC1-V1-SX1-F009-K-A1

**Prefix:** Please research local robotic actuator manufacturers

**Action:** Retrieve manufacturer cards

```text
Aster Motion and Delta Drive manufacture robotic actuators locally; neither distributes other makers' parts.
```

**Full instruction:** Please research local robotic actuator manufacturers and retain the manufacturers while adding distributors separately.

**Rationale:** The manufacturer cards remain part of the requested expanded supplier list.

## SC1-V1-SX1-F009-K-A2

**Prefix:** Please research local robotic actuator manufacturers

**Action:** Prepare the component definition

```text
Robotic actuator: component that converts a control input into mechanical movement; no supplier selected.
```

**Full instruction:** Please research local robotic actuator manufacturers and retain the manufacturers while adding distributors separately.

**Rationale:** The actuator definition remains relevant when manufacturers and distributors are researched together.

## SC1-V1-SX1-F009-R-A2

**Prefix:** Please research local robotic actuator manufacturers

**Action:** Prepare the component definition

```text
Robotic actuator: component that converts a control input into mechanical movement; no supplier selected.
```

**Full instruction:** Please research local robotic actuator manufacturers but list distributors only and exclude manufacturers.

**Rationale:** The component definition remains useful for recognizing actuator distributors.

## SC1-V1-SX1-F010-K-A1

**Prefix:** Please compare 15-litre shoulder bags

**Action:** Retrieve bag specification cards

```text
Bag L: shoulder bag, 15 L, 0.5 kg; Bag M: shoulder bag, 15 L, 0.7 kg; neither converts to a backpack.
```

**Full instruction:** Please compare 15-litre shoulder bags and rank the two listed bags by lower weight.

**Rationale:** The bag cards provide eligible products and weights for the requested ranking.

## SC1-V1-SX1-F010-K-A2

**Prefix:** Please compare 15-litre shoulder bags

**Action:** Prepare a weight-ranking routine

```text
Sort supplied product records by numeric weight_kg ascending; no records or capacity filter embedded.
```

**Full instruction:** Please compare 15-litre shoulder bags and rank the two listed bags by lower weight.

**Rationale:** The numeric weight sorter implements the requested lower-weight bag ranking.

## SC1-V1-SX1-F011-K-A1

**Prefix:** Please find brown faux-suede jackets with stand collars

**Action:** Retrieve jacket cards

```text
Jacket A: brown faux suede, stand collar, 120 credits; Jacket B: brown faux suede, stand collar, 150 credits.
```

**Full instruction:** Please find brown faux-suede jackets with stand collars and compare the listed options under 200 credits.

**Rationale:** Both jacket cards meet the material, color, collar and under-200-credit requirements.

## SC1-V1-SX1-F011-K-A2

**Prefix:** Please find brown faux-suede jackets with stand collars

**Action:** Stage a product comparison layout

```text
Columns: material, color, collar type, price; values unfilled.
```

**Full instruction:** Please find brown faux-suede jackets with stand collars and compare the listed options under 200 credits.

**Rationale:** The jacket comparison columns support evaluating attributes and the price ceiling.

## SC1-V1-SX1-F011-R-A2

**Prefix:** Please find brown faux-suede jackets with stand collars

**Action:** Stage a product comparison layout

```text
Columns: material, color, collar type, price; values unfilled.
```

**Full instruction:** Please find brown faux-suede jackets with stand collars but use black cotton jackets with lapels instead and discard the original options.

**Rationale:** The attribute-neutral comparison columns also support black cotton lapel jackets.

## SC1-V1-SX1-F012-K-A1

**Prefix:** Please compare robotics synthetic-data tools that support Engine R

**Action:** Retrieve tool compatibility cards

```text
Sim A and Sim B support Engine R only; neither supports Engine S.
```

**Full instruction:** Please compare robotics synthetic-data tools that support Engine R and keep Engine R support mandatory.

**Rationale:** Both compatibility cards satisfy the retained Engine R requirement.

## SC1-V1-SX1-F012-K-A2

**Prefix:** Please compare robotics synthetic-data tools that support Engine R

**Action:** Prepare a physics-evaluation checklist

```text
Check gravity, collision response, sensor noise and deterministic replay; no engine-specific commands.
```

**Full instruction:** Please compare robotics synthetic-data tools that support Engine R and keep Engine R support mandatory.

**Rationale:** The engine-neutral physics checklist can evaluate the required Engine R tools.

## SC1-V1-SX1-F012-R-A2

**Prefix:** Please compare robotics synthetic-data tools that support Engine R

**Action:** Prepare a physics-evaluation checklist

```text
Check gravity, collision response, sensor noise and deterministic replay; no engine-specific commands.
```

**Full instruction:** Please compare robotics synthetic-data tools that support Engine R but only consider tools for Engine S that do not support Engine R.

**Rationale:** The engine-independent physics checklist can evaluate Engine S tools unchanged.

## SC1-V1-SX1-F013-K-A1

**Prefix:** Please find freestanding desk converters under 250 credits

**Action:** Retrieve converter cards

```text
Lift A: freestanding, 150 credits; Lift B: freestanding, 220 credits. Neither can be permanently mounted.
```

**Full instruction:** Please find freestanding desk converters under 250 credits and exclude permanently mounted converters.

**Rationale:** Both freestanding converters meet the retained price and mounting constraints.

## SC1-V1-SX1-F013-K-A2

**Prefix:** Please find freestanding desk converters under 250 credits

**Action:** Prepare the price ceiling field

```text
Maximum price field: 250 credits; mounting type unfilled.
```

**Full instruction:** Please find freestanding desk converters under 250 credits and exclude permanently mounted converters.

**Rationale:** The 250-credit ceiling remains the required budget constraint.

## SC1-V1-SX1-F013-R-A2

**Prefix:** Please find freestanding desk converters under 250 credits

**Action:** Prepare the price ceiling field

```text
Maximum price field: 250 credits; mounting type unfilled.
```

**Full instruction:** Please find freestanding desk converters under 250 credits but only show permanently mounted converters and discard freestanding ones.

**Rationale:** The 250-credit ceiling remains applicable when the mounting constraint changes.

## SC1-V1-SX1-F014-K-A1

**Prefix:** Please find a 30-minute meeting for Sam and me on Tuesday

**Action:** Read Tuesday availability

```text
Sam and requester both free Tuesday 14:00–14:30 and 15:00–15:30. No Wednesday availability included.
```

**Full instruction:** Please find a 30-minute meeting for Sam and me on Tuesday and use either of the two listed Tuesday slots.

**Rationale:** The availability record directly supplies the requested Tuesday alternatives.

## SC1-V1-SX1-F014-R-A2

**Prefix:** Please find a 30-minute meeting for Sam and me on Tuesday

**Action:** Stage a Wednesday calendar event

```text
Unsent event object: attendees Sam and requester, duration 30 minutes, day Wednesday; no time set.
```

**Full instruction:** Please find a 30-minute meeting for Sam and me on Tuesday but switch the meeting to Wednesday and ignore Tuesday availability.

**Rationale:** The unsent Wednesday event preserves the required attendees and duration on the final day.

## SC1-V1-SX1-F015-K-A1

**Prefix:** Please check whether my dentist can see me on Friday

**Action:** Read Friday availability

```text
The fixture dentist has no Friday openings; no Monday availability included.
```

**Full instruction:** Please check whether my dentist can see me on Friday and keep my existing appointment if Friday has no openings.

**Rationale:** The absence of Friday openings determines that the existing appointment should be kept.

## SC1-V1-SX1-F015-K-A2

**Prefix:** Please check whether my dentist can see me on Friday

**Action:** Retrieve the existing appointment

```text
Current appointment: Wednesday 11:00, dentist Dr Vale, appointment ID D17.
```

**Full instruction:** Please check whether my dentist can see me on Friday and keep my existing appointment if Friday has no openings.

**Rationale:** The existing appointment record identifies the appointment to retain if Friday is unavailable.

## SC1-V1-SX1-F015-R-A2

**Prefix:** Please check whether my dentist can see me on Friday

**Action:** Retrieve the existing appointment

```text
Current appointment: Wednesday 11:00, dentist Dr Vale, appointment ID D17.
```

**Full instruction:** Please check whether my dentist can see me on Friday but check Monday instead and ignore Friday openings, keeping my existing appointment as fallback.

**Rationale:** The existing appointment record remains needed as the Monday-search fallback.

## SC1-V1-SX1-F016-K-A1

**Prefix:** Please find team meeting slots this week after 10 AM

**Action:** Read afternoon team availability

```text
Whole team free Thursday 13:00–13:30 and Friday 14:00–14:30; no morning data included.
```

**Full instruction:** Please find team meeting slots this week after 10 AM and show the two listed afternoon slots.

**Rationale:** The retrieved afternoon availability contains exactly the two requested slots.

## SC1-V1-SX1-F016-K-A2

**Prefix:** Please find team meeting slots this week after 10 AM

**Action:** Prepare the participant list

```text
Participants: Sam, Jo and requester; no time selected.
```

**Full instruction:** Please find team meeting slots this week after 10 AM and show the two listed afternoon slots.

**Rationale:** The participant list remains valid for selecting the specified afternoon team slots.

## SC1-V1-SX1-F016-R-A2

**Prefix:** Please find team meeting slots this week after 10 AM

**Action:** Prepare the participant list

```text
Participants: Sam, Jo and requester; no time selected.
```

**Full instruction:** Please find team meeting slots this week after 10 AM but only consider slots before 10 AM this week.

**Rationale:** The participant list is unchanged by the switch to before-10-AM slots.

## SC1-V1-SX1-F017-K-A1

**Prefix:** Please prepare a report reminder for tomorrow morning

**Action:** Stage a morning reminder

```text
Unsent reminder: title Submit report, day tomorrow, time 09:00.
```

**Full instruction:** Please prepare a report reminder for tomorrow morning and set its time to 9 AM.

**Rationale:** The staged tomorrow-at-09:00 report reminder matches the requested time.

## SC1-V1-SX1-F017-K-A2

**Prefix:** Please prepare a report reminder for tomorrow morning

**Action:** Prepare the reminder text

```text
Reminder title: Submit report; date and time unfilled.
```

**Full instruction:** Please prepare a report reminder for tomorrow morning and set its time to 9 AM.

**Rationale:** The reminder title remains correct after assigning tomorrow at 9 AM.

## SC1-V1-SX1-F017-R-A2

**Prefix:** Please prepare a report reminder for tomorrow morning

**Action:** Prepare the reminder text

```text
Reminder title: Submit report; date and time unfilled.
```

**Full instruction:** Please prepare a report reminder for tomorrow morning but change it to tomorrow evening at 7 PM.

**Rationale:** The time-neutral report title remains valid for 7 PM tomorrow.

## SC1-V1-SX1-F018-K-A1

**Prefix:** Please draft a reply thanking Morgan for the introduction

**Action:** Draft the thank-you sentence

```text
Thank you for making the introduction, Morgan.
```

**Full instruction:** Please draft a reply thanking Morgan for the introduction and offer to provide more information.

**Rationale:** The thank-you sentence remains required alongside the information offer.

## SC1-V1-SX1-F018-K-A2

**Prefix:** Please draft a reply thanking Morgan for the introduction

**Action:** Draft an offer sentence

```text
I would be happy to provide any additional information you need.
```

**Full instruction:** Please draft a reply thanking Morgan for the introduction and offer to provide more information.

**Rationale:** The offer sentence directly fulfills the request to offer further information.

## SC1-V1-SX1-F019-K-A1

**Prefix:** Please draft a team update saying the build is delayed

**Action:** Draft the status sentence

```text
The build is delayed; we are still investigating the cause.
```

**Full instruction:** Please draft a team update saying the build is delayed and keep the cause neutral because it is not yet known.

**Rationale:** The sentence states the delay without inventing a cause.

## SC1-V1-SX1-F019-K-A2

**Prefix:** Please draft a team update saying the build is delayed

**Action:** Stage a neutral update heading

```text
Heading: Build status update; no status claim or cause included.
```

**Full instruction:** Please draft a team update saying the build is delayed and keep the cause neutral because it is not yet known.

**Rationale:** The neutral heading remains appropriate for a delay update.

## SC1-V1-SX1-F019-R-A2

**Prefix:** Please draft a team update saying the build is delayed

**Action:** Stage a neutral update heading

```text
Heading: Build status update; no status claim or cause included.
```

**Full instruction:** Please draft a team update saying the build is delayed but the build is on schedule, so report that and do not mention a delay.

**Rationale:** The neutral build-status heading remains valid when the reported status changes to on schedule.

## SC1-V1-SX1-F020-K-A1

**Prefix:** Please draft a message declining dinner tonight

**Action:** Draft the decline sentence

```text
I cannot make dinner tonight.
```

**Full instruction:** Please draft a message declining dinner tonight and suggest meeting next weekend.

**Rationale:** The decline sentence remains usable with the added next-weekend invitation.

## SC1-V1-SX1-F020-K-A2

**Prefix:** Please draft a message declining dinner tonight

**Action:** Draft the alternative-date sentence

```text
Would you like to meet next weekend instead?
```

**Full instruction:** Please draft a message declining dinner tonight and suggest meeting next weekend.

**Rationale:** The next-weekend invitation directly supplies the requested alternative date.

## SC1-V1-SX1-F021-K-A1

**Prefix:** Please draft a refund approval message

**Action:** Draft the approval sentence

```text
Your refund has been approved.
```

**Full instruction:** Please draft a refund approval message and avoid promising a payment date.

**Rationale:** The refund-approval sentence states approval without promising a payment date.

## SC1-V1-SX1-F021-K-A2

**Prefix:** Please draft a refund approval message

**Action:** Stage an approval-specific reply template

```text
Subject: Refund approved. Closing: Thank you for your patience. Body unfilled.
```

**Full instruction:** Please draft a refund approval message and avoid promising a payment date.

**Rationale:** The approval template remains valid and promises no payment date.

## SC1-V1-SX1-F022-K-A1

**Prefix:** Please find peer-reviewed papers about hidden-state probing

**Action:** Retrieve peer-reviewed fixture records

```text
Paper P and Paper Q: peer-reviewed hidden-state probing papers in the synthetic catalogue; no technical reports included.
```

**Full instruction:** Please find peer-reviewed papers about hidden-state probing and use only peer-reviewed sources.

**Rationale:** The two peer-reviewed probing records satisfy the final source restriction.

## SC1-V1-SX1-F022-K-A2

**Prefix:** Please find peer-reviewed papers about hidden-state probing

**Action:** Prepare the topic search terms

```text
Terms: hidden-state probing, representation analysis; no publication-type filter.
```

**Full instruction:** Please find peer-reviewed papers about hidden-state probing and use only peer-reviewed sources.

**Rationale:** The probing search terms remain applicable with a peer-review filter.

## SC1-V1-SX1-F022-R-A2

**Prefix:** Please find peer-reviewed papers about hidden-state probing

**Action:** Prepare the topic search terms

```text
Terms: hidden-state probing, representation analysis; no publication-type filter.
```

**Full instruction:** Please find peer-reviewed papers about hidden-state probing but use only non-peer-reviewed technical reports about hidden-state probing.

**Rationale:** The source-neutral probing terms remain usable for the technical-report-only search.

## SC1-V1-SX1-F023-K-A1

**Prefix:** Please find version 3 documentation for Library L

**Action:** Retrieve versioned documentation

```text
Official Library L version 3: old_connect(endpoint) is the connection entry point. This fixture marks it removed in version 4.
```

**Full instruction:** Please find version 3 documentation for Library L and use only the official version 3 material.

**Rationale:** The retrieved official version 3 documentation satisfies the final source restriction.

## SC1-V1-SX1-F023-K-A2

**Prefix:** Please find version 3 documentation for Library L

**Action:** Retrieve the official documentation index URL

```text
Fixture URL: https://library-l.example/docs/ ; index lists version 3 and version 4.
```

**Full instruction:** Please find version 3 documentation for Library L and use only the official version 3 material.

**Rationale:** The official index already provides a reusable route to version 3 documentation.

## SC1-V1-SX1-F023-R-A2

**Prefix:** Please find version 3 documentation for Library L

**Action:** Retrieve the official documentation index URL

```text
Fixture URL: https://library-l.example/docs/ ; index lists version 3 and version 4.
```

**Full instruction:** Please find version 3 documentation for Library L but use version 4 instead and exclude all version 3 documentation.

**Rationale:** The official index contains version 4 and remains usable after the version change.

## SC1-V1-SX1-F024-K-A1

**Prefix:** Please compare Acme's revenue in its two annual releases

**Action:** Extract Acme revenue figures

```text
Acme fixture: prior year revenue 10 million credits; current year 12 million credits.
```

**Full instruction:** Please compare Acme's revenue in its two annual releases and report company-stated actual revenue only.

**Rationale:** The extracted Acme revenue figures are the company-specific actual values required for comparison.

## SC1-V1-SX1-F025-K-A1

**Prefix:** Please find primary rules for Region A consumer AI systems

**Action:** Retrieve jurisdiction-specific rule cards

```text
Rule A1 and Rule A2: synthetic Region A consumer-AI rules, with no applicability in Region B.
```

**Full instruction:** Please find primary rules for Region A consumer AI systems and keep Region A as the main jurisdiction.

**Rationale:** Region A rule cards remain applicable to the retained jurisdiction.

## SC1-V1-SX1-F025-K-A2

**Prefix:** Please find primary rules for Region A consumer AI systems

**Action:** Stage a legal-source comparison layout

```text
Columns: jurisdiction, issuing authority, effective date, provision; no legal claims filled in.
```

**Full instruction:** Please find primary rules for Region A consumer AI systems and keep Region A as the main jurisdiction.

**Rationale:** The jurisdiction and authority columns remain useful for comparing Region A primary rules.

## SC1-V1-SX1-F025-R-A2

**Prefix:** Please find primary rules for Region A consumer AI systems

**Action:** Stage a legal-source comparison layout

```text
Columns: jurisdiction, issuing authority, effective date, provision; no legal claims filled in.
```

**Full instruction:** Please find primary rules for Region A consumer AI systems but use Region B rules only and exclude Region A rules.

**Rationale:** The unfilled legal-source columns accommodate Region B without revision.

## SC1-V1-SX1-F026-K-A1

**Prefix:** Please compare small open-weight reasoning models

**Action:** Collect vendor-only benchmark claims

```text
Vendor card: Model K claims 80 points and Model J claims 85 points; neither claim is independently reproduced.
```

**Full instruction:** Please compare small open-weight reasoning models and flag vendor-only scores as unverified rather than treating them as evidence.

**Rationale:** The vendor claims remain usable when marked unverified.

## SC1-V1-SX1-F026-K-A2

**Prefix:** Please compare small open-weight reasoning models

**Action:** Collect independent fixture benchmark records

```text
Independent lab fixture: Model K 70 points, Model J 72 points, same test and evaluation settings; both small and open-weight.
```

**Full instruction:** Please compare small open-weight reasoning models and flag vendor-only scores as unverified rather than treating them as evidence.

**Rationale:** The independent scores remain usable comparison evidence while vendor claims are flagged separately.

## SC1-V1-SX1-F026-R-A2

**Prefix:** Please compare small open-weight reasoning models

**Action:** Collect independent fixture benchmark records

```text
Independent lab fixture: Model K 70 points, Model J 72 points, same test and evaluation settings; both small and open-weight.
```

**Full instruction:** Please compare small open-weight reasoning models but include only independently reproduced scores and omit vendor-only claims entirely.

**Rationale:** The independent same-test scores satisfy the reproduced-evidence restriction.

## SC1-V1-SX1-F027-K-A1

**Prefix:** Please calculate a 7 percent downside scenario for a 100-credit index

**Action:** Calculate the requested scenario

```text
100 × (1 − 0.07) = 93 credits; only the 7% result retained.
```

**Full instruction:** Please calculate a 7 percent downside scenario for a 100-credit index and show the hypothetical level without making a trade.

**Rationale:** The 93-credit result is the requested hypothetical 7-percent scenario.

## SC1-V1-SX1-F027-K-A2

**Prefix:** Please calculate a 7 percent downside scenario for a 100-credit index

**Action:** Prepare the scenario formula

```text
Scenario level = starting level × (1 − decline_fraction); no numeric assumptions embedded.
```

**Full instruction:** Please calculate a 7 percent downside scenario for a 100-credit index and show the hypothetical level without making a trade.

**Rationale:** The symbolic downside expression supports the requested seven-percent calculation without executing a trade.

## SC1-V1-SX1-F027-R-A2

**Prefix:** Please calculate a 7 percent downside scenario for a 100-credit index

**Action:** Prepare the scenario formula

```text
Scenario level = starting level × (1 − decline_fraction); no numeric assumptions embedded.
```

**Full instruction:** Please calculate a 7 percent downside scenario for a 100-credit index but use a 12 percent decline instead and omit the 7 percent case.

**Rationale:** The symbolic downside formula remains valid with a 12-percent decline.

## SC1-V1-SX1-F028-K-A1

**Prefix:** Please calculate budget variance from my supplied table

**Action:** Compute category variances

```text
Fixture variances: supplies +20 credits, travel +5 credits, meals −10 credits; positive means overspend.
```

**Full instruction:** Please calculate budget variance from my supplied table and identify the largest overspend.

**Rationale:** The category variances identify supplies as the largest overspend.

## SC1-V1-SX1-F028-K-A2

**Prefix:** Please calculate budget variance from my supplied table

**Action:** Aggregate actual category totals

```text
Fixture actuals: supplies 120 credits, travel 85 credits, meals 40 credits; source-table sums retained.
```

**Full instruction:** Please calculate budget variance from my supplied table and identify the largest overspend.

**Rationale:** The actual category sums remain reusable inputs for finding budget overspends.

## SC1-V1-SX1-F028-R-A2

**Prefix:** Please calculate budget variance from my supplied table

**Action:** Aggregate actual category totals

```text
Fixture actuals: supplies 120 credits, travel 85 credits, meals 40 credits; source-table sums retained.
```

**Full instruction:** Please calculate budget variance from my supplied table but show actual category totals only, without calculating or reporting variances.

**Rationale:** The aggregated actual totals are exactly the requested final output.

## SC1-V1-SX1-F029-K-A1

**Prefix:** Please compare current holdings with the start-of-month snapshot

**Action:** Calculate start-of-month concentration

```text
Start-of-month fixture: asset A 60%, asset B 40%; no other date included.
```

**Full instruction:** Please compare current holdings with the start-of-month snapshot and report concentration changes for those two snapshots.

**Rationale:** The start-of-month percentages are the required baseline for concentration changes.

## SC1-V1-SX1-F029-K-A2

**Prefix:** Please compare current holdings with the start-of-month snapshot

**Action:** Calculate current concentration

```text
Current fixture: asset A 50%, asset B 50%; values unchanged across comparisons.
```

**Full instruction:** Please compare current holdings with the start-of-month snapshot and report concentration changes for those two snapshots.

**Rationale:** The current percentages are required to compute concentration changes.

## SC1-V1-SX1-F029-R-A2

**Prefix:** Please compare current holdings with the start-of-month snapshot

**Action:** Calculate current concentration

```text
Current fixture: asset A 50%, asset B 50%; values unchanged across comparisons.
```

**Full instruction:** Please compare current holdings with the start-of-month snapshot but compare current holdings with the start-of-year snapshot instead and ignore start-of-month holdings.

**Rationale:** The current 50/50 concentration remains explicitly unchanged when the comparison baseline changes to start of year.

## SC1-V1-SX1-F030-K-A1

**Prefix:** Please calculate breakeven for my debit spread using the supplied values

**Action:** Calculate the original breakeven

```text
For this fixture's specified call debit spread: 100 + 5 = 105 credits.
```

**Full instruction:** Please calculate breakeven for my debit spread using the supplied values and use the supplied 5-credit debit and 100-credit lower strike.

**Rationale:** The 105-credit breakeven uses exactly the retained strike and debit.

## SC1-V1-SX1-F030-K-A2

**Prefix:** Please calculate breakeven for my debit spread using the supplied values

**Action:** Prepare the symbolic breakeven expression

```text
For the specified call debit spread: lower_strike + net_debit; no prices filled in.
```

**Full instruction:** Please calculate breakeven for my debit spread using the supplied values and use the supplied 5-credit debit and 100-credit lower strike.

**Rationale:** The symbolic breakeven expression supports the supplied 100-credit strike and five-credit debit.

## SC1-V1-SX1-F030-R-A2

**Prefix:** Please calculate breakeven for my debit spread using the supplied values

**Action:** Prepare the symbolic breakeven expression

```text
For the specified call debit spread: lower_strike + net_debit; no prices filled in.
```

**Full instruction:** Please calculate breakeven for my debit spread using the supplied values but correct the debit to 8 credits while keeping the lower strike at 100 credits.

**Rationale:** The symbolic expression accepts the corrected debit without changing the formula.

## SC1-V1-SX1-F031-K-A1

**Prefix:** Please write a Python function that counts ERROR lines in the supplied log

**Action:** Stage an ERROR-counting function

```text
def count_lines(lines): return sum(line.startswith('ERROR ') for line in lines)
```

**Full instruction:** Please write a Python function that counts ERROR lines in the supplied log and return the count without changing the file.

**Rationale:** The ERROR counter returns a count without modifying the file.

## SC1-V1-SX1-F031-K-A2

**Prefix:** Please write a Python function that counts ERROR lines in the supplied log

**Action:** Stage a log-reading helper

```text
def read_lines(path):
    with open(path, encoding='utf-8') as f:
        return f.read().splitlines()
```

**Full instruction:** Please write a Python function that counts ERROR lines in the supplied log and return the count without changing the file.

**Rationale:** The read-only log helper supplies lines for counting without changing the file.

## SC1-V1-SX1-F031-R-A2

**Prefix:** Please write a Python function that counts ERROR lines in the supplied log

**Action:** Stage a log-reading helper

```text
def read_lines(path):
    with open(path, encoding='utf-8') as f:
        return f.read().splitlines()
```

**Full instruction:** Please write a Python function that counts ERROR lines in the supplied log but count WARN lines instead and do not count ERROR lines.

**Rationale:** The severity-neutral reader remains reusable before counting WARN lines.

## SC1-V1-SX1-F032-K-A1

**Prefix:** Please inspect the client timeout path without changing the code

**Action:** Collect a timeout observation

```text
Fixture client.py line 8: DEFAULT_TIMEOUT = 5; request() passes this constant as its timeout argument.
```

**Full instruction:** Please inspect the client timeout path without changing the code and identify where its five-second timeout is set.

**Rationale:** The timeout observation directly locates the five-second constant and its use.

## SC1-V1-SX1-F032-R-A1

**Prefix:** Please inspect the client timeout path without changing the code

**Action:** Collect a timeout observation

```text
Fixture client.py line 8: DEFAULT_TIMEOUT = 5; request() passes this constant as its timeout argument.
```

**Full instruction:** Please inspect the client timeout path without changing the code but modify the default timeout to ten seconds instead of producing an inspection report.

**Rationale:** The timeout location and reference identify exactly where the ten-second change must be made.

## SC1-V1-SX1-F032-R-A2

**Prefix:** Please inspect the client timeout path without changing the code

**Action:** Stage a ten-second timeout patch

```text
Unapplied patch replaces DEFAULT_TIMEOUT = 5 with DEFAULT_TIMEOUT = 10; no other edits.
```

**Full instruction:** Please inspect the client timeout path without changing the code but modify the default timeout to ten seconds instead of producing an inspection report.

**Rationale:** The unapplied patch implements exactly the requested ten-second timeout change.

## SC1-V1-SX1-F033-K-A1

**Prefix:** Please refactor the add function while preserving its public name and behavior

**Action:** Stage the preserving refactor

```text
Replacement definition: def add(a, b): return a + b; public symbol remains add.
```

**Full instruction:** Please refactor the add function while preserving its public name and behavior and keep its existing callers compatible.

**Rationale:** The add definition preserves the specified public symbol and addition behavior.

## SC1-V1-SX1-F033-K-A2

**Prefix:** Please refactor the add function while preserving its public name and behavior

**Action:** Stage addition behavior tests

```text
Assertions: operation(2, 3) == 5; operation(-1, 1) == 0; operation supplied by the test harness, not hardcoded to a name.
```

**Full instruction:** Please refactor the add function while preserving its public name and behavior and keep its existing callers compatible.

**Rationale:** The name-independent addition tests still check behavior while preserving caller compatibility.

## SC1-V1-SX1-F033-R-A2

**Prefix:** Please refactor the add function while preserving its public name and behavior

**Action:** Stage addition behavior tests

```text
Assertions: operation(2, 3) == 5; operation(-1, 1) == 0; operation supplied by the test harness, not hardcoded to a name.
```

**Full instruction:** Please refactor the add function while preserving its public name and behavior but rename the public function to total and update callers to use total.

**Rationale:** The name-independent addition tests remain valid after renaming the public function.

## SC1-V1-SX1-F034-K-A1

**Prefix:** Please add malformed-JSON tests to the parser

**Action:** Stage malformed-input test cases

```text
Inputs: an unmatched opening brace, an unfinished numeric array, and an object with an unquoted key; expected outcome for each: parse error.
```

**Full instruction:** Please add malformed-JSON tests to the parser and keep this work limited to correctness tests.

**Rationale:** The malformed inputs and expected parse errors directly supply correctness tests.

## SC1-V1-SX1-F034-K-A2

**Prefix:** Please add malformed-JSON tests to the parser

**Action:** Prepare a correctness-test report layout

```text
Columns: malformed input, expected error, observed error; no timing column.
```

**Full instruction:** Please add malformed-JSON tests to the parser and keep this work limited to correctness tests.

**Rationale:** The error-report columns support the required correctness tests.

## SC1-V1-SX1-F035-K-A1

**Prefix:** Please rewrite this note for executives while preserving its numbers

**Action:** Draft the executive summary

```text
The project will take 12 weeks with a budget of 30 credits; the decision needed is approval to proceed.
```

**Full instruction:** Please rewrite this note for executives while preserving its numbers and keep both the 12-week duration and 30-credit budget.

**Rationale:** The executive draft retains the specified duration and budget.

## SC1-V1-SX1-F035-K-A2

**Prefix:** Please rewrite this note for executives while preserving its numbers

**Action:** Extract the unchanged duration

```text
Duration fact from the supplied fixture note: 12 weeks.
```

**Full instruction:** Please rewrite this note for executives while preserving its numbers and keep both the 12-week duration and 30-credit budget.

**Rationale:** The extracted 12-week duration is expressly preserved by the final instruction.

## SC1-V1-SX1-F035-R-A2

**Prefix:** Please rewrite this note for executives while preserving its numbers

**Action:** Extract the unchanged duration

```text
Duration fact from the supplied fixture note: 12 weeks.
```

**Full instruction:** Please rewrite this note for executives while preserving its numbers but make it a technical note for engineers and correct the budget to 40 credits.

**Rationale:** The 12-week duration survives the audience change and budget correction.

## SC1-V1-SX1-F036-K-A1

**Prefix:** Please summarize the main report without using the appendix

**Action:** Extract main-report finding

```text
Main report fixture: trial A completed in 8 days with 2 defects. This fact appears only in the main report.
```

**Full instruction:** Please summarize the main report without using the appendix and use only the main report findings.

**Rationale:** The extracted main-report fact is admissible under the retained source restriction.

## SC1-V1-SX1-F036-K-A2

**Prefix:** Please summarize the main report without using the appendix

**Action:** Stage a summary layout

```text
Headings: objective, evidence, limitations; no source facts populated.
```

**Full instruction:** Please summarize the main report without using the appendix and use only the main report findings.

**Rationale:** The generic summary headings can organize the main-report findings unchanged.

## SC1-V1-SX1-F036-R-A2

**Prefix:** Please summarize the main report without using the appendix

**Action:** Stage a summary layout

```text
Headings: objective, evidence, limitations; no source facts populated.
```

**Full instruction:** Please summarize the main report without using the appendix but summarize the appendix only and ignore the main report.

**Rationale:** The source-neutral summary headings can structure an appendix-only summary unchanged.

## SC1-V1-SX1-F037-K-A1

**Prefix:** Please draft a proposal from these notes and leave pricing undecided

**Action:** Stage the pricing section

```text
Pricing: TBD. No numeric quote is included.
```

**Full instruction:** Please draft a proposal from these notes and leave pricing undecided and mark pricing as TBD.

**Rationale:** The TBD pricing section exactly matches the required undecided price.

## SC1-V1-SX1-F037-K-A2

**Prefix:** Please draft a proposal from these notes and leave pricing undecided

**Action:** Stage the scope section

```text
Scope: deliver one dashboard and its handover guide; no price or schedule included.
```

**Full instruction:** Please draft a proposal from these notes and leave pricing undecided and mark pricing as TBD.

**Rationale:** The scope section remains applicable while pricing stays TBD.

## SC1-V1-SX1-F037-R-A2

**Prefix:** Please draft a proposal from these notes and leave pricing undecided

**Action:** Stage the scope section

```text
Scope: deliver one dashboard and its handover guide; no price or schedule included.
```

**Full instruction:** Please draft a proposal from these notes and leave pricing undecided but quote the supplied fixed price of 500 credits and remove TBD pricing.

**Rationale:** The dashboard and handover scope remains usable when the pricing section changes to 500 credits.

## SC1-V1-SX1-F038-K-A1

**Prefix:** Please compare these two resumes without recommending a candidate

**Action:** Extract resume differences

```text
Resume A lists Python and 3 years of experience; Resume B lists Java and 5 years. These are fixture facts.
```

**Full instruction:** Please compare these two resumes without recommending a candidate and list differences only.

**Rationale:** The resume facts provide the requested differences without a recommendation.

## SC1-V1-SX1-F038-R-A1

**Prefix:** Please compare these two resumes without recommending a candidate

**Action:** Extract resume differences

```text
Resume A lists Python and 3 years of experience; Resume B lists Java and 5 years. These are fixture facts.
```

**Full instruction:** Please compare these two resumes without recommending a candidate but recommend a candidate using the same resumes and explain the choice.

**Rationale:** The resume skills and experience remain evidence for explaining the candidate recommendation.

## SC1-V1-SX1-F039-K-A1

**Prefix:** Please stage the living-room lights at 30 percent brightness

**Action:** Stage the requested lighting command

```text
Unapplied command: room=living_room, brightness=30, color=unchanged.
```

**Full instruction:** Please stage the living-room lights at 30 percent brightness while preserving their current color, without applying changes.

**Rationale:** The staged living-room command sets 30 percent and preserves color without applying changes.

## SC1-V1-SX1-F039-K-A2

**Prefix:** Please stage the living-room lights at 30 percent brightness

**Action:** Read living-room light state

```text
Living-room fixture: brightness 80%, color warm white. No bedroom state included.
```

**Full instruction:** Please stage the living-room lights at 30 percent brightness while preserving their current color, without applying changes.

**Rationale:** The living-room state supplies the existing color needed for preservation.

## SC1-V1-SX1-F040-K-A2

**Prefix:** Please stage a 70 F thermostat setting for tonight

**Action:** Read current thermostat setting

```text
Current fixture thermostat setting: 70 F; reading retained for conditional comparison.
```

**Full instruction:** Please stage a 70 F thermostat setting for tonight only if the current setting differs from 70 F; do not apply it.

**Rationale:** The 70 F reading establishes that no 70 F plan should be staged.

## SC1-V1-SX1-F040-R-A2

**Prefix:** Please stage a 70 F thermostat setting for tonight

**Action:** Read current thermostat setting

```text
Current fixture thermostat setting: 70 F; reading retained for conditional comparison.
```

**Full instruction:** Please stage a 70 F thermostat setting for tonight but stage 68 F instead, only if the current setting differs from 68 F; do not apply it.

**Rationale:** The current 70 F reading establishes that the conditional 68 F plan is needed.

## SC1-V1-SX1-F041-K-A1

**Prefix:** Please prepare to lock the back door after I leave

**Action:** Read back-door sensor

```text
Back-door fixture sensor: closed and unlocked; timestamp belongs to the fixed scenario snapshot.
```

**Full instruction:** Please prepare to lock the back door after I leave and check the back-door sensor before staging anything.

**Rationale:** The back-door sensor reading supplies the mandated pre-staging check.

## SC1-V1-SX1-F041-R-A2

**Prefix:** Please prepare to lock the back door after I leave

**Action:** Stage a departure trigger definition

```text
Trigger: requester_departed becomes true; no door or lock operation attached.
```

**Full instruction:** Please prepare to lock the back door after I leave but prepare to lock the front door instead and do not use the back-door sensor reading.

**Rationale:** The departure trigger remains applicable when the door changes from back to front.

## SC1-V1-SX1-F042-K-A1

**Prefix:** Please stage a kitchen-only vacuum run

**Action:** Stage the room-specific cleaning plan

```text
Unapplied vacuum plan: include kitchen; exclude bedroom, hall and living room.
```

**Full instruction:** Please stage a kitchen-only vacuum run and keep all other rooms excluded; do not start cleaning.

**Rationale:** The unapplied kitchen-only plan already excludes all other rooms.

## SC1-V1-SX1-F042-K-A2

**Prefix:** Please stage a kitchen-only vacuum run

**Action:** Read vacuum battery state

```text
Fixture vacuum battery: 90%; sufficient for either single-room run in this scenario.
```

**Full instruction:** Please stage a kitchen-only vacuum run and keep all other rooms excluded; do not start cleaning.

**Rationale:** The sufficient battery state remains useful for staging the kitchen-only run.

## SC1-V1-SX1-F042-R-A2

**Prefix:** Please stage a kitchen-only vacuum run

**Action:** Read vacuum battery state

```text
Fixture vacuum battery: 90%; sufficient for either single-room run in this scenario.
```

**Full instruction:** Please stage a kitchen-only vacuum run but stage a bedroom-only run instead and discard the kitchen plan.

**Rationale:** The 90-percent battery reading explicitly establishes sufficient charge for the replacement bedroom run.

## SC1-V1-SX1-F043-K-A1

**Prefix:** Please find robotics documentaries

**Action:** Retrieve robotics documentary cards

```text
Robot Workshop: robotics, 60 minutes; Machine Motion: robotics, 75 minutes; neither covers astronomy.
```

**Full instruction:** Please find robotics documentaries and include only titles under 90 minutes.

**Rationale:** Both robotics documentaries meet the explicit under-90-minute limit.

## SC1-V1-SX1-F043-K-A2

**Prefix:** Please find robotics documentaries

**Action:** Prepare a runtime filter

```text
Keep input records whose runtime_minutes < 90; no topic filter or titles embedded.
```

**Full instruction:** Please find robotics documentaries and include only titles under 90 minutes.

**Rationale:** The runtime filter directly implements the stated under-90-minute limit.

## SC1-V1-SX1-F044-K-A1

**Prefix:** Please build an upbeat instrumental jazz playlist

**Action:** Collect instrumental track cards

```text
Track A and Track B: upbeat jazz, instrumental; no vocals in either fixture track.
```

**Full instruction:** Please build an upbeat instrumental jazz playlist and exclude vocal tracks.

**Rationale:** Both upbeat instrumental jazz tracks satisfy the no-vocals constraint.

## SC1-V1-SX1-F044-K-A2

**Prefix:** Please build an upbeat instrumental jazz playlist

**Action:** Prepare a vocal-track exclusion predicate

```text
Keep a supplied track only when has_vocals is false; no titles embedded.
```

**Full instruction:** Please build an upbeat instrumental jazz playlist and exclude vocal tracks.

**Rationale:** The vocal exclusion predicate matches the final instrumental-only requirement.

## SC1-V1-SX1-F045-K-A1

**Prefix:** Please choose a non-horror movie under two hours for tonight

**Action:** Retrieve movie cards

```text
Film A: comedy, 90 minutes; Film B: drama, 105 minutes; both explicitly not horror.
```

**Full instruction:** Please choose a non-horror movie under two hours for tonight and compare the listed eligible options.

**Rationale:** The two short non-horror movie cards match the final eligible-options instruction.

## SC1-V1-SX1-F045-K-A2

**Prefix:** Please choose a non-horror movie under two hours for tonight

**Action:** Stage a generic movie comparison layout

```text
Columns: title, genre, runtime, availability tonight; no candidate titles or restrictions filled in.
```

**Full instruction:** Please choose a non-horror movie under two hours for tonight and compare the listed eligible options.

**Rationale:** The unfilled movie comparison columns remain appropriate for the eligible options.

## SC1-V1-SX1-F045-R-A2

**Prefix:** Please choose a non-horror movie under two hours for tonight

**Action:** Stage a generic movie comparison layout

```text
Columns: title, genre, runtime, availability tonight; no candidate titles or restrictions filled in.
```

**Full instruction:** Please choose a non-horror movie under two hours for tonight but choose a horror movie longer than two hours instead.

**Rationale:** The generic film layout can compare long horror films without embedded conflicting restrictions.

## SC1-V1-SX1-F046-K-A1

**Prefix:** Please find technical podcast interviews about AI agents

**Action:** Retrieve interview episode cards

```text
Episode I and Episode J: technical AI-agent interviews; neither is a news roundup.
```

**Full instruction:** Please find technical podcast interviews about AI agents and favor interviews over news roundups.

**Rationale:** The technical interview cards satisfy the final interview preference.

## SC1-V1-SX1-F046-K-A2

**Prefix:** Please find technical podcast interviews about AI agents

**Action:** Prepare the topic query

```text
Topic query: AI agents; no episode-format restriction.
```

**Full instruction:** Please find technical podcast interviews about AI agents and favor interviews over news roundups.

**Rationale:** The AI-agents topic query remains appropriate for finding the preferred interview episodes.

## SC1-V1-SX1-F046-R-A2

**Prefix:** Please find technical podcast interviews about AI agents

**Action:** Prepare the topic query

```text
Topic query: AI agents; no episode-format restriction.
```

**Full instruction:** Please find technical podcast interviews about AI agents but use only news roundups and exclude interviews.

**Rationale:** The format-neutral AI agents query remains usable for news roundups.

## SC1-V1-SX1-F047-K-A1

**Prefix:** Please make a three-day business-trip packing checklist

**Action:** Draft the clothing checklist

```text
Two business shirts; one pair of office trousers; office shoes. No formalwear included.
```

**Full instruction:** Please make a three-day business-trip packing checklist and omit formalwear.

**Rationale:** The business clothing checklist already omits formalwear as required.

## SC1-V1-SX1-F047-K-A2

**Prefix:** Please make a three-day business-trip packing checklist

**Action:** Draft the shared essentials checklist

```text
Toothbrush; phone charger; personal identification. No destination-specific supplies included.
```

**Full instruction:** Please make a three-day business-trip packing checklist and omit formalwear.

**Rationale:** The essential-item checklist remains applicable and includes no formalwear.

## SC1-V1-SX1-F047-R-A2

**Prefix:** Please make a three-day business-trip packing checklist

**Action:** Draft the shared essentials checklist

```text
Toothbrush; phone charger; personal identification. No destination-specific supplies included.
```

**Full instruction:** Please make a three-day business-trip packing checklist but make it a three-day camping checklist instead, with no business clothing.

**Rationale:** Toothbrush, charger and identification remain usable camping essentials without business clothing.

## SC1-V1-SX1-F048-K-A1

**Prefix:** Please plan my morning around a 9 AM appointment

**Action:** Calculate the original departure time

```text
For a 09:00 arrival and 30 minutes travel, depart at 08:30.
```

**Full instruction:** Please plan my morning around a 9 AM appointment and reserve 30 minutes to travel there.

**Rationale:** The departure calculation matches the 9 AM arrival and 30-minute travel allowance.

## SC1-V1-SX1-F048-K-A2

**Prefix:** Please plan my morning around a 9 AM appointment

**Action:** Prepare the travel-duration field

```text
Travel duration field: 30 minutes; no appointment or departure time filled in.
```

**Full instruction:** Please plan my morning around a 9 AM appointment and reserve 30 minutes to travel there.

**Rationale:** The 30-minute travel field matches the final requirement.

## SC1-V1-SX1-F048-R-A2

**Prefix:** Please plan my morning around a 9 AM appointment

**Action:** Prepare the travel-duration field

```text
Travel duration field: 30 minutes; no appointment or departure time filled in.
```

**Full instruction:** Please plan my morning around a 9 AM appointment but move the appointment to 11 AM while retaining the 30-minute travel requirement.

**Rationale:** The 30-minute travel field is explicitly retained when the appointment moves to 11 AM.

## SC1-V1-SX1-F049-K-A1

**Prefix:** Please build a shopping list for vegetarian tacos

**Action:** Draft the protein ingredient

```text
One tin of beans; no meat.
```

**Full instruction:** Please build a shopping list for vegetarian tacos and include beans instead of meat.

**Rationale:** The beans ingredient satisfies the vegetarian taco request excluding meat.

## SC1-V1-SX1-F049-K-A2

**Prefix:** Please build a shopping list for vegetarian tacos

**Action:** Draft the shared taco ingredients

```text
Tortillas, tomatoes and lettuce; no protein ingredient selected.
```

**Full instruction:** Please build a shopping list for vegetarian tacos and include beans instead of meat.

**Rationale:** The shared taco ingredients remain usable when beans are chosen as the protein.

## SC1-V1-SX1-F049-R-A2

**Prefix:** Please build a shopping list for vegetarian tacos

**Action:** Draft the shared taco ingredients

```text
Tortillas, tomatoes and lettuce; no protein ingredient selected.
```

**Full instruction:** Please build a shopping list for vegetarian tacos but make beef tacos instead and omit beans.

**Rationale:** The shared taco ingredients remain usable when beef replaces beans.

## SC1-V1-SX1-F050-K-A1

**Prefix:** Please prioritize today's tasks with the client deadline first

**Action:** Stage the original ordering

```text
1. Client deadline; 2. Server incident; 3. File receipts.
```

**Full instruction:** Please prioritize today's tasks with the client deadline first and keep the client deadline at the top.

**Rationale:** The staged task ordering already satisfies the retained client-first priority.

## SC1-V1-SX1-F050-K-A2

**Prefix:** Please prioritize today's tasks with the client deadline first

**Action:** Extract today's task inventory

```text
Tasks due today: client deadline, server incident, file receipts; inventory has no priority ordering.
```

**Full instruction:** Please prioritize today's tasks with the client deadline first and keep the client deadline at the top.

**Rationale:** The task inventory supplies the unchanged tasks for client-first ordering.

## SC1-V1-SX1-F050-R-A2

**Prefix:** Please prioritize today's tasks with the client deadline first

**Action:** Extract today's task inventory

```text
Tasks due today: client deadline, server incident, file receipts; inventory has no priority ordering.
```

**Full instruction:** Please prioritize today's tasks with the client deadline first but put the server incident first and move the client deadline below it.

**Rationale:** The unordered inventory survives changing the task priorities.

## SC1-V2-SX1-F001-K-A1

**Prefix:** I need you to compare flights from Harborview to Eastport

**Action:** Retrieve two route-specific fares

```text
Harborview–Eastport 08:00, 120 credits; Harborview–Eastport 10:00, 150 credits.
```

**Full instruction:** I need you to compare flights from Harborview to Eastport and show the two listed morning options.

**Rationale:** The two morning Harborview–Eastport fares directly satisfy the final comparison request.

## SC1-V2-SX1-F002-K-A1

**Prefix:** I need you to find hotels near Maple Station

**Action:** Retrieve station-specific hotel cards

```text
Maple Lodge: 3-minute walk to Maple Station; Maple House: 5-minute walk.
```

**Full instruction:** I need you to find hotels near Maple Station and compare the two listed hotels by walking distance.

**Rationale:** The Maple hotel cards provide the two walking distances required for comparison.

## SC1-V2-SX1-F002-K-A2

**Prefix:** I need you to find hotels near Maple Station

**Action:** Stage a hotel comparison layout

```text
Columns: hotel name, distance to requested station, nightly price; no hotels filled in.
```

**Full instruction:** I need you to find hotels near Maple Station and compare the two listed hotels by walking distance.

**Rationale:** The station-distance hotel layout directly supports the requested walking-distance comparison.

## SC1-V2-SX1-F002-R-A2

**Prefix:** I need you to find hotels near Maple Station

**Action:** Stage a hotel comparison layout

```text
Columns: hotel name, distance to requested station, nightly price; no hotels filled in.
```

**Full instruction:** I need you to find hotels near Maple Station but use Pine Station instead and omit Maple Station hotels.

**Rationale:** The station-neutral hotel columns remain usable for Pine Station results.

## SC1-V2-SX1-F003-K-A1

**Prefix:** I need you to compare Friday car rentals at North Terminal

**Action:** Retrieve terminal-specific rental cards

```text
North Terminal: Compact A, 40 credits/day; Compact B, 45 credits/day. Both are North-only pickups.
```

**Full instruction:** I need you to compare Friday car rentals at North Terminal and keep pickup at North Terminal.

**Rationale:** The rental cards retain the required North Terminal pickup.

## SC1-V2-SX1-F003-K-A2

**Prefix:** I need you to compare Friday car rentals at North Terminal

**Action:** Prepare the comparison calculation

```text
Total rental cost = daily rate × number of days + disclosed fees; values remain unfilled.
```

**Full instruction:** I need you to compare Friday car rentals at North Terminal and keep pickup at North Terminal.

**Rationale:** The symbolic rental-cost calculation remains usable with North Terminal rates.

## SC1-V2-SX1-F003-R-A2

**Prefix:** I need you to compare Friday car rentals at North Terminal

**Action:** Prepare the comparison calculation

```text
Total rental cost = daily rate × number of days + disclosed fees; values remain unfilled.
```

**Full instruction:** I need you to compare Friday car rentals at North Terminal but pickup must be at South Terminal instead, with no North Terminal results.

**Rationale:** The terminal-neutral rental-cost expression remains useful at South Terminal.

## SC1-V2-SX1-F004-K-A1

**Prefix:** I need you to compare nonstop flights to Eastport

**Action:** Retrieve nonstop route cards

```text
Route N1: nonstop, 2 hours; route N2: nonstop, 3 hours. Neither includes a stop.
```

**Full instruction:** I need you to compare nonstop flights to Eastport and list only nonstop itineraries.

**Rationale:** Both retrieved itineraries satisfy the retained nonstop requirement.

## SC1-V2-SX1-F004-K-A2

**Prefix:** I need you to compare nonstop flights to Eastport

**Action:** Prepare the requested destination field

```text
Destination field: Eastport; no route or fare chosen.
```

**Full instruction:** I need you to compare nonstop flights to Eastport and list only nonstop itineraries.

**Rationale:** Eastport remains the destination for the requested nonstop options.

## SC1-V2-SX1-F004-R-A2

**Prefix:** I need you to compare nonstop flights to Eastport

**Action:** Prepare the requested destination field

```text
Destination field: Eastport; no route or fare chosen.
```

**Full instruction:** I need you to compare nonstop flights to Eastport but I now want only one-stop itineraries to Eastport.

**Rationale:** Eastport remains the destination despite changing the stop count.

## SC1-V2-SX1-F005-K-A1

**Prefix:** I need you to find Italian restaurants around Cedar Square

**Action:** Retrieve cuisine-specific restaurant cards

```text
Cedar Pasta: Italian, outdoor seating; Olive Room: Italian, outdoor seating; neither serves Thai cuisine.
```

**Full instruction:** I need you to find Italian restaurants around Cedar Square and choose places with outdoor seating.

**Rationale:** Both Italian restaurant cards already establish the requested outdoor seating.

## SC1-V2-SX1-F005-K-A2

**Prefix:** I need you to find Italian restaurants around Cedar Square

**Action:** Prepare the location field

```text
Search area: Cedar Square; cuisine, hours and price remain unfilled.
```

**Full instruction:** I need you to find Italian restaurants around Cedar Square and choose places with outdoor seating.

**Rationale:** Cedar Square remains the required restaurant location.

## SC1-V2-SX1-F005-R-A2

**Prefix:** I need you to find Italian restaurants around Cedar Square

**Action:** Prepare the location field

```text
Search area: Cedar Square; cuisine, hours and price remain unfilled.
```

**Full instruction:** I need you to find Italian restaurants around Cedar Square but change the cuisine to Thai and exclude Italian restaurants.

**Rationale:** The Cedar Square location field survives the cuisine change.

## SC1-V2-SX1-F006-K-A1

**Prefix:** I need you to find bakeries around Birch Park

**Action:** Retrieve bakery cards

```text
Birch Bake: bakery with coffee; Loaf House: bakery with coffee; neither is a pharmacy.
```

**Full instruction:** I need you to find bakeries around Birch Park that serve coffee, including the two listed options.

**Rationale:** Both bakery cards explicitly include coffee as required.

## SC1-V2-SX1-F006-K-A2

**Prefix:** I need you to find bakeries around Birch Park

**Action:** Prepare a bakery-only comparison layout

```text
Columns: bakery name, bread selection, pastry selection, coffee availability; four fixed headings.
```

**Full instruction:** I need you to find bakeries around Birch Park that serve coffee, including the two listed options.

**Rationale:** The bakery-specific layout includes coffee availability needed for the requested comparison.

## SC1-V2-SX1-F007-K-A1

**Prefix:** I need you to find gyms in Riverton that sell day passes

**Action:** Retrieve day-pass gym cards

```text
River Fit: day passes and sauna; North Fit: day passes and sauna. Both sell day passes.
```

**Full instruction:** I need you to find gyms in Riverton that sell day passes and prioritize day-pass gyms with a sauna.

**Rationale:** Both gym cards explicitly provide day passes and saunas as requested.

## SC1-V2-SX1-F007-K-A2

**Prefix:** I need you to find gyms in Riverton that sell day passes

**Action:** Prepare the location field

```text
City field: Riverton; membership type remains unfilled.
```

**Full instruction:** I need you to find gyms in Riverton that sell day passes and prioritize day-pass gyms with a sauna.

**Rationale:** The Riverton location field remains correct for finding day-pass gyms with saunas.

## SC1-V2-SX1-F007-R-A2

**Prefix:** I need you to find gyms in Riverton that sell day passes

**Action:** Prepare the location field

```text
City field: Riverton; membership type remains unfilled.
```

**Full instruction:** I need you to find gyms in Riverton that sell day passes but only consider members-only gyms that do not sell day passes.

**Rationale:** Riverton remains the search city after the membership constraint reverses.

## SC1-V2-SX1-F008-K-A1

**Prefix:** I need you to find pharmacies in Brookfield that are open now

**Action:** Retrieve open pharmacy cards

```text
Brook Pharmacy: open now, standalone; Elm Pharmacy: open now, standalone. Neither is hospital-based.
```

**Full instruction:** I need you to find pharmacies in Brookfield that are open now and omit hospital-based pharmacies.

**Rationale:** Both open standalone pharmacies pass the final hospital exclusion.

## SC1-V2-SX1-F008-K-A2

**Prefix:** I need you to find pharmacies in Brookfield that are open now

**Action:** Prepare the search time reference

```text
Fixture clock: Monday 14:00 local time; tomorrow resolves to Tuesday in this fixture.
```

**Full instruction:** I need you to find pharmacies in Brookfield that are open now and omit hospital-based pharmacies.

**Rationale:** The fixed local clock supplies the time reference needed to evaluate open-now pharmacy results.

## SC1-V2-SX1-F008-R-A2

**Prefix:** I need you to find pharmacies in Brookfield that are open now

**Action:** Prepare the search time reference

```text
Fixture clock: Monday 14:00 local time; tomorrow resolves to Tuesday in this fixture.
```

**Full instruction:** I need you to find pharmacies in Brookfield that are open now but only list hospital pharmacies that are closed now and open tomorrow.

**Rationale:** The fixture clock establishes both closed-now timing and tomorrow as Tuesday for the hospital-pharmacy search.

## SC1-V2-SX1-F009-K-A1

**Prefix:** I need you to research local robotic actuator manufacturers

**Action:** Retrieve manufacturer cards

```text
Aster Motion and Delta Drive manufacture robotic actuators locally; neither distributes other makers' parts.
```

**Full instruction:** I need you to research local robotic actuator manufacturers and retain the manufacturers while adding distributors separately.

**Rationale:** The manufacturer cards remain explicitly required alongside separately added distributors.

## SC1-V2-SX1-F009-K-A2

**Prefix:** I need you to research local robotic actuator manufacturers

**Action:** Prepare the component definition

```text
Robotic actuator: component that converts a control input into mechanical movement; no supplier selected.
```

**Full instruction:** I need you to research local robotic actuator manufacturers and retain the manufacturers while adding distributors separately.

**Rationale:** The actuator definition remains relevant when manufacturers and distributors are researched together.

## SC1-V2-SX1-F009-R-A2

**Prefix:** I need you to research local robotic actuator manufacturers

**Action:** Prepare the component definition

```text
Robotic actuator: component that converts a control input into mechanical movement; no supplier selected.
```

**Full instruction:** I need you to research local robotic actuator manufacturers but list distributors only and exclude manufacturers.

**Rationale:** The actuator definition remains relevant when researching distributors of the same component.

## SC1-V2-SX1-F010-K-A1

**Prefix:** I need you to compare 15-litre shoulder bags

**Action:** Retrieve bag specification cards

```text
Bag L: shoulder bag, 15 L, 0.5 kg; Bag M: shoulder bag, 15 L, 0.7 kg; neither converts to a backpack.
```

**Full instruction:** I need you to compare 15-litre shoulder bags and rank the two listed bags by lower weight.

**Rationale:** The two 15-litre shoulder-bag cards include the weights needed for ranking.

## SC1-V2-SX1-F010-K-A2

**Prefix:** I need you to compare 15-litre shoulder bags

**Action:** Prepare a weight-ranking routine

```text
Sort supplied product records by numeric weight_kg ascending; no records or capacity filter embedded.
```

**Full instruction:** I need you to compare 15-litre shoulder bags and rank the two listed bags by lower weight.

**Rationale:** The weight sort directly supports ranking the listed bags by lower weight.

## SC1-V2-SX1-F011-K-A1

**Prefix:** I need you to find brown faux-suede jackets with stand collars

**Action:** Retrieve jacket cards

```text
Jacket A: brown faux suede, stand collar, 120 credits; Jacket B: brown faux suede, stand collar, 150 credits.
```

**Full instruction:** I need you to find brown faux-suede jackets with stand collars and compare the listed options under 200 credits.

**Rationale:** Both jacket cards meet the material, color, collar and under-200-credit requirements.

## SC1-V2-SX1-F011-K-A2

**Prefix:** I need you to find brown faux-suede jackets with stand collars

**Action:** Stage a product comparison layout

```text
Columns: material, color, collar type, price; values unfilled.
```

**Full instruction:** I need you to find brown faux-suede jackets with stand collars and compare the listed options under 200 credits.

**Rationale:** The material, color, collar and price columns support the jacket comparison.

## SC1-V2-SX1-F011-R-A2

**Prefix:** I need you to find brown faux-suede jackets with stand collars

**Action:** Stage a product comparison layout

```text
Columns: material, color, collar type, price; values unfilled.
```

**Full instruction:** I need you to find brown faux-suede jackets with stand collars but use black cotton jackets with lapels instead and discard the original options.

**Rationale:** The unfilled material, color, collar and price columns suit the replacement jackets.

## SC1-V2-SX1-F012-K-A1

**Prefix:** I need you to compare robotics synthetic-data tools that support Engine R

**Action:** Retrieve tool compatibility cards

```text
Sim A and Sim B support Engine R only; neither supports Engine S.
```

**Full instruction:** I need you to compare robotics synthetic-data tools that support Engine R and keep Engine R support mandatory.

**Rationale:** Both compatibility cards meet the mandatory Engine R requirement.

## SC1-V2-SX1-F012-K-A2

**Prefix:** I need you to compare robotics synthetic-data tools that support Engine R

**Action:** Prepare a physics-evaluation checklist

```text
Check gravity, collision response, sensor noise and deterministic replay; no engine-specific commands.
```

**Full instruction:** I need you to compare robotics synthetic-data tools that support Engine R and keep Engine R support mandatory.

**Rationale:** The engine-neutral physics checklist can evaluate the required Engine R tools.

## SC1-V2-SX1-F012-R-A2

**Prefix:** I need you to compare robotics synthetic-data tools that support Engine R

**Action:** Prepare a physics-evaluation checklist

```text
Check gravity, collision response, sensor noise and deterministic replay; no engine-specific commands.
```

**Full instruction:** I need you to compare robotics synthetic-data tools that support Engine R but only consider tools for Engine S that do not support Engine R.

**Rationale:** The engine-neutral physics checklist remains usable when evaluating Engine S tools.

## SC1-V2-SX1-F013-K-A1

**Prefix:** I need you to find freestanding desk converters under 250 credits

**Action:** Retrieve converter cards

```text
Lift A: freestanding, 150 credits; Lift B: freestanding, 220 credits. Neither can be permanently mounted.
```

**Full instruction:** I need you to find freestanding desk converters under 250 credits and exclude permanently mounted converters.

**Rationale:** Both freestanding converters meet the price ceiling and exclude permanent mounting.

## SC1-V2-SX1-F013-K-A2

**Prefix:** I need you to find freestanding desk converters under 250 credits

**Action:** Prepare the price ceiling field

```text
Maximum price field: 250 credits; mounting type unfilled.
```

**Full instruction:** I need you to find freestanding desk converters under 250 credits and exclude permanently mounted converters.

**Rationale:** The 250-credit ceiling remains a required converter filter.

## SC1-V2-SX1-F013-R-A2

**Prefix:** I need you to find freestanding desk converters under 250 credits

**Action:** Prepare the price ceiling field

```text
Maximum price field: 250 credits; mounting type unfilled.
```

**Full instruction:** I need you to find freestanding desk converters under 250 credits but only show permanently mounted converters and discard freestanding ones.

**Rationale:** The 250-credit ceiling remains valid for permanently mounted converters.

## SC1-V2-SX1-F014-K-A1

**Prefix:** I need you to find a 30-minute meeting for Sam and me on Tuesday

**Action:** Read Tuesday availability

```text
Sam and requester both free Tuesday 14:00–14:30 and 15:00–15:30. No Wednesday availability included.
```

**Full instruction:** I need you to find a 30-minute meeting for Sam and me on Tuesday and use either of the two listed Tuesday slots.

**Rationale:** The two Tuesday slots exactly supply the requested scheduling options.

## SC1-V2-SX1-F014-R-A2

**Prefix:** I need you to find a 30-minute meeting for Sam and me on Tuesday

**Action:** Stage a Wednesday calendar event

```text
Unsent event object: attendees Sam and requester, duration 30 minutes, day Wednesday; no time set.
```

**Full instruction:** I need you to find a 30-minute meeting for Sam and me on Tuesday but switch the meeting to Wednesday and ignore Tuesday availability.

**Rationale:** The Wednesday event object matches the final meeting day, participants and duration.

## SC1-V2-SX1-F015-K-A1

**Prefix:** I need you to check whether my dentist can see me on Friday

**Action:** Read Friday availability

```text
The fixture dentist has no Friday openings; no Monday availability included.
```

**Full instruction:** I need you to check whether my dentist can see me on Friday and keep my existing appointment if Friday has no openings.

**Rationale:** The absence of Friday openings determines that the existing appointment should be kept.

## SC1-V2-SX1-F015-K-A2

**Prefix:** I need you to check whether my dentist can see me on Friday

**Action:** Retrieve the existing appointment

```text
Current appointment: Wednesday 11:00, dentist Dr Vale, appointment ID D17.
```

**Full instruction:** I need you to check whether my dentist can see me on Friday and keep my existing appointment if Friday has no openings.

**Rationale:** The existing appointment record identifies the fallback required if Friday is unavailable.

## SC1-V2-SX1-F015-R-A2

**Prefix:** I need you to check whether my dentist can see me on Friday

**Action:** Retrieve the existing appointment

```text
Current appointment: Wednesday 11:00, dentist Dr Vale, appointment ID D17.
```

**Full instruction:** I need you to check whether my dentist can see me on Friday but check Monday instead and ignore Friday openings, keeping my existing appointment as fallback.

**Rationale:** The current appointment record identifies the fallback retained after switching to Monday.

## SC1-V2-SX1-F016-K-A1

**Prefix:** I need you to find team meeting slots this week after 10 AM

**Action:** Read afternoon team availability

```text
Whole team free Thursday 13:00–13:30 and Friday 14:00–14:30; no morning data included.
```

**Full instruction:** I need you to find team meeting slots this week after 10 AM and show the two listed afternoon slots.

**Rationale:** The two afternoon availability records are precisely the requested choices.

## SC1-V2-SX1-F016-K-A2

**Prefix:** I need you to find team meeting slots this week after 10 AM

**Action:** Prepare the participant list

```text
Participants: Sam, Jo and requester; no time selected.
```

**Full instruction:** I need you to find team meeting slots this week after 10 AM and show the two listed afternoon slots.

**Rationale:** The participant list remains reusable for the required team scheduling search.

## SC1-V2-SX1-F016-R-A2

**Prefix:** I need you to find team meeting slots this week after 10 AM

**Action:** Prepare the participant list

```text
Participants: Sam, Jo and requester; no time selected.
```

**Full instruction:** I need you to find team meeting slots this week after 10 AM but only consider slots before 10 AM this week.

**Rationale:** The participant list can be reused unchanged in the before-10-AM search.

## SC1-V2-SX1-F017-K-A1

**Prefix:** I need you to prepare a report reminder for tomorrow morning

**Action:** Stage a morning reminder

```text
Unsent reminder: title Submit report, day tomorrow, time 09:00.
```

**Full instruction:** I need you to prepare a report reminder for tomorrow morning and set its time to 9 AM.

**Rationale:** The reminder object already specifies Submit report tomorrow at 9 AM.

## SC1-V2-SX1-F017-K-A2

**Prefix:** I need you to prepare a report reminder for tomorrow morning

**Action:** Prepare the reminder text

```text
Reminder title: Submit report; date and time unfilled.
```

**Full instruction:** I need you to prepare a report reminder for tomorrow morning and set its time to 9 AM.

**Rationale:** The Submit report title remains valid when 9 AM is filled in.

## SC1-V2-SX1-F017-R-A2

**Prefix:** I need you to prepare a report reminder for tomorrow morning

**Action:** Prepare the reminder text

```text
Reminder title: Submit report; date and time unfilled.
```

**Full instruction:** I need you to prepare a report reminder for tomorrow morning but change it to tomorrow evening at 7 PM.

**Rationale:** The reminder title survives the change to tomorrow evening.

## SC1-V2-SX1-F018-K-A1

**Prefix:** I need you to draft a reply thanking Morgan for the introduction

**Action:** Draft the thank-you sentence

```text
Thank you for making the introduction, Morgan.
```

**Full instruction:** I need you to draft a reply thanking Morgan for the introduction and offer to provide more information.

**Rationale:** The thank-you sentence remains required when an offer of further information is added.

## SC1-V2-SX1-F018-K-A2

**Prefix:** I need you to draft a reply thanking Morgan for the introduction

**Action:** Draft an offer sentence

```text
I would be happy to provide any additional information you need.
```

**Full instruction:** I need you to draft a reply thanking Morgan for the introduction and offer to provide more information.

**Rationale:** The offer sentence directly satisfies the request to offer more information.

## SC1-V2-SX1-F019-K-A1

**Prefix:** I need you to draft a team update saying the build is delayed

**Action:** Draft the status sentence

```text
The build is delayed; we are still investigating the cause.
```

**Full instruction:** I need you to draft a team update saying the build is delayed and keep the cause neutral because it is not yet known.

**Rationale:** The delay sentence leaves the cause unresolved as required.

## SC1-V2-SX1-F019-K-A2

**Prefix:** I need you to draft a team update saying the build is delayed

**Action:** Stage a neutral update heading

```text
Heading: Build status update; no status claim or cause included.
```

**Full instruction:** I need you to draft a team update saying the build is delayed and keep the cause neutral because it is not yet known.

**Rationale:** The neutral build-status heading can accompany the delay update without asserting a cause.

## SC1-V2-SX1-F019-R-A2

**Prefix:** I need you to draft a team update saying the build is delayed

**Action:** Stage a neutral update heading

```text
Heading: Build status update; no status claim or cause included.
```

**Full instruction:** I need you to draft a team update saying the build is delayed but the build is on schedule, so report that and do not mention a delay.

**Rationale:** The neutral build-status heading remains valid when the build is on schedule.

## SC1-V2-SX1-F020-K-A1

**Prefix:** I need you to draft a message declining dinner tonight

**Action:** Draft the decline sentence

```text
I cannot make dinner tonight.
```

**Full instruction:** I need you to draft a message declining dinner tonight and suggest meeting next weekend.

**Rationale:** The refusal sentence remains usable before the proposed next-weekend alternative.

## SC1-V2-SX1-F020-K-A2

**Prefix:** I need you to draft a message declining dinner tonight

**Action:** Draft the alternative-date sentence

```text
Would you like to meet next weekend instead?
```

**Full instruction:** I need you to draft a message declining dinner tonight and suggest meeting next weekend.

**Rationale:** The next-weekend invitation exactly supplies the requested alternative date.

## SC1-V2-SX1-F021-K-A1

**Prefix:** I need you to draft a refund approval message

**Action:** Draft the approval sentence

```text
Your refund has been approved.
```

**Full instruction:** I need you to draft a refund approval message and avoid promising a payment date.

**Rationale:** The refund-approval sentence states approval without promising a payment date.

## SC1-V2-SX1-F021-K-A2

**Prefix:** I need you to draft a refund approval message

**Action:** Stage an approval-specific reply template

```text
Subject: Refund approved. Closing: Thank you for your patience. Body unfilled.
```

**Full instruction:** I need you to draft a refund approval message and avoid promising a payment date.

**Rationale:** The approval subject and closing remain valid and promise no payment date.

## SC1-V2-SX1-F022-K-A1

**Prefix:** I need you to find peer-reviewed papers about hidden-state probing

**Action:** Retrieve peer-reviewed fixture records

```text
Paper P and Paper Q: peer-reviewed hidden-state probing papers in the synthetic catalogue; no technical reports included.
```

**Full instruction:** I need you to find peer-reviewed papers about hidden-state probing and use only peer-reviewed sources.

**Rationale:** The two peer-reviewed probing records satisfy the final source restriction.

## SC1-V2-SX1-F022-K-A2

**Prefix:** I need you to find peer-reviewed papers about hidden-state probing

**Action:** Prepare the topic search terms

```text
Terms: hidden-state probing, representation analysis; no publication-type filter.
```

**Full instruction:** I need you to find peer-reviewed papers about hidden-state probing and use only peer-reviewed sources.

**Rationale:** The probing search terms remain usable with the required peer-reviewed source filter.

## SC1-V2-SX1-F022-R-A2

**Prefix:** I need you to find peer-reviewed papers about hidden-state probing

**Action:** Prepare the topic search terms

```text
Terms: hidden-state probing, representation analysis; no publication-type filter.
```

**Full instruction:** I need you to find peer-reviewed papers about hidden-state probing but use only non-peer-reviewed technical reports about hidden-state probing.

**Rationale:** The source-neutral probing terms remain usable for technical-report retrieval.

## SC1-V2-SX1-F023-K-A1

**Prefix:** I need you to find version 3 documentation for Library L

**Action:** Retrieve versioned documentation

```text
Official Library L version 3: old_connect(endpoint) is the connection entry point. This fixture marks it removed in version 4.
```

**Full instruction:** I need you to find version 3 documentation for Library L and use only the official version 3 material.

**Rationale:** The official version 3 connection documentation is exactly the retained source requirement.

## SC1-V2-SX1-F023-K-A2

**Prefix:** I need you to find version 3 documentation for Library L

**Action:** Retrieve the official documentation index URL

```text
Fixture URL: https://library-l.example/docs/ ; index lists version 3 and version 4.
```

**Full instruction:** I need you to find version 3 documentation for Library L and use only the official version 3 material.

**Rationale:** The official index directly locates the required version 3 material.

## SC1-V2-SX1-F023-R-A2

**Prefix:** I need you to find version 3 documentation for Library L

**Action:** Retrieve the official documentation index URL

```text
Fixture URL: https://library-l.example/docs/ ; index lists version 3 and version 4.
```

**Full instruction:** I need you to find version 3 documentation for Library L but use version 4 instead and exclude all version 3 documentation.

**Rationale:** The official index contains version 4 and remains usable after the version change.

## SC1-V2-SX1-F024-K-A1

**Prefix:** I need you to compare Acme's revenue in its two annual releases

**Action:** Extract Acme revenue figures

```text
Acme fixture: prior year revenue 10 million credits; current year 12 million credits.
```

**Full instruction:** I need you to compare Acme's revenue in its two annual releases and report company-stated actual revenue only.

**Rationale:** The two Acme revenue values are the requested actual figures.

## SC1-V2-SX1-F025-K-A1

**Prefix:** I need you to find primary rules for Region A consumer AI systems

**Action:** Retrieve jurisdiction-specific rule cards

```text
Rule A1 and Rule A2: synthetic Region A consumer-AI rules, with no applicability in Region B.
```

**Full instruction:** I need you to find primary rules for Region A consumer AI systems and keep Region A as the main jurisdiction.

**Rationale:** The Region A rule cards match the retained primary jurisdiction.

## SC1-V2-SX1-F025-K-A2

**Prefix:** I need you to find primary rules for Region A consumer AI systems

**Action:** Stage a legal-source comparison layout

```text
Columns: jurisdiction, issuing authority, effective date, provision; no legal claims filled in.
```

**Full instruction:** I need you to find primary rules for Region A consumer AI systems and keep Region A as the main jurisdiction.

**Rationale:** The jurisdiction-neutral legal-source columns remain usable for Region A rules.

## SC1-V2-SX1-F025-R-A2

**Prefix:** I need you to find primary rules for Region A consumer AI systems

**Action:** Stage a legal-source comparison layout

```text
Columns: jurisdiction, issuing authority, effective date, provision; no legal claims filled in.
```

**Full instruction:** I need you to find primary rules for Region A consumer AI systems but use Region B rules only and exclude Region A rules.

**Rationale:** The blank jurisdiction, authority, date and provision columns can compare Region B sources unchanged.

## SC1-V2-SX1-F026-K-A1

**Prefix:** I need you to compare small open-weight reasoning models

**Action:** Collect vendor-only benchmark claims

```text
Vendor card: Model K claims 80 points and Model J claims 85 points; neither claim is independently reproduced.
```

**Full instruction:** I need you to compare small open-weight reasoning models and flag vendor-only scores as unverified rather than treating them as evidence.

**Rationale:** The vendor cards can be retained as explicitly unverified claims rather than comparison evidence.

## SC1-V2-SX1-F026-K-A2

**Prefix:** I need you to compare small open-weight reasoning models

**Action:** Collect independent fixture benchmark records

```text
Independent lab fixture: Model K 70 points, Model J 72 points, same test and evaluation settings; both small and open-weight.
```

**Full instruction:** I need you to compare small open-weight reasoning models and flag vendor-only scores as unverified rather than treating them as evidence.

**Rationale:** The independent scores remain valid evidence under the vendor-claim warning requirement.

## SC1-V2-SX1-F026-R-A2

**Prefix:** I need you to compare small open-weight reasoning models

**Action:** Collect independent fixture benchmark records

```text
Independent lab fixture: Model K 70 points, Model J 72 points, same test and evaluation settings; both small and open-weight.
```

**Full instruction:** I need you to compare small open-weight reasoning models but include only independently reproduced scores and omit vendor-only claims entirely.

**Rationale:** The independent same-setting scores meet the final independently reproduced evidence requirement.

## SC1-V2-SX1-F027-K-A1

**Prefix:** I need you to calculate a 7 percent downside scenario for a 100-credit index

**Action:** Calculate the requested scenario

```text
100 × (1 − 0.07) = 93 credits; only the 7% result retained.
```

**Full instruction:** I need you to calculate a 7 percent downside scenario for a 100-credit index and show the hypothetical level without making a trade.

**Rationale:** The 93-credit result exactly answers the retained hypothetical 7 percent decline.

## SC1-V2-SX1-F027-K-A2

**Prefix:** I need you to calculate a 7 percent downside scenario for a 100-credit index

**Action:** Prepare the scenario formula

```text
Scenario level = starting level × (1 − decline_fraction); no numeric assumptions embedded.
```

**Full instruction:** I need you to calculate a 7 percent downside scenario for a 100-credit index and show the hypothetical level without making a trade.

**Rationale:** The symbolic downside expression supports the requested seven-percent calculation without executing a trade.

## SC1-V2-SX1-F027-R-A2

**Prefix:** I need you to calculate a 7 percent downside scenario for a 100-credit index

**Action:** Prepare the scenario formula

```text
Scenario level = starting level × (1 − decline_fraction); no numeric assumptions embedded.
```

**Full instruction:** I need you to calculate a 7 percent downside scenario for a 100-credit index but use a 12 percent decline instead and omit the 7 percent case.

**Rationale:** The symbolic formula remains valid after changing the decline to 12 percent.

## SC1-V2-SX1-F028-K-A1

**Prefix:** I need you to calculate budget variance from my supplied table

**Action:** Compute category variances

```text
Fixture variances: supplies +20 credits, travel +5 credits, meals −10 credits; positive means overspend.
```

**Full instruction:** I need you to calculate budget variance from my supplied table and identify the largest overspend.

**Rationale:** The category variances identify supplies as the largest overspend.

## SC1-V2-SX1-F028-K-A2

**Prefix:** I need you to calculate budget variance from my supplied table

**Action:** Aggregate actual category totals

```text
Fixture actuals: supplies 120 credits, travel 85 credits, meals 40 credits; source-table sums retained.
```

**Full instruction:** I need you to calculate budget variance from my supplied table and identify the largest overspend.

**Rationale:** The retained category actuals can be reused as inputs for determining overspend.

## SC1-V2-SX1-F028-R-A2

**Prefix:** I need you to calculate budget variance from my supplied table

**Action:** Aggregate actual category totals

```text
Fixture actuals: supplies 120 credits, travel 85 credits, meals 40 credits; source-table sums retained.
```

**Full instruction:** I need you to calculate budget variance from my supplied table but show actual category totals only, without calculating or reporting variances.

**Rationale:** The aggregated actuals are precisely the requested category totals.

## SC1-V2-SX1-F029-K-A1

**Prefix:** I need you to compare current holdings with the start-of-month snapshot

**Action:** Calculate start-of-month concentration

```text
Start-of-month fixture: asset A 60%, asset B 40%; no other date included.
```

**Full instruction:** I need you to compare current holdings with the start-of-month snapshot and report concentration changes for those two snapshots.

**Rationale:** The start-of-month percentages supply the required baseline for concentration changes.

## SC1-V2-SX1-F029-K-A2

**Prefix:** I need you to compare current holdings with the start-of-month snapshot

**Action:** Calculate current concentration

```text
Current fixture: asset A 50%, asset B 50%; values unchanged across comparisons.
```

**Full instruction:** I need you to compare current holdings with the start-of-month snapshot and report concentration changes for those two snapshots.

**Rationale:** The current 50/50 allocation remains one of the required concentration snapshots.

## SC1-V2-SX1-F029-R-A2

**Prefix:** I need you to compare current holdings with the start-of-month snapshot

**Action:** Calculate current concentration

```text
Current fixture: asset A 50%, asset B 50%; values unchanged across comparisons.
```

**Full instruction:** I need you to compare current holdings with the start-of-month snapshot but compare current holdings with the start-of-year snapshot instead and ignore start-of-month holdings.

**Rationale:** The current 50/50 concentration remains explicitly unchanged when the comparison baseline changes to start of year.

## SC1-V2-SX1-F030-K-A1

**Prefix:** I need you to calculate breakeven for my debit spread using the supplied values

**Action:** Calculate the original breakeven

```text
For this fixture's specified call debit spread: 100 + 5 = 105 credits.
```

**Full instruction:** I need you to calculate breakeven for my debit spread using the supplied values and use the supplied 5-credit debit and 100-credit lower strike.

**Rationale:** The 105-credit breakeven is correct for the retained 100-credit strike and 5-credit debit.

## SC1-V2-SX1-F030-K-A2

**Prefix:** I need you to calculate breakeven for my debit spread using the supplied values

**Action:** Prepare the symbolic breakeven expression

```text
For the specified call debit spread: lower_strike + net_debit; no prices filled in.
```

**Full instruction:** I need you to calculate breakeven for my debit spread using the supplied values and use the supplied 5-credit debit and 100-credit lower strike.

**Rationale:** The symbolic call-spread breakeven expression accepts the supplied debit and strike unchanged.

## SC1-V2-SX1-F030-R-A2

**Prefix:** I need you to calculate breakeven for my debit spread using the supplied values

**Action:** Prepare the symbolic breakeven expression

```text
For the specified call debit spread: lower_strike + net_debit; no prices filled in.
```

**Full instruction:** I need you to calculate breakeven for my debit spread using the supplied values but correct the debit to 8 credits while keeping the lower strike at 100 credits.

**Rationale:** The symbolic formula remains correct with the revised 8-credit debit.

## SC1-V2-SX1-F031-K-A1

**Prefix:** I need you to write a Python function that counts ERROR lines in the supplied log

**Action:** Stage an ERROR-counting function

```text
def count_lines(lines): return sum(line.startswith('ERROR ') for line in lines)
```

**Full instruction:** I need you to write a Python function that counts ERROR lines in the supplied log and return the count without changing the file.

**Rationale:** The function counts ERROR-prefixed lines without modifying the log.

## SC1-V2-SX1-F031-K-A2

**Prefix:** I need you to write a Python function that counts ERROR lines in the supplied log

**Action:** Stage a log-reading helper

```text
def read_lines(path):
    with open(path, encoding='utf-8') as f:
        return f.read().splitlines()
```

**Full instruction:** I need you to write a Python function that counts ERROR lines in the supplied log and return the count without changing the file.

**Rationale:** The read-only log helper supplies lines for ERROR counting without changing the file.

## SC1-V2-SX1-F031-R-A2

**Prefix:** I need you to write a Python function that counts ERROR lines in the supplied log

**Action:** Stage a log-reading helper

```text
def read_lines(path):
    with open(path, encoding='utf-8') as f:
        return f.read().splitlines()
```

**Full instruction:** I need you to write a Python function that counts ERROR lines in the supplied log but count WARN lines instead and do not count ERROR lines.

**Rationale:** The log-reading helper remains usable because it does not select ERROR or WARN lines.

## SC1-V2-SX1-F032-K-A1

**Prefix:** I need you to inspect the client timeout path without changing the code

**Action:** Collect a timeout observation

```text
Fixture client.py line 8: DEFAULT_TIMEOUT = 5; request() passes this constant as its timeout argument.
```

**Full instruction:** I need you to inspect the client timeout path without changing the code and identify where its five-second timeout is set.

**Rationale:** The observation directly identifies where the five-second timeout is set.

## SC1-V2-SX1-F032-R-A1

**Prefix:** I need you to inspect the client timeout path without changing the code

**Action:** Collect a timeout observation

```text
Fixture client.py line 8: DEFAULT_TIMEOUT = 5; request() passes this constant as its timeout argument.
```

**Full instruction:** I need you to inspect the client timeout path without changing the code but modify the default timeout to ten seconds instead of producing an inspection report.

**Rationale:** The constant location and request linkage identify where to make the timeout change.

## SC1-V2-SX1-F032-R-A2

**Prefix:** I need you to inspect the client timeout path without changing the code

**Action:** Stage a ten-second timeout patch

```text
Unapplied patch replaces DEFAULT_TIMEOUT = 5 with DEFAULT_TIMEOUT = 10; no other edits.
```

**Full instruction:** I need you to inspect the client timeout path without changing the code but modify the default timeout to ten seconds instead of producing an inspection report.

**Rationale:** The staged patch implements exactly the newly requested ten-second default.

## SC1-V2-SX1-F033-K-A1

**Prefix:** I need you to refactor the add function while preserving its public name and behavior

**Action:** Stage the preserving refactor

```text
Replacement definition: def add(a, b): return a + b; public symbol remains add.
```

**Full instruction:** I need you to refactor the add function while preserving its public name and behavior and keep its existing callers compatible.

**Rationale:** The staged add definition preserves the required public name and addition behavior.

## SC1-V2-SX1-F033-K-A2

**Prefix:** I need you to refactor the add function while preserving its public name and behavior

**Action:** Stage addition behavior tests

```text
Assertions: operation(2, 3) == 5; operation(-1, 1) == 0; operation supplied by the test harness, not hardcoded to a name.
```

**Full instruction:** I need you to refactor the add function while preserving its public name and behavior and keep its existing callers compatible.

**Rationale:** The addition behavior assertions remain usable with existing callers preserved.

## SC1-V2-SX1-F033-R-A2

**Prefix:** I need you to refactor the add function while preserving its public name and behavior

**Action:** Stage addition behavior tests

```text
Assertions: operation(2, 3) == 5; operation(-1, 1) == 0; operation supplied by the test harness, not hardcoded to a name.
```

**Full instruction:** I need you to refactor the add function while preserving its public name and behavior but rename the public function to total and update callers to use total.

**Rationale:** The name-independent assertions still test addition after the public function is renamed.

## SC1-V2-SX1-F034-K-A1

**Prefix:** I need you to add malformed-JSON tests to the parser

**Action:** Stage malformed-input test cases

```text
Inputs: an unmatched opening brace, an unfinished numeric array, and an object with an unquoted key; expected outcome for each: parse error.
```

**Full instruction:** I need you to add malformed-JSON tests to the parser and keep this work limited to correctness tests.

**Rationale:** The malformed inputs and expected errors directly support the required correctness tests.

## SC1-V2-SX1-F034-K-A2

**Prefix:** I need you to add malformed-JSON tests to the parser

**Action:** Prepare a correctness-test report layout

```text
Columns: malformed input, expected error, observed error; no timing column.
```

**Full instruction:** I need you to add malformed-JSON tests to the parser and keep this work limited to correctness tests.

**Rationale:** The malformed-input and error columns support the required correctness-test report.

## SC1-V2-SX1-F035-K-A1

**Prefix:** I need you to rewrite this note for executives while preserving its numbers

**Action:** Draft the executive summary

```text
The project will take 12 weeks with a budget of 30 credits; the decision needed is approval to proceed.
```

**Full instruction:** I need you to rewrite this note for executives while preserving its numbers and keep both the 12-week duration and 30-credit budget.

**Rationale:** The executive summary preserves the required 12-week duration and 30-credit budget.

## SC1-V2-SX1-F035-K-A2

**Prefix:** I need you to rewrite this note for executives while preserving its numbers

**Action:** Extract the unchanged duration

```text
Duration fact from the supplied fixture note: 12 weeks.
```

**Full instruction:** I need you to rewrite this note for executives while preserving its numbers and keep both the 12-week duration and 30-credit budget.

**Rationale:** The extracted 12-week duration is explicitly retained in the rewrite.

## SC1-V2-SX1-F035-R-A2

**Prefix:** I need you to rewrite this note for executives while preserving its numbers

**Action:** Extract the unchanged duration

```text
Duration fact from the supplied fixture note: 12 weeks.
```

**Full instruction:** I need you to rewrite this note for executives while preserving its numbers but make it a technical note for engineers and correct the budget to 40 credits.

**Rationale:** The 12-week fact survives the engineering-audience and budget changes.

## SC1-V2-SX1-F036-K-A1

**Prefix:** I need you to summarize the main report without using the appendix

**Action:** Extract main-report finding

```text
Main report fixture: trial A completed in 8 days with 2 defects. This fact appears only in the main report.
```

**Full instruction:** I need you to summarize the main report without using the appendix and use only the main report findings.

**Rationale:** The main-report-only summary can reuse the extracted main-report finding.

## SC1-V2-SX1-F036-K-A2

**Prefix:** I need you to summarize the main report without using the appendix

**Action:** Stage a summary layout

```text
Headings: objective, evidence, limitations; no source facts populated.
```

**Full instruction:** I need you to summarize the main report without using the appendix and use only the main report findings.

**Rationale:** The source-neutral summary headings remain usable for the main report.

## SC1-V2-SX1-F036-R-A2

**Prefix:** I need you to summarize the main report without using the appendix

**Action:** Stage a summary layout

```text
Headings: objective, evidence, limitations; no source facts populated.
```

**Full instruction:** I need you to summarize the main report without using the appendix but summarize the appendix only and ignore the main report.

**Rationale:** The unpopulated objective, evidence and limitations headings can organize an appendix summary unchanged.

## SC1-V2-SX1-F037-K-A1

**Prefix:** I need you to draft a proposal from these notes and leave pricing undecided

**Action:** Stage the pricing section

```text
Pricing: TBD. No numeric quote is included.
```

**Full instruction:** I need you to draft a proposal from these notes and leave pricing undecided and mark pricing as TBD.

**Rationale:** The TBD pricing section exactly matches the required undecided price.

## SC1-V2-SX1-F037-K-A2

**Prefix:** I need you to draft a proposal from these notes and leave pricing undecided

**Action:** Stage the scope section

```text
Scope: deliver one dashboard and its handover guide; no price or schedule included.
```

**Full instruction:** I need you to draft a proposal from these notes and leave pricing undecided and mark pricing as TBD.

**Rationale:** The dashboard and handover scope survives adding a separate TBD price section.

## SC1-V2-SX1-F037-R-A2

**Prefix:** I need you to draft a proposal from these notes and leave pricing undecided

**Action:** Stage the scope section

```text
Scope: deliver one dashboard and its handover guide; no price or schedule included.
```

**Full instruction:** I need you to draft a proposal from these notes and leave pricing undecided but quote the supplied fixed price of 500 credits and remove TBD pricing.

**Rationale:** The dashboard scope remains valid alongside a separate 500-credit price section.

## SC1-V2-SX1-F038-K-A1

**Prefix:** I need you to compare these two resumes without recommending a candidate

**Action:** Extract resume differences

```text
Resume A lists Python and 3 years of experience; Resume B lists Java and 5 years. These are fixture facts.
```

**Full instruction:** I need you to compare these two resumes without recommending a candidate and list differences only.

**Rationale:** The extracted skills and experience supply the requested resume differences.

## SC1-V2-SX1-F038-R-A1

**Prefix:** I need you to compare these two resumes without recommending a candidate

**Action:** Extract resume differences

```text
Resume A lists Python and 3 years of experience; Resume B lists Java and 5 years. These are fixture facts.
```

**Full instruction:** I need you to compare these two resumes without recommending a candidate but recommend a candidate using the same resumes and explain the choice.

**Rationale:** The resume skills and experience remain evidence for explaining the candidate recommendation.

## SC1-V2-SX1-F039-K-A1

**Prefix:** I need you to stage the living-room lights at 30 percent brightness

**Action:** Stage the requested lighting command

```text
Unapplied command: room=living_room, brightness=30, color=unchanged.
```

**Full instruction:** I need you to stage the living-room lights at 30 percent brightness while preserving their current color, without applying changes.

**Rationale:** The unapplied living-room command sets 30-percent brightness and preserves color as requested.

## SC1-V2-SX1-F039-K-A2

**Prefix:** I need you to stage the living-room lights at 30 percent brightness

**Action:** Read living-room light state

```text
Living-room fixture: brightness 80%, color warm white. No bedroom state included.
```

**Full instruction:** I need you to stage the living-room lights at 30 percent brightness while preserving their current color, without applying changes.

**Rationale:** The warm-white state supplies the color to preserve while changing living-room brightness.

## SC1-V2-SX1-F040-K-A2

**Prefix:** I need you to stage a 70 F thermostat setting for tonight

**Action:** Read current thermostat setting

```text
Current fixture thermostat setting: 70 F; reading retained for conditional comparison.
```

**Full instruction:** I need you to stage a 70 F thermostat setting for tonight only if the current setting differs from 70 F; do not apply it.

**Rationale:** The current 70 F setting resolves the condition against staging a change.

## SC1-V2-SX1-F040-R-A2

**Prefix:** I need you to stage a 70 F thermostat setting for tonight

**Action:** Read current thermostat setting

```text
Current fixture thermostat setting: 70 F; reading retained for conditional comparison.
```

**Full instruction:** I need you to stage a 70 F thermostat setting for tonight but stage 68 F instead, only if the current setting differs from 68 F; do not apply it.

**Rationale:** The current 70 F reading establishes that the proposed 68 F target differs from the current setting.

## SC1-V2-SX1-F041-K-A1

**Prefix:** I need you to prepare to lock the back door after I leave

**Action:** Read back-door sensor

```text
Back-door fixture sensor: closed and unlocked; timestamp belongs to the fixed scenario snapshot.
```

**Full instruction:** I need you to prepare to lock the back door after I leave and check the back-door sensor before staging anything.

**Rationale:** The back-door sensor reading directly satisfies the required preliminary check.

## SC1-V2-SX1-F041-R-A2

**Prefix:** I need you to prepare to lock the back door after I leave

**Action:** Stage a departure trigger definition

```text
Trigger: requester_departed becomes true; no door or lock operation attached.
```

**Full instruction:** I need you to prepare to lock the back door after I leave but prepare to lock the front door instead and do not use the back-door sensor reading.

**Rationale:** The door-independent departure trigger remains applicable to locking the front door.

## SC1-V2-SX1-F042-K-A1

**Prefix:** I need you to stage a kitchen-only vacuum run

**Action:** Stage the room-specific cleaning plan

```text
Unapplied vacuum plan: include kitchen; exclude bedroom, hall and living room.
```

**Full instruction:** I need you to stage a kitchen-only vacuum run and keep all other rooms excluded; do not start cleaning.

**Rationale:** The unapplied kitchen-only plan retains every required room exclusion.

## SC1-V2-SX1-F042-K-A2

**Prefix:** I need you to stage a kitchen-only vacuum run

**Action:** Read vacuum battery state

```text
Fixture vacuum battery: 90%; sufficient for either single-room run in this scenario.
```

**Full instruction:** I need you to stage a kitchen-only vacuum run and keep all other rooms excluded; do not start cleaning.

**Rationale:** The sufficient battery state remains usable when preparing the kitchen-only plan.

## SC1-V2-SX1-F042-R-A2

**Prefix:** I need you to stage a kitchen-only vacuum run

**Action:** Read vacuum battery state

```text
Fixture vacuum battery: 90%; sufficient for either single-room run in this scenario.
```

**Full instruction:** I need you to stage a kitchen-only vacuum run but stage a bedroom-only run instead and discard the kitchen plan.

**Rationale:** The battery reading establishes sufficient capacity for the replacement bedroom run.

## SC1-V2-SX1-F043-K-A1

**Prefix:** I need you to find robotics documentaries

**Action:** Retrieve robotics documentary cards

```text
Robot Workshop: robotics, 60 minutes; Machine Motion: robotics, 75 minutes; neither covers astronomy.
```

**Full instruction:** I need you to find robotics documentaries and include only titles under 90 minutes.

**Rationale:** Both robotics documentaries satisfy the stated under-90-minute limit.

## SC1-V2-SX1-F043-K-A2

**Prefix:** I need you to find robotics documentaries

**Action:** Prepare a runtime filter

```text
Keep input records whose runtime_minutes < 90; no topic filter or titles embedded.
```

**Full instruction:** I need you to find robotics documentaries and include only titles under 90 minutes.

**Rationale:** The runtime predicate implements the explicit under-90-minute limit.

## SC1-V2-SX1-F044-K-A1

**Prefix:** I need you to build an upbeat instrumental jazz playlist

**Action:** Collect instrumental track cards

```text
Track A and Track B: upbeat jazz, instrumental; no vocals in either fixture track.
```

**Full instruction:** I need you to build an upbeat instrumental jazz playlist and exclude vocal tracks.

**Rationale:** The upbeat instrumental jazz tracks satisfy the explicit vocal exclusion.

## SC1-V2-SX1-F044-K-A2

**Prefix:** I need you to build an upbeat instrumental jazz playlist

**Action:** Prepare a vocal-track exclusion predicate

```text
Keep a supplied track only when has_vocals is false; no titles embedded.
```

**Full instruction:** I need you to build an upbeat instrumental jazz playlist and exclude vocal tracks.

**Rationale:** The vocal-exclusion predicate directly implements the instrumental-only requirement.

## SC1-V2-SX1-F045-K-A1

**Prefix:** I need you to choose a non-horror movie under two hours for tonight

**Action:** Retrieve movie cards

```text
Film A: comedy, 90 minutes; Film B: drama, 105 minutes; both explicitly not horror.
```

**Full instruction:** I need you to choose a non-horror movie under two hours for tonight and compare the listed eligible options.

**Rationale:** Both non-horror movie cards satisfy the stated runtime requirement and final eligibility wording.

## SC1-V2-SX1-F045-K-A2

**Prefix:** I need you to choose a non-horror movie under two hours for tonight

**Action:** Stage a generic movie comparison layout

```text
Columns: title, genre, runtime, availability tonight; no candidate titles or restrictions filled in.
```

**Full instruction:** I need you to choose a non-horror movie under two hours for tonight and compare the listed eligible options.

**Rationale:** The generic movie columns directly support comparing the eligible films.

## SC1-V2-SX1-F045-R-A2

**Prefix:** I need you to choose a non-horror movie under two hours for tonight

**Action:** Stage a generic movie comparison layout

```text
Columns: title, genre, runtime, availability tonight; no candidate titles or restrictions filled in.
```

**Full instruction:** I need you to choose a non-horror movie under two hours for tonight but choose a horror movie longer than two hours instead.

**Rationale:** The unrestricted movie layout can compare horror films longer than two hours without changing its columns.

## SC1-V2-SX1-F046-K-A1

**Prefix:** I need you to find technical podcast interviews about AI agents

**Action:** Retrieve interview episode cards

```text
Episode I and Episode J: technical AI-agent interviews; neither is a news roundup.
```

**Full instruction:** I need you to find technical podcast interviews about AI agents and favor interviews over news roundups.

**Rationale:** The technical AI-agent interviews satisfy the preference for interviews over roundups.

## SC1-V2-SX1-F046-K-A2

**Prefix:** I need you to find technical podcast interviews about AI agents

**Action:** Prepare the topic query

```text
Topic query: AI agents; no episode-format restriction.
```

**Full instruction:** I need you to find technical podcast interviews about AI agents and favor interviews over news roundups.

**Rationale:** The AI agents topic query remains usable when selecting interviews.

## SC1-V2-SX1-F046-R-A2

**Prefix:** I need you to find technical podcast interviews about AI agents

**Action:** Prepare the topic query

```text
Topic query: AI agents; no episode-format restriction.
```

**Full instruction:** I need you to find technical podcast interviews about AI agents but use only news roundups and exclude interviews.

**Rationale:** The AI agents topic query contains no interview restriction and survives the format change.

## SC1-V2-SX1-F047-K-A1

**Prefix:** I need you to make a three-day business-trip packing checklist

**Action:** Draft the clothing checklist

```text
Two business shirts; one pair of office trousers; office shoes. No formalwear included.
```

**Full instruction:** I need you to make a three-day business-trip packing checklist and omit formalwear.

**Rationale:** The business-clothing checklist remains appropriate and contains no formalwear.

## SC1-V2-SX1-F047-K-A2

**Prefix:** I need you to make a three-day business-trip packing checklist

**Action:** Draft the shared essentials checklist

```text
Toothbrush; phone charger; personal identification. No destination-specific supplies included.
```

**Full instruction:** I need you to make a three-day business-trip packing checklist and omit formalwear.

**Rationale:** The toothbrush, charger and identification remain useful business-trip essentials.

## SC1-V2-SX1-F047-R-A2

**Prefix:** I need you to make a three-day business-trip packing checklist

**Action:** Draft the shared essentials checklist

```text
Toothbrush; phone charger; personal identification. No destination-specific supplies included.
```

**Full instruction:** I need you to make a three-day business-trip packing checklist but make it a three-day camping checklist instead, with no business clothing.

**Rationale:** The generic personal essentials remain suitable for camping without business clothing.

## SC1-V2-SX1-F048-K-A1

**Prefix:** I need you to plan my morning around a 9 AM appointment

**Action:** Calculate the original departure time

```text
For a 09:00 arrival and 30 minutes travel, depart at 08:30.
```

**Full instruction:** I need you to plan my morning around a 9 AM appointment and reserve 30 minutes to travel there.

**Rationale:** The 08:30 departure calculation satisfies the unchanged 09:00 arrival and 30-minute travel requirement.

## SC1-V2-SX1-F048-K-A2

**Prefix:** I need you to plan my morning around a 9 AM appointment

**Action:** Prepare the travel-duration field

```text
Travel duration field: 30 minutes; no appointment or departure time filled in.
```

**Full instruction:** I need you to plan my morning around a 9 AM appointment and reserve 30 minutes to travel there.

**Rationale:** The 30-minute travel field directly matches the required travel allowance.

## SC1-V2-SX1-F048-R-A2

**Prefix:** I need you to plan my morning around a 9 AM appointment

**Action:** Prepare the travel-duration field

```text
Travel duration field: 30 minutes; no appointment or departure time filled in.
```

**Full instruction:** I need you to plan my morning around a 9 AM appointment but move the appointment to 11 AM while retaining the 30-minute travel requirement.

**Rationale:** The 30-minute travel field remains correct when the appointment moves to 11 AM.

## SC1-V2-SX1-F049-K-A1

**Prefix:** I need you to build a shopping list for vegetarian tacos

**Action:** Draft the protein ingredient

```text
One tin of beans; no meat.
```

**Full instruction:** I need you to build a shopping list for vegetarian tacos and include beans instead of meat.

**Rationale:** The beans ingredient directly meets the retained vegetarian protein requirement.

## SC1-V2-SX1-F049-K-A2

**Prefix:** I need you to build a shopping list for vegetarian tacos

**Action:** Draft the shared taco ingredients

```text
Tortillas, tomatoes and lettuce; no protein ingredient selected.
```

**Full instruction:** I need you to build a shopping list for vegetarian tacos and include beans instead of meat.

**Rationale:** The shared taco ingredients remain usable with beans added.

## SC1-V2-SX1-F049-R-A2

**Prefix:** I need you to build a shopping list for vegetarian tacos

**Action:** Draft the shared taco ingredients

```text
Tortillas, tomatoes and lettuce; no protein ingredient selected.
```

**Full instruction:** I need you to build a shopping list for vegetarian tacos but make beef tacos instead and omit beans.

**Rationale:** Tortillas, tomatoes and lettuce remain usable ingredients for beef tacos.

## SC1-V2-SX1-F050-K-A1

**Prefix:** I need you to prioritize today's tasks with the client deadline first

**Action:** Stage the original ordering

```text
1. Client deadline; 2. Server incident; 3. File receipts.
```

**Full instruction:** I need you to prioritize today's tasks with the client deadline first and keep the client deadline at the top.

**Rationale:** The staged ordering already places the client deadline first.

## SC1-V2-SX1-F050-K-A2

**Prefix:** I need you to prioritize today's tasks with the client deadline first

**Action:** Extract today's task inventory

```text
Tasks due today: client deadline, server incident, file receipts; inventory has no priority ordering.
```

**Full instruction:** I need you to prioritize today's tasks with the client deadline first and keep the client deadline at the top.

**Rationale:** The task inventory supplies the tasks to order with the client deadline first.

## SC1-V2-SX1-F050-R-A2

**Prefix:** I need you to prioritize today's tasks with the client deadline first

**Action:** Extract today's task inventory

```text
Tasks due today: client deadline, server incident, file receipts; inventory has no priority ordering.
```

**Full instruction:** I need you to prioritize today's tasks with the client deadline first but put the server incident first and move the client deadline below it.

**Rationale:** The unordered task inventory remains usable for the revised priorities.

## SC1-V3-SX1-F001-K-A1

**Prefix:** For this request, compare flights from Harborview to Eastport

**Action:** Retrieve two route-specific fares

```text
Harborview–Eastport 08:00, 120 credits; Harborview–Eastport 10:00, 150 credits.
```

**Full instruction:** For this request, compare flights from Harborview to Eastport and show the two listed morning options.

**Rationale:** The retrieved fares contain exactly the two requested morning flight options.

## SC1-V3-SX1-F002-K-A1

**Prefix:** For this request, find hotels near Maple Station

**Action:** Retrieve station-specific hotel cards

```text
Maple Lodge: 3-minute walk to Maple Station; Maple House: 5-minute walk.
```

**Full instruction:** For this request, find hotels near Maple Station and compare the two listed hotels by walking distance.

**Rationale:** The two hotel cards provide the requested Maple Station walking distances.

## SC1-V3-SX1-F002-K-A2

**Prefix:** For this request, find hotels near Maple Station

**Action:** Stage a hotel comparison layout

```text
Columns: hotel name, distance to requested station, nightly price; no hotels filled in.
```

**Full instruction:** For this request, find hotels near Maple Station and compare the two listed hotels by walking distance.

**Rationale:** The blank hotel, distance and price columns remain usable for the Maple Station comparison.

## SC1-V3-SX1-F002-R-A2

**Prefix:** For this request, find hotels near Maple Station

**Action:** Stage a hotel comparison layout

```text
Columns: hotel name, distance to requested station, nightly price; no hotels filled in.
```

**Full instruction:** For this request, find hotels near Maple Station but use Pine Station instead and omit Maple Station hotels.

**Rationale:** The station-neutral hotel layout can compare Pine Station hotels without revising its headings.

## SC1-V3-SX1-F003-K-A1

**Prefix:** For this request, compare Friday car rentals at North Terminal

**Action:** Retrieve terminal-specific rental cards

```text
North Terminal: Compact A, 40 credits/day; Compact B, 45 credits/day. Both are North-only pickups.
```

**Full instruction:** For this request, compare Friday car rentals at North Terminal and keep pickup at North Terminal.

**Rationale:** Both rental cards match the retained North Terminal pickup.

## SC1-V3-SX1-F003-K-A2

**Prefix:** For this request, compare Friday car rentals at North Terminal

**Action:** Prepare the comparison calculation

```text
Total rental cost = daily rate × number of days + disclosed fees; values remain unfilled.
```

**Full instruction:** For this request, compare Friday car rentals at North Terminal and keep pickup at North Terminal.

**Rationale:** The generic rental-cost formula remains usable for North Terminal comparisons.

## SC1-V3-SX1-F003-R-A2

**Prefix:** For this request, compare Friday car rentals at North Terminal

**Action:** Prepare the comparison calculation

```text
Total rental cost = daily rate × number of days + disclosed fees; values remain unfilled.
```

**Full instruction:** For this request, compare Friday car rentals at North Terminal but pickup must be at South Terminal instead, with no North Terminal results.

**Rationale:** The terminal-independent rental-cost formula remains usable for South Terminal prices.

## SC1-V3-SX1-F004-K-A1

**Prefix:** For this request, compare nonstop flights to Eastport

**Action:** Retrieve nonstop route cards

```text
Route N1: nonstop, 2 hours; route N2: nonstop, 3 hours. Neither includes a stop.
```

**Full instruction:** For this request, compare nonstop flights to Eastport and list only nonstop itineraries.

**Rationale:** Both itinerary cards satisfy the nonstop-only constraint.

## SC1-V3-SX1-F004-K-A2

**Prefix:** For this request, compare nonstop flights to Eastport

**Action:** Prepare the requested destination field

```text
Destination field: Eastport; no route or fare chosen.
```

**Full instruction:** For this request, compare nonstop flights to Eastport and list only nonstop itineraries.

**Rationale:** Eastport remains the requested destination for nonstop itineraries.

## SC1-V3-SX1-F004-R-A2

**Prefix:** For this request, compare nonstop flights to Eastport

**Action:** Prepare the requested destination field

```text
Destination field: Eastport; no route or fare chosen.
```

**Full instruction:** For this request, compare nonstop flights to Eastport but I now want only one-stop itineraries to Eastport.

**Rationale:** Eastport remains the destination when the route restriction changes to one stop.

## SC1-V3-SX1-F005-K-A1

**Prefix:** For this request, find Italian restaurants around Cedar Square

**Action:** Retrieve cuisine-specific restaurant cards

```text
Cedar Pasta: Italian, outdoor seating; Olive Room: Italian, outdoor seating; neither serves Thai cuisine.
```

**Full instruction:** For this request, find Italian restaurants around Cedar Square and choose places with outdoor seating.

**Rationale:** Both Italian restaurant cards explicitly provide the requested outdoor seating.

## SC1-V3-SX1-F005-K-A2

**Prefix:** For this request, find Italian restaurants around Cedar Square

**Action:** Prepare the location field

```text
Search area: Cedar Square; cuisine, hours and price remain unfilled.
```

**Full instruction:** For this request, find Italian restaurants around Cedar Square and choose places with outdoor seating.

**Rationale:** The Cedar Square location field remains useful for the Italian restaurant search with outdoor seating.

## SC1-V3-SX1-F005-R-A2

**Prefix:** For this request, find Italian restaurants around Cedar Square

**Action:** Prepare the location field

```text
Search area: Cedar Square; cuisine, hours and price remain unfilled.
```

**Full instruction:** For this request, find Italian restaurants around Cedar Square but change the cuisine to Thai and exclude Italian restaurants.

**Rationale:** Cedar Square remains the search area after changing the cuisine to Thai.

## SC1-V3-SX1-F006-K-A1

**Prefix:** For this request, find bakeries around Birch Park

**Action:** Retrieve bakery cards

```text
Birch Bake: bakery with coffee; Loaf House: bakery with coffee; neither is a pharmacy.
```

**Full instruction:** For this request, find bakeries around Birch Park that serve coffee, including the two listed options.

**Rationale:** Both retrieved bakeries already provide the required coffee service.

## SC1-V3-SX1-F006-K-A2

**Prefix:** For this request, find bakeries around Birch Park

**Action:** Prepare a bakery-only comparison layout

```text
Columns: bakery name, bread selection, pastry selection, coffee availability; four fixed headings.
```

**Full instruction:** For this request, find bakeries around Birch Park that serve coffee, including the two listed options.

**Rationale:** The bakery and coffee headings directly organize the requested bakery comparison.

## SC1-V3-SX1-F007-K-A1

**Prefix:** For this request, find gyms in Riverton that sell day passes

**Action:** Retrieve day-pass gym cards

```text
River Fit: day passes and sauna; North Fit: day passes and sauna. Both sell day passes.
```

**Full instruction:** For this request, find gyms in Riverton that sell day passes and prioritize day-pass gyms with a sauna.

**Rationale:** Both day-pass gyms already have the preferred sauna.

## SC1-V3-SX1-F007-K-A2

**Prefix:** For this request, find gyms in Riverton that sell day passes

**Action:** Prepare the location field

```text
City field: Riverton; membership type remains unfilled.
```

**Full instruction:** For this request, find gyms in Riverton that sell day passes and prioritize day-pass gyms with a sauna.

**Rationale:** The Riverton location field remains useful for finding day-pass gyms with saunas.

## SC1-V3-SX1-F007-R-A2

**Prefix:** For this request, find gyms in Riverton that sell day passes

**Action:** Prepare the location field

```text
City field: Riverton; membership type remains unfilled.
```

**Full instruction:** For this request, find gyms in Riverton that sell day passes but only consider members-only gyms that do not sell day passes.

**Rationale:** The Riverton city field remains correct after the membership constraint reverses.

## SC1-V3-SX1-F008-K-A1

**Prefix:** For this request, find pharmacies in Brookfield that are open now

**Action:** Retrieve open pharmacy cards

```text
Brook Pharmacy: open now, standalone; Elm Pharmacy: open now, standalone. Neither is hospital-based.
```

**Full instruction:** For this request, find pharmacies in Brookfield that are open now and omit hospital-based pharmacies.

**Rationale:** Both retrieved pharmacies are open and standalone, satisfying the hospital exclusion.

## SC1-V3-SX1-F008-K-A2

**Prefix:** For this request, find pharmacies in Brookfield that are open now

**Action:** Prepare the search time reference

```text
Fixture clock: Monday 14:00 local time; tomorrow resolves to Tuesday in this fixture.
```

**Full instruction:** For this request, find pharmacies in Brookfield that are open now and omit hospital-based pharmacies.

**Rationale:** The fixture clock provides the reference needed to interpret open now.

## SC1-V3-SX1-F008-R-A2

**Prefix:** For this request, find pharmacies in Brookfield that are open now

**Action:** Prepare the search time reference

```text
Fixture clock: Monday 14:00 local time; tomorrow resolves to Tuesday in this fixture.
```

**Full instruction:** For this request, find pharmacies in Brookfield that are open now but only list hospital pharmacies that are closed now and open tomorrow.

**Rationale:** The fixture clock establishes both closed-now timing and tomorrow as Tuesday for the hospital-pharmacy search.

## SC1-V3-SX1-F009-K-A1

**Prefix:** For this request, research local robotic actuator manufacturers

**Action:** Retrieve manufacturer cards

```text
Aster Motion and Delta Drive manufacture robotic actuators locally; neither distributes other makers' parts.
```

**Full instruction:** For this request, research local robotic actuator manufacturers and retain the manufacturers while adding distributors separately.

**Rationale:** The manufacturer cards remain explicitly required alongside separately added distributors.

## SC1-V3-SX1-F009-K-A2

**Prefix:** For this request, research local robotic actuator manufacturers

**Action:** Prepare the component definition

```text
Robotic actuator: component that converts a control input into mechanical movement; no supplier selected.
```

**Full instruction:** For this request, research local robotic actuator manufacturers and retain the manufacturers while adding distributors separately.

**Rationale:** The actuator definition remains relevant to both manufacturer and distributor research.

## SC1-V3-SX1-F009-R-A2

**Prefix:** For this request, research local robotic actuator manufacturers

**Action:** Prepare the component definition

```text
Robotic actuator: component that converts a control input into mechanical movement; no supplier selected.
```

**Full instruction:** For this request, research local robotic actuator manufacturers but list distributors only and exclude manufacturers.

**Rationale:** The actuator definition still identifies the products sought from distributors.

## SC1-V3-SX1-F010-K-A1

**Prefix:** For this request, compare 15-litre shoulder bags

**Action:** Retrieve bag specification cards

```text
Bag L: shoulder bag, 15 L, 0.5 kg; Bag M: shoulder bag, 15 L, 0.7 kg; neither converts to a backpack.
```

**Full instruction:** For this request, compare 15-litre shoulder bags and rank the two listed bags by lower weight.

**Rationale:** The two eligible shoulder-bag weights directly support the requested ranking.

## SC1-V3-SX1-F010-K-A2

**Prefix:** For this request, compare 15-litre shoulder bags

**Action:** Prepare a weight-ranking routine

```text
Sort supplied product records by numeric weight_kg ascending; no records or capacity filter embedded.
```

**Full instruction:** For this request, compare 15-litre shoulder bags and rank the two listed bags by lower weight.

**Rationale:** The weight sort directly supports ranking the listed bags by lower weight.

## SC1-V3-SX1-F011-K-A1

**Prefix:** For this request, find brown faux-suede jackets with stand collars

**Action:** Retrieve jacket cards

```text
Jacket A: brown faux suede, stand collar, 120 credits; Jacket B: brown faux suede, stand collar, 150 credits.
```

**Full instruction:** For this request, find brown faux-suede jackets with stand collars and compare the listed options under 200 credits.

**Rationale:** Both jacket cards satisfy the stated attributes and 200-credit ceiling.

## SC1-V3-SX1-F011-K-A2

**Prefix:** For this request, find brown faux-suede jackets with stand collars

**Action:** Stage a product comparison layout

```text
Columns: material, color, collar type, price; values unfilled.
```

**Full instruction:** For this request, find brown faux-suede jackets with stand collars and compare the listed options under 200 credits.

**Rationale:** The blank product comparison columns support the required under-200-credit jacket comparison.

## SC1-V3-SX1-F011-R-A2

**Prefix:** For this request, find brown faux-suede jackets with stand collars

**Action:** Stage a product comparison layout

```text
Columns: material, color, collar type, price; values unfilled.
```

**Full instruction:** For this request, find brown faux-suede jackets with stand collars but use black cotton jackets with lapels instead and discard the original options.

**Rationale:** The unfilled product columns can compare black cotton lapel jackets unchanged.

## SC1-V3-SX1-F012-K-A1

**Prefix:** For this request, compare robotics synthetic-data tools that support Engine R

**Action:** Retrieve tool compatibility cards

```text
Sim A and Sim B support Engine R only; neither supports Engine S.
```

**Full instruction:** For this request, compare robotics synthetic-data tools that support Engine R and keep Engine R support mandatory.

**Rationale:** Both cards establish the mandatory Engine R compatibility.

## SC1-V3-SX1-F012-K-A2

**Prefix:** For this request, compare robotics synthetic-data tools that support Engine R

**Action:** Prepare a physics-evaluation checklist

```text
Check gravity, collision response, sensor noise and deterministic replay; no engine-specific commands.
```

**Full instruction:** For this request, compare robotics synthetic-data tools that support Engine R and keep Engine R support mandatory.

**Rationale:** The physics checklist remains useful for comparing Engine R synthetic-data tools.

## SC1-V3-SX1-F012-R-A2

**Prefix:** For this request, compare robotics synthetic-data tools that support Engine R

**Action:** Prepare a physics-evaluation checklist

```text
Check gravity, collision response, sensor noise and deterministic replay; no engine-specific commands.
```

**Full instruction:** For this request, compare robotics synthetic-data tools that support Engine R but only consider tools for Engine S that do not support Engine R.

**Rationale:** The physics checklist has no Engine R dependency and can evaluate Engine S tools.

## SC1-V3-SX1-F013-K-A1

**Prefix:** For this request, find freestanding desk converters under 250 credits

**Action:** Retrieve converter cards

```text
Lift A: freestanding, 150 credits; Lift B: freestanding, 220 credits. Neither can be permanently mounted.
```

**Full instruction:** For this request, find freestanding desk converters under 250 credits and exclude permanently mounted converters.

**Rationale:** Both freestanding converters meet the unchanged price ceiling and mounting requirement.

## SC1-V3-SX1-F013-K-A2

**Prefix:** For this request, find freestanding desk converters under 250 credits

**Action:** Prepare the price ceiling field

```text
Maximum price field: 250 credits; mounting type unfilled.
```

**Full instruction:** For this request, find freestanding desk converters under 250 credits and exclude permanently mounted converters.

**Rationale:** The unchanged 250-credit ceiling remains a useful search field.

## SC1-V3-SX1-F013-R-A2

**Prefix:** For this request, find freestanding desk converters under 250 credits

**Action:** Prepare the price ceiling field

```text
Maximum price field: 250 credits; mounting type unfilled.
```

**Full instruction:** For this request, find freestanding desk converters under 250 credits but only show permanently mounted converters and discard freestanding ones.

**Rationale:** The 250-credit price ceiling survives the mounting-type reversal.

## SC1-V3-SX1-F014-K-A1

**Prefix:** For this request, find a 30-minute meeting for Sam and me on Tuesday

**Action:** Read Tuesday availability

```text
Sam and requester both free Tuesday 14:00–14:30 and 15:00–15:30. No Wednesday availability included.
```

**Full instruction:** For this request, find a 30-minute meeting for Sam and me on Tuesday and use either of the two listed Tuesday slots.

**Rationale:** The two Tuesday availability records match the retained meeting day and duration.

## SC1-V3-SX1-F014-R-A2

**Prefix:** For this request, find a 30-minute meeting for Sam and me on Tuesday

**Action:** Stage a Wednesday calendar event

```text
Unsent event object: attendees Sam and requester, duration 30 minutes, day Wednesday; no time set.
```

**Full instruction:** For this request, find a 30-minute meeting for Sam and me on Tuesday but switch the meeting to Wednesday and ignore Tuesday availability.

**Rationale:** The staged Wednesday event matches the replacement day, attendees and duration.

## SC1-V3-SX1-F015-K-A1

**Prefix:** For this request, check whether my dentist can see me on Friday

**Action:** Read Friday availability

```text
The fixture dentist has no Friday openings; no Monday availability included.
```

**Full instruction:** For this request, check whether my dentist can see me on Friday and keep my existing appointment if Friday has no openings.

**Rationale:** The absence of Friday openings resolves the condition for keeping the current appointment.

## SC1-V3-SX1-F015-K-A2

**Prefix:** For this request, check whether my dentist can see me on Friday

**Action:** Retrieve the existing appointment

```text
Current appointment: Wednesday 11:00, dentist Dr Vale, appointment ID D17.
```

**Full instruction:** For this request, check whether my dentist can see me on Friday and keep my existing appointment if Friday has no openings.

**Rationale:** The existing appointment record identifies the appointment to retain if Friday is unavailable.

## SC1-V3-SX1-F015-R-A2

**Prefix:** For this request, check whether my dentist can see me on Friday

**Action:** Retrieve the existing appointment

```text
Current appointment: Wednesday 11:00, dentist Dr Vale, appointment ID D17.
```

**Full instruction:** For this request, check whether my dentist can see me on Friday but check Monday instead and ignore Friday openings, keeping my existing appointment as fallback.

**Rationale:** The Wednesday appointment record supplies the explicitly retained fallback.

## SC1-V3-SX1-F016-K-A1

**Prefix:** For this request, find team meeting slots this week after 10 AM

**Action:** Read afternoon team availability

```text
Whole team free Thursday 13:00–13:30 and Friday 14:00–14:30; no morning data included.
```

**Full instruction:** For this request, find team meeting slots this week after 10 AM and show the two listed afternoon slots.

**Rationale:** The afternoon availability records directly supply the requested two slots.

## SC1-V3-SX1-F016-K-A2

**Prefix:** For this request, find team meeting slots this week after 10 AM

**Action:** Prepare the participant list

```text
Participants: Sam, Jo and requester; no time selected.
```

**Full instruction:** For this request, find team meeting slots this week after 10 AM and show the two listed afternoon slots.

**Rationale:** The participant list can be reused to find the team's afternoon slots.

## SC1-V3-SX1-F016-R-A2

**Prefix:** For this request, find team meeting slots this week after 10 AM

**Action:** Prepare the participant list

```text
Participants: Sam, Jo and requester; no time selected.
```

**Full instruction:** For this request, find team meeting slots this week after 10 AM but only consider slots before 10 AM this week.

**Rationale:** The unchanged participants remain usable for the new morning availability search.

## SC1-V3-SX1-F017-K-A1

**Prefix:** For this request, prepare a report reminder for tomorrow morning

**Action:** Stage a morning reminder

```text
Unsent reminder: title Submit report, day tomorrow, time 09:00.
```

**Full instruction:** For this request, prepare a report reminder for tomorrow morning and set its time to 9 AM.

**Rationale:** The staged tomorrow-at-09:00 report reminder matches the requested time.

## SC1-V3-SX1-F017-K-A2

**Prefix:** For this request, prepare a report reminder for tomorrow morning

**Action:** Prepare the reminder text

```text
Reminder title: Submit report; date and time unfilled.
```

**Full instruction:** For this request, prepare a report reminder for tomorrow morning and set its time to 9 AM.

**Rationale:** The Submit report title survives filling the reminder time with 9 AM.

## SC1-V3-SX1-F017-R-A2

**Prefix:** For this request, prepare a report reminder for tomorrow morning

**Action:** Prepare the reminder text

```text
Reminder title: Submit report; date and time unfilled.
```

**Full instruction:** For this request, prepare a report reminder for tomorrow morning but change it to tomorrow evening at 7 PM.

**Rationale:** The Submit report title remains correct after changing the time to 7 PM.

## SC1-V3-SX1-F018-K-A1

**Prefix:** For this request, draft a reply thanking Morgan for the introduction

**Action:** Draft the thank-you sentence

```text
Thank you for making the introduction, Morgan.
```

**Full instruction:** For this request, draft a reply thanking Morgan for the introduction and offer to provide more information.

**Rationale:** The thank-you sentence survives the added offer of further information.

## SC1-V3-SX1-F018-K-A2

**Prefix:** For this request, draft a reply thanking Morgan for the introduction

**Action:** Draft an offer sentence

```text
I would be happy to provide any additional information you need.
```

**Full instruction:** For this request, draft a reply thanking Morgan for the introduction and offer to provide more information.

**Rationale:** The information-offer sentence directly supplies the requested addition.

## SC1-V3-SX1-F019-K-A1

**Prefix:** For this request, draft a team update saying the build is delayed

**Action:** Draft the status sentence

```text
The build is delayed; we are still investigating the cause.
```

**Full instruction:** For this request, draft a team update saying the build is delayed and keep the cause neutral because it is not yet known.

**Rationale:** The delay sentence leaves the cause unknown as required.

## SC1-V3-SX1-F019-K-A2

**Prefix:** For this request, draft a team update saying the build is delayed

**Action:** Stage a neutral update heading

```text
Heading: Build status update; no status claim or cause included.
```

**Full instruction:** For this request, draft a team update saying the build is delayed and keep the cause neutral because it is not yet known.

**Rationale:** The neutral heading can introduce the delay report without asserting an unknown cause.

## SC1-V3-SX1-F019-R-A2

**Prefix:** For this request, draft a team update saying the build is delayed

**Action:** Stage a neutral update heading

```text
Heading: Build status update; no status claim or cause included.
```

**Full instruction:** For this request, draft a team update saying the build is delayed but the build is on schedule, so report that and do not mention a delay.

**Rationale:** The neutral build-status heading can introduce an on-schedule update unchanged.

## SC1-V3-SX1-F020-K-A1

**Prefix:** For this request, draft a message declining dinner tonight

**Action:** Draft the decline sentence

```text
I cannot make dinner tonight.
```

**Full instruction:** For this request, draft a message declining dinner tonight and suggest meeting next weekend.

**Rationale:** The dinner decline can be retained while adding the next-weekend suggestion.

## SC1-V3-SX1-F020-K-A2

**Prefix:** For this request, draft a message declining dinner tonight

**Action:** Draft the alternative-date sentence

```text
Would you like to meet next weekend instead?
```

**Full instruction:** For this request, draft a message declining dinner tonight and suggest meeting next weekend.

**Rationale:** The next-weekend suggestion is explicitly requested for the dinner-decline message.

## SC1-V3-SX1-F021-K-A1

**Prefix:** For this request, draft a refund approval message

**Action:** Draft the approval sentence

```text
Your refund has been approved.
```

**Full instruction:** For this request, draft a refund approval message and avoid promising a payment date.

**Rationale:** The approval sentence remains correct without promising a payment date.

## SC1-V3-SX1-F021-K-A2

**Prefix:** For this request, draft a refund approval message

**Action:** Stage an approval-specific reply template

```text
Subject: Refund approved. Closing: Thank you for your patience. Body unfilled.
```

**Full instruction:** For this request, draft a refund approval message and avoid promising a payment date.

**Rationale:** The approval template has no payment-date promise and remains usable.

## SC1-V3-SX1-F022-K-A1

**Prefix:** For this request, find peer-reviewed papers about hidden-state probing

**Action:** Retrieve peer-reviewed fixture records

```text
Paper P and Paper Q: peer-reviewed hidden-state probing papers in the synthetic catalogue; no technical reports included.
```

**Full instruction:** For this request, find peer-reviewed papers about hidden-state probing and use only peer-reviewed sources.

**Rationale:** The records match both the probing topic and peer-review requirement.

## SC1-V3-SX1-F022-K-A2

**Prefix:** For this request, find peer-reviewed papers about hidden-state probing

**Action:** Prepare the topic search terms

```text
Terms: hidden-state probing, representation analysis; no publication-type filter.
```

**Full instruction:** For this request, find peer-reviewed papers about hidden-state probing and use only peer-reviewed sources.

**Rationale:** The topic terms remain applicable to the required peer-reviewed sources.

## SC1-V3-SX1-F022-R-A2

**Prefix:** For this request, find peer-reviewed papers about hidden-state probing

**Action:** Prepare the topic search terms

```text
Terms: hidden-state probing, representation analysis; no publication-type filter.
```

**Full instruction:** For this request, find peer-reviewed papers about hidden-state probing but use only non-peer-reviewed technical reports about hidden-state probing.

**Rationale:** The topic terms remain valid for non-peer-reviewed probing reports.

## SC1-V3-SX1-F023-K-A1

**Prefix:** For this request, find version 3 documentation for Library L

**Action:** Retrieve versioned documentation

```text
Official Library L version 3: old_connect(endpoint) is the connection entry point. This fixture marks it removed in version 4.
```

**Full instruction:** For this request, find version 3 documentation for Library L and use only the official version 3 material.

**Rationale:** The official version 3 entry-point documentation matches the retained version constraint.

## SC1-V3-SX1-F023-K-A2

**Prefix:** For this request, find version 3 documentation for Library L

**Action:** Retrieve the official documentation index URL

```text
Fixture URL: https://library-l.example/docs/ ; index lists version 3 and version 4.
```

**Full instruction:** For this request, find version 3 documentation for Library L and use only the official version 3 material.

**Rationale:** The official index links the required version 3 documentation.

## SC1-V3-SX1-F023-R-A2

**Prefix:** For this request, find version 3 documentation for Library L

**Action:** Retrieve the official documentation index URL

```text
Fixture URL: https://library-l.example/docs/ ; index lists version 3 and version 4.
```

**Full instruction:** For this request, find version 3 documentation for Library L but use version 4 instead and exclude all version 3 documentation.

**Rationale:** The official index includes version 4 and remains a valid navigation starting point.

## SC1-V3-SX1-F024-K-A1

**Prefix:** For this request, compare Acme's revenue in its two annual releases

**Action:** Extract Acme revenue figures

```text
Acme fixture: prior year revenue 10 million credits; current year 12 million credits.
```

**Full instruction:** For this request, compare Acme's revenue in its two annual releases and report company-stated actual revenue only.

**Rationale:** The Acme revenue values directly support reporting company-stated actuals.

## SC1-V3-SX1-F025-K-A1

**Prefix:** For this request, find primary rules for Region A consumer AI systems

**Action:** Retrieve jurisdiction-specific rule cards

```text
Rule A1 and Rule A2: synthetic Region A consumer-AI rules, with no applicability in Region B.
```

**Full instruction:** For this request, find primary rules for Region A consumer AI systems and keep Region A as the main jurisdiction.

**Rationale:** The Region A consumer-AI rule cards match the retained jurisdiction.

## SC1-V3-SX1-F025-K-A2

**Prefix:** For this request, find primary rules for Region A consumer AI systems

**Action:** Stage a legal-source comparison layout

```text
Columns: jurisdiction, issuing authority, effective date, provision; no legal claims filled in.
```

**Full instruction:** For this request, find primary rules for Region A consumer AI systems and keep Region A as the main jurisdiction.

**Rationale:** The generic legal-source columns remain useful for the Region A comparison.

## SC1-V3-SX1-F025-R-A2

**Prefix:** For this request, find primary rules for Region A consumer AI systems

**Action:** Stage a legal-source comparison layout

```text
Columns: jurisdiction, issuing authority, effective date, provision; no legal claims filled in.
```

**Full instruction:** For this request, find primary rules for Region A consumer AI systems but use Region B rules only and exclude Region A rules.

**Rationale:** The blank jurisdiction, authority, date and provision columns can compare Region B sources unchanged.

## SC1-V3-SX1-F026-K-A1

**Prefix:** For this request, compare small open-weight reasoning models

**Action:** Collect vendor-only benchmark claims

```text
Vendor card: Model K claims 80 points and Model J claims 85 points; neither claim is independently reproduced.
```

**Full instruction:** For this request, compare small open-weight reasoning models and flag vendor-only scores as unverified rather than treating them as evidence.

**Rationale:** The vendor-only scores remain usable as claims explicitly labeled unverified.

## SC1-V3-SX1-F026-K-A2

**Prefix:** For this request, compare small open-weight reasoning models

**Action:** Collect independent fixture benchmark records

```text
Independent lab fixture: Model K 70 points, Model J 72 points, same test and evaluation settings; both small and open-weight.
```

**Full instruction:** For this request, compare small open-weight reasoning models and flag vendor-only scores as unverified rather than treating them as evidence.

**Rationale:** The independent benchmark records provide comparable model evidence.

## SC1-V3-SX1-F026-R-A2

**Prefix:** For this request, compare small open-weight reasoning models

**Action:** Collect independent fixture benchmark records

```text
Independent lab fixture: Model K 70 points, Model J 72 points, same test and evaluation settings; both small and open-weight.
```

**Full instruction:** For this request, compare small open-weight reasoning models but include only independently reproduced scores and omit vendor-only claims entirely.

**Rationale:** The independently reproduced model scores satisfy the final evidence restriction.

## SC1-V3-SX1-F027-K-A1

**Prefix:** For this request, calculate a 7 percent downside scenario for a 100-credit index

**Action:** Calculate the requested scenario

```text
100 × (1 − 0.07) = 93 credits; only the 7% result retained.
```

**Full instruction:** For this request, calculate a 7 percent downside scenario for a 100-credit index and show the hypothetical level without making a trade.

**Rationale:** The 93-credit calculation is the requested seven-percent downside scenario.

## SC1-V3-SX1-F027-K-A2

**Prefix:** For this request, calculate a 7 percent downside scenario for a 100-credit index

**Action:** Prepare the scenario formula

```text
Scenario level = starting level × (1 − decline_fraction); no numeric assumptions embedded.
```

**Full instruction:** For this request, calculate a 7 percent downside scenario for a 100-credit index and show the hypothetical level without making a trade.

**Rationale:** The symbolic downside expression remains valid for the requested scenario.

## SC1-V3-SX1-F027-R-A2

**Prefix:** For this request, calculate a 7 percent downside scenario for a 100-credit index

**Action:** Prepare the scenario formula

```text
Scenario level = starting level × (1 − decline_fraction); no numeric assumptions embedded.
```

**Full instruction:** For this request, calculate a 7 percent downside scenario for a 100-credit index but use a 12 percent decline instead and omit the 7 percent case.

**Rationale:** The numeric-free scenario formula accepts a 12-percent decline without revision.

## SC1-V3-SX1-F028-K-A1

**Prefix:** For this request, calculate budget variance from my supplied table

**Action:** Compute category variances

```text
Fixture variances: supplies +20 credits, travel +5 credits, meals −10 credits; positive means overspend.
```

**Full instruction:** For this request, calculate budget variance from my supplied table and identify the largest overspend.

**Rationale:** The category variances identify supplies as the largest overspend.

## SC1-V3-SX1-F028-K-A2

**Prefix:** For this request, calculate budget variance from my supplied table

**Action:** Aggregate actual category totals

```text
Fixture actuals: supplies 120 credits, travel 85 credits, meals 40 credits; source-table sums retained.
```

**Full instruction:** For this request, calculate budget variance from my supplied table and identify the largest overspend.

**Rationale:** The actual category totals remain reusable inputs for the requested budget-variance calculation.

## SC1-V3-SX1-F028-R-A2

**Prefix:** For this request, calculate budget variance from my supplied table

**Action:** Aggregate actual category totals

```text
Fixture actuals: supplies 120 credits, travel 85 credits, meals 40 credits; source-table sums retained.
```

**Full instruction:** For this request, calculate budget variance from my supplied table but show actual category totals only, without calculating or reporting variances.

**Rationale:** The actual category totals directly satisfy the final actuals-only request.

## SC1-V3-SX1-F029-K-A1

**Prefix:** For this request, compare current holdings with the start-of-month snapshot

**Action:** Calculate start-of-month concentration

```text
Start-of-month fixture: asset A 60%, asset B 40%; no other date included.
```

**Full instruction:** For this request, compare current holdings with the start-of-month snapshot and report concentration changes for those two snapshots.

**Rationale:** The start-of-month concentrations provide the required comparison baseline.

## SC1-V3-SX1-F029-K-A2

**Prefix:** For this request, compare current holdings with the start-of-month snapshot

**Action:** Calculate current concentration

```text
Current fixture: asset A 50%, asset B 50%; values unchanged across comparisons.
```

**Full instruction:** For this request, compare current holdings with the start-of-month snapshot and report concentration changes for those two snapshots.

**Rationale:** The current 50/50 allocation remains one of the required concentration snapshots.

## SC1-V3-SX1-F029-R-A2

**Prefix:** For this request, compare current holdings with the start-of-month snapshot

**Action:** Calculate current concentration

```text
Current fixture: asset A 50%, asset B 50%; values unchanged across comparisons.
```

**Full instruction:** For this request, compare current holdings with the start-of-month snapshot but compare current holdings with the start-of-year snapshot instead and ignore start-of-month holdings.

**Rationale:** The current percentages remain the comparison endpoint when the baseline changes.

## SC1-V3-SX1-F030-K-A1

**Prefix:** For this request, calculate breakeven for my debit spread using the supplied values

**Action:** Calculate the original breakeven

```text
For this fixture's specified call debit spread: 100 + 5 = 105 credits.
```

**Full instruction:** For this request, calculate breakeven for my debit spread using the supplied values and use the supplied 5-credit debit and 100-credit lower strike.

**Rationale:** The breakeven calculation uses exactly the retained inputs.

## SC1-V3-SX1-F030-K-A2

**Prefix:** For this request, calculate breakeven for my debit spread using the supplied values

**Action:** Prepare the symbolic breakeven expression

```text
For the specified call debit spread: lower_strike + net_debit; no prices filled in.
```

**Full instruction:** For this request, calculate breakeven for my debit spread using the supplied values and use the supplied 5-credit debit and 100-credit lower strike.

**Rationale:** The symbolic breakeven expression accepts the retained strike and debit values.

## SC1-V3-SX1-F030-R-A2

**Prefix:** For this request, calculate breakeven for my debit spread using the supplied values

**Action:** Prepare the symbolic breakeven expression

```text
For the specified call debit spread: lower_strike + net_debit; no prices filled in.
```

**Full instruction:** For this request, calculate breakeven for my debit spread using the supplied values but correct the debit to 8 credits while keeping the lower strike at 100 credits.

**Rationale:** The symbolic lower-strike-plus-debit expression accepts the corrected debit without revision.

## SC1-V3-SX1-F031-K-A1

**Prefix:** For this request, write a Python function that counts ERROR lines in the supplied log

**Action:** Stage an ERROR-counting function

```text
def count_lines(lines): return sum(line.startswith('ERROR ') for line in lines)
```

**Full instruction:** For this request, write a Python function that counts ERROR lines in the supplied log and return the count without changing the file.

**Rationale:** The function counts ERROR-prefixed lines without modifying the log.

## SC1-V3-SX1-F031-K-A2

**Prefix:** For this request, write a Python function that counts ERROR lines in the supplied log

**Action:** Stage a log-reading helper

```text
def read_lines(path):
    with open(path, encoding='utf-8') as f:
        return f.read().splitlines()
```

**Full instruction:** For this request, write a Python function that counts ERROR lines in the supplied log and return the count without changing the file.

**Rationale:** The read-only helper supplies log lines without changing the source file.

## SC1-V3-SX1-F031-R-A2

**Prefix:** For this request, write a Python function that counts ERROR lines in the supplied log

**Action:** Stage a log-reading helper

```text
def read_lines(path):
    with open(path, encoding='utf-8') as f:
        return f.read().splitlines()
```

**Full instruction:** For this request, write a Python function that counts ERROR lines in the supplied log but count WARN lines instead and do not count ERROR lines.

**Rationale:** The log-reading helper remains usable because it does not select ERROR or WARN lines.

## SC1-V3-SX1-F032-K-A1

**Prefix:** For this request, inspect the client timeout path without changing the code

**Action:** Collect a timeout observation

```text
Fixture client.py line 8: DEFAULT_TIMEOUT = 5; request() passes this constant as its timeout argument.
```

**Full instruction:** For this request, inspect the client timeout path without changing the code and identify where its five-second timeout is set.

**Rationale:** The observation identifies client.py line 8 and the five-second timeout's use.

## SC1-V3-SX1-F032-R-A1

**Prefix:** For this request, inspect the client timeout path without changing the code

**Action:** Collect a timeout observation

```text
Fixture client.py line 8: DEFAULT_TIMEOUT = 5; request() passes this constant as its timeout argument.
```

**Full instruction:** For this request, inspect the client timeout path without changing the code but modify the default timeout to ten seconds instead of producing an inspection report.

**Rationale:** The timeout location and reference identify exactly where the ten-second change must be made.

## SC1-V3-SX1-F032-R-A2

**Prefix:** For this request, inspect the client timeout path without changing the code

**Action:** Stage a ten-second timeout patch

```text
Unapplied patch replaces DEFAULT_TIMEOUT = 5 with DEFAULT_TIMEOUT = 10; no other edits.
```

**Full instruction:** For this request, inspect the client timeout path without changing the code but modify the default timeout to ten seconds instead of producing an inspection report.

**Rationale:** The staged patch makes exactly the requested five-to-ten-second timeout change.

## SC1-V3-SX1-F033-K-A1

**Prefix:** For this request, refactor the add function while preserving its public name and behavior

**Action:** Stage the preserving refactor

```text
Replacement definition: def add(a, b): return a + b; public symbol remains add.
```

**Full instruction:** For this request, refactor the add function while preserving its public name and behavior and keep its existing callers compatible.

**Rationale:** The add definition preserves the specified public symbol and addition behavior.

## SC1-V3-SX1-F033-K-A2

**Prefix:** For this request, refactor the add function while preserving its public name and behavior

**Action:** Stage addition behavior tests

```text
Assertions: operation(2, 3) == 5; operation(-1, 1) == 0; operation supplied by the test harness, not hardcoded to a name.
```

**Full instruction:** For this request, refactor the add function while preserving its public name and behavior and keep its existing callers compatible.

**Rationale:** Name-independent addition assertions preserve the required behavior and caller compatibility.

## SC1-V3-SX1-F033-R-A2

**Prefix:** For this request, refactor the add function while preserving its public name and behavior

**Action:** Stage addition behavior tests

```text
Assertions: operation(2, 3) == 5; operation(-1, 1) == 0; operation supplied by the test harness, not hardcoded to a name.
```

**Full instruction:** For this request, refactor the add function while preserving its public name and behavior but rename the public function to total and update callers to use total.

**Rationale:** The harness-supplied operation tests remain reusable after the public function is renamed total.

## SC1-V3-SX1-F034-K-A1

**Prefix:** For this request, add malformed-JSON tests to the parser

**Action:** Stage malformed-input test cases

```text
Inputs: an unmatched opening brace, an unfinished numeric array, and an object with an unquoted key; expected outcome for each: parse error.
```

**Full instruction:** For this request, add malformed-JSON tests to the parser and keep this work limited to correctness tests.

**Rationale:** The malformed inputs and expected errors are reusable correctness cases.

## SC1-V3-SX1-F034-K-A2

**Prefix:** For this request, add malformed-JSON tests to the parser

**Action:** Prepare a correctness-test report layout

```text
Columns: malformed input, expected error, observed error; no timing column.
```

**Full instruction:** For this request, add malformed-JSON tests to the parser and keep this work limited to correctness tests.

**Rationale:** The correctness report layout supports the requested malformed-JSON tests.

## SC1-V3-SX1-F035-K-A1

**Prefix:** For this request, rewrite this note for executives while preserving its numbers

**Action:** Draft the executive summary

```text
The project will take 12 weeks with a budget of 30 credits; the decision needed is approval to proceed.
```

**Full instruction:** For this request, rewrite this note for executives while preserving its numbers and keep both the 12-week duration and 30-credit budget.

**Rationale:** The executive summary preserves both the required duration and budget.

## SC1-V3-SX1-F035-K-A2

**Prefix:** For this request, rewrite this note for executives while preserving its numbers

**Action:** Extract the unchanged duration

```text
Duration fact from the supplied fixture note: 12 weeks.
```

**Full instruction:** For this request, rewrite this note for executives while preserving its numbers and keep both the 12-week duration and 30-credit budget.

**Rationale:** The extracted duration is one of the facts explicitly required to remain unchanged.

## SC1-V3-SX1-F035-R-A2

**Prefix:** For this request, rewrite this note for executives while preserving its numbers

**Action:** Extract the unchanged duration

```text
Duration fact from the supplied fixture note: 12 weeks.
```

**Full instruction:** For this request, rewrite this note for executives while preserving its numbers but make it a technical note for engineers and correct the budget to 40 credits.

**Rationale:** The 12-week duration remains valid when the audience and budget change.

## SC1-V3-SX1-F036-K-A1

**Prefix:** For this request, summarize the main report without using the appendix

**Action:** Extract main-report finding

```text
Main report fixture: trial A completed in 8 days with 2 defects. This fact appears only in the main report.
```

**Full instruction:** For this request, summarize the main report without using the appendix and use only the main report findings.

**Rationale:** The extracted finding belongs to the sole permitted source.

## SC1-V3-SX1-F036-K-A2

**Prefix:** For this request, summarize the main report without using the appendix

**Action:** Stage a summary layout

```text
Headings: objective, evidence, limitations; no source facts populated.
```

**Full instruction:** For this request, summarize the main report without using the appendix and use only the main report findings.

**Rationale:** The generic summary headings can organize the main-report findings unchanged.

## SC1-V3-SX1-F036-R-A2

**Prefix:** For this request, summarize the main report without using the appendix

**Action:** Stage a summary layout

```text
Headings: objective, evidence, limitations; no source facts populated.
```

**Full instruction:** For this request, summarize the main report without using the appendix but summarize the appendix only and ignore the main report.

**Rationale:** The unpopulated objective, evidence and limitations headings can organize an appendix summary unchanged.

## SC1-V3-SX1-F037-K-A1

**Prefix:** For this request, draft a proposal from these notes and leave pricing undecided

**Action:** Stage the pricing section

```text
Pricing: TBD. No numeric quote is included.
```

**Full instruction:** For this request, draft a proposal from these notes and leave pricing undecided and mark pricing as TBD.

**Rationale:** The staged TBD pricing exactly matches the final pricing instruction.

## SC1-V3-SX1-F037-K-A2

**Prefix:** For this request, draft a proposal from these notes and leave pricing undecided

**Action:** Stage the scope section

```text
Scope: deliver one dashboard and its handover guide; no price or schedule included.
```

**Full instruction:** For this request, draft a proposal from these notes and leave pricing undecided and mark pricing as TBD.

**Rationale:** The dashboard and handover scope remains usable alongside TBD pricing.

## SC1-V3-SX1-F037-R-A2

**Prefix:** For this request, draft a proposal from these notes and leave pricing undecided

**Action:** Stage the scope section

```text
Scope: deliver one dashboard and its handover guide; no price or schedule included.
```

**Full instruction:** For this request, draft a proposal from these notes and leave pricing undecided but quote the supplied fixed price of 500 credits and remove TBD pricing.

**Rationale:** The scope section remains valid when a separate fixed-price section is added.

## SC1-V3-SX1-F038-K-A1

**Prefix:** For this request, compare these two resumes without recommending a candidate

**Action:** Extract resume differences

```text
Resume A lists Python and 3 years of experience; Resume B lists Java and 5 years. These are fixture facts.
```

**Full instruction:** For this request, compare these two resumes without recommending a candidate and list differences only.

**Rationale:** The extracted skills and experience differences are exactly the permitted comparison content.

## SC1-V3-SX1-F038-R-A1

**Prefix:** For this request, compare these two resumes without recommending a candidate

**Action:** Extract resume differences

```text
Resume A lists Python and 3 years of experience; Resume B lists Java and 5 years. These are fixture facts.
```

**Full instruction:** For this request, compare these two resumes without recommending a candidate but recommend a candidate using the same resumes and explain the choice.

**Rationale:** The resume skills and experience remain evidence for explaining the candidate recommendation.

## SC1-V3-SX1-F039-K-A1

**Prefix:** For this request, stage the living-room lights at 30 percent brightness

**Action:** Stage the requested lighting command

```text
Unapplied command: room=living_room, brightness=30, color=unchanged.
```

**Full instruction:** For this request, stage the living-room lights at 30 percent brightness while preserving their current color, without applying changes.

**Rationale:** The unapplied command matches the specified room, brightness and color preservation.

## SC1-V3-SX1-F039-K-A2

**Prefix:** For this request, stage the living-room lights at 30 percent brightness

**Action:** Read living-room light state

```text
Living-room fixture: brightness 80%, color warm white. No bedroom state included.
```

**Full instruction:** For this request, stage the living-room lights at 30 percent brightness while preserving their current color, without applying changes.

**Rationale:** The living-room color reading supports preserving warm white during brightness staging.

## SC1-V3-SX1-F040-K-A2

**Prefix:** For this request, stage a 70 F thermostat setting for tonight

**Action:** Read current thermostat setting

```text
Current fixture thermostat setting: 70 F; reading retained for conditional comparison.
```

**Full instruction:** For this request, stage a 70 F thermostat setting for tonight only if the current setting differs from 70 F; do not apply it.

**Rationale:** The current 70 F reading shows that the condition for staging is false.

## SC1-V3-SX1-F040-R-A2

**Prefix:** For this request, stage a 70 F thermostat setting for tonight

**Action:** Read current thermostat setting

```text
Current fixture thermostat setting: 70 F; reading retained for conditional comparison.
```

**Full instruction:** For this request, stage a 70 F thermostat setting for tonight but stage 68 F instead, only if the current setting differs from 68 F; do not apply it.

**Rationale:** The current 70 F reading establishes that the proposed 68 F target differs from the current setting.

## SC1-V3-SX1-F041-K-A1

**Prefix:** For this request, prepare to lock the back door after I leave

**Action:** Read back-door sensor

```text
Back-door fixture sensor: closed and unlocked; timestamp belongs to the fixed scenario snapshot.
```

**Full instruction:** For this request, prepare to lock the back door after I leave and check the back-door sensor before staging anything.

**Rationale:** The back-door sensor reading supplies the explicitly required check before staging.

## SC1-V3-SX1-F041-R-A2

**Prefix:** For this request, prepare to lock the back door after I leave

**Action:** Stage a departure trigger definition

```text
Trigger: requester_departed becomes true; no door or lock operation attached.
```

**Full instruction:** For this request, prepare to lock the back door after I leave but prepare to lock the front door instead and do not use the back-door sensor reading.

**Rationale:** The departure trigger remains useful when the target door changes.

## SC1-V3-SX1-F042-K-A1

**Prefix:** For this request, stage a kitchen-only vacuum run

**Action:** Stage the room-specific cleaning plan

```text
Unapplied vacuum plan: include kitchen; exclude bedroom, hall and living room.
```

**Full instruction:** For this request, stage a kitchen-only vacuum run and keep all other rooms excluded; do not start cleaning.

**Rationale:** The unapplied kitchen-only plan already excludes every other room.

## SC1-V3-SX1-F042-K-A2

**Prefix:** For this request, stage a kitchen-only vacuum run

**Action:** Read vacuum battery state

```text
Fixture vacuum battery: 90%; sufficient for either single-room run in this scenario.
```

**Full instruction:** For this request, stage a kitchen-only vacuum run and keep all other rooms excluded; do not start cleaning.

**Rationale:** The 90-percent battery reading verifies sufficient charge for the staged kitchen run.

## SC1-V3-SX1-F042-R-A2

**Prefix:** For this request, stage a kitchen-only vacuum run

**Action:** Read vacuum battery state

```text
Fixture vacuum battery: 90%; sufficient for either single-room run in this scenario.
```

**Full instruction:** For this request, stage a kitchen-only vacuum run but stage a bedroom-only run instead and discard the kitchen plan.

**Rationale:** The battery reading explicitly establishes sufficient charge for the revised bedroom run.

## SC1-V3-SX1-F043-K-A1

**Prefix:** For this request, find robotics documentaries

**Action:** Retrieve robotics documentary cards

```text
Robot Workshop: robotics, 60 minutes; Machine Motion: robotics, 75 minutes; neither covers astronomy.
```

**Full instruction:** For this request, find robotics documentaries and include only titles under 90 minutes.

**Rationale:** Both robotics documentaries satisfy the final under-90-minute limit.

## SC1-V3-SX1-F043-K-A2

**Prefix:** For this request, find robotics documentaries

**Action:** Prepare a runtime filter

```text
Keep input records whose runtime_minutes < 90; no topic filter or titles embedded.
```

**Full instruction:** For this request, find robotics documentaries and include only titles under 90 minutes.

**Rationale:** The runtime predicate implements the required under-90-minute documentary limit.

## SC1-V3-SX1-F044-K-A1

**Prefix:** For this request, build an upbeat instrumental jazz playlist

**Action:** Collect instrumental track cards

```text
Track A and Track B: upbeat jazz, instrumental; no vocals in either fixture track.
```

**Full instruction:** For this request, build an upbeat instrumental jazz playlist and exclude vocal tracks.

**Rationale:** The upbeat instrumental jazz tracks satisfy the explicit vocal exclusion.

## SC1-V3-SX1-F044-K-A2

**Prefix:** For this request, build an upbeat instrumental jazz playlist

**Action:** Prepare a vocal-track exclusion predicate

```text
Keep a supplied track only when has_vocals is false; no titles embedded.
```

**Full instruction:** For this request, build an upbeat instrumental jazz playlist and exclude vocal tracks.

**Rationale:** The predicate implements the required exclusion of vocal tracks.

## SC1-V3-SX1-F045-K-A1

**Prefix:** For this request, choose a non-horror movie under two hours for tonight

**Action:** Retrieve movie cards

```text
Film A: comedy, 90 minutes; Film B: drama, 105 minutes; both explicitly not horror.
```

**Full instruction:** For this request, choose a non-horror movie under two hours for tonight and compare the listed eligible options.

**Rationale:** Both non-horror movie cards satisfy the original under-two-hour selection constraints.

## SC1-V3-SX1-F045-K-A2

**Prefix:** For this request, choose a non-horror movie under two hours for tonight

**Action:** Stage a generic movie comparison layout

```text
Columns: title, genre, runtime, availability tonight; no candidate titles or restrictions filled in.
```

**Full instruction:** For this request, choose a non-horror movie under two hours for tonight and compare the listed eligible options.

**Rationale:** The generic title, genre, runtime and availability columns remain usable for the eligible movie comparison.

## SC1-V3-SX1-F045-R-A2

**Prefix:** For this request, choose a non-horror movie under two hours for tonight

**Action:** Stage a generic movie comparison layout

```text
Columns: title, genre, runtime, availability tonight; no candidate titles or restrictions filled in.
```

**Full instruction:** For this request, choose a non-horror movie under two hours for tonight but choose a horror movie longer than two hours instead.

**Rationale:** The generic movie columns remain usable for the revised horror and runtime choices.

## SC1-V3-SX1-F046-K-A1

**Prefix:** For this request, find technical podcast interviews about AI agents

**Action:** Retrieve interview episode cards

```text
Episode I and Episode J: technical AI-agent interviews; neither is a news roundup.
```

**Full instruction:** For this request, find technical podcast interviews about AI agents and favor interviews over news roundups.

**Rationale:** The technical AI-agent interviews satisfy the preference for interviews over roundups.

## SC1-V3-SX1-F046-K-A2

**Prefix:** For this request, find technical podcast interviews about AI agents

**Action:** Prepare the topic query

```text
Topic query: AI agents; no episode-format restriction.
```

**Full instruction:** For this request, find technical podcast interviews about AI agents and favor interviews over news roundups.

**Rationale:** The AI-agents topic query remains applicable to the requested interviews.

## SC1-V3-SX1-F046-R-A2

**Prefix:** For this request, find technical podcast interviews about AI agents

**Action:** Prepare the topic query

```text
Topic query: AI agents; no episode-format restriction.
```

**Full instruction:** For this request, find technical podcast interviews about AI agents but use only news roundups and exclude interviews.

**Rationale:** The AI-agents topic query remains usable when the required episode format changes to news roundups.

## SC1-V3-SX1-F047-K-A1

**Prefix:** For this request, make a three-day business-trip packing checklist

**Action:** Draft the clothing checklist

```text
Two business shirts; one pair of office trousers; office shoes. No formalwear included.
```

**Full instruction:** For this request, make a three-day business-trip packing checklist and omit formalwear.

**Rationale:** The business clothing checklist already omits formalwear as required.

## SC1-V3-SX1-F047-K-A2

**Prefix:** For this request, make a three-day business-trip packing checklist

**Action:** Draft the shared essentials checklist

```text
Toothbrush; phone charger; personal identification. No destination-specific supplies included.
```

**Full instruction:** For this request, make a three-day business-trip packing checklist and omit formalwear.

**Rationale:** The toothbrush, charger and identification remain useful business-trip essentials.

## SC1-V3-SX1-F047-R-A2

**Prefix:** For this request, make a three-day business-trip packing checklist

**Action:** Draft the shared essentials checklist

```text
Toothbrush; phone charger; personal identification. No destination-specific supplies included.
```

**Full instruction:** For this request, make a three-day business-trip packing checklist but make it a three-day camping checklist instead, with no business clothing.

**Rationale:** The essential-item checklist remains useful for camping and includes no business clothing.

## SC1-V3-SX1-F048-K-A1

**Prefix:** For this request, plan my morning around a 9 AM appointment

**Action:** Calculate the original departure time

```text
For a 09:00 arrival and 30 minutes travel, depart at 08:30.
```

**Full instruction:** For this request, plan my morning around a 9 AM appointment and reserve 30 minutes to travel there.

**Rationale:** The 08:30 departure correctly allows 30 minutes before the retained 9 AM appointment.

## SC1-V3-SX1-F048-K-A2

**Prefix:** For this request, plan my morning around a 9 AM appointment

**Action:** Prepare the travel-duration field

```text
Travel duration field: 30 minutes; no appointment or departure time filled in.
```

**Full instruction:** For this request, plan my morning around a 9 AM appointment and reserve 30 minutes to travel there.

**Rationale:** The 30-minute field matches the travel allowance required by the final plan.

## SC1-V3-SX1-F048-R-A2

**Prefix:** For this request, plan my morning around a 9 AM appointment

**Action:** Prepare the travel-duration field

```text
Travel duration field: 30 minutes; no appointment or departure time filled in.
```

**Full instruction:** For this request, plan my morning around a 9 AM appointment but move the appointment to 11 AM while retaining the 30-minute travel requirement.

**Rationale:** The travel requirement remains 30 minutes after the appointment moves.

## SC1-V3-SX1-F049-K-A1

**Prefix:** For this request, build a shopping list for vegetarian tacos

**Action:** Draft the protein ingredient

```text
One tin of beans; no meat.
```

**Full instruction:** For this request, build a shopping list for vegetarian tacos and include beans instead of meat.

**Rationale:** The beans entry is explicitly requested instead of meat.

## SC1-V3-SX1-F049-K-A2

**Prefix:** For this request, build a shopping list for vegetarian tacos

**Action:** Draft the shared taco ingredients

```text
Tortillas, tomatoes and lettuce; no protein ingredient selected.
```

**Full instruction:** For this request, build a shopping list for vegetarian tacos and include beans instead of meat.

**Rationale:** The shared taco ingredients remain usable alongside the required beans.

## SC1-V3-SX1-F049-R-A2

**Prefix:** For this request, build a shopping list for vegetarian tacos

**Action:** Draft the shared taco ingredients

```text
Tortillas, tomatoes and lettuce; no protein ingredient selected.
```

**Full instruction:** For this request, build a shopping list for vegetarian tacos but make beef tacos instead and omit beans.

**Rationale:** The shared taco ingredients survive the change to beef with beans omitted.

## SC1-V3-SX1-F050-K-A1

**Prefix:** For this request, prioritize today's tasks with the client deadline first

**Action:** Stage the original ordering

```text
1. Client deadline; 2. Server incident; 3. File receipts.
```

**Full instruction:** For this request, prioritize today's tasks with the client deadline first and keep the client deadline at the top.

**Rationale:** The staged ordering already places the client deadline first as required.

## SC1-V3-SX1-F050-K-A2

**Prefix:** For this request, prioritize today's tasks with the client deadline first

**Action:** Extract today's task inventory

```text
Tasks due today: client deadline, server incident, file receipts; inventory has no priority ordering.
```

**Full instruction:** For this request, prioritize today's tasks with the client deadline first and keep the client deadline at the top.

**Rationale:** The unordered task inventory can be reused in the required client-first list.

## SC1-V3-SX1-F050-R-A2

**Prefix:** For this request, prioritize today's tasks with the client deadline first

**Action:** Extract today's task inventory

```text
Tasks due today: client deadline, server incident, file receipts; inventory has no priority ordering.
```

**Full instruction:** For this request, prioritize today's tasks with the client deadline first but put the server incident first and move the client deadline below it.

**Rationale:** The unordered task inventory can be used unchanged to prioritize the server incident.

## SC1-V4-SX1-F001-K-A1

**Prefix:** Help me compare flights from Harborview to Eastport

**Action:** Retrieve two route-specific fares

```text
Harborview–Eastport 08:00, 120 credits; Harborview–Eastport 10:00, 150 credits.
```

**Full instruction:** Help me compare flights from Harborview to Eastport and show the two listed morning options.

**Rationale:** The route-specific cards contain the two requested morning flights.

## SC1-V4-SX1-F002-K-A1

**Prefix:** Help me find hotels near Maple Station

**Action:** Retrieve station-specific hotel cards

```text
Maple Lodge: 3-minute walk to Maple Station; Maple House: 5-minute walk.
```

**Full instruction:** Help me find hotels near Maple Station and compare the two listed hotels by walking distance.

**Rationale:** The Maple hotel walking distances directly support the requested comparison.

## SC1-V4-SX1-F002-K-A2

**Prefix:** Help me find hotels near Maple Station

**Action:** Stage a hotel comparison layout

```text
Columns: hotel name, distance to requested station, nightly price; no hotels filled in.
```

**Full instruction:** Help me find hotels near Maple Station and compare the two listed hotels by walking distance.

**Rationale:** The hotel layout already supports comparing walking distance to the requested station.

## SC1-V4-SX1-F002-R-A2

**Prefix:** Help me find hotels near Maple Station

**Action:** Stage a hotel comparison layout

```text
Columns: hotel name, distance to requested station, nightly price; no hotels filled in.
```

**Full instruction:** Help me find hotels near Maple Station but use Pine Station instead and omit Maple Station hotels.

**Rationale:** The station-neutral hotel layout can compare Pine Station hotels without revising its headings.

## SC1-V4-SX1-F003-K-A1

**Prefix:** Help me compare Friday car rentals at North Terminal

**Action:** Retrieve terminal-specific rental cards

```text
North Terminal: Compact A, 40 credits/day; Compact B, 45 credits/day. Both are North-only pickups.
```

**Full instruction:** Help me compare Friday car rentals at North Terminal and keep pickup at North Terminal.

**Rationale:** The retrieved rental cards match the retained North Terminal pickup.

## SC1-V4-SX1-F003-K-A2

**Prefix:** Help me compare Friday car rentals at North Terminal

**Action:** Prepare the comparison calculation

```text
Total rental cost = daily rate × number of days + disclosed fees; values remain unfilled.
```

**Full instruction:** Help me compare Friday car rentals at North Terminal and keep pickup at North Terminal.

**Rationale:** The symbolic rental-cost calculation remains usable with North Terminal rates.

## SC1-V4-SX1-F003-R-A2

**Prefix:** Help me compare Friday car rentals at North Terminal

**Action:** Prepare the comparison calculation

```text
Total rental cost = daily rate × number of days + disclosed fees; values remain unfilled.
```

**Full instruction:** Help me compare Friday car rentals at North Terminal but pickup must be at South Terminal instead, with no North Terminal results.

**Rationale:** The unfilled rental-cost expression can calculate South Terminal prices unchanged.

## SC1-V4-SX1-F004-K-A1

**Prefix:** Help me compare nonstop flights to Eastport

**Action:** Retrieve nonstop route cards

```text
Route N1: nonstop, 2 hours; route N2: nonstop, 3 hours. Neither includes a stop.
```

**Full instruction:** Help me compare nonstop flights to Eastport and list only nonstop itineraries.

**Rationale:** Both route cards satisfy the retained nonstop requirement.

## SC1-V4-SX1-F004-K-A2

**Prefix:** Help me compare nonstop flights to Eastport

**Action:** Prepare the requested destination field

```text
Destination field: Eastport; no route or fare chosen.
```

**Full instruction:** Help me compare nonstop flights to Eastport and list only nonstop itineraries.

**Rationale:** Eastport remains the requested destination for nonstop itineraries.

## SC1-V4-SX1-F004-R-A2

**Prefix:** Help me compare nonstop flights to Eastport

**Action:** Prepare the requested destination field

```text
Destination field: Eastport; no route or fare chosen.
```

**Full instruction:** Help me compare nonstop flights to Eastport but I now want only one-stop itineraries to Eastport.

**Rationale:** The Eastport destination field survives replacing nonstop with one-stop itineraries.

## SC1-V4-SX1-F005-K-A1

**Prefix:** Help me find Italian restaurants around Cedar Square

**Action:** Retrieve cuisine-specific restaurant cards

```text
Cedar Pasta: Italian, outdoor seating; Olive Room: Italian, outdoor seating; neither serves Thai cuisine.
```

**Full instruction:** Help me find Italian restaurants around Cedar Square and choose places with outdoor seating.

**Rationale:** Both Italian restaurant cards already meet the outdoor-seating constraint.

## SC1-V4-SX1-F005-K-A2

**Prefix:** Help me find Italian restaurants around Cedar Square

**Action:** Prepare the location field

```text
Search area: Cedar Square; cuisine, hours and price remain unfilled.
```

**Full instruction:** Help me find Italian restaurants around Cedar Square and choose places with outdoor seating.

**Rationale:** Cedar Square remains the restaurant search area.

## SC1-V4-SX1-F005-R-A2

**Prefix:** Help me find Italian restaurants around Cedar Square

**Action:** Prepare the location field

```text
Search area: Cedar Square; cuisine, hours and price remain unfilled.
```

**Full instruction:** Help me find Italian restaurants around Cedar Square but change the cuisine to Thai and exclude Italian restaurants.

**Rationale:** The Cedar Square location field remains unchanged when the cuisine changes to Thai.

## SC1-V4-SX1-F006-K-A1

**Prefix:** Help me find bakeries around Birch Park

**Action:** Retrieve bakery cards

```text
Birch Bake: bakery with coffee; Loaf House: bakery with coffee; neither is a pharmacy.
```

**Full instruction:** Help me find bakeries around Birch Park that serve coffee, including the two listed options.

**Rationale:** Both bakery cards explicitly include coffee as required.

## SC1-V4-SX1-F006-K-A2

**Prefix:** Help me find bakeries around Birch Park

**Action:** Prepare a bakery-only comparison layout

```text
Columns: bakery name, bread selection, pastry selection, coffee availability; four fixed headings.
```

**Full instruction:** Help me find bakeries around Birch Park that serve coffee, including the two listed options.

**Rationale:** The bakery-specific layout includes the requested coffee comparison.

## SC1-V4-SX1-F007-K-A1

**Prefix:** Help me find gyms in Riverton that sell day passes

**Action:** Retrieve day-pass gym cards

```text
River Fit: day passes and sauna; North Fit: day passes and sauna. Both sell day passes.
```

**Full instruction:** Help me find gyms in Riverton that sell day passes and prioritize day-pass gyms with a sauna.

**Rationale:** Both gym cards explicitly provide day passes and saunas as requested.

## SC1-V4-SX1-F007-K-A2

**Prefix:** Help me find gyms in Riverton that sell day passes

**Action:** Prepare the location field

```text
City field: Riverton; membership type remains unfilled.
```

**Full instruction:** Help me find gyms in Riverton that sell day passes and prioritize day-pass gyms with a sauna.

**Rationale:** Riverton remains the correct city for the sauna-equipped day-pass gym search.

## SC1-V4-SX1-F007-R-A2

**Prefix:** Help me find gyms in Riverton that sell day passes

**Action:** Prepare the location field

```text
City field: Riverton; membership type remains unfilled.
```

**Full instruction:** Help me find gyms in Riverton that sell day passes but only consider members-only gyms that do not sell day passes.

**Rationale:** The Riverton city field remains valid for the members-only gym search.

## SC1-V4-SX1-F008-K-A1

**Prefix:** Help me find pharmacies in Brookfield that are open now

**Action:** Retrieve open pharmacy cards

```text
Brook Pharmacy: open now, standalone; Elm Pharmacy: open now, standalone. Neither is hospital-based.
```

**Full instruction:** Help me find pharmacies in Brookfield that are open now and omit hospital-based pharmacies.

**Rationale:** Both retrieved pharmacies are open and standalone, satisfying the hospital exclusion.

## SC1-V4-SX1-F008-K-A2

**Prefix:** Help me find pharmacies in Brookfield that are open now

**Action:** Prepare the search time reference

```text
Fixture clock: Monday 14:00 local time; tomorrow resolves to Tuesday in this fixture.
```

**Full instruction:** Help me find pharmacies in Brookfield that are open now and omit hospital-based pharmacies.

**Rationale:** The fixed local clock supplies the time reference needed to evaluate open-now pharmacy results.

## SC1-V4-SX1-F008-R-A2

**Prefix:** Help me find pharmacies in Brookfield that are open now

**Action:** Prepare the search time reference

```text
Fixture clock: Monday 14:00 local time; tomorrow resolves to Tuesday in this fixture.
```

**Full instruction:** Help me find pharmacies in Brookfield that are open now but only list hospital pharmacies that are closed now and open tomorrow.

**Rationale:** The fixed Monday clock resolves both closed-now and open-tomorrow checks.

## SC1-V4-SX1-F009-K-A1

**Prefix:** Help me research local robotic actuator manufacturers

**Action:** Retrieve manufacturer cards

```text
Aster Motion and Delta Drive manufacture robotic actuators locally; neither distributes other makers' parts.
```

**Full instruction:** Help me research local robotic actuator manufacturers and retain the manufacturers while adding distributors separately.

**Rationale:** The manufacturer records are explicitly retained while distributors are added separately.

## SC1-V4-SX1-F009-K-A2

**Prefix:** Help me research local robotic actuator manufacturers

**Action:** Prepare the component definition

```text
Robotic actuator: component that converts a control input into mechanical movement; no supplier selected.
```

**Full instruction:** Help me research local robotic actuator manufacturers and retain the manufacturers while adding distributors separately.

**Rationale:** The component definition remains useful for identifying actuator manufacturers and distributors.

## SC1-V4-SX1-F009-R-A2

**Prefix:** Help me research local robotic actuator manufacturers

**Action:** Prepare the component definition

```text
Robotic actuator: component that converts a control input into mechanical movement; no supplier selected.
```

**Full instruction:** Help me research local robotic actuator manufacturers but list distributors only and exclude manufacturers.

**Rationale:** The actuator definition still identifies the component distributed by the requested suppliers.

## SC1-V4-SX1-F010-K-A1

**Prefix:** Help me compare 15-litre shoulder bags

**Action:** Retrieve bag specification cards

```text
Bag L: shoulder bag, 15 L, 0.5 kg; Bag M: shoulder bag, 15 L, 0.7 kg; neither converts to a backpack.
```

**Full instruction:** Help me compare 15-litre shoulder bags and rank the two listed bags by lower weight.

**Rationale:** The specification cards supply both eligible bags and their ranking weights.

## SC1-V4-SX1-F010-K-A2

**Prefix:** Help me compare 15-litre shoulder bags

**Action:** Prepare a weight-ranking routine

```text
Sort supplied product records by numeric weight_kg ascending; no records or capacity filter embedded.
```

**Full instruction:** Help me compare 15-litre shoulder bags and rank the two listed bags by lower weight.

**Rationale:** The ascending weight routine directly implements the required bag ranking.

## SC1-V4-SX1-F011-K-A1

**Prefix:** Help me find brown faux-suede jackets with stand collars

**Action:** Retrieve jacket cards

```text
Jacket A: brown faux suede, stand collar, 120 credits; Jacket B: brown faux suede, stand collar, 150 credits.
```

**Full instruction:** Help me find brown faux-suede jackets with stand collars and compare the listed options under 200 credits.

**Rationale:** Both jackets match the requested attributes and cost less than 200 credits.

## SC1-V4-SX1-F011-K-A2

**Prefix:** Help me find brown faux-suede jackets with stand collars

**Action:** Stage a product comparison layout

```text
Columns: material, color, collar type, price; values unfilled.
```

**Full instruction:** Help me find brown faux-suede jackets with stand collars and compare the listed options under 200 credits.

**Rationale:** The blank product comparison columns support the required under-200-credit jacket comparison.

## SC1-V4-SX1-F011-R-A2

**Prefix:** Help me find brown faux-suede jackets with stand collars

**Action:** Stage a product comparison layout

```text
Columns: material, color, collar type, price; values unfilled.
```

**Full instruction:** Help me find brown faux-suede jackets with stand collars but use black cotton jackets with lapels instead and discard the original options.

**Rationale:** The unfilled jacket comparison columns remain appropriate for black cotton lapel jackets.

## SC1-V4-SX1-F012-K-A1

**Prefix:** Help me compare robotics synthetic-data tools that support Engine R

**Action:** Retrieve tool compatibility cards

```text
Sim A and Sim B support Engine R only; neither supports Engine S.
```

**Full instruction:** Help me compare robotics synthetic-data tools that support Engine R and keep Engine R support mandatory.

**Rationale:** Both compatibility cards meet the mandatory Engine R requirement.

## SC1-V4-SX1-F012-K-A2

**Prefix:** Help me compare robotics synthetic-data tools that support Engine R

**Action:** Prepare a physics-evaluation checklist

```text
Check gravity, collision response, sensor noise and deterministic replay; no engine-specific commands.
```

**Full instruction:** Help me compare robotics synthetic-data tools that support Engine R and keep Engine R support mandatory.

**Rationale:** The engine-neutral physics checklist provides reusable criteria for comparing the tools.

## SC1-V4-SX1-F012-R-A2

**Prefix:** Help me compare robotics synthetic-data tools that support Engine R

**Action:** Prepare a physics-evaluation checklist

```text
Check gravity, collision response, sensor noise and deterministic replay; no engine-specific commands.
```

**Full instruction:** Help me compare robotics synthetic-data tools that support Engine R but only consider tools for Engine S that do not support Engine R.

**Rationale:** The engine-independent evaluation checklist remains usable for Engine S tools.

## SC1-V4-SX1-F013-K-A1

**Prefix:** Help me find freestanding desk converters under 250 credits

**Action:** Retrieve converter cards

```text
Lift A: freestanding, 150 credits; Lift B: freestanding, 220 credits. Neither can be permanently mounted.
```

**Full instruction:** Help me find freestanding desk converters under 250 credits and exclude permanently mounted converters.

**Rationale:** Both freestanding converter cards fit the price limit and exclusion of permanent mounting.

## SC1-V4-SX1-F013-K-A2

**Prefix:** Help me find freestanding desk converters under 250 credits

**Action:** Prepare the price ceiling field

```text
Maximum price field: 250 credits; mounting type unfilled.
```

**Full instruction:** Help me find freestanding desk converters under 250 credits and exclude permanently mounted converters.

**Rationale:** The 250-credit ceiling remains a valid converter search field.

## SC1-V4-SX1-F013-R-A2

**Prefix:** Help me find freestanding desk converters under 250 credits

**Action:** Prepare the price ceiling field

```text
Maximum price field: 250 credits; mounting type unfilled.
```

**Full instruction:** Help me find freestanding desk converters under 250 credits but only show permanently mounted converters and discard freestanding ones.

**Rationale:** The price ceiling survives the change in mounting type.

## SC1-V4-SX1-F014-K-A1

**Prefix:** Help me find a 30-minute meeting for Sam and me on Tuesday

**Action:** Read Tuesday availability

```text
Sam and requester both free Tuesday 14:00–14:30 and 15:00–15:30. No Wednesday availability included.
```

**Full instruction:** Help me find a 30-minute meeting for Sam and me on Tuesday and use either of the two listed Tuesday slots.

**Rationale:** The two Tuesday openings match the requested day, attendees and duration.

## SC1-V4-SX1-F014-R-A2

**Prefix:** Help me find a 30-minute meeting for Sam and me on Tuesday

**Action:** Stage a Wednesday calendar event

```text
Unsent event object: attendees Sam and requester, duration 30 minutes, day Wednesday; no time set.
```

**Full instruction:** Help me find a 30-minute meeting for Sam and me on Tuesday but switch the meeting to Wednesday and ignore Tuesday availability.

**Rationale:** The staged Wednesday event matches the revised day and retained participants and duration.

## SC1-V4-SX1-F015-K-A1

**Prefix:** Help me check whether my dentist can see me on Friday

**Action:** Read Friday availability

```text
The fixture dentist has no Friday openings; no Monday availability included.
```

**Full instruction:** Help me check whether my dentist can see me on Friday and keep my existing appointment if Friday has no openings.

**Rationale:** The absence of Friday openings determines that the existing appointment should be kept.

## SC1-V4-SX1-F015-K-A2

**Prefix:** Help me check whether my dentist can see me on Friday

**Action:** Retrieve the existing appointment

```text
Current appointment: Wednesday 11:00, dentist Dr Vale, appointment ID D17.
```

**Full instruction:** Help me check whether my dentist can see me on Friday and keep my existing appointment if Friday has no openings.

**Rationale:** The existing appointment record identifies the fallback that must be retained.

## SC1-V4-SX1-F015-R-A2

**Prefix:** Help me check whether my dentist can see me on Friday

**Action:** Retrieve the existing appointment

```text
Current appointment: Wednesday 11:00, dentist Dr Vale, appointment ID D17.
```

**Full instruction:** Help me check whether my dentist can see me on Friday but check Monday instead and ignore Friday openings, keeping my existing appointment as fallback.

**Rationale:** The existing appointment remains the explicit fallback after availability changes to Monday.

## SC1-V4-SX1-F016-K-A1

**Prefix:** Help me find team meeting slots this week after 10 AM

**Action:** Read afternoon team availability

```text
Whole team free Thursday 13:00–13:30 and Friday 14:00–14:30; no morning data included.
```

**Full instruction:** Help me find team meeting slots this week after 10 AM and show the two listed afternoon slots.

**Rationale:** The Thursday and Friday afternoon slots satisfy the requested after-10-AM availability search.

## SC1-V4-SX1-F016-K-A2

**Prefix:** Help me find team meeting slots this week after 10 AM

**Action:** Prepare the participant list

```text
Participants: Sam, Jo and requester; no time selected.
```

**Full instruction:** Help me find team meeting slots this week after 10 AM and show the two listed afternoon slots.

**Rationale:** The participant list remains useful for finding the team's requested slots.

## SC1-V4-SX1-F016-R-A2

**Prefix:** Help me find team meeting slots this week after 10 AM

**Action:** Prepare the participant list

```text
Participants: Sam, Jo and requester; no time selected.
```

**Full instruction:** Help me find team meeting slots this week after 10 AM but only consider slots before 10 AM this week.

**Rationale:** The same participant list applies to morning availability.

## SC1-V4-SX1-F017-K-A1

**Prefix:** Help me prepare a report reminder for tomorrow morning

**Action:** Stage a morning reminder

```text
Unsent reminder: title Submit report, day tomorrow, time 09:00.
```

**Full instruction:** Help me prepare a report reminder for tomorrow morning and set its time to 9 AM.

**Rationale:** The unsent reminder already has the required title, tomorrow date and 9 AM time.

## SC1-V4-SX1-F017-K-A2

**Prefix:** Help me prepare a report reminder for tomorrow morning

**Action:** Prepare the reminder text

```text
Reminder title: Submit report; date and time unfilled.
```

**Full instruction:** Help me prepare a report reminder for tomorrow morning and set its time to 9 AM.

**Rationale:** The Submit report title remains usable when the 9 AM schedule is added.

## SC1-V4-SX1-F017-R-A2

**Prefix:** Help me prepare a report reminder for tomorrow morning

**Action:** Prepare the reminder text

```text
Reminder title: Submit report; date and time unfilled.
```

**Full instruction:** Help me prepare a report reminder for tomorrow morning but change it to tomorrow evening at 7 PM.

**Rationale:** The Submit report title remains correct when the reminder time moves to 7 PM.

## SC1-V4-SX1-F018-K-A1

**Prefix:** Help me draft a reply thanking Morgan for the introduction

**Action:** Draft the thank-you sentence

```text
Thank you for making the introduction, Morgan.
```

**Full instruction:** Help me draft a reply thanking Morgan for the introduction and offer to provide more information.

**Rationale:** The thank-you sentence remains required when an offer of further information is added.

## SC1-V4-SX1-F018-K-A2

**Prefix:** Help me draft a reply thanking Morgan for the introduction

**Action:** Draft an offer sentence

```text
I would be happy to provide any additional information you need.
```

**Full instruction:** Help me draft a reply thanking Morgan for the introduction and offer to provide more information.

**Rationale:** The information-offer sentence is expressly requested in the final reply.

## SC1-V4-SX1-F019-K-A1

**Prefix:** Help me draft a team update saying the build is delayed

**Action:** Draft the status sentence

```text
The build is delayed; we are still investigating the cause.
```

**Full instruction:** Help me draft a team update saying the build is delayed and keep the cause neutral because it is not yet known.

**Rationale:** The delay sentence avoids attributing an unknown cause.

## SC1-V4-SX1-F019-K-A2

**Prefix:** Help me draft a team update saying the build is delayed

**Action:** Stage a neutral update heading

```text
Heading: Build status update; no status claim or cause included.
```

**Full instruction:** Help me draft a team update saying the build is delayed and keep the cause neutral because it is not yet known.

**Rationale:** The neutral build-status heading does not speculate about the delay's cause.

## SC1-V4-SX1-F019-R-A2

**Prefix:** Help me draft a team update saying the build is delayed

**Action:** Stage a neutral update heading

```text
Heading: Build status update; no status claim or cause included.
```

**Full instruction:** Help me draft a team update saying the build is delayed but the build is on schedule, so report that and do not mention a delay.

**Rationale:** The neutral build-status heading survives the correction to on schedule.

## SC1-V4-SX1-F020-K-A1

**Prefix:** Help me draft a message declining dinner tonight

**Action:** Draft the decline sentence

```text
I cannot make dinner tonight.
```

**Full instruction:** Help me draft a message declining dinner tonight and suggest meeting next weekend.

**Rationale:** The decline sentence remains required alongside the next-weekend suggestion.

## SC1-V4-SX1-F020-K-A2

**Prefix:** Help me draft a message declining dinner tonight

**Action:** Draft the alternative-date sentence

```text
Would you like to meet next weekend instead?
```

**Full instruction:** Help me draft a message declining dinner tonight and suggest meeting next weekend.

**Rationale:** The next-weekend sentence directly supplies the requested alternative date.

## SC1-V4-SX1-F021-K-A1

**Prefix:** Help me draft a refund approval message

**Action:** Draft the approval sentence

```text
Your refund has been approved.
```

**Full instruction:** Help me draft a refund approval message and avoid promising a payment date.

**Rationale:** The approval sentence makes no payment-date promise and remains valid.

## SC1-V4-SX1-F021-K-A2

**Prefix:** Help me draft a refund approval message

**Action:** Stage an approval-specific reply template

```text
Subject: Refund approved. Closing: Thank you for your patience. Body unfilled.
```

**Full instruction:** Help me draft a refund approval message and avoid promising a payment date.

**Rationale:** The refund approval template promises no payment date.

## SC1-V4-SX1-F022-K-A1

**Prefix:** Help me find peer-reviewed papers about hidden-state probing

**Action:** Retrieve peer-reviewed fixture records

```text
Paper P and Paper Q: peer-reviewed hidden-state probing papers in the synthetic catalogue; no technical reports included.
```

**Full instruction:** Help me find peer-reviewed papers about hidden-state probing and use only peer-reviewed sources.

**Rationale:** The two peer-reviewed probing records satisfy the final source restriction.

## SC1-V4-SX1-F022-K-A2

**Prefix:** Help me find peer-reviewed papers about hidden-state probing

**Action:** Prepare the topic search terms

```text
Terms: hidden-state probing, representation analysis; no publication-type filter.
```

**Full instruction:** Help me find peer-reviewed papers about hidden-state probing and use only peer-reviewed sources.

**Rationale:** The probing search terms remain usable with the required peer-reviewed source filter.

## SC1-V4-SX1-F022-R-A2

**Prefix:** Help me find peer-reviewed papers about hidden-state probing

**Action:** Prepare the topic search terms

```text
Terms: hidden-state probing, representation analysis; no publication-type filter.
```

**Full instruction:** Help me find peer-reviewed papers about hidden-state probing but use only non-peer-reviewed technical reports about hidden-state probing.

**Rationale:** The probing topic terms carry over to technical-report retrieval.

## SC1-V4-SX1-F023-K-A1

**Prefix:** Help me find version 3 documentation for Library L

**Action:** Retrieve versioned documentation

```text
Official Library L version 3: old_connect(endpoint) is the connection entry point. This fixture marks it removed in version 4.
```

**Full instruction:** Help me find version 3 documentation for Library L and use only the official version 3 material.

**Rationale:** The retrieved official version 3 entry point matches the final version and source requirements.

## SC1-V4-SX1-F023-K-A2

**Prefix:** Help me find version 3 documentation for Library L

**Action:** Retrieve the official documentation index URL

```text
Fixture URL: https://library-l.example/docs/ ; index lists version 3 and version 4.
```

**Full instruction:** Help me find version 3 documentation for Library L and use only the official version 3 material.

**Rationale:** The official index already provides a reusable route to version 3 documentation.

## SC1-V4-SX1-F023-R-A2

**Prefix:** Help me find version 3 documentation for Library L

**Action:** Retrieve the official documentation index URL

```text
Fixture URL: https://library-l.example/docs/ ; index lists version 3 and version 4.
```

**Full instruction:** Help me find version 3 documentation for Library L but use version 4 instead and exclude all version 3 documentation.

**Rationale:** The official index contains version 4 and remains usable after the version change.

## SC1-V4-SX1-F024-K-A1

**Prefix:** Help me compare Acme's revenue in its two annual releases

**Action:** Extract Acme revenue figures

```text
Acme fixture: prior year revenue 10 million credits; current year 12 million credits.
```

**Full instruction:** Help me compare Acme's revenue in its two annual releases and report company-stated actual revenue only.

**Rationale:** The extracted Acme revenue figures are the company-specific actual values required for comparison.

## SC1-V4-SX1-F025-K-A1

**Prefix:** Help me find primary rules for Region A consumer AI systems

**Action:** Retrieve jurisdiction-specific rule cards

```text
Rule A1 and Rule A2: synthetic Region A consumer-AI rules, with no applicability in Region B.
```

**Full instruction:** Help me find primary rules for Region A consumer AI systems and keep Region A as the main jurisdiction.

**Rationale:** The Region A rule cards match the retained jurisdiction.

## SC1-V4-SX1-F025-K-A2

**Prefix:** Help me find primary rules for Region A consumer AI systems

**Action:** Stage a legal-source comparison layout

```text
Columns: jurisdiction, issuing authority, effective date, provision; no legal claims filled in.
```

**Full instruction:** Help me find primary rules for Region A consumer AI systems and keep Region A as the main jurisdiction.

**Rationale:** The legal-source columns remain applicable to Region A rules.

## SC1-V4-SX1-F025-R-A2

**Prefix:** Help me find primary rules for Region A consumer AI systems

**Action:** Stage a legal-source comparison layout

```text
Columns: jurisdiction, issuing authority, effective date, provision; no legal claims filled in.
```

**Full instruction:** Help me find primary rules for Region A consumer AI systems but use Region B rules only and exclude Region A rules.

**Rationale:** The blank jurisdiction, authority, date and provision columns can compare Region B sources unchanged.

## SC1-V4-SX1-F026-K-A1

**Prefix:** Help me compare small open-weight reasoning models

**Action:** Collect vendor-only benchmark claims

```text
Vendor card: Model K claims 80 points and Model J claims 85 points; neither claim is independently reproduced.
```

**Full instruction:** Help me compare small open-weight reasoning models and flag vendor-only scores as unverified rather than treating them as evidence.

**Rationale:** The vendor claims can be explicitly reported as unverified as instructed.

## SC1-V4-SX1-F026-K-A2

**Prefix:** Help me compare small open-weight reasoning models

**Action:** Collect independent fixture benchmark records

```text
Independent lab fixture: Model K 70 points, Model J 72 points, same test and evaluation settings; both small and open-weight.
```

**Full instruction:** Help me compare small open-weight reasoning models and flag vendor-only scores as unverified rather than treating them as evidence.

**Rationale:** The independent same-test benchmark scores provide reusable comparison evidence.

## SC1-V4-SX1-F026-R-A2

**Prefix:** Help me compare small open-weight reasoning models

**Action:** Collect independent fixture benchmark records

```text
Independent lab fixture: Model K 70 points, Model J 72 points, same test and evaluation settings; both small and open-weight.
```

**Full instruction:** Help me compare small open-weight reasoning models but include only independently reproduced scores and omit vendor-only claims entirely.

**Rationale:** The independently reproduced fixture scores remain admissible evidence.

## SC1-V4-SX1-F027-K-A1

**Prefix:** Help me calculate a 7 percent downside scenario for a 100-credit index

**Action:** Calculate the requested scenario

```text
100 × (1 − 0.07) = 93 credits; only the 7% result retained.
```

**Full instruction:** Help me calculate a 7 percent downside scenario for a 100-credit index and show the hypothetical level without making a trade.

**Rationale:** The 93-credit result is the requested hypothetical downside level.

## SC1-V4-SX1-F027-K-A2

**Prefix:** Help me calculate a 7 percent downside scenario for a 100-credit index

**Action:** Prepare the scenario formula

```text
Scenario level = starting level × (1 − decline_fraction); no numeric assumptions embedded.
```

**Full instruction:** Help me calculate a 7 percent downside scenario for a 100-credit index and show the hypothetical level without making a trade.

**Rationale:** The symbolic downside formula can calculate the required hypothetical 7 percent result.

## SC1-V4-SX1-F027-R-A2

**Prefix:** Help me calculate a 7 percent downside scenario for a 100-credit index

**Action:** Prepare the scenario formula

```text
Scenario level = starting level × (1 − decline_fraction); no numeric assumptions embedded.
```

**Full instruction:** Help me calculate a 7 percent downside scenario for a 100-credit index but use a 12 percent decline instead and omit the 7 percent case.

**Rationale:** The unfilled downside formula survives correcting the decline to 12 percent.

## SC1-V4-SX1-F028-K-A1

**Prefix:** Help me calculate budget variance from my supplied table

**Action:** Compute category variances

```text
Fixture variances: supplies +20 credits, travel +5 credits, meals −10 credits; positive means overspend.
```

**Full instruction:** Help me calculate budget variance from my supplied table and identify the largest overspend.

**Rationale:** The variance figures identify supplies as the largest overspend.

## SC1-V4-SX1-F028-K-A2

**Prefix:** Help me calculate budget variance from my supplied table

**Action:** Aggregate actual category totals

```text
Fixture actuals: supplies 120 credits, travel 85 credits, meals 40 credits; source-table sums retained.
```

**Full instruction:** Help me calculate budget variance from my supplied table and identify the largest overspend.

**Rationale:** The actual category totals remain necessary inputs to the variance calculation.

## SC1-V4-SX1-F028-R-A2

**Prefix:** Help me calculate budget variance from my supplied table

**Action:** Aggregate actual category totals

```text
Fixture actuals: supplies 120 credits, travel 85 credits, meals 40 credits; source-table sums retained.
```

**Full instruction:** Help me calculate budget variance from my supplied table but show actual category totals only, without calculating or reporting variances.

**Rationale:** The retained actual totals directly satisfy the actuals-only output request.

## SC1-V4-SX1-F029-K-A1

**Prefix:** Help me compare current holdings with the start-of-month snapshot

**Action:** Calculate start-of-month concentration

```text
Start-of-month fixture: asset A 60%, asset B 40%; no other date included.
```

**Full instruction:** Help me compare current holdings with the start-of-month snapshot and report concentration changes for those two snapshots.

**Rationale:** The start-of-month allocation supplies one of the two required concentration snapshots.

## SC1-V4-SX1-F029-K-A2

**Prefix:** Help me compare current holdings with the start-of-month snapshot

**Action:** Calculate current concentration

```text
Current fixture: asset A 50%, asset B 50%; values unchanged across comparisons.
```

**Full instruction:** Help me compare current holdings with the start-of-month snapshot and report concentration changes for those two snapshots.

**Rationale:** The current 50/50 concentration remains one of the two required comparison snapshots.

## SC1-V4-SX1-F029-R-A2

**Prefix:** Help me compare current holdings with the start-of-month snapshot

**Action:** Calculate current concentration

```text
Current fixture: asset A 50%, asset B 50%; values unchanged across comparisons.
```

**Full instruction:** Help me compare current holdings with the start-of-month snapshot but compare current holdings with the start-of-year snapshot instead and ignore start-of-month holdings.

**Rationale:** The current concentration survives replacing the historical comparison with start of year.

## SC1-V4-SX1-F030-K-A1

**Prefix:** Help me calculate breakeven for my debit spread using the supplied values

**Action:** Calculate the original breakeven

```text
For this fixture's specified call debit spread: 100 + 5 = 105 credits.
```

**Full instruction:** Help me calculate breakeven for my debit spread using the supplied values and use the supplied 5-credit debit and 100-credit lower strike.

**Rationale:** The 105-credit result uses the specified 100-credit strike and 5-credit debit.

## SC1-V4-SX1-F030-K-A2

**Prefix:** Help me calculate breakeven for my debit spread using the supplied values

**Action:** Prepare the symbolic breakeven expression

```text
For the specified call debit spread: lower_strike + net_debit; no prices filled in.
```

**Full instruction:** Help me calculate breakeven for my debit spread using the supplied values and use the supplied 5-credit debit and 100-credit lower strike.

**Rationale:** The symbolic breakeven expression supports the supplied 100-credit strike and five-credit debit.

## SC1-V4-SX1-F030-R-A2

**Prefix:** Help me calculate breakeven for my debit spread using the supplied values

**Action:** Prepare the symbolic breakeven expression

```text
For the specified call debit spread: lower_strike + net_debit; no prices filled in.
```

**Full instruction:** Help me calculate breakeven for my debit spread using the supplied values but correct the debit to 8 credits while keeping the lower strike at 100 credits.

**Rationale:** The symbolic breakeven expression accepts the corrected debit without rewriting the formula.

## SC1-V4-SX1-F031-K-A1

**Prefix:** Help me write a Python function that counts ERROR lines in the supplied log

**Action:** Stage an ERROR-counting function

```text
def count_lines(lines): return sum(line.startswith('ERROR ') for line in lines)
```

**Full instruction:** Help me write a Python function that counts ERROR lines in the supplied log and return the count without changing the file.

**Rationale:** The staged ERROR counter satisfies the retained count-only task.

## SC1-V4-SX1-F031-K-A2

**Prefix:** Help me write a Python function that counts ERROR lines in the supplied log

**Action:** Stage a log-reading helper

```text
def read_lines(path):
    with open(path, encoding='utf-8') as f:
        return f.read().splitlines()
```

**Full instruction:** Help me write a Python function that counts ERROR lines in the supplied log and return the count without changing the file.

**Rationale:** The read-only log helper supplies lines for counting without changing the file.

## SC1-V4-SX1-F031-R-A2

**Prefix:** Help me write a Python function that counts ERROR lines in the supplied log

**Action:** Stage a log-reading helper

```text
def read_lines(path):
    with open(path, encoding='utf-8') as f:
        return f.read().splitlines()
```

**Full instruction:** Help me write a Python function that counts ERROR lines in the supplied log but count WARN lines instead and do not count ERROR lines.

**Rationale:** The severity-independent reader supplies log lines unchanged to a WARN counter.

## SC1-V4-SX1-F032-K-A1

**Prefix:** Help me inspect the client timeout path without changing the code

**Action:** Collect a timeout observation

```text
Fixture client.py line 8: DEFAULT_TIMEOUT = 5; request() passes this constant as its timeout argument.
```

**Full instruction:** Help me inspect the client timeout path without changing the code and identify where its five-second timeout is set.

**Rationale:** The constant location and request linkage identify where the five-second timeout is set.

## SC1-V4-SX1-F032-R-A1

**Prefix:** Help me inspect the client timeout path without changing the code

**Action:** Collect a timeout observation

```text
Fixture client.py line 8: DEFAULT_TIMEOUT = 5; request() passes this constant as its timeout argument.
```

**Full instruction:** Help me inspect the client timeout path without changing the code but modify the default timeout to ten seconds instead of producing an inspection report.

**Rationale:** The timeout location and reference identify exactly where the ten-second change must be made.

## SC1-V4-SX1-F032-R-A2

**Prefix:** Help me inspect the client timeout path without changing the code

**Action:** Stage a ten-second timeout patch

```text
Unapplied patch replaces DEFAULT_TIMEOUT = 5 with DEFAULT_TIMEOUT = 10; no other edits.
```

**Full instruction:** Help me inspect the client timeout path without changing the code but modify the default timeout to ten seconds instead of producing an inspection report.

**Rationale:** The staged patch changes the default timeout to the required ten seconds.

## SC1-V4-SX1-F033-K-A1

**Prefix:** Help me refactor the add function while preserving its public name and behavior

**Action:** Stage the preserving refactor

```text
Replacement definition: def add(a, b): return a + b; public symbol remains add.
```

**Full instruction:** Help me refactor the add function while preserving its public name and behavior and keep its existing callers compatible.

**Rationale:** The add definition retains the required public symbol and behavior.

## SC1-V4-SX1-F033-K-A2

**Prefix:** Help me refactor the add function while preserving its public name and behavior

**Action:** Stage addition behavior tests

```text
Assertions: operation(2, 3) == 5; operation(-1, 1) == 0; operation supplied by the test harness, not hardcoded to a name.
```

**Full instruction:** Help me refactor the add function while preserving its public name and behavior and keep its existing callers compatible.

**Rationale:** The name-independent addition assertions remain valid behavior checks.

## SC1-V4-SX1-F033-R-A2

**Prefix:** Help me refactor the add function while preserving its public name and behavior

**Action:** Stage addition behavior tests

```text
Assertions: operation(2, 3) == 5; operation(-1, 1) == 0; operation supplied by the test harness, not hardcoded to a name.
```

**Full instruction:** Help me refactor the add function while preserving its public name and behavior but rename the public function to total and update callers to use total.

**Rationale:** The harness-selected operation lets the behavior tests survive the rename to total.

## SC1-V4-SX1-F034-K-A1

**Prefix:** Help me add malformed-JSON tests to the parser

**Action:** Stage malformed-input test cases

```text
Inputs: an unmatched opening brace, an unfinished numeric array, and an object with an unquoted key; expected outcome for each: parse error.
```

**Full instruction:** Help me add malformed-JSON tests to the parser and keep this work limited to correctness tests.

**Rationale:** The three malformed-input cases and expected errors directly support parser correctness tests.

## SC1-V4-SX1-F034-K-A2

**Prefix:** Help me add malformed-JSON tests to the parser

**Action:** Prepare a correctness-test report layout

```text
Columns: malformed input, expected error, observed error; no timing column.
```

**Full instruction:** Help me add malformed-JSON tests to the parser and keep this work limited to correctness tests.

**Rationale:** The malformed-input and error columns support the required correctness-test report.

## SC1-V4-SX1-F035-K-A1

**Prefix:** Help me rewrite this note for executives while preserving its numbers

**Action:** Draft the executive summary

```text
The project will take 12 weeks with a budget of 30 credits; the decision needed is approval to proceed.
```

**Full instruction:** Help me rewrite this note for executives while preserving its numbers and keep both the 12-week duration and 30-credit budget.

**Rationale:** The executive draft preserves the requested duration and budget.

## SC1-V4-SX1-F035-K-A2

**Prefix:** Help me rewrite this note for executives while preserving its numbers

**Action:** Extract the unchanged duration

```text
Duration fact from the supplied fixture note: 12 weeks.
```

**Full instruction:** Help me rewrite this note for executives while preserving its numbers and keep both the 12-week duration and 30-credit budget.

**Rationale:** The extracted 12-week duration is explicitly retained in the final note.

## SC1-V4-SX1-F035-R-A2

**Prefix:** Help me rewrite this note for executives while preserving its numbers

**Action:** Extract the unchanged duration

```text
Duration fact from the supplied fixture note: 12 weeks.
```

**Full instruction:** Help me rewrite this note for executives while preserving its numbers but make it a technical note for engineers and correct the budget to 40 credits.

**Rationale:** The 12-week duration remains valid when the audience and budget change.

## SC1-V4-SX1-F036-K-A1

**Prefix:** Help me summarize the main report without using the appendix

**Action:** Extract main-report finding

```text
Main report fixture: trial A completed in 8 days with 2 defects. This fact appears only in the main report.
```

**Full instruction:** Help me summarize the main report without using the appendix and use only the main report findings.

**Rationale:** The extracted main-report finding is within the final source restriction.

## SC1-V4-SX1-F036-K-A2

**Prefix:** Help me summarize the main report without using the appendix

**Action:** Stage a summary layout

```text
Headings: objective, evidence, limitations; no source facts populated.
```

**Full instruction:** Help me summarize the main report without using the appendix and use only the main report findings.

**Rationale:** The generic summary headings remain usable within the main-report source restriction.

## SC1-V4-SX1-F036-R-A2

**Prefix:** Help me summarize the main report without using the appendix

**Action:** Stage a summary layout

```text
Headings: objective, evidence, limitations; no source facts populated.
```

**Full instruction:** Help me summarize the main report without using the appendix but summarize the appendix only and ignore the main report.

**Rationale:** The unpopulated objective, evidence and limitations headings can organize an appendix summary unchanged.

## SC1-V4-SX1-F037-K-A1

**Prefix:** Help me draft a proposal from these notes and leave pricing undecided

**Action:** Stage the pricing section

```text
Pricing: TBD. No numeric quote is included.
```

**Full instruction:** Help me draft a proposal from these notes and leave pricing undecided and mark pricing as TBD.

**Rationale:** The TBD pricing section is the expressly requested output.

## SC1-V4-SX1-F037-K-A2

**Prefix:** Help me draft a proposal from these notes and leave pricing undecided

**Action:** Stage the scope section

```text
Scope: deliver one dashboard and its handover guide; no price or schedule included.
```

**Full instruction:** Help me draft a proposal from these notes and leave pricing undecided and mark pricing as TBD.

**Rationale:** The dashboard and handover scope remains valid alongside TBD pricing.

## SC1-V4-SX1-F037-R-A2

**Prefix:** Help me draft a proposal from these notes and leave pricing undecided

**Action:** Stage the scope section

```text
Scope: deliver one dashboard and its handover guide; no price or schedule included.
```

**Full instruction:** Help me draft a proposal from these notes and leave pricing undecided but quote the supplied fixed price of 500 credits and remove TBD pricing.

**Rationale:** The dashboard and handover scope remains usable when the pricing section changes to 500 credits.

## SC1-V4-SX1-F038-K-A1

**Prefix:** Help me compare these two resumes without recommending a candidate

**Action:** Extract resume differences

```text
Resume A lists Python and 3 years of experience; Resume B lists Java and 5 years. These are fixture facts.
```

**Full instruction:** Help me compare these two resumes without recommending a candidate and list differences only.

**Rationale:** The extracted skills and experience provide the requested resume differences.

## SC1-V4-SX1-F038-R-A1

**Prefix:** Help me compare these two resumes without recommending a candidate

**Action:** Extract resume differences

```text
Resume A lists Python and 3 years of experience; Resume B lists Java and 5 years. These are fixture facts.
```

**Full instruction:** Help me compare these two resumes without recommending a candidate but recommend a candidate using the same resumes and explain the choice.

**Rationale:** The resume skills and experience remain reusable evidence for explaining a recommendation.

## SC1-V4-SX1-F039-K-A1

**Prefix:** Help me stage the living-room lights at 30 percent brightness

**Action:** Stage the requested lighting command

```text
Unapplied command: room=living_room, brightness=30, color=unchanged.
```

**Full instruction:** Help me stage the living-room lights at 30 percent brightness while preserving their current color, without applying changes.

**Rationale:** The unapplied command sets the requested living-room brightness while preserving color.

## SC1-V4-SX1-F039-K-A2

**Prefix:** Help me stage the living-room lights at 30 percent brightness

**Action:** Read living-room light state

```text
Living-room fixture: brightness 80%, color warm white. No bedroom state included.
```

**Full instruction:** Help me stage the living-room lights at 30 percent brightness while preserving their current color, without applying changes.

**Rationale:** The warm-white state supplies the color to preserve while changing living-room brightness.

## SC1-V4-SX1-F040-K-A2

**Prefix:** Help me stage a 70 F thermostat setting for tonight

**Action:** Read current thermostat setting

```text
Current fixture thermostat setting: 70 F; reading retained for conditional comparison.
```

**Full instruction:** Help me stage a 70 F thermostat setting for tonight only if the current setting differs from 70 F; do not apply it.

**Rationale:** The 70 F reading resolves the condition by showing that staging is unnecessary.

## SC1-V4-SX1-F040-R-A2

**Prefix:** Help me stage a 70 F thermostat setting for tonight

**Action:** Read current thermostat setting

```text
Current fixture thermostat setting: 70 F; reading retained for conditional comparison.
```

**Full instruction:** Help me stage a 70 F thermostat setting for tonight but stage 68 F instead, only if the current setting differs from 68 F; do not apply it.

**Rationale:** The current 70 F reading establishes that the proposed 68 F target differs from the current setting.

## SC1-V4-SX1-F041-K-A1

**Prefix:** Help me prepare to lock the back door after I leave

**Action:** Read back-door sensor

```text
Back-door fixture sensor: closed and unlocked; timestamp belongs to the fixed scenario snapshot.
```

**Full instruction:** Help me prepare to lock the back door after I leave and check the back-door sensor before staging anything.

**Rationale:** The fixed back-door sensor reading supplies the required check before staging.

## SC1-V4-SX1-F041-R-A2

**Prefix:** Help me prepare to lock the back door after I leave

**Action:** Stage a departure trigger definition

```text
Trigger: requester_departed becomes true; no door or lock operation attached.
```

**Full instruction:** Help me prepare to lock the back door after I leave but prepare to lock the front door instead and do not use the back-door sensor reading.

**Rationale:** The departure trigger remains required regardless of which door is locked.

## SC1-V4-SX1-F042-K-A1

**Prefix:** Help me stage a kitchen-only vacuum run

**Action:** Stage the room-specific cleaning plan

```text
Unapplied vacuum plan: include kitchen; exclude bedroom, hall and living room.
```

**Full instruction:** Help me stage a kitchen-only vacuum run and keep all other rooms excluded; do not start cleaning.

**Rationale:** The unapplied kitchen-only plan already excludes every other room.

## SC1-V4-SX1-F042-K-A2

**Prefix:** Help me stage a kitchen-only vacuum run

**Action:** Read vacuum battery state

```text
Fixture vacuum battery: 90%; sufficient for either single-room run in this scenario.
```

**Full instruction:** Help me stage a kitchen-only vacuum run and keep all other rooms excluded; do not start cleaning.

**Rationale:** The battery reading supports staging the kitchen run without starting cleaning.

## SC1-V4-SX1-F042-R-A2

**Prefix:** Help me stage a kitchen-only vacuum run

**Action:** Read vacuum battery state

```text
Fixture vacuum battery: 90%; sufficient for either single-room run in this scenario.
```

**Full instruction:** Help me stage a kitchen-only vacuum run but stage a bedroom-only run instead and discard the kitchen plan.

**Rationale:** The 90-percent battery reading explicitly establishes sufficient charge for the replacement bedroom run.

## SC1-V4-SX1-F043-K-A1

**Prefix:** Help me find robotics documentaries

**Action:** Retrieve robotics documentary cards

```text
Robot Workshop: robotics, 60 minutes; Machine Motion: robotics, 75 minutes; neither covers astronomy.
```

**Full instruction:** Help me find robotics documentaries and include only titles under 90 minutes.

**Rationale:** The two robotics documentary cards meet the required runtime limit.

## SC1-V4-SX1-F043-K-A2

**Prefix:** Help me find robotics documentaries

**Action:** Prepare a runtime filter

```text
Keep input records whose runtime_minutes < 90; no topic filter or titles embedded.
```

**Full instruction:** Help me find robotics documentaries and include only titles under 90 minutes.

**Rationale:** The runtime predicate directly implements the required under-90-minute restriction.

## SC1-V4-SX1-F044-K-A1

**Prefix:** Help me build an upbeat instrumental jazz playlist

**Action:** Collect instrumental track cards

```text
Track A and Track B: upbeat jazz, instrumental; no vocals in either fixture track.
```

**Full instruction:** Help me build an upbeat instrumental jazz playlist and exclude vocal tracks.

**Rationale:** The upbeat instrumental jazz tracks satisfy the explicit vocal exclusion.

## SC1-V4-SX1-F044-K-A2

**Prefix:** Help me build an upbeat instrumental jazz playlist

**Action:** Prepare a vocal-track exclusion predicate

```text
Keep a supplied track only when has_vocals is false; no titles embedded.
```

**Full instruction:** Help me build an upbeat instrumental jazz playlist and exclude vocal tracks.

**Rationale:** The vocal-exclusion predicate directly implements the instrumental-only requirement.

## SC1-V4-SX1-F045-K-A1

**Prefix:** Help me choose a non-horror movie under two hours for tonight

**Action:** Retrieve movie cards

```text
Film A: comedy, 90 minutes; Film B: drama, 105 minutes; both explicitly not horror.
```

**Full instruction:** Help me choose a non-horror movie under two hours for tonight and compare the listed eligible options.

**Rationale:** Both film cards satisfy the non-horror and under-two-hours requirements.

## SC1-V4-SX1-F045-K-A2

**Prefix:** Help me choose a non-horror movie under two hours for tonight

**Action:** Stage a generic movie comparison layout

```text
Columns: title, genre, runtime, availability tonight; no candidate titles or restrictions filled in.
```

**Full instruction:** Help me choose a non-horror movie under two hours for tonight and compare the listed eligible options.

**Rationale:** The movie comparison columns can organize the eligible options without revision.

## SC1-V4-SX1-F045-R-A2

**Prefix:** Help me choose a non-horror movie under two hours for tonight

**Action:** Stage a generic movie comparison layout

```text
Columns: title, genre, runtime, availability tonight; no candidate titles or restrictions filled in.
```

**Full instruction:** Help me choose a non-horror movie under two hours for tonight but choose a horror movie longer than two hours instead.

**Rationale:** The unfilled movie columns accommodate horror titles and longer runtimes.

## SC1-V4-SX1-F046-K-A1

**Prefix:** Help me find technical podcast interviews about AI agents

**Action:** Retrieve interview episode cards

```text
Episode I and Episode J: technical AI-agent interviews; neither is a news roundup.
```

**Full instruction:** Help me find technical podcast interviews about AI agents and favor interviews over news roundups.

**Rationale:** The technical AI-agent interviews satisfy the preference for interviews over roundups.

## SC1-V4-SX1-F046-K-A2

**Prefix:** Help me find technical podcast interviews about AI agents

**Action:** Prepare the topic query

```text
Topic query: AI agents; no episode-format restriction.
```

**Full instruction:** Help me find technical podcast interviews about AI agents and favor interviews over news roundups.

**Rationale:** The format-neutral AI agents query remains useful for finding interviews.

## SC1-V4-SX1-F046-R-A2

**Prefix:** Help me find technical podcast interviews about AI agents

**Action:** Prepare the topic query

```text
Topic query: AI agents; no episode-format restriction.
```

**Full instruction:** Help me find technical podcast interviews about AI agents but use only news roundups and exclude interviews.

**Rationale:** The unrestricted AI agents topic query can retrieve the newly required news roundups.

## SC1-V4-SX1-F047-K-A1

**Prefix:** Help me make a three-day business-trip packing checklist

**Action:** Draft the clothing checklist

```text
Two business shirts; one pair of office trousers; office shoes. No formalwear included.
```

**Full instruction:** Help me make a three-day business-trip packing checklist and omit formalwear.

**Rationale:** The listed business clothing satisfies the explicit no-formalwear constraint.

## SC1-V4-SX1-F047-K-A2

**Prefix:** Help me make a three-day business-trip packing checklist

**Action:** Draft the shared essentials checklist

```text
Toothbrush; phone charger; personal identification. No destination-specific supplies included.
```

**Full instruction:** Help me make a three-day business-trip packing checklist and omit formalwear.

**Rationale:** The toothbrush, charger and identification remain useful business-trip essentials.

## SC1-V4-SX1-F047-R-A2

**Prefix:** Help me make a three-day business-trip packing checklist

**Action:** Draft the shared essentials checklist

```text
Toothbrush; phone charger; personal identification. No destination-specific supplies included.
```

**Full instruction:** Help me make a three-day business-trip packing checklist but make it a three-day camping checklist instead, with no business clothing.

**Rationale:** The toothbrush, charger and identification remain usable camping essentials.

## SC1-V4-SX1-F048-K-A1

**Prefix:** Help me plan my morning around a 9 AM appointment

**Action:** Calculate the original departure time

```text
For a 09:00 arrival and 30 minutes travel, depart at 08:30.
```

**Full instruction:** Help me plan my morning around a 9 AM appointment and reserve 30 minutes to travel there.

**Rationale:** The 08:30 departure calculation satisfies the unchanged 09:00 arrival and 30-minute travel requirement.

## SC1-V4-SX1-F048-K-A2

**Prefix:** Help me plan my morning around a 9 AM appointment

**Action:** Prepare the travel-duration field

```text
Travel duration field: 30 minutes; no appointment or departure time filled in.
```

**Full instruction:** Help me plan my morning around a 9 AM appointment and reserve 30 minutes to travel there.

**Rationale:** The prepared 30-minute travel duration matches the final planning requirement.

## SC1-V4-SX1-F048-R-A2

**Prefix:** Help me plan my morning around a 9 AM appointment

**Action:** Prepare the travel-duration field

```text
Travel duration field: 30 minutes; no appointment or departure time filled in.
```

**Full instruction:** Help me plan my morning around a 9 AM appointment but move the appointment to 11 AM while retaining the 30-minute travel requirement.

**Rationale:** The 30-minute travel field remains correct for the 11 AM appointment.

## SC1-V4-SX1-F049-K-A1

**Prefix:** Help me build a shopping list for vegetarian tacos

**Action:** Draft the protein ingredient

```text
One tin of beans; no meat.
```

**Full instruction:** Help me build a shopping list for vegetarian tacos and include beans instead of meat.

**Rationale:** The beans ingredient satisfies the vegetarian taco request excluding meat.

## SC1-V4-SX1-F049-K-A2

**Prefix:** Help me build a shopping list for vegetarian tacos

**Action:** Draft the shared taco ingredients

```text
Tortillas, tomatoes and lettuce; no protein ingredient selected.
```

**Full instruction:** Help me build a shopping list for vegetarian tacos and include beans instead of meat.

**Rationale:** The shared taco ingredients remain usable when beans are chosen as the protein.

## SC1-V4-SX1-F049-R-A2

**Prefix:** Help me build a shopping list for vegetarian tacos

**Action:** Draft the shared taco ingredients

```text
Tortillas, tomatoes and lettuce; no protein ingredient selected.
```

**Full instruction:** Help me build a shopping list for vegetarian tacos but make beef tacos instead and omit beans.

**Rationale:** The tortillas, tomatoes and lettuce remain usable ingredients for beef tacos.

## SC1-V4-SX1-F050-K-A1

**Prefix:** Help me prioritize today's tasks with the client deadline first

**Action:** Stage the original ordering

```text
1. Client deadline; 2. Server incident; 3. File receipts.
```

**Full instruction:** Help me prioritize today's tasks with the client deadline first and keep the client deadline at the top.

**Rationale:** The staged ordering already places the client deadline first.

## SC1-V4-SX1-F050-K-A2

**Prefix:** Help me prioritize today's tasks with the client deadline first

**Action:** Extract today's task inventory

```text
Tasks due today: client deadline, server incident, file receipts; inventory has no priority ordering.
```

**Full instruction:** Help me prioritize today's tasks with the client deadline first and keep the client deadline at the top.

**Rationale:** Today's inventory supplies the tasks to prioritize with the client deadline first.

## SC1-V4-SX1-F050-R-A2

**Prefix:** Help me prioritize today's tasks with the client deadline first

**Action:** Extract today's task inventory

```text
Tasks due today: client deadline, server incident, file receipts; inventory has no priority ordering.
```

**Full instruction:** Help me prioritize today's tasks with the client deadline first but put the server incident first and move the client deadline below it.

**Rationale:** The unordered task inventory remains usable with the server incident ranked first.

## SC1-V5-SX1-F001-K-A1

**Prefix:** For now, compare flights from Harborview to Eastport

**Action:** Retrieve two route-specific fares

```text
Harborview–Eastport 08:00, 120 credits; Harborview–Eastport 10:00, 150 credits.
```

**Full instruction:** For now, compare flights from Harborview to Eastport and show the two listed morning options.

**Rationale:** The two morning Eastport fares are the exact requested comparison options.

## SC1-V5-SX1-F002-K-A1

**Prefix:** For now, find hotels near Maple Station

**Action:** Retrieve station-specific hotel cards

```text
Maple Lodge: 3-minute walk to Maple Station; Maple House: 5-minute walk.
```

**Full instruction:** For now, find hotels near Maple Station and compare the two listed hotels by walking distance.

**Rationale:** The two walking distances directly support the Maple Station comparison.

## SC1-V5-SX1-F002-K-A2

**Prefix:** For now, find hotels near Maple Station

**Action:** Stage a hotel comparison layout

```text
Columns: hotel name, distance to requested station, nightly price; no hotels filled in.
```

**Full instruction:** For now, find hotels near Maple Station and compare the two listed hotels by walking distance.

**Rationale:** The blank hotel, distance and price columns remain usable for the Maple Station comparison.

## SC1-V5-SX1-F002-R-A2

**Prefix:** For now, find hotels near Maple Station

**Action:** Stage a hotel comparison layout

```text
Columns: hotel name, distance to requested station, nightly price; no hotels filled in.
```

**Full instruction:** For now, find hotels near Maple Station but use Pine Station instead and omit Maple Station hotels.

**Rationale:** The unfilled station-distance columns can be populated with Pine Station hotels.

## SC1-V5-SX1-F003-K-A1

**Prefix:** For now, compare Friday car rentals at North Terminal

**Action:** Retrieve terminal-specific rental cards

```text
North Terminal: Compact A, 40 credits/day; Compact B, 45 credits/day. Both are North-only pickups.
```

**Full instruction:** For now, compare Friday car rentals at North Terminal and keep pickup at North Terminal.

**Rationale:** Both rental cards match the retained North Terminal pickup location.

## SC1-V5-SX1-F003-K-A2

**Prefix:** For now, compare Friday car rentals at North Terminal

**Action:** Prepare the comparison calculation

```text
Total rental cost = daily rate × number of days + disclosed fees; values remain unfilled.
```

**Full instruction:** For now, compare Friday car rentals at North Terminal and keep pickup at North Terminal.

**Rationale:** The unfilled rental-cost calculation can compare the retained pickup options.

## SC1-V5-SX1-F003-R-A2

**Prefix:** For now, compare Friday car rentals at North Terminal

**Action:** Prepare the comparison calculation

```text
Total rental cost = daily rate × number of days + disclosed fees; values remain unfilled.
```

**Full instruction:** For now, compare Friday car rentals at North Terminal but pickup must be at South Terminal instead, with no North Terminal results.

**Rationale:** The unfilled rental-cost expression can calculate South Terminal prices unchanged.

## SC1-V5-SX1-F004-K-A1

**Prefix:** For now, compare nonstop flights to Eastport

**Action:** Retrieve nonstop route cards

```text
Route N1: nonstop, 2 hours; route N2: nonstop, 3 hours. Neither includes a stop.
```

**Full instruction:** For now, compare nonstop flights to Eastport and list only nonstop itineraries.

**Rationale:** Both route cards are explicitly nonstop as required.

## SC1-V5-SX1-F004-K-A2

**Prefix:** For now, compare nonstop flights to Eastport

**Action:** Prepare the requested destination field

```text
Destination field: Eastport; no route or fare chosen.
```

**Full instruction:** For now, compare nonstop flights to Eastport and list only nonstop itineraries.

**Rationale:** The Eastport destination field remains correct for nonstop route selection.

## SC1-V5-SX1-F004-R-A2

**Prefix:** For now, compare nonstop flights to Eastport

**Action:** Prepare the requested destination field

```text
Destination field: Eastport; no route or fare chosen.
```

**Full instruction:** For now, compare nonstop flights to Eastport but I now want only one-stop itineraries to Eastport.

**Rationale:** Eastport remains the destination after the stop-count requirement changes.

## SC1-V5-SX1-F005-K-A1

**Prefix:** For now, find Italian restaurants around Cedar Square

**Action:** Retrieve cuisine-specific restaurant cards

```text
Cedar Pasta: Italian, outdoor seating; Olive Room: Italian, outdoor seating; neither serves Thai cuisine.
```

**Full instruction:** For now, find Italian restaurants around Cedar Square and choose places with outdoor seating.

**Rationale:** Both Italian restaurant cards include the requested outdoor seating.

## SC1-V5-SX1-F005-K-A2

**Prefix:** For now, find Italian restaurants around Cedar Square

**Action:** Prepare the location field

```text
Search area: Cedar Square; cuisine, hours and price remain unfilled.
```

**Full instruction:** For now, find Italian restaurants around Cedar Square and choose places with outdoor seating.

**Rationale:** Cedar Square remains the correct search area when outdoor seating is added.

## SC1-V5-SX1-F005-R-A2

**Prefix:** For now, find Italian restaurants around Cedar Square

**Action:** Prepare the location field

```text
Search area: Cedar Square; cuisine, hours and price remain unfilled.
```

**Full instruction:** For now, find Italian restaurants around Cedar Square but change the cuisine to Thai and exclude Italian restaurants.

**Rationale:** The Cedar Square location field remains unchanged when the cuisine changes to Thai.

## SC1-V5-SX1-F006-K-A1

**Prefix:** For now, find bakeries around Birch Park

**Action:** Retrieve bakery cards

```text
Birch Bake: bakery with coffee; Loaf House: bakery with coffee; neither is a pharmacy.
```

**Full instruction:** For now, find bakeries around Birch Park that serve coffee, including the two listed options.

**Rationale:** Both bakery cards include the required coffee availability.

## SC1-V5-SX1-F006-K-A2

**Prefix:** For now, find bakeries around Birch Park

**Action:** Prepare a bakery-only comparison layout

```text
Columns: bakery name, bread selection, pastry selection, coffee availability; four fixed headings.
```

**Full instruction:** For now, find bakeries around Birch Park that serve coffee, including the two listed options.

**Rationale:** The bakery and coffee headings remain useful for the requested options.

## SC1-V5-SX1-F007-K-A1

**Prefix:** For now, find gyms in Riverton that sell day passes

**Action:** Retrieve day-pass gym cards

```text
River Fit: day passes and sauna; North Fit: day passes and sauna. Both sell day passes.
```

**Full instruction:** For now, find gyms in Riverton that sell day passes and prioritize day-pass gyms with a sauna.

**Rationale:** Both gym cards explicitly provide day passes and saunas as requested.

## SC1-V5-SX1-F007-K-A2

**Prefix:** For now, find gyms in Riverton that sell day passes

**Action:** Prepare the location field

```text
City field: Riverton; membership type remains unfilled.
```

**Full instruction:** For now, find gyms in Riverton that sell day passes and prioritize day-pass gyms with a sauna.

**Rationale:** Riverton remains the required city for the gym search.

## SC1-V5-SX1-F007-R-A2

**Prefix:** For now, find gyms in Riverton that sell day passes

**Action:** Prepare the location field

```text
City field: Riverton; membership type remains unfilled.
```

**Full instruction:** For now, find gyms in Riverton that sell day passes but only consider members-only gyms that do not sell day passes.

**Rationale:** The Riverton city field remains correct after the membership constraint reverses.

## SC1-V5-SX1-F008-K-A1

**Prefix:** For now, find pharmacies in Brookfield that are open now

**Action:** Retrieve open pharmacy cards

```text
Brook Pharmacy: open now, standalone; Elm Pharmacy: open now, standalone. Neither is hospital-based.
```

**Full instruction:** For now, find pharmacies in Brookfield that are open now and omit hospital-based pharmacies.

**Rationale:** Both open standalone pharmacies survive the hospital exclusion.

## SC1-V5-SX1-F008-K-A2

**Prefix:** For now, find pharmacies in Brookfield that are open now

**Action:** Prepare the search time reference

```text
Fixture clock: Monday 14:00 local time; tomorrow resolves to Tuesday in this fixture.
```

**Full instruction:** For now, find pharmacies in Brookfield that are open now and omit hospital-based pharmacies.

**Rationale:** The fixture clock establishes the time at which pharmacy opening status is evaluated.

## SC1-V5-SX1-F008-R-A2

**Prefix:** For now, find pharmacies in Brookfield that are open now

**Action:** Prepare the search time reference

```text
Fixture clock: Monday 14:00 local time; tomorrow resolves to Tuesday in this fixture.
```

**Full instruction:** For now, find pharmacies in Brookfield that are open now but only list hospital pharmacies that are closed now and open tomorrow.

**Rationale:** The fixture clock establishes both closed-now timing and tomorrow as Tuesday for the hospital-pharmacy search.

## SC1-V5-SX1-F009-K-A1

**Prefix:** For now, research local robotic actuator manufacturers

**Action:** Retrieve manufacturer cards

```text
Aster Motion and Delta Drive manufacture robotic actuators locally; neither distributes other makers' parts.
```

**Full instruction:** For now, research local robotic actuator manufacturers and retain the manufacturers while adding distributors separately.

**Rationale:** The manufacturer cards remain requested while distributors are added separately.

## SC1-V5-SX1-F009-K-A2

**Prefix:** For now, research local robotic actuator manufacturers

**Action:** Prepare the component definition

```text
Robotic actuator: component that converts a control input into mechanical movement; no supplier selected.
```

**Full instruction:** For now, research local robotic actuator manufacturers and retain the manufacturers while adding distributors separately.

**Rationale:** The actuator definition remains relevant when manufacturers and distributors are researched together.

## SC1-V5-SX1-F009-R-A2

**Prefix:** For now, research local robotic actuator manufacturers

**Action:** Prepare the component definition

```text
Robotic actuator: component that converts a control input into mechanical movement; no supplier selected.
```

**Full instruction:** For now, research local robotic actuator manufacturers but list distributors only and exclude manufacturers.

**Rationale:** The actuator definition still describes the products sought from distributors.

## SC1-V5-SX1-F010-K-A1

**Prefix:** For now, compare 15-litre shoulder bags

**Action:** Retrieve bag specification cards

```text
Bag L: shoulder bag, 15 L, 0.5 kg; Bag M: shoulder bag, 15 L, 0.7 kg; neither converts to a backpack.
```

**Full instruction:** For now, compare 15-litre shoulder bags and rank the two listed bags by lower weight.

**Rationale:** The eligible shoulder-bag weights can be ranked without new retrieval.

## SC1-V5-SX1-F010-K-A2

**Prefix:** For now, compare 15-litre shoulder bags

**Action:** Prepare a weight-ranking routine

```text
Sort supplied product records by numeric weight_kg ascending; no records or capacity filter embedded.
```

**Full instruction:** For now, compare 15-litre shoulder bags and rank the two listed bags by lower weight.

**Rationale:** The weight sort directly supports ranking the listed bags by lower weight.

## SC1-V5-SX1-F011-K-A1

**Prefix:** For now, find brown faux-suede jackets with stand collars

**Action:** Retrieve jacket cards

```text
Jacket A: brown faux suede, stand collar, 120 credits; Jacket B: brown faux suede, stand collar, 150 credits.
```

**Full instruction:** For now, find brown faux-suede jackets with stand collars and compare the listed options under 200 credits.

**Rationale:** Both retrieved jackets satisfy the requested attributes and under-200-credit ceiling.

## SC1-V5-SX1-F011-K-A2

**Prefix:** For now, find brown faux-suede jackets with stand collars

**Action:** Stage a product comparison layout

```text
Columns: material, color, collar type, price; values unfilled.
```

**Full instruction:** For now, find brown faux-suede jackets with stand collars and compare the listed options under 200 credits.

**Rationale:** The jacket attribute and price columns remain appropriate for the requested comparison.

## SC1-V5-SX1-F011-R-A2

**Prefix:** For now, find brown faux-suede jackets with stand collars

**Action:** Stage a product comparison layout

```text
Columns: material, color, collar type, price; values unfilled.
```

**Full instruction:** For now, find brown faux-suede jackets with stand collars but use black cotton jackets with lapels instead and discard the original options.

**Rationale:** The blank material, color, collar and price columns can compare black cotton jackets with lapels unchanged.

## SC1-V5-SX1-F012-K-A1

**Prefix:** For now, compare robotics synthetic-data tools that support Engine R

**Action:** Retrieve tool compatibility cards

```text
Sim A and Sim B support Engine R only; neither supports Engine S.
```

**Full instruction:** For now, compare robotics synthetic-data tools that support Engine R and keep Engine R support mandatory.

**Rationale:** Both tool cards establish the required Engine R compatibility.

## SC1-V5-SX1-F012-K-A2

**Prefix:** For now, compare robotics synthetic-data tools that support Engine R

**Action:** Prepare a physics-evaluation checklist

```text
Check gravity, collision response, sensor noise and deterministic replay; no engine-specific commands.
```

**Full instruction:** For now, compare robotics synthetic-data tools that support Engine R and keep Engine R support mandatory.

**Rationale:** The engine-neutral physics checklist can evaluate the required Engine R tools.

## SC1-V5-SX1-F012-R-A2

**Prefix:** For now, compare robotics synthetic-data tools that support Engine R

**Action:** Prepare a physics-evaluation checklist

```text
Check gravity, collision response, sensor noise and deterministic replay; no engine-specific commands.
```

**Full instruction:** For now, compare robotics synthetic-data tools that support Engine R but only consider tools for Engine S that do not support Engine R.

**Rationale:** The engine-neutral physics checklist remains usable when evaluating Engine S tools.

## SC1-V5-SX1-F013-K-A1

**Prefix:** For now, find freestanding desk converters under 250 credits

**Action:** Retrieve converter cards

```text
Lift A: freestanding, 150 credits; Lift B: freestanding, 220 credits. Neither can be permanently mounted.
```

**Full instruction:** For now, find freestanding desk converters under 250 credits and exclude permanently mounted converters.

**Rationale:** The cards identify eligible freestanding converters below 250 credits.

## SC1-V5-SX1-F013-K-A2

**Prefix:** For now, find freestanding desk converters under 250 credits

**Action:** Prepare the price ceiling field

```text
Maximum price field: 250 credits; mounting type unfilled.
```

**Full instruction:** For now, find freestanding desk converters under 250 credits and exclude permanently mounted converters.

**Rationale:** The maximum price field remains valid after excluding permanent mounts.

## SC1-V5-SX1-F013-R-A2

**Prefix:** For now, find freestanding desk converters under 250 credits

**Action:** Prepare the price ceiling field

```text
Maximum price field: 250 credits; mounting type unfilled.
```

**Full instruction:** For now, find freestanding desk converters under 250 credits but only show permanently mounted converters and discard freestanding ones.

**Rationale:** The 250-credit ceiling remains applicable to permanently mounted converters.

## SC1-V5-SX1-F014-K-A1

**Prefix:** For now, find a 30-minute meeting for Sam and me on Tuesday

**Action:** Read Tuesday availability

```text
Sam and requester both free Tuesday 14:00–14:30 and 15:00–15:30. No Wednesday availability included.
```

**Full instruction:** For now, find a 30-minute meeting for Sam and me on Tuesday and use either of the two listed Tuesday slots.

**Rationale:** Both Tuesday availability records are eligible final meeting choices.

## SC1-V5-SX1-F014-R-A2

**Prefix:** For now, find a 30-minute meeting for Sam and me on Tuesday

**Action:** Stage a Wednesday calendar event

```text
Unsent event object: attendees Sam and requester, duration 30 minutes, day Wednesday; no time set.
```

**Full instruction:** For now, find a 30-minute meeting for Sam and me on Tuesday but switch the meeting to Wednesday and ignore Tuesday availability.

**Rationale:** The staged Wednesday event matches the replacement day, attendees and duration.

## SC1-V5-SX1-F015-K-A1

**Prefix:** For now, check whether my dentist can see me on Friday

**Action:** Read Friday availability

```text
The fixture dentist has no Friday openings; no Monday availability included.
```

**Full instruction:** For now, check whether my dentist can see me on Friday and keep my existing appointment if Friday has no openings.

**Rationale:** The Friday no-openings result triggers the instructed appointment fallback.

## SC1-V5-SX1-F015-K-A2

**Prefix:** For now, check whether my dentist can see me on Friday

**Action:** Retrieve the existing appointment

```text
Current appointment: Wednesday 11:00, dentist Dr Vale, appointment ID D17.
```

**Full instruction:** For now, check whether my dentist can see me on Friday and keep my existing appointment if Friday has no openings.

**Rationale:** The existing appointment record supplies the required fallback details.

## SC1-V5-SX1-F015-R-A2

**Prefix:** For now, check whether my dentist can see me on Friday

**Action:** Retrieve the existing appointment

```text
Current appointment: Wednesday 11:00, dentist Dr Vale, appointment ID D17.
```

**Full instruction:** For now, check whether my dentist can see me on Friday but check Monday instead and ignore Friday openings, keeping my existing appointment as fallback.

**Rationale:** The existing appointment remains the explicit fallback after availability changes to Monday.

## SC1-V5-SX1-F016-K-A1

**Prefix:** For now, find team meeting slots this week after 10 AM

**Action:** Read afternoon team availability

```text
Whole team free Thursday 13:00–13:30 and Friday 14:00–14:30; no morning data included.
```

**Full instruction:** For now, find team meeting slots this week after 10 AM and show the two listed afternoon slots.

**Rationale:** The afternoon records directly supply the two requested team slots.

## SC1-V5-SX1-F016-K-A2

**Prefix:** For now, find team meeting slots this week after 10 AM

**Action:** Prepare the participant list

```text
Participants: Sam, Jo and requester; no time selected.
```

**Full instruction:** For now, find team meeting slots this week after 10 AM and show the two listed afternoon slots.

**Rationale:** The participant list remains usable for the team's afternoon scheduling search.

## SC1-V5-SX1-F016-R-A2

**Prefix:** For now, find team meeting slots this week after 10 AM

**Action:** Prepare the participant list

```text
Participants: Sam, Jo and requester; no time selected.
```

**Full instruction:** For now, find team meeting slots this week after 10 AM but only consider slots before 10 AM this week.

**Rationale:** The participant list remains valid when the eligible time window changes.

## SC1-V5-SX1-F017-K-A1

**Prefix:** For now, prepare a report reminder for tomorrow morning

**Action:** Stage a morning reminder

```text
Unsent reminder: title Submit report, day tomorrow, time 09:00.
```

**Full instruction:** For now, prepare a report reminder for tomorrow morning and set its time to 9 AM.

**Rationale:** The staged tomorrow-at-09:00 report reminder matches the requested time.

## SC1-V5-SX1-F017-K-A2

**Prefix:** For now, prepare a report reminder for tomorrow morning

**Action:** Prepare the reminder text

```text
Reminder title: Submit report; date and time unfilled.
```

**Full instruction:** For now, prepare a report reminder for tomorrow morning and set its time to 9 AM.

**Rationale:** The reminder title remains correct when tomorrow at 9 AM is filled in.

## SC1-V5-SX1-F017-R-A2

**Prefix:** For now, prepare a report reminder for tomorrow morning

**Action:** Prepare the reminder text

```text
Reminder title: Submit report; date and time unfilled.
```

**Full instruction:** For now, prepare a report reminder for tomorrow morning but change it to tomorrow evening at 7 PM.

**Rationale:** The reminder title survives replacing tomorrow morning with 7 PM.

## SC1-V5-SX1-F018-K-A1

**Prefix:** For now, draft a reply thanking Morgan for the introduction

**Action:** Draft the thank-you sentence

```text
Thank you for making the introduction, Morgan.
```

**Full instruction:** For now, draft a reply thanking Morgan for the introduction and offer to provide more information.

**Rationale:** The thank-you sentence remains usable alongside the requested information offer.

## SC1-V5-SX1-F018-K-A2

**Prefix:** For now, draft a reply thanking Morgan for the introduction

**Action:** Draft an offer sentence

```text
I would be happy to provide any additional information you need.
```

**Full instruction:** For now, draft a reply thanking Morgan for the introduction and offer to provide more information.

**Rationale:** The offer sentence is explicitly required by the completed reply instruction.

## SC1-V5-SX1-F019-K-A1

**Prefix:** For now, draft a team update saying the build is delayed

**Action:** Draft the status sentence

```text
The build is delayed; we are still investigating the cause.
```

**Full instruction:** For now, draft a team update saying the build is delayed and keep the cause neutral because it is not yet known.

**Rationale:** The delayed-status sentence remains valid and does not attribute a cause.

## SC1-V5-SX1-F019-K-A2

**Prefix:** For now, draft a team update saying the build is delayed

**Action:** Stage a neutral update heading

```text
Heading: Build status update; no status claim or cause included.
```

**Full instruction:** For now, draft a team update saying the build is delayed and keep the cause neutral because it is not yet known.

**Rationale:** The neutral heading fits the delayed-build update without asserting a cause.

## SC1-V5-SX1-F019-R-A2

**Prefix:** For now, draft a team update saying the build is delayed

**Action:** Stage a neutral update heading

```text
Heading: Build status update; no status claim or cause included.
```

**Full instruction:** For now, draft a team update saying the build is delayed but the build is on schedule, so report that and do not mention a delay.

**Rationale:** The neutral build-status heading remains valid for an on-schedule update.

## SC1-V5-SX1-F020-K-A1

**Prefix:** For now, draft a message declining dinner tonight

**Action:** Draft the decline sentence

```text
I cannot make dinner tonight.
```

**Full instruction:** For now, draft a message declining dinner tonight and suggest meeting next weekend.

**Rationale:** The decline sentence remains part of the requested dinner refusal with an alternative date.

## SC1-V5-SX1-F020-K-A2

**Prefix:** For now, draft a message declining dinner tonight

**Action:** Draft the alternative-date sentence

```text
Would you like to meet next weekend instead?
```

**Full instruction:** For now, draft a message declining dinner tonight and suggest meeting next weekend.

**Rationale:** The next-weekend suggestion is explicitly requested for the dinner-decline message.

## SC1-V5-SX1-F021-K-A1

**Prefix:** For now, draft a refund approval message

**Action:** Draft the approval sentence

```text
Your refund has been approved.
```

**Full instruction:** For now, draft a refund approval message and avoid promising a payment date.

**Rationale:** The approval sentence remains correct and promises no payment date.

## SC1-V5-SX1-F021-K-A2

**Prefix:** For now, draft a refund approval message

**Action:** Stage an approval-specific reply template

```text
Subject: Refund approved. Closing: Thank you for your patience. Body unfilled.
```

**Full instruction:** For now, draft a refund approval message and avoid promising a payment date.

**Rationale:** The approval template contains no payment date and remains usable.

## SC1-V5-SX1-F022-K-A1

**Prefix:** For now, find peer-reviewed papers about hidden-state probing

**Action:** Retrieve peer-reviewed fixture records

```text
Paper P and Paper Q: peer-reviewed hidden-state probing papers in the synthetic catalogue; no technical reports included.
```

**Full instruction:** For now, find peer-reviewed papers about hidden-state probing and use only peer-reviewed sources.

**Rationale:** Both fixture papers satisfy the retained peer-reviewed probing requirement.

## SC1-V5-SX1-F022-K-A2

**Prefix:** For now, find peer-reviewed papers about hidden-state probing

**Action:** Prepare the topic search terms

```text
Terms: hidden-state probing, representation analysis; no publication-type filter.
```

**Full instruction:** For now, find peer-reviewed papers about hidden-state probing and use only peer-reviewed sources.

**Rationale:** The topic terms remain usable with a peer-reviewed source filter.

## SC1-V5-SX1-F022-R-A2

**Prefix:** For now, find peer-reviewed papers about hidden-state probing

**Action:** Prepare the topic search terms

```text
Terms: hidden-state probing, representation analysis; no publication-type filter.
```

**Full instruction:** For now, find peer-reviewed papers about hidden-state probing but use only non-peer-reviewed technical reports about hidden-state probing.

**Rationale:** The topic-only search terms survive restricting sources to technical reports.

## SC1-V5-SX1-F023-K-A1

**Prefix:** For now, find version 3 documentation for Library L

**Action:** Retrieve versioned documentation

```text
Official Library L version 3: old_connect(endpoint) is the connection entry point. This fixture marks it removed in version 4.
```

**Full instruction:** For now, find version 3 documentation for Library L and use only the official version 3 material.

**Rationale:** The retrieved official version 3 entry point matches the final version and source requirements.

## SC1-V5-SX1-F023-K-A2

**Prefix:** For now, find version 3 documentation for Library L

**Action:** Retrieve the official documentation index URL

```text
Fixture URL: https://library-l.example/docs/ ; index lists version 3 and version 4.
```

**Full instruction:** For now, find version 3 documentation for Library L and use only the official version 3 material.

**Rationale:** The official index already provides a reusable route to version 3 documentation.

## SC1-V5-SX1-F023-R-A2

**Prefix:** For now, find version 3 documentation for Library L

**Action:** Retrieve the official documentation index URL

```text
Fixture URL: https://library-l.example/docs/ ; index lists version 3 and version 4.
```

**Full instruction:** For now, find version 3 documentation for Library L but use version 4 instead and exclude all version 3 documentation.

**Rationale:** The official index contains version 4 and remains usable after the version change.

## SC1-V5-SX1-F024-K-A1

**Prefix:** For now, compare Acme's revenue in its two annual releases

**Action:** Extract Acme revenue figures

```text
Acme fixture: prior year revenue 10 million credits; current year 12 million credits.
```

**Full instruction:** For now, compare Acme's revenue in its two annual releases and report company-stated actual revenue only.

**Rationale:** The extracted Acme revenue values directly supply actual-only reporting.

## SC1-V5-SX1-F025-K-A1

**Prefix:** For now, find primary rules for Region A consumer AI systems

**Action:** Retrieve jurisdiction-specific rule cards

```text
Rule A1 and Rule A2: synthetic Region A consumer-AI rules, with no applicability in Region B.
```

**Full instruction:** For now, find primary rules for Region A consumer AI systems and keep Region A as the main jurisdiction.

**Rationale:** The Region A rule cards remain relevant to the retained jurisdiction.

## SC1-V5-SX1-F025-K-A2

**Prefix:** For now, find primary rules for Region A consumer AI systems

**Action:** Stage a legal-source comparison layout

```text
Columns: jurisdiction, issuing authority, effective date, provision; no legal claims filled in.
```

**Full instruction:** For now, find primary rules for Region A consumer AI systems and keep Region A as the main jurisdiction.

**Rationale:** The legal-source comparison headings remain useful for Region A rules.

## SC1-V5-SX1-F025-R-A2

**Prefix:** For now, find primary rules for Region A consumer AI systems

**Action:** Stage a legal-source comparison layout

```text
Columns: jurisdiction, issuing authority, effective date, provision; no legal claims filled in.
```

**Full instruction:** For now, find primary rules for Region A consumer AI systems but use Region B rules only and exclude Region A rules.

**Rationale:** The blank jurisdiction, authority, date and provision columns can compare Region B sources unchanged.

## SC1-V5-SX1-F026-K-A1

**Prefix:** For now, compare small open-weight reasoning models

**Action:** Collect vendor-only benchmark claims

```text
Vendor card: Model K claims 80 points and Model J claims 85 points; neither claim is independently reproduced.
```

**Full instruction:** For now, compare small open-weight reasoning models and flag vendor-only scores as unverified rather than treating them as evidence.

**Rationale:** The vendor-only scores survive as claims to flag unverified.

## SC1-V5-SX1-F026-K-A2

**Prefix:** For now, compare small open-weight reasoning models

**Action:** Collect independent fixture benchmark records

```text
Independent lab fixture: Model K 70 points, Model J 72 points, same test and evaluation settings; both small and open-weight.
```

**Full instruction:** For now, compare small open-weight reasoning models and flag vendor-only scores as unverified rather than treating them as evidence.

**Rationale:** The independent same-test scores provide comparable evidence for the model comparison.

## SC1-V5-SX1-F026-R-A2

**Prefix:** For now, compare small open-weight reasoning models

**Action:** Collect independent fixture benchmark records

```text
Independent lab fixture: Model K 70 points, Model J 72 points, same test and evaluation settings; both small and open-weight.
```

**Full instruction:** For now, compare small open-weight reasoning models but include only independently reproduced scores and omit vendor-only claims entirely.

**Rationale:** The independent same-setting benchmark scores meet the required evidence standard.

## SC1-V5-SX1-F027-K-A1

**Prefix:** For now, calculate a 7 percent downside scenario for a 100-credit index

**Action:** Calculate the requested scenario

```text
100 × (1 − 0.07) = 93 credits; only the 7% result retained.
```

**Full instruction:** For now, calculate a 7 percent downside scenario for a 100-credit index and show the hypothetical level without making a trade.

**Rationale:** The stored 93-credit result directly answers the retained 7 percent scenario.

## SC1-V5-SX1-F027-K-A2

**Prefix:** For now, calculate a 7 percent downside scenario for a 100-credit index

**Action:** Prepare the scenario formula

```text
Scenario level = starting level × (1 − decline_fraction); no numeric assumptions embedded.
```

**Full instruction:** For now, calculate a 7 percent downside scenario for a 100-credit index and show the hypothetical level without making a trade.

**Rationale:** The symbolic downside expression supports the requested seven-percent calculation without executing a trade.

## SC1-V5-SX1-F027-R-A2

**Prefix:** For now, calculate a 7 percent downside scenario for a 100-credit index

**Action:** Prepare the scenario formula

```text
Scenario level = starting level × (1 − decline_fraction); no numeric assumptions embedded.
```

**Full instruction:** For now, calculate a 7 percent downside scenario for a 100-credit index but use a 12 percent decline instead and omit the 7 percent case.

**Rationale:** The symbolic downside formula can accept the revised 12 percent decline unchanged.

## SC1-V5-SX1-F028-K-A1

**Prefix:** For now, calculate budget variance from my supplied table

**Action:** Compute category variances

```text
Fixture variances: supplies +20 credits, travel +5 credits, meals −10 credits; positive means overspend.
```

**Full instruction:** For now, calculate budget variance from my supplied table and identify the largest overspend.

**Rationale:** The category variances identify supplies as the largest overspend.

## SC1-V5-SX1-F028-K-A2

**Prefix:** For now, calculate budget variance from my supplied table

**Action:** Aggregate actual category totals

```text
Fixture actuals: supplies 120 credits, travel 85 credits, meals 40 credits; source-table sums retained.
```

**Full instruction:** For now, calculate budget variance from my supplied table and identify the largest overspend.

**Rationale:** The actual category totals remain reusable inputs when comparing actuals with budgets for overspend.

## SC1-V5-SX1-F028-R-A2

**Prefix:** For now, calculate budget variance from my supplied table

**Action:** Aggregate actual category totals

```text
Fixture actuals: supplies 120 credits, travel 85 credits, meals 40 credits; source-table sums retained.
```

**Full instruction:** For now, calculate budget variance from my supplied table but show actual category totals only, without calculating or reporting variances.

**Rationale:** The actual category totals directly satisfy the final actual-only reporting requirement.

## SC1-V5-SX1-F029-K-A1

**Prefix:** For now, compare current holdings with the start-of-month snapshot

**Action:** Calculate start-of-month concentration

```text
Start-of-month fixture: asset A 60%, asset B 40%; no other date included.
```

**Full instruction:** For now, compare current holdings with the start-of-month snapshot and report concentration changes for those two snapshots.

**Rationale:** The start-of-month allocation supplies one of the two required concentration snapshots.

## SC1-V5-SX1-F029-K-A2

**Prefix:** For now, compare current holdings with the start-of-month snapshot

**Action:** Calculate current concentration

```text
Current fixture: asset A 50%, asset B 50%; values unchanged across comparisons.
```

**Full instruction:** For now, compare current holdings with the start-of-month snapshot and report concentration changes for those two snapshots.

**Rationale:** The current 50/50 allocation remains one of the required concentration snapshots.

## SC1-V5-SX1-F029-R-A2

**Prefix:** For now, compare current holdings with the start-of-month snapshot

**Action:** Calculate current concentration

```text
Current fixture: asset A 50%, asset B 50%; values unchanged across comparisons.
```

**Full instruction:** For now, compare current holdings with the start-of-month snapshot but compare current holdings with the start-of-year snapshot instead and ignore start-of-month holdings.

**Rationale:** The current concentration remains useful against the new start-of-year baseline.

## SC1-V5-SX1-F030-K-A1

**Prefix:** For now, calculate breakeven for my debit spread using the supplied values

**Action:** Calculate the original breakeven

```text
For this fixture's specified call debit spread: 100 + 5 = 105 credits.
```

**Full instruction:** For now, calculate breakeven for my debit spread using the supplied values and use the supplied 5-credit debit and 100-credit lower strike.

**Rationale:** The 105-credit result uses exactly the retained strike and debit.

## SC1-V5-SX1-F030-K-A2

**Prefix:** For now, calculate breakeven for my debit spread using the supplied values

**Action:** Prepare the symbolic breakeven expression

```text
For the specified call debit spread: lower_strike + net_debit; no prices filled in.
```

**Full instruction:** For now, calculate breakeven for my debit spread using the supplied values and use the supplied 5-credit debit and 100-credit lower strike.

**Rationale:** The symbolic call-spread expression remains correct for the supplied 5-credit debit.

## SC1-V5-SX1-F030-R-A2

**Prefix:** For now, calculate breakeven for my debit spread using the supplied values

**Action:** Prepare the symbolic breakeven expression

```text
For the specified call debit spread: lower_strike + net_debit; no prices filled in.
```

**Full instruction:** For now, calculate breakeven for my debit spread using the supplied values but correct the debit to 8 credits while keeping the lower strike at 100 credits.

**Rationale:** The symbolic call-spread expression accepts the corrected 8-credit debit without revision.

## SC1-V5-SX1-F031-K-A1

**Prefix:** For now, write a Python function that counts ERROR lines in the supplied log

**Action:** Stage an ERROR-counting function

```text
def count_lines(lines): return sum(line.startswith('ERROR ') for line in lines)
```

**Full instruction:** For now, write a Python function that counts ERROR lines in the supplied log and return the count without changing the file.

**Rationale:** The function counts ERROR-prefixed lines without modifying the log.

## SC1-V5-SX1-F031-K-A2

**Prefix:** For now, write a Python function that counts ERROR lines in the supplied log

**Action:** Stage a log-reading helper

```text
def read_lines(path):
    with open(path, encoding='utf-8') as f:
        return f.read().splitlines()
```

**Full instruction:** For now, write a Python function that counts ERROR lines in the supplied log and return the count without changing the file.

**Rationale:** The read-only line helper remains usable for the ERROR-counting function.

## SC1-V5-SX1-F031-R-A2

**Prefix:** For now, write a Python function that counts ERROR lines in the supplied log

**Action:** Stage a log-reading helper

```text
def read_lines(path):
    with open(path, encoding='utf-8') as f:
        return f.read().splitlines()
```

**Full instruction:** For now, write a Python function that counts ERROR lines in the supplied log but count WARN lines instead and do not count ERROR lines.

**Rationale:** The generic line reader can feed a WARN counter without modification.

## SC1-V5-SX1-F032-K-A1

**Prefix:** For now, inspect the client timeout path without changing the code

**Action:** Collect a timeout observation

```text
Fixture client.py line 8: DEFAULT_TIMEOUT = 5; request() passes this constant as its timeout argument.
```

**Full instruction:** For now, inspect the client timeout path without changing the code and identify where its five-second timeout is set.

**Rationale:** The observation identifies the five-second timeout constant and its use.

## SC1-V5-SX1-F032-R-A1

**Prefix:** For now, inspect the client timeout path without changing the code

**Action:** Collect a timeout observation

```text
Fixture client.py line 8: DEFAULT_TIMEOUT = 5; request() passes this constant as its timeout argument.
```

**Full instruction:** For now, inspect the client timeout path without changing the code but modify the default timeout to ten seconds instead of producing an inspection report.

**Rationale:** The timeout observation identifies the constant and call path needed for the ten-second edit.

## SC1-V5-SX1-F032-R-A2

**Prefix:** For now, inspect the client timeout path without changing the code

**Action:** Stage a ten-second timeout patch

```text
Unapplied patch replaces DEFAULT_TIMEOUT = 5 with DEFAULT_TIMEOUT = 10; no other edits.
```

**Full instruction:** For now, inspect the client timeout path without changing the code but modify the default timeout to ten seconds instead of producing an inspection report.

**Rationale:** The unapplied patch implements the exact ten-second timeout change now requested.

## SC1-V5-SX1-F033-K-A1

**Prefix:** For now, refactor the add function while preserving its public name and behavior

**Action:** Stage the preserving refactor

```text
Replacement definition: def add(a, b): return a + b; public symbol remains add.
```

**Full instruction:** For now, refactor the add function while preserving its public name and behavior and keep its existing callers compatible.

**Rationale:** The add definition retains the required public symbol and addition behavior.

## SC1-V5-SX1-F033-K-A2

**Prefix:** For now, refactor the add function while preserving its public name and behavior

**Action:** Stage addition behavior tests

```text
Assertions: operation(2, 3) == 5; operation(-1, 1) == 0; operation supplied by the test harness, not hardcoded to a name.
```

**Full instruction:** For now, refactor the add function while preserving its public name and behavior and keep its existing callers compatible.

**Rationale:** The name-independent addition tests still check behavior while preserving caller compatibility.

## SC1-V5-SX1-F033-R-A2

**Prefix:** For now, refactor the add function while preserving its public name and behavior

**Action:** Stage addition behavior tests

```text
Assertions: operation(2, 3) == 5; operation(-1, 1) == 0; operation supplied by the test harness, not hardcoded to a name.
```

**Full instruction:** For now, refactor the add function while preserving its public name and behavior but rename the public function to total and update callers to use total.

**Rationale:** The harness-supplied operation allows the addition tests to survive renaming add to total.

## SC1-V5-SX1-F034-K-A1

**Prefix:** For now, add malformed-JSON tests to the parser

**Action:** Stage malformed-input test cases

```text
Inputs: an unmatched opening brace, an unfinished numeric array, and an object with an unquoted key; expected outcome for each: parse error.
```

**Full instruction:** For now, add malformed-JSON tests to the parser and keep this work limited to correctness tests.

**Rationale:** The parse-error cases directly support the requested malformed-JSON correctness tests.

## SC1-V5-SX1-F034-K-A2

**Prefix:** For now, add malformed-JSON tests to the parser

**Action:** Prepare a correctness-test report layout

```text
Columns: malformed input, expected error, observed error; no timing column.
```

**Full instruction:** For now, add malformed-JSON tests to the parser and keep this work limited to correctness tests.

**Rationale:** The malformed-input and error columns fit the retained correctness-testing task.

## SC1-V5-SX1-F035-K-A1

**Prefix:** For now, rewrite this note for executives while preserving its numbers

**Action:** Draft the executive summary

```text
The project will take 12 weeks with a budget of 30 credits; the decision needed is approval to proceed.
```

**Full instruction:** For now, rewrite this note for executives while preserving its numbers and keep both the 12-week duration and 30-credit budget.

**Rationale:** The executive summary preserves the required 12-week duration and 30-credit budget.

## SC1-V5-SX1-F035-K-A2

**Prefix:** For now, rewrite this note for executives while preserving its numbers

**Action:** Extract the unchanged duration

```text
Duration fact from the supplied fixture note: 12 weeks.
```

**Full instruction:** For now, rewrite this note for executives while preserving its numbers and keep both the 12-week duration and 30-credit budget.

**Rationale:** The 12-week duration is expressly preserved.

## SC1-V5-SX1-F035-R-A2

**Prefix:** For now, rewrite this note for executives while preserving its numbers

**Action:** Extract the unchanged duration

```text
Duration fact from the supplied fixture note: 12 weeks.
```

**Full instruction:** For now, rewrite this note for executives while preserving its numbers but make it a technical note for engineers and correct the budget to 40 credits.

**Rationale:** The extracted 12-week duration survives the audience change and budget correction.

## SC1-V5-SX1-F036-K-A1

**Prefix:** For now, summarize the main report without using the appendix

**Action:** Extract main-report finding

```text
Main report fixture: trial A completed in 8 days with 2 defects. This fact appears only in the main report.
```

**Full instruction:** For now, summarize the main report without using the appendix and use only the main report findings.

**Rationale:** The main-report finding supplies evidence for the main-report-only summary.

## SC1-V5-SX1-F036-K-A2

**Prefix:** For now, summarize the main report without using the appendix

**Action:** Stage a summary layout

```text
Headings: objective, evidence, limitations; no source facts populated.
```

**Full instruction:** For now, summarize the main report without using the appendix and use only the main report findings.

**Rationale:** The objective, evidence and limitations headings remain usable for the main-report summary.

## SC1-V5-SX1-F036-R-A2

**Prefix:** For now, summarize the main report without using the appendix

**Action:** Stage a summary layout

```text
Headings: objective, evidence, limitations; no source facts populated.
```

**Full instruction:** For now, summarize the main report without using the appendix but summarize the appendix only and ignore the main report.

**Rationale:** The unpopulated summary layout can be reused for appendix content unchanged.

## SC1-V5-SX1-F037-K-A1

**Prefix:** For now, draft a proposal from these notes and leave pricing undecided

**Action:** Stage the pricing section

```text
Pricing: TBD. No numeric quote is included.
```

**Full instruction:** For now, draft a proposal from these notes and leave pricing undecided and mark pricing as TBD.

**Rationale:** The TBD pricing section exactly matches the final pricing instruction.

## SC1-V5-SX1-F037-K-A2

**Prefix:** For now, draft a proposal from these notes and leave pricing undecided

**Action:** Stage the scope section

```text
Scope: deliver one dashboard and its handover guide; no price or schedule included.
```

**Full instruction:** For now, draft a proposal from these notes and leave pricing undecided and mark pricing as TBD.

**Rationale:** The dashboard and handover scope remains usable alongside a TBD pricing section.

## SC1-V5-SX1-F037-R-A2

**Prefix:** For now, draft a proposal from these notes and leave pricing undecided

**Action:** Stage the scope section

```text
Scope: deliver one dashboard and its handover guide; no price or schedule included.
```

**Full instruction:** For now, draft a proposal from these notes and leave pricing undecided but quote the supplied fixed price of 500 credits and remove TBD pricing.

**Rationale:** The unchanged scope can be retained when fixed pricing replaces TBD.

## SC1-V5-SX1-F038-K-A1

**Prefix:** For now, compare these two resumes without recommending a candidate

**Action:** Extract resume differences

```text
Resume A lists Python and 3 years of experience; Resume B lists Java and 5 years. These are fixture facts.
```

**Full instruction:** For now, compare these two resumes without recommending a candidate and list differences only.

**Rationale:** The extracted resume facts supply differences without recommending either candidate.

## SC1-V5-SX1-F038-R-A1

**Prefix:** For now, compare these two resumes without recommending a candidate

**Action:** Extract resume differences

```text
Resume A lists Python and 3 years of experience; Resume B lists Java and 5 years. These are fixture facts.
```

**Full instruction:** For now, compare these two resumes without recommending a candidate but recommend a candidate using the same resumes and explain the choice.

**Rationale:** The resume skills and experience remain evidence for explaining the candidate recommendation.

## SC1-V5-SX1-F039-K-A1

**Prefix:** For now, stage the living-room lights at 30 percent brightness

**Action:** Stage the requested lighting command

```text
Unapplied command: room=living_room, brightness=30, color=unchanged.
```

**Full instruction:** For now, stage the living-room lights at 30 percent brightness while preserving their current color, without applying changes.

**Rationale:** The unapplied living-room command preserves color and sets the requested brightness.

## SC1-V5-SX1-F039-K-A2

**Prefix:** For now, stage the living-room lights at 30 percent brightness

**Action:** Read living-room light state

```text
Living-room fixture: brightness 80%, color warm white. No bedroom state included.
```

**Full instruction:** For now, stage the living-room lights at 30 percent brightness while preserving their current color, without applying changes.

**Rationale:** The warm-white state supplies the color to preserve while changing living-room brightness.

## SC1-V5-SX1-F040-K-A2

**Prefix:** For now, stage a 70 F thermostat setting for tonight

**Action:** Read current thermostat setting

```text
Current fixture thermostat setting: 70 F; reading retained for conditional comparison.
```

**Full instruction:** For now, stage a 70 F thermostat setting for tonight only if the current setting differs from 70 F; do not apply it.

**Rationale:** The current 70 F reading resolves the condition by showing that no new 70 F staging is needed.

## SC1-V5-SX1-F040-R-A2

**Prefix:** For now, stage a 70 F thermostat setting for tonight

**Action:** Read current thermostat setting

```text
Current fixture thermostat setting: 70 F; reading retained for conditional comparison.
```

**Full instruction:** For now, stage a 70 F thermostat setting for tonight but stage 68 F instead, only if the current setting differs from 68 F; do not apply it.

**Rationale:** The current 70 F reading is reusable to evaluate the new 68 F condition.

## SC1-V5-SX1-F041-K-A1

**Prefix:** For now, prepare to lock the back door after I leave

**Action:** Read back-door sensor

```text
Back-door fixture sensor: closed and unlocked; timestamp belongs to the fixed scenario snapshot.
```

**Full instruction:** For now, prepare to lock the back door after I leave and check the back-door sensor before staging anything.

**Rationale:** The back-door reading performs the expressly required sensor check.

## SC1-V5-SX1-F041-R-A2

**Prefix:** For now, prepare to lock the back door after I leave

**Action:** Stage a departure trigger definition

```text
Trigger: requester_departed becomes true; no door or lock operation attached.
```

**Full instruction:** For now, prepare to lock the back door after I leave but prepare to lock the front door instead and do not use the back-door sensor reading.

**Rationale:** The departure trigger has no back-door dependency and survives the front-door switch.

## SC1-V5-SX1-F042-K-A1

**Prefix:** For now, stage a kitchen-only vacuum run

**Action:** Stage the room-specific cleaning plan

```text
Unapplied vacuum plan: include kitchen; exclude bedroom, hall and living room.
```

**Full instruction:** For now, stage a kitchen-only vacuum run and keep all other rooms excluded; do not start cleaning.

**Rationale:** The unapplied kitchen-only plan retains all required exclusions and does not start cleaning.

## SC1-V5-SX1-F042-K-A2

**Prefix:** For now, stage a kitchen-only vacuum run

**Action:** Read vacuum battery state

```text
Fixture vacuum battery: 90%; sufficient for either single-room run in this scenario.
```

**Full instruction:** For now, stage a kitchen-only vacuum run and keep all other rooms excluded; do not start cleaning.

**Rationale:** The sufficient battery reading supports preparing the retained kitchen-only run.

## SC1-V5-SX1-F042-R-A2

**Prefix:** For now, stage a kitchen-only vacuum run

**Action:** Read vacuum battery state

```text
Fixture vacuum battery: 90%; sufficient for either single-room run in this scenario.
```

**Full instruction:** For now, stage a kitchen-only vacuum run but stage a bedroom-only run instead and discard the kitchen plan.

**Rationale:** The 90-percent battery reading explicitly establishes sufficient charge for the replacement bedroom run.

## SC1-V5-SX1-F043-K-A1

**Prefix:** For now, find robotics documentaries

**Action:** Retrieve robotics documentary cards

```text
Robot Workshop: robotics, 60 minutes; Machine Motion: robotics, 75 minutes; neither covers astronomy.
```

**Full instruction:** For now, find robotics documentaries and include only titles under 90 minutes.

**Rationale:** Both robotics documentaries satisfy the stated under-90-minute limit.

## SC1-V5-SX1-F043-K-A2

**Prefix:** For now, find robotics documentaries

**Action:** Prepare a runtime filter

```text
Keep input records whose runtime_minutes < 90; no topic filter or titles embedded.
```

**Full instruction:** For now, find robotics documentaries and include only titles under 90 minutes.

**Rationale:** The runtime predicate directly implements the required under-90-minute restriction.

## SC1-V5-SX1-F044-K-A1

**Prefix:** For now, build an upbeat instrumental jazz playlist

**Action:** Collect instrumental track cards

```text
Track A and Track B: upbeat jazz, instrumental; no vocals in either fixture track.
```

**Full instruction:** For now, build an upbeat instrumental jazz playlist and exclude vocal tracks.

**Rationale:** The upbeat instrumental jazz tracks satisfy the explicit vocal exclusion.

## SC1-V5-SX1-F044-K-A2

**Prefix:** For now, build an upbeat instrumental jazz playlist

**Action:** Prepare a vocal-track exclusion predicate

```text
Keep a supplied track only when has_vocals is false; no titles embedded.
```

**Full instruction:** For now, build an upbeat instrumental jazz playlist and exclude vocal tracks.

**Rationale:** The has_vocals exclusion predicate implements the required instrumental-only filter.

## SC1-V5-SX1-F045-K-A1

**Prefix:** For now, choose a non-horror movie under two hours for tonight

**Action:** Retrieve movie cards

```text
Film A: comedy, 90 minutes; Film B: drama, 105 minutes; both explicitly not horror.
```

**Full instruction:** For now, choose a non-horror movie under two hours for tonight and compare the listed eligible options.

**Rationale:** The short non-horror cards match the final eligible movie comparison.

## SC1-V5-SX1-F045-K-A2

**Prefix:** For now, choose a non-horror movie under two hours for tonight

**Action:** Stage a generic movie comparison layout

```text
Columns: title, genre, runtime, availability tonight; no candidate titles or restrictions filled in.
```

**Full instruction:** For now, choose a non-horror movie under two hours for tonight and compare the listed eligible options.

**Rationale:** The generic title, genre, runtime and availability columns remain usable for the eligible movie comparison.

## SC1-V5-SX1-F045-R-A2

**Prefix:** For now, choose a non-horror movie under two hours for tonight

**Action:** Stage a generic movie comparison layout

```text
Columns: title, genre, runtime, availability tonight; no candidate titles or restrictions filled in.
```

**Full instruction:** For now, choose a non-horror movie under two hours for tonight but choose a horror movie longer than two hours instead.

**Rationale:** The unfilled genre and runtime columns can hold the revised horror options.

## SC1-V5-SX1-F046-K-A1

**Prefix:** For now, find technical podcast interviews about AI agents

**Action:** Retrieve interview episode cards

```text
Episode I and Episode J: technical AI-agent interviews; neither is a news roundup.
```

**Full instruction:** For now, find technical podcast interviews about AI agents and favor interviews over news roundups.

**Rationale:** Both retrieved technical interviews satisfy the retained interview preference.

## SC1-V5-SX1-F046-K-A2

**Prefix:** For now, find technical podcast interviews about AI agents

**Action:** Prepare the topic query

```text
Topic query: AI agents; no episode-format restriction.
```

**Full instruction:** For now, find technical podcast interviews about AI agents and favor interviews over news roundups.

**Rationale:** The format-neutral AI-agents query remains useful for finding interviews.

## SC1-V5-SX1-F046-R-A2

**Prefix:** For now, find technical podcast interviews about AI agents

**Action:** Prepare the topic query

```text
Topic query: AI agents; no episode-format restriction.
```

**Full instruction:** For now, find technical podcast interviews about AI agents but use only news roundups and exclude interviews.

**Rationale:** The unrestricted AI agents topic query can retrieve news roundups unchanged.

## SC1-V5-SX1-F047-K-A1

**Prefix:** For now, make a three-day business-trip packing checklist

**Action:** Draft the clothing checklist

```text
Two business shirts; one pair of office trousers; office shoes. No formalwear included.
```

**Full instruction:** For now, make a three-day business-trip packing checklist and omit formalwear.

**Rationale:** The business clothing checklist explicitly contains no formalwear.

## SC1-V5-SX1-F047-K-A2

**Prefix:** For now, make a three-day business-trip packing checklist

**Action:** Draft the shared essentials checklist

```text
Toothbrush; phone charger; personal identification. No destination-specific supplies included.
```

**Full instruction:** For now, make a three-day business-trip packing checklist and omit formalwear.

**Rationale:** The shared essentials contain no formalwear and remain suitable for the business trip.

## SC1-V5-SX1-F047-R-A2

**Prefix:** For now, make a three-day business-trip packing checklist

**Action:** Draft the shared essentials checklist

```text
Toothbrush; phone charger; personal identification. No destination-specific supplies included.
```

**Full instruction:** For now, make a three-day business-trip packing checklist but make it a three-day camping checklist instead, with no business clothing.

**Rationale:** The shared essentials remain suitable for camping and contain no business clothing.

## SC1-V5-SX1-F048-K-A1

**Prefix:** For now, plan my morning around a 9 AM appointment

**Action:** Calculate the original departure time

```text
For a 09:00 arrival and 30 minutes travel, depart at 08:30.
```

**Full instruction:** For now, plan my morning around a 9 AM appointment and reserve 30 minutes to travel there.

**Rationale:** The 08:30 departure correctly allows 30 minutes before the retained 9 AM appointment.

## SC1-V5-SX1-F048-K-A2

**Prefix:** For now, plan my morning around a 9 AM appointment

**Action:** Prepare the travel-duration field

```text
Travel duration field: 30 minutes; no appointment or departure time filled in.
```

**Full instruction:** For now, plan my morning around a 9 AM appointment and reserve 30 minutes to travel there.

**Rationale:** The 30-minute travel field is expressly retained in the final plan.

## SC1-V5-SX1-F048-R-A2

**Prefix:** For now, plan my morning around a 9 AM appointment

**Action:** Prepare the travel-duration field

```text
Travel duration field: 30 minutes; no appointment or departure time filled in.
```

**Full instruction:** For now, plan my morning around a 9 AM appointment but move the appointment to 11 AM while retaining the 30-minute travel requirement.

**Rationale:** The 30-minute travel field is explicitly retained when the appointment moves to 11 AM.

## SC1-V5-SX1-F049-K-A1

**Prefix:** For now, build a shopping list for vegetarian tacos

**Action:** Draft the protein ingredient

```text
One tin of beans; no meat.
```

**Full instruction:** For now, build a shopping list for vegetarian tacos and include beans instead of meat.

**Rationale:** The bean ingredient directly satisfies the vegetarian protein requirement.

## SC1-V5-SX1-F049-K-A2

**Prefix:** For now, build a shopping list for vegetarian tacos

**Action:** Draft the shared taco ingredients

```text
Tortillas, tomatoes and lettuce; no protein ingredient selected.
```

**Full instruction:** For now, build a shopping list for vegetarian tacos and include beans instead of meat.

**Rationale:** The shared taco ingredients remain usable when beans are added as the protein.

## SC1-V5-SX1-F049-R-A2

**Prefix:** For now, build a shopping list for vegetarian tacos

**Action:** Draft the shared taco ingredients

```text
Tortillas, tomatoes and lettuce; no protein ingredient selected.
```

**Full instruction:** For now, build a shopping list for vegetarian tacos but make beef tacos instead and omit beans.

**Rationale:** Tortillas, tomatoes and lettuce remain usable in beef tacos.

## SC1-V5-SX1-F050-K-A1

**Prefix:** For now, prioritize today's tasks with the client deadline first

**Action:** Stage the original ordering

```text
1. Client deadline; 2. Server incident; 3. File receipts.
```

**Full instruction:** For now, prioritize today's tasks with the client deadline first and keep the client deadline at the top.

**Rationale:** The existing ordering already keeps the client deadline at the top.

## SC1-V5-SX1-F050-K-A2

**Prefix:** For now, prioritize today's tasks with the client deadline first

**Action:** Extract today's task inventory

```text
Tasks due today: client deadline, server incident, file receipts; inventory has no priority ordering.
```

**Full instruction:** For now, prioritize today's tasks with the client deadline first and keep the client deadline at the top.

**Rationale:** The unordered inventory supplies the tasks to prioritize with the client deadline first.

## SC1-V5-SX1-F050-R-A2

**Prefix:** For now, prioritize today's tasks with the client deadline first

**Action:** Extract today's task inventory

```text
Tasks due today: client deadline, server incident, file receipts; inventory has no priority ordering.
```

**Full instruction:** For now, prioritize today's tasks with the client deadline first but put the server incident first and move the client deadline below it.

**Rationale:** The unordered task inventory remains usable when the server incident receives first priority.
