# All 200 synthetic items and adjudicated labels

AI-provisional judgments on fictional, unexecuted artifacts. This is not human gold or evidence of predictive efficacy. Original owner labels are unchanged.

## SX1-F001-K-A1

**Travel · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Compare flights from Harborview to Eastport

**Candidate:** Retrieve two route-specific fares

**Concrete work product:**

```text
Harborview–Eastport 08:00, 120 credits; Harborview–Eastport 10:00, 150 credits.
```

**Full instruction:** Compare flights from Harborview to Eastport and show the two listed morning options.

**Judge:** The two morning Eastport fares are precisely the requested options.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F001-K-A2

**Travel · reusable · fraction 1 · confidence 3/5 · ambiguity Y

**Observed prefix:** Compare flights from Harborview to Eastport

**Candidate:** Retrieve the origin airport access note

**Concrete work product:**

```text
Harborview airport: rail shuttle departs downtown every 20 minutes.
```

**Full instruction:** Compare flights from Harborview to Eastport and show the two listed morning options.

**Judge:** The unchanged origin access note can support travel context, although the rubric does not specify how much ancillary context qualifies.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F001-R-A1

**Travel · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Compare flights from Harborview to Eastport

**Candidate:** Retrieve two route-specific fares

**Concrete work product:**

```text
Harborview–Eastport 08:00, 120 credits; Harborview–Eastport 10:00, 150 credits.
```

**Full instruction:** Compare flights from Harborview to Eastport but change the destination to Westhaven and discard the Eastport options.

**Judge:** Both fares concern the expressly discarded Eastport destination.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F001-R-A2

**Travel · reusable · fraction 1 · confidence 3/5 · ambiguity Y

**Observed prefix:** Compare flights from Harborview to Eastport

**Candidate:** Retrieve the origin airport access note

**Concrete work product:**

```text
Harborview airport: rail shuttle departs downtown every 20 minutes.
```

**Full instruction:** Compare flights from Harborview to Eastport but change the destination to Westhaven and discard the Eastport options.

**Judge:** The Harborview shuttle note remains possible origin-access context after the destination change, with ancillary relevance a rubric judgment call.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F002-K-A1

**Travel · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find hotels near Maple Station

**Candidate:** Retrieve station-specific hotel cards

**Concrete work product:**

```text
Maple Lodge: 3-minute walk to Maple Station; Maple House: 5-minute walk.
```

**Full instruction:** Find hotels near Maple Station and compare the two listed hotels by walking distance.

**Judge:** The two Maple walking distances provide the requested hotel comparison.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F002-K-A2

**Travel · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find hotels near Maple Station

**Candidate:** Stage a hotel comparison layout

**Concrete work product:**

```text
Columns: hotel name, distance to requested station, nightly price; no hotels filled in.
```

**Full instruction:** Find hotels near Maple Station and compare the two listed hotels by walking distance.

**Judge:** The station-distance column directly supports the walking-distance comparison.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F002-R-A1

**Travel · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find hotels near Maple Station

**Candidate:** Retrieve station-specific hotel cards

**Concrete work product:**

```text
Maple Lodge: 3-minute walk to Maple Station; Maple House: 5-minute walk.
```

**Full instruction:** Find hotels near Maple Station but use Pine Station instead and omit Maple Station hotels.

**Judge:** The only hotel distances concern Maple Station hotels that must be omitted.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F002-R-A2

**Travel · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find hotels near Maple Station

**Candidate:** Stage a hotel comparison layout

**Concrete work product:**

```text
Columns: hotel name, distance to requested station, nightly price; no hotels filled in.
```

**Full instruction:** Find hotels near Maple Station but use Pine Station instead and omit Maple Station hotels.

**Judge:** The empty requested-station distance column can represent Pine Station.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F003-K-A1

**Travel · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Compare Friday car rentals at North Terminal

**Candidate:** Retrieve terminal-specific rental cards

**Concrete work product:**

```text
North Terminal: Compact A, 40 credits/day; Compact B, 45 credits/day. Both are North-only pickups.
```

**Full instruction:** Compare Friday car rentals at North Terminal and keep pickup at North Terminal.

**Judge:** Both North Terminal rental cards match the retained pickup location.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F003-K-A2

**Travel · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Compare Friday car rentals at North Terminal

**Candidate:** Prepare the comparison calculation

**Concrete work product:**

```text
Total rental cost = daily rate × number of days + disclosed fees; values remain unfilled.
```

**Full instruction:** Compare Friday car rentals at North Terminal and keep pickup at North Terminal.

**Judge:** The unfilled rental-cost formula applies to the North Terminal options.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F003-R-A1

**Travel · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Compare Friday car rentals at North Terminal

**Candidate:** Retrieve terminal-specific rental cards

**Concrete work product:**

```text
North Terminal: Compact A, 40 credits/day; Compact B, 45 credits/day. Both are North-only pickups.
```

**Full instruction:** Compare Friday car rentals at North Terminal but pickup must be at South Terminal instead, with no North Terminal results.

**Judge:** Both rental cards are limited to the excluded North Terminal pickup.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F003-R-A2

**Travel · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Compare Friday car rentals at North Terminal

**Candidate:** Prepare the comparison calculation

**Concrete work product:**

```text
Total rental cost = daily rate × number of days + disclosed fees; values remain unfilled.
```

**Full instruction:** Compare Friday car rentals at North Terminal but pickup must be at South Terminal instead, with no North Terminal results.

**Judge:** The unfilled cost formula contains no pickup-terminal dependency.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F004-K-A1

**Travel · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Compare nonstop flights to Eastport

**Candidate:** Retrieve nonstop route cards

**Concrete work product:**

```text
Route N1: nonstop, 2 hours; route N2: nonstop, 3 hours. Neither includes a stop.
```

**Full instruction:** Compare nonstop flights to Eastport and list only nonstop itineraries.

**Judge:** Both route cards satisfy the nonstop-only restriction.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F004-K-A2

**Travel · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Compare nonstop flights to Eastport

**Candidate:** Prepare the requested destination field

**Concrete work product:**

```text
Destination field: Eastport; no route or fare chosen.
```

**Full instruction:** Compare nonstop flights to Eastport and list only nonstop itineraries.

**Judge:** Eastport remains the destination for the nonstop search.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F004-R-A1

**Travel · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Compare nonstop flights to Eastport

**Candidate:** Retrieve nonstop route cards

**Concrete work product:**

```text
Route N1: nonstop, 2 hours; route N2: nonstop, 3 hours. Neither includes a stop.
```

**Full instruction:** Compare nonstop flights to Eastport but I now want only one-stop itineraries to Eastport.

**Judge:** Neither nonstop route is a required one-stop itinerary.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F004-R-A2

**Travel · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Compare nonstop flights to Eastport

**Candidate:** Prepare the requested destination field

**Concrete work product:**

```text
Destination field: Eastport; no route or fare chosen.
```

**Full instruction:** Compare nonstop flights to Eastport but I now want only one-stop itineraries to Eastport.

**Judge:** Eastport remains the destination when the itinerary changes to one stop.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F005-K-A1

**Local Search · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find Italian restaurants around Cedar Square

**Candidate:** Retrieve cuisine-specific restaurant cards

**Concrete work product:**

```text
Cedar Pasta: Italian, outdoor seating; Olive Room: Italian, outdoor seating; neither serves Thai cuisine.
```

**Full instruction:** Find Italian restaurants around Cedar Square and choose places with outdoor seating.

**Judge:** Both Italian restaurant cards establish the requested outdoor seating.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F005-K-A2

**Local Search · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find Italian restaurants around Cedar Square

**Candidate:** Prepare the location field

**Concrete work product:**

```text
Search area: Cedar Square; cuisine, hours and price remain unfilled.
```

**Full instruction:** Find Italian restaurants around Cedar Square and choose places with outdoor seating.

**Judge:** Cedar Square remains the search area for the outdoor Italian restaurants.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F005-R-A1

**Local Search · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find Italian restaurants around Cedar Square

**Candidate:** Retrieve cuisine-specific restaurant cards

**Concrete work product:**

```text
Cedar Pasta: Italian, outdoor seating; Olive Room: Italian, outdoor seating; neither serves Thai cuisine.
```

**Full instruction:** Find Italian restaurants around Cedar Square but change the cuisine to Thai and exclude Italian restaurants.

**Judge:** Both restaurant cards are Italian and explicitly lack the required Thai cuisine.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F005-R-A2

**Local Search · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find Italian restaurants around Cedar Square

**Candidate:** Prepare the location field

**Concrete work product:**

```text
Search area: Cedar Square; cuisine, hours and price remain unfilled.
```

**Full instruction:** Find Italian restaurants around Cedar Square but change the cuisine to Thai and exclude Italian restaurants.

**Judge:** Cedar Square remains the search location when the cuisine changes.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F006-K-A1

**Local Search · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find bakeries around Birch Park

**Candidate:** Retrieve bakery cards

**Concrete work product:**

```text
Birch Bake: bakery with coffee; Loaf House: bakery with coffee; neither is a pharmacy.
```

**Full instruction:** Find bakeries around Birch Park that serve coffee, including the two listed options.

**Judge:** Both bakery cards already establish the requested coffee availability.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F006-K-A2

**Local Search · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find bakeries around Birch Park

**Candidate:** Prepare a bakery-only comparison layout

**Concrete work product:**

```text
Columns: bakery name, bread selection, pastry selection, coffee availability; four fixed headings.
```

**Full instruction:** Find bakeries around Birch Park that serve coffee, including the two listed options.

**Judge:** The bakery layout includes the coffee field needed for the requested comparison.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F006-R-A1

**Local Search · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find bakeries around Birch Park

**Candidate:** Retrieve bakery cards

**Concrete work product:**

```text
Birch Bake: bakery with coffee; Loaf House: bakery with coffee; neither is a pharmacy.
```

**Full instruction:** Find bakeries around Birch Park but I meant pharmacies around Birch Park, not bakeries.

**Judge:** Neither retrieved bakery is a pharmacy.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F006-R-A2

**Local Search · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find bakeries around Birch Park

**Candidate:** Prepare a bakery-only comparison layout

**Concrete work product:**

```text
Columns: bakery name, bread selection, pastry selection, coffee availability; four fixed headings.
```

**Full instruction:** Find bakeries around Birch Park but I meant pharmacies around Birch Park, not bakeries.

**Judge:** The fixed bakery and food headings require replacement to compare pharmacies.

**Author expectation / rater A / rater B:** reusable / non-reusable / non-reusable

## SX1-F007-K-A1

**Local Search · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find gyms in Riverton that sell day passes

**Candidate:** Retrieve day-pass gym cards

**Concrete work product:**

```text
River Fit: day passes and sauna; North Fit: day passes and sauna. Both sell day passes.
```

**Full instruction:** Find gyms in Riverton that sell day passes and prioritize day-pass gyms with a sauna.

**Judge:** Both day-pass gym cards also meet the requested sauna preference.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F007-K-A2

**Local Search · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find gyms in Riverton that sell day passes

**Candidate:** Prepare the location field

**Concrete work product:**

```text
City field: Riverton; membership type remains unfilled.
```

**Full instruction:** Find gyms in Riverton that sell day passes and prioritize day-pass gyms with a sauna.

**Judge:** Riverton remains the location for the day-pass gym search.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F007-R-A1

**Local Search · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find gyms in Riverton that sell day passes

**Candidate:** Retrieve day-pass gym cards

**Concrete work product:**

```text
River Fit: day passes and sauna; North Fit: day passes and sauna. Both sell day passes.
```

**Full instruction:** Find gyms in Riverton that sell day passes but only consider members-only gyms that do not sell day passes.

**Judge:** Both gyms sell day passes and therefore fail the members-only restriction.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F007-R-A2

**Local Search · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find gyms in Riverton that sell day passes

**Candidate:** Prepare the location field

**Concrete work product:**

```text
City field: Riverton; membership type remains unfilled.
```

**Full instruction:** Find gyms in Riverton that sell day passes but only consider members-only gyms that do not sell day passes.

**Judge:** Riverton remains the search city under the members-only constraint.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F008-K-A1

**Local Search · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find pharmacies in Brookfield that are open now

**Candidate:** Retrieve open pharmacy cards

**Concrete work product:**

```text
Brook Pharmacy: open now, standalone; Elm Pharmacy: open now, standalone. Neither is hospital-based.
```

**Full instruction:** Find pharmacies in Brookfield that are open now and omit hospital-based pharmacies.

**Judge:** Both open pharmacy cards are standalone and meet the hospital exclusion.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F008-K-A2

**Local Search · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find pharmacies in Brookfield that are open now

**Candidate:** Prepare the search time reference

**Concrete work product:**

```text
Fixture clock: Monday 14:00 local time; tomorrow resolves to Tuesday in this fixture.
```

**Full instruction:** Find pharmacies in Brookfield that are open now and omit hospital-based pharmacies.

**Judge:** The frozen local clock supports checking which standalone pharmacies are open now.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F008-R-A1

**Local Search · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find pharmacies in Brookfield that are open now

**Candidate:** Retrieve open pharmacy cards

**Concrete work product:**

```text
Brook Pharmacy: open now, standalone; Elm Pharmacy: open now, standalone. Neither is hospital-based.
```

**Full instruction:** Find pharmacies in Brookfield that are open now but only list hospital pharmacies that are closed now and open tomorrow.

**Judge:** Both open standalone pharmacies fail the closed hospital-pharmacy requirement.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F008-R-A2

**Local Search · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find pharmacies in Brookfield that are open now

**Candidate:** Prepare the search time reference

**Concrete work product:**

```text
Fixture clock: Monday 14:00 local time; tomorrow resolves to Tuesday in this fixture.
```

**Full instruction:** Find pharmacies in Brookfield that are open now but only list hospital pharmacies that are closed now and open tomorrow.

**Judge:** The frozen Monday clock and Tuesday resolution support the revised now-and-tomorrow opening checks.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F009-K-A1

**Shopping/Research · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Research local robotic actuator manufacturers

**Candidate:** Retrieve manufacturer cards

**Concrete work product:**

```text
Aster Motion and Delta Drive manufacture robotic actuators locally; neither distributes other makers' parts.
```

**Full instruction:** Research local robotic actuator manufacturers and retain the manufacturers while adding distributors separately.

**Judge:** Both manufacturer cards remain required while distributors are added separately.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F009-K-A2

**Shopping/Research · reusable · fraction 1.0 · confidence 4/5 · ambiguity N

**Observed prefix:** Research local robotic actuator manufacturers

**Candidate:** Prepare the component definition

**Concrete work product:**

```text
Robotic actuator: component that converts a control input into mechanical movement; no supplier selected.
```

**Full instruction:** Research local robotic actuator manufacturers and retain the manufacturers while adding distributors separately.

**Judge:** The actuator definition supports the unchanged component research across supplier types.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F009-R-A1

**Shopping/Research · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Research local robotic actuator manufacturers

**Candidate:** Retrieve manufacturer cards

**Concrete work product:**

```text
Aster Motion and Delta Drive manufacture robotic actuators locally; neither distributes other makers' parts.
```

**Full instruction:** Research local robotic actuator manufacturers but list distributors only and exclude manufacturers.

**Judge:** Both suppliers are manufacturers and neither meets the distributor-only requirement.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F009-R-A2

**Shopping/Research · reusable · fraction 1.0 · confidence 4/5 · ambiguity N

**Observed prefix:** Research local robotic actuator manufacturers

**Candidate:** Prepare the component definition

**Concrete work product:**

```text
Robotic actuator: component that converts a control input into mechanical movement; no supplier selected.
```

**Full instruction:** Research local robotic actuator manufacturers but list distributors only and exclude manufacturers.

**Judge:** The actuator definition remains applicable to researching distributors of those components.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F010-K-A1

**Shopping/Research · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Compare 15-litre shoulder bags

**Candidate:** Retrieve bag specification cards

**Concrete work product:**

```text
Bag L: shoulder bag, 15 L, 0.5 kg; Bag M: shoulder bag, 15 L, 0.7 kg; neither converts to a backpack.
```

**Full instruction:** Compare 15-litre shoulder bags and rank the two listed bags by lower weight.

**Judge:** Both requested shoulder-bag cards contain the weights needed for ranking.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F010-K-A2

**Shopping/Research · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Compare 15-litre shoulder bags

**Candidate:** Prepare a weight-ranking routine

**Concrete work product:**

```text
Sort supplied product records by numeric weight_kg ascending; no records or capacity filter embedded.
```

**Full instruction:** Compare 15-litre shoulder bags and rank the two listed bags by lower weight.

**Judge:** The weight sorter directly implements the requested lower-weight ranking.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F010-R-A1

**Shopping/Research · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Compare 15-litre shoulder bags

**Candidate:** Retrieve bag specification cards

**Concrete work product:**

```text
Bag L: shoulder bag, 15 L, 0.5 kg; Bag M: shoulder bag, 15 L, 0.7 kg; neither converts to a backpack.
```

**Full instruction:** Compare 15-litre shoulder bags but compare 30-litre backpacks instead and do not include shoulder bags.

**Judge:** Neither 15-litre shoulder bag is an allowed 30-litre backpack.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F010-R-A2

**Shopping/Research · reusable · fraction 1 · confidence 3/5 · ambiguity Y

**Observed prefix:** Compare 15-litre shoulder bags

**Candidate:** Prepare a weight-ranking routine

**Concrete work product:**

```text
Sort supplied product records by numeric weight_kg ascending; no records or capacity filter embedded.
```

**Full instruction:** Compare 15-litre shoulder bags but compare 30-litre backpacks instead and do not include shoulder bags.

**Judge:** The generic sorter can organize backpack weights unchanged, although weight ranking is optional rather than explicitly requested in this full instruction.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F011-K-A1

**Shopping/Research · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find brown faux-suede jackets with stand collars

**Candidate:** Retrieve jacket cards

**Concrete work product:**

```text
Jacket A: brown faux suede, stand collar, 120 credits; Jacket B: brown faux suede, stand collar, 150 credits.
```

**Full instruction:** Find brown faux-suede jackets with stand collars and compare the listed options under 200 credits.

**Judge:** Both listed jackets match the attributes and fall below 200 credits.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F011-K-A2

**Shopping/Research · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find brown faux-suede jackets with stand collars

**Candidate:** Stage a product comparison layout

**Concrete work product:**

```text
Columns: material, color, collar type, price; values unfilled.
```

**Full instruction:** Find brown faux-suede jackets with stand collars and compare the listed options under 200 credits.

**Judge:** The unfilled product columns support comparing the requested jacket attributes and prices.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F011-R-A1

**Shopping/Research · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find brown faux-suede jackets with stand collars

**Candidate:** Retrieve jacket cards

**Concrete work product:**

```text
Jacket A: brown faux suede, stand collar, 120 credits; Jacket B: brown faux suede, stand collar, 150 credits.
```

**Full instruction:** Find brown faux-suede jackets with stand collars but use black cotton jackets with lapels instead and discard the original options.

**Judge:** The brown faux-suede stand-collar products are explicitly replaced and discarded.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F011-R-A2

**Shopping/Research · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find brown faux-suede jackets with stand collars

**Candidate:** Stage a product comparison layout

**Concrete work product:**

```text
Columns: material, color, collar type, price; values unfilled.
```

**Full instruction:** Find brown faux-suede jackets with stand collars but use black cotton jackets with lapels instead and discard the original options.

**Judge:** The unfilled material, color, collar and price columns accommodate the replacement jackets.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F012-K-A1

**Shopping/Research · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Compare robotics synthetic-data tools that support Engine R

**Candidate:** Retrieve tool compatibility cards

**Concrete work product:**

```text
Sim A and Sim B support Engine R only; neither supports Engine S.
```

**Full instruction:** Compare robotics synthetic-data tools that support Engine R and keep Engine R support mandatory.

**Judge:** Both compatibility cards establish mandatory Engine R support.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F012-K-A2

**Shopping/Research · reusable · fraction 1.0 · confidence 4/5 · ambiguity N

**Observed prefix:** Compare robotics synthetic-data tools that support Engine R

**Candidate:** Prepare a physics-evaluation checklist

**Concrete work product:**

```text
Check gravity, collision response, sensor noise and deterministic replay; no engine-specific commands.
```

**Full instruction:** Compare robotics synthetic-data tools that support Engine R and keep Engine R support mandatory.

**Judge:** The physics checklist remains applicable to evaluating Engine R simulation tools.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F012-R-A1

**Shopping/Research · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Compare robotics synthetic-data tools that support Engine R

**Candidate:** Retrieve tool compatibility cards

**Concrete work product:**

```text
Sim A and Sim B support Engine R only; neither supports Engine S.
```

**Full instruction:** Compare robotics synthetic-data tools that support Engine R but only consider tools for Engine S that do not support Engine R.

**Judge:** Neither Engine R-only tool supports the required Engine S.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F012-R-A2

**Shopping/Research · reusable · fraction 1.0 · confidence 4/5 · ambiguity N

**Observed prefix:** Compare robotics synthetic-data tools that support Engine R

**Candidate:** Prepare a physics-evaluation checklist

**Concrete work product:**

```text
Check gravity, collision response, sensor noise and deterministic replay; no engine-specific commands.
```

**Full instruction:** Compare robotics synthetic-data tools that support Engine R but only consider tools for Engine S that do not support Engine R.

**Judge:** The physics criteria contain no Engine R dependency and can evaluate Engine S tools.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F013-K-A1

**Shopping/Research · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find freestanding desk converters under 250 credits

**Candidate:** Retrieve converter cards

**Concrete work product:**

```text
Lift A: freestanding, 150 credits; Lift B: freestanding, 220 credits. Neither can be permanently mounted.
```

**Full instruction:** Find freestanding desk converters under 250 credits and exclude permanently mounted converters.

**Judge:** Both affordable converters are freestanding and satisfy the mounting exclusion.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F013-K-A2

**Shopping/Research · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find freestanding desk converters under 250 credits

**Candidate:** Prepare the price ceiling field

**Concrete work product:**

```text
Maximum price field: 250 credits; mounting type unfilled.
```

**Full instruction:** Find freestanding desk converters under 250 credits and exclude permanently mounted converters.

**Judge:** The 250-credit ceiling remains applicable to the freestanding search.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F013-R-A1

**Shopping/Research · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find freestanding desk converters under 250 credits

**Candidate:** Retrieve converter cards

**Concrete work product:**

```text
Lift A: freestanding, 150 credits; Lift B: freestanding, 220 credits. Neither can be permanently mounted.
```

**Full instruction:** Find freestanding desk converters under 250 credits but only show permanently mounted converters and discard freestanding ones.

**Judge:** Neither freestanding converter can meet the permanent-mount requirement.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F013-R-A2

**Shopping/Research · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find freestanding desk converters under 250 credits

**Candidate:** Prepare the price ceiling field

**Concrete work product:**

```text
Maximum price field: 250 credits; mounting type unfilled.
```

**Full instruction:** Find freestanding desk converters under 250 credits but only show permanently mounted converters and discard freestanding ones.

**Judge:** The price ceiling survives the mounting change because no mounting filter is filled in.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F014-K-A1

**Scheduling · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find a 30-minute meeting for Sam and me on Tuesday

**Candidate:** Read Tuesday availability

**Concrete work product:**

```text
Sam and requester both free Tuesday 14:00–14:30 and 15:00–15:30. No Wednesday availability included.
```

**Full instruction:** Find a 30-minute meeting for Sam and me on Tuesday and use either of the two listed Tuesday slots.

**Judge:** Both shared Tuesday slots satisfy the requested day and duration.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F014-K-A2

**Scheduling · non-reusable · fraction 0.67 · confidence 5/5 · ambiguity N

**Observed prefix:** Find a 30-minute meeting for Sam and me on Tuesday

**Candidate:** Stage a Wednesday calendar event

**Concrete work product:**

```text
Unsent event object: attendees Sam and requester, duration 30 minutes, day Wednesday; no time set.
```

**Full instruction:** Find a 30-minute meeting for Sam and me on Tuesday and use either of the two listed Tuesday slots.

**Judge:** Attendees and duration survive, while the Wednesday argument must be replaced with Tuesday.

**Author expectation / rater A / rater B:** reusable / non-reusable / non-reusable

## SX1-F014-R-A1

**Scheduling · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find a 30-minute meeting for Sam and me on Tuesday

**Candidate:** Read Tuesday availability

**Concrete work product:**

```text
Sam and requester both free Tuesday 14:00–14:30 and 15:00–15:30. No Wednesday availability included.
```

**Full instruction:** Find a 30-minute meeting for Sam and me on Tuesday but switch the meeting to Wednesday and ignore Tuesday availability.

**Judge:** Tuesday-only availability provides no Wednesday slots and is explicitly ignored.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F014-R-A2

**Scheduling · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find a 30-minute meeting for Sam and me on Tuesday

**Candidate:** Stage a Wednesday calendar event

**Concrete work product:**

```text
Unsent event object: attendees Sam and requester, duration 30 minutes, day Wednesday; no time set.
```

**Full instruction:** Find a 30-minute meeting for Sam and me on Tuesday but switch the meeting to Wednesday and ignore Tuesday availability.

**Judge:** The unsent Wednesday event already has the revised day, participants and duration.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F015-K-A1

**Scheduling · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Check whether my dentist can see me on Friday

**Candidate:** Read Friday availability

**Concrete work product:**

```text
The fixture dentist has no Friday openings; no Monday availability included.
```

**Full instruction:** Check whether my dentist can see me on Friday and keep my existing appointment if Friday has no openings.

**Judge:** The no-openings result resolves the condition for keeping the current appointment.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F015-K-A2

**Scheduling · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Check whether my dentist can see me on Friday

**Candidate:** Retrieve the existing appointment

**Concrete work product:**

```text
Current appointment: Wednesday 11:00, dentist Dr Vale, appointment ID D17.
```

**Full instruction:** Check whether my dentist can see me on Friday and keep my existing appointment if Friday has no openings.

**Judge:** The existing appointment record supplies the appointment retained when Friday is unavailable.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F015-R-A1

**Scheduling · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Check whether my dentist can see me on Friday

**Candidate:** Read Friday availability

**Concrete work product:**

```text
The fixture dentist has no Friday openings; no Monday availability included.
```

**Full instruction:** Check whether my dentist can see me on Friday but check Monday instead and ignore Friday openings, keeping my existing appointment as fallback.

**Judge:** Friday-only availability must be ignored and supplies no Monday openings.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F015-R-A2

**Scheduling · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Check whether my dentist can see me on Friday

**Candidate:** Retrieve the existing appointment

**Concrete work product:**

```text
Current appointment: Wednesday 11:00, dentist Dr Vale, appointment ID D17.
```

**Full instruction:** Check whether my dentist can see me on Friday but check Monday instead and ignore Friday openings, keeping my existing appointment as fallback.

**Judge:** The existing appointment record supplies the fallback retained under the Monday search.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F016-K-A1

**Scheduling · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find team meeting slots this week after 10 AM

**Candidate:** Read afternoon team availability

**Concrete work product:**

```text
Whole team free Thursday 13:00–13:30 and Friday 14:00–14:30; no morning data included.
```

**Full instruction:** Find team meeting slots this week after 10 AM and show the two listed afternoon slots.

**Judge:** The two afternoon slots meet the after-10-AM condition and are expressly requested.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F016-K-A2

**Scheduling · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find team meeting slots this week after 10 AM

**Candidate:** Prepare the participant list

**Concrete work product:**

```text
Participants: Sam, Jo and requester; no time selected.
```

**Full instruction:** Find team meeting slots this week after 10 AM and show the two listed afternoon slots.

**Judge:** The participant list remains needed for the requested team slots.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F016-R-A1

**Scheduling · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find team meeting slots this week after 10 AM

**Candidate:** Read afternoon team availability

**Concrete work product:**

```text
Whole team free Thursday 13:00–13:30 and Friday 14:00–14:30; no morning data included.
```

**Full instruction:** Find team meeting slots this week after 10 AM but only consider slots before 10 AM this week.

**Judge:** Only afternoon availability is retained for a before-10-AM search.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F016-R-A2

**Scheduling · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find team meeting slots this week after 10 AM

**Candidate:** Prepare the participant list

**Concrete work product:**

```text
Participants: Sam, Jo and requester; no time selected.
```

**Full instruction:** Find team meeting slots this week after 10 AM but only consider slots before 10 AM this week.

**Judge:** The same participants are needed for the revised morning availability search.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F017-K-A1

**Scheduling · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Prepare a report reminder for tomorrow morning

**Candidate:** Stage a morning reminder

**Concrete work product:**

```text
Unsent reminder: title Submit report, day tomorrow, time 09:00.
```

**Full instruction:** Prepare a report reminder for tomorrow morning and set its time to 9 AM.

**Judge:** The staged tomorrow-at-09:00 reminder matches the final requested schedule.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F017-K-A2

**Scheduling · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Prepare a report reminder for tomorrow morning

**Candidate:** Prepare the reminder text

**Concrete work product:**

```text
Reminder title: Submit report; date and time unfilled.
```

**Full instruction:** Prepare a report reminder for tomorrow morning and set its time to 9 AM.

**Judge:** The report reminder title remains usable when the requested morning time is filled in.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F017-R-A1

**Scheduling · non-reusable · fraction 0.67 · confidence 5/5 · ambiguity N

**Observed prefix:** Prepare a report reminder for tomorrow morning

**Candidate:** Stage a morning reminder

**Concrete work product:**

```text
Unsent reminder: title Submit report, day tomorrow, time 09:00.
```

**Full instruction:** Prepare a report reminder for tomorrow morning but change it to tomorrow evening at 7 PM.

**Judge:** The title and day survive, but changing 09:00 to 19:00 materially changes the staged reminder argument.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F017-R-A2

**Scheduling · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Prepare a report reminder for tomorrow morning

**Candidate:** Prepare the reminder text

**Concrete work product:**

```text
Reminder title: Submit report; date and time unfilled.
```

**Full instruction:** Prepare a report reminder for tomorrow morning but change it to tomorrow evening at 7 PM.

**Judge:** The reminder title survives the change from morning to evening.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F018-K-A1

**Communication · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Draft a reply thanking Morgan for the introduction

**Candidate:** Draft the thank-you sentence

**Concrete work product:**

```text
Thank you for making the introduction, Morgan.
```

**Full instruction:** Draft a reply thanking Morgan for the introduction and offer to provide more information.

**Judge:** The thank-you sentence remains required before the additional offer.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F018-K-A2

**Communication · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Draft a reply thanking Morgan for the introduction

**Candidate:** Draft an offer sentence

**Concrete work product:**

```text
I would be happy to provide any additional information you need.
```

**Full instruction:** Draft a reply thanking Morgan for the introduction and offer to provide more information.

**Judge:** The offer sentence directly satisfies the request for additional-information wording.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F018-R-A1

**Communication · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Draft a reply thanking Morgan for the introduction

**Candidate:** Draft the thank-you sentence

**Concrete work product:**

```text
Thank you for making the introduction, Morgan.
```

**Full instruction:** Draft a reply thanking Morgan for the introduction but do not thank Morgan or mention the introduction; only decline the invitation.

**Judge:** The sentence thanks Morgan and mentions the expressly excluded introduction.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F018-R-A2

**Communication · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Draft a reply thanking Morgan for the introduction

**Candidate:** Draft an offer sentence

**Concrete work product:**

```text
I would be happy to provide any additional information you need.
```

**Full instruction:** Draft a reply thanking Morgan for the introduction but do not thank Morgan or mention the introduction; only decline the invitation.

**Judge:** An offer of further information does not belong in the requested decline-only reply.

**Author expectation / rater A / rater B:** reusable / non-reusable / non-reusable

## SX1-F019-K-A1

**Communication · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Draft a team update saying the build is delayed

**Candidate:** Draft the status sentence

**Concrete work product:**

```text
The build is delayed; we are still investigating the cause.
```

**Full instruction:** Draft a team update saying the build is delayed and keep the cause neutral because it is not yet known.

**Judge:** The delay sentence states that the cause remains under investigation without assigning blame.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F019-K-A2

**Communication · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Draft a team update saying the build is delayed

**Candidate:** Stage a neutral update heading

**Concrete work product:**

```text
Heading: Build status update; no status claim or cause included.
```

**Full instruction:** Draft a team update saying the build is delayed and keep the cause neutral because it is not yet known.

**Judge:** The neutral build-status heading makes no unsupported causal claim.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F019-R-A1

**Communication · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Draft a team update saying the build is delayed

**Candidate:** Draft the status sentence

**Concrete work product:**

```text
The build is delayed; we are still investigating the cause.
```

**Full instruction:** Draft a team update saying the build is delayed but the build is on schedule, so report that and do not mention a delay.

**Judge:** The delay statement and investigation wording conflict with the on-schedule update.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F019-R-A2

**Communication · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Draft a team update saying the build is delayed

**Candidate:** Stage a neutral update heading

**Concrete work product:**

```text
Heading: Build status update; no status claim or cause included.
```

**Full instruction:** Draft a team update saying the build is delayed but the build is on schedule, so report that and do not mention a delay.

**Judge:** The neutral heading accommodates an on-schedule status without mentioning delay.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F020-K-A1

**Communication · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Draft a message declining dinner tonight

**Candidate:** Draft the decline sentence

**Concrete work product:**

```text
I cannot make dinner tonight.
```

**Full instruction:** Draft a message declining dinner tonight and suggest meeting next weekend.

**Judge:** The dinner decline remains needed alongside the alternative date.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F020-K-A2

**Communication · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Draft a message declining dinner tonight

**Candidate:** Draft the alternative-date sentence

**Concrete work product:**

```text
Would you like to meet next weekend instead?
```

**Full instruction:** Draft a message declining dinner tonight and suggest meeting next weekend.

**Judge:** The next-weekend invitation directly supplies the requested alternative.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F020-R-A1

**Communication · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Draft a message declining dinner tonight

**Candidate:** Draft the decline sentence

**Concrete work product:**

```text
I cannot make dinner tonight.
```

**Full instruction:** Draft a message declining dinner tonight but accept dinner tonight instead and do not suggest another date.

**Judge:** The decline sentence contradicts the required acceptance.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F020-R-A2

**Communication · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Draft a message declining dinner tonight

**Candidate:** Draft the alternative-date sentence

**Concrete work product:**

```text
Would you like to meet next weekend instead?
```

**Full instruction:** Draft a message declining dinner tonight but accept dinner tonight instead and do not suggest another date.

**Judge:** The next-weekend proposal directly violates the instruction not to suggest another date.

**Author expectation / rater A / rater B:** reusable / non-reusable / non-reusable

## SX1-F021-K-A1

**Communication · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Draft a refund approval message

**Candidate:** Draft the approval sentence

**Concrete work product:**

```text
Your refund has been approved.
```

**Full instruction:** Draft a refund approval message and avoid promising a payment date.

**Judge:** The approval sentence promises no payment date.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F021-K-A2

**Communication · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Draft a refund approval message

**Candidate:** Stage an approval-specific reply template

**Concrete work product:**

```text
Subject: Refund approved. Closing: Thank you for your patience. Body unfilled.
```

**Full instruction:** Draft a refund approval message and avoid promising a payment date.

**Judge:** The approval subject and polite closing promise no payment date.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F021-R-A1

**Communication · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Draft a refund approval message

**Candidate:** Draft the approval sentence

**Concrete work product:**

```text
Your refund has been approved.
```

**Full instruction:** Draft a refund approval message but the refund is denied, so explain the denial and do not promise payment.

**Judge:** The approval sentence contradicts the required denial.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F021-R-A2

**Communication · non-reusable · fraction 0.5 · confidence 5/5 · ambiguity N

**Observed prefix:** Draft a refund approval message

**Candidate:** Stage an approval-specific reply template

**Concrete work product:**

```text
Subject: Refund approved. Closing: Thank you for your patience. Body unfilled.
```

**Full instruction:** Draft a refund approval message but the refund is denied, so explain the denial and do not promise payment.

**Judge:** The closing survives, while the approval subject must be replaced to avoid falsely approving a denied refund.

**Author expectation / rater A / rater B:** reusable / non-reusable / non-reusable

## SX1-F022-K-A1

**Information Retrieval · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find peer-reviewed papers about hidden-state probing

**Candidate:** Retrieve peer-reviewed fixture records

**Concrete work product:**

```text
Paper P and Paper Q: peer-reviewed hidden-state probing papers in the synthetic catalogue; no technical reports included.
```

**Full instruction:** Find peer-reviewed papers about hidden-state probing and use only peer-reviewed sources.

**Judge:** Both stipulated papers satisfy the peer-review and topic requirements.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F022-K-A2

**Information Retrieval · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find peer-reviewed papers about hidden-state probing

**Candidate:** Prepare the topic search terms

**Concrete work product:**

```text
Terms: hidden-state probing, representation analysis; no publication-type filter.
```

**Full instruction:** Find peer-reviewed papers about hidden-state probing and use only peer-reviewed sources.

**Judge:** The topic terms remain usable when a peer-review restriction is added.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F022-R-A1

**Information Retrieval · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find peer-reviewed papers about hidden-state probing

**Candidate:** Retrieve peer-reviewed fixture records

**Concrete work product:**

```text
Paper P and Paper Q: peer-reviewed hidden-state probing papers in the synthetic catalogue; no technical reports included.
```

**Full instruction:** Find peer-reviewed papers about hidden-state probing but use only non-peer-reviewed technical reports about hidden-state probing.

**Judge:** Neither peer-reviewed record is an allowed non-peer-reviewed technical report.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F022-R-A2

**Information Retrieval · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find peer-reviewed papers about hidden-state probing

**Candidate:** Prepare the topic search terms

**Concrete work product:**

```text
Terms: hidden-state probing, representation analysis; no publication-type filter.
```

**Full instruction:** Find peer-reviewed papers about hidden-state probing but use only non-peer-reviewed technical reports about hidden-state probing.

**Judge:** The topic terms remain usable for technical reports because no peer-review filter is embedded.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F023-K-A1

**Information Retrieval · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find version 3 documentation for Library L

**Candidate:** Retrieve versioned documentation

**Concrete work product:**

```text
Official Library L version 3: old_connect(endpoint) is the connection entry point. This fixture marks it removed in version 4.
```

**Full instruction:** Find version 3 documentation for Library L and use only the official version 3 material.

**Judge:** The official version 3 entry point belongs to the required documentation version.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F023-K-A2

**Information Retrieval · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find version 3 documentation for Library L

**Candidate:** Retrieve the official documentation index URL

**Concrete work product:**

```text
Fixture URL: https://library-l.example/docs/ ; index lists version 3 and version 4.
```

**Full instruction:** Find version 3 documentation for Library L and use only the official version 3 material.

**Judge:** The official index provides the required version 3 documentation entry.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F023-R-A1

**Information Retrieval · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find version 3 documentation for Library L

**Candidate:** Retrieve versioned documentation

**Concrete work product:**

```text
Official Library L version 3: old_connect(endpoint) is the connection entry point. This fixture marks it removed in version 4.
```

**Full instruction:** Find version 3 documentation for Library L but use version 4 instead and exclude all version 3 documentation.

**Judge:** The retrieved version 3 entry point is removed in the required version 4.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F023-R-A2

**Information Retrieval · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find version 3 documentation for Library L

**Candidate:** Retrieve the official documentation index URL

**Concrete work product:**

```text
Fixture URL: https://library-l.example/docs/ ; index lists version 3 and version 4.
```

**Full instruction:** Find version 3 documentation for Library L but use version 4 instead and exclude all version 3 documentation.

**Judge:** The same documentation index provides an entry to version 4.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F024-K-A1

**Information Retrieval · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Compare Acme's revenue in its two annual releases

**Candidate:** Extract Acme revenue figures

**Concrete work product:**

```text
Acme fixture: prior year revenue 10 million credits; current year 12 million credits.
```

**Full instruction:** Compare Acme's revenue in its two annual releases and report company-stated actual revenue only.

**Judge:** The extracted revenue figures are the requested actual company revenues.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F024-K-A2

**Information Retrieval · unresolved · fraction None · confidence 2/5 · ambiguity Y

**Observed prefix:** Compare Acme's revenue in its two annual releases

**Candidate:** Calculate Acme revenue growth

**Concrete work product:**

```text
Acme revenue growth = (12 − 10) / 10 = 20%; calculation uses Acme values.
```

**Full instruction:** Compare Acme's revenue in its two annual releases and report company-stated actual revenue only.

**Judge:** The growth result is excluded, and this item does not establish the operands as company-stated actual revenue with units and year mapping; neither their reportability nor salvage materiality is settled.

**Author expectation / rater A / rater B:** reusable / non-reusable / reusable

## SX1-F024-R-A1

**Information Retrieval · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Compare Acme's revenue in its two annual releases

**Candidate:** Extract Acme revenue figures

**Concrete work product:**

```text
Acme fixture: prior year revenue 10 million credits; current year 12 million credits.
```

**Full instruction:** Compare Acme's revenue in its two annual releases but compare Beacon's releases instead, with no Acme figures.

**Judge:** The Acme revenue figures are expressly excluded from the Beacon comparison.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F024-R-A2

**Information Retrieval · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Compare Acme's revenue in its two annual releases

**Candidate:** Calculate Acme revenue growth

**Concrete work product:**

```text
Acme revenue growth = (12 − 10) / 10 = 20%; calculation uses Acme values.
```

**Full instruction:** Compare Acme's revenue in its two annual releases but compare Beacon's releases instead, with no Acme figures.

**Judge:** The calculation uses Acme figures that are expressly excluded from the Beacon task.

**Author expectation / rater A / rater B:** reusable / non-reusable / non-reusable

## SX1-F025-K-A1

**Information Retrieval · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find primary rules for Region A consumer AI systems

**Candidate:** Retrieve jurisdiction-specific rule cards

**Concrete work product:**

```text
Rule A1 and Rule A2: synthetic Region A consumer-AI rules, with no applicability in Region B.
```

**Full instruction:** Find primary rules for Region A consumer AI systems and keep Region A as the main jurisdiction.

**Judge:** Both rule cards belong to the retained Region A jurisdiction.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F025-K-A2

**Information Retrieval · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find primary rules for Region A consumer AI systems

**Candidate:** Stage a legal-source comparison layout

**Concrete work product:**

```text
Columns: jurisdiction, issuing authority, effective date, provision; no legal claims filled in.
```

**Full instruction:** Find primary rules for Region A consumer AI systems and keep Region A as the main jurisdiction.

**Judge:** The unpopulated legal-source columns support the Region A comparison.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F025-R-A1

**Information Retrieval · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find primary rules for Region A consumer AI systems

**Candidate:** Retrieve jurisdiction-specific rule cards

**Concrete work product:**

```text
Rule A1 and Rule A2: synthetic Region A consumer-AI rules, with no applicability in Region B.
```

**Full instruction:** Find primary rules for Region A consumer AI systems but use Region B rules only and exclude Region A rules.

**Judge:** Neither Region A rule applies to the required Region B jurisdiction.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F025-R-A2

**Information Retrieval · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find primary rules for Region A consumer AI systems

**Candidate:** Stage a legal-source comparison layout

**Concrete work product:**

```text
Columns: jurisdiction, issuing authority, effective date, provision; no legal claims filled in.
```

**Full instruction:** Find primary rules for Region A consumer AI systems but use Region B rules only and exclude Region A rules.

**Judge:** The jurisdiction-neutral source layout can be populated with Region B rules.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F026-K-A1

**Information Retrieval · reusable · fraction 1 · confidence 5/5 · ambiguity N

**Observed prefix:** Compare small open-weight reasoning models

**Candidate:** Collect vendor-only benchmark claims

**Concrete work product:**

```text
Vendor card: Model K claims 80 points and Model J claims 85 points; neither claim is independently reproduced.
```

**Full instruction:** Compare small open-weight reasoning models and flag vendor-only scores as unverified rather than treating them as evidence.

**Judge:** The vendor claims survive specifically as claims to flag unverified, with no need to treat them as evidence.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F026-K-A2

**Information Retrieval · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Compare small open-weight reasoning models

**Candidate:** Collect independent fixture benchmark records

**Concrete work product:**

```text
Independent lab fixture: Model K 70 points, Model J 72 points, same test and evaluation settings; both small and open-weight.
```

**Full instruction:** Compare small open-weight reasoning models and flag vendor-only scores as unverified rather than treating them as evidence.

**Judge:** The independent scores remain usable evidence under the vendor-score warning.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F026-R-A1

**Information Retrieval · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Compare small open-weight reasoning models

**Candidate:** Collect vendor-only benchmark claims

**Concrete work product:**

```text
Vendor card: Model K claims 80 points and Model J claims 85 points; neither claim is independently reproduced.
```

**Full instruction:** Compare small open-weight reasoning models but include only independently reproduced scores and omit vendor-only claims entirely.

**Judge:** Both retained scores are vendor-only claims expressly excluded from the comparison.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F026-R-A2

**Information Retrieval · reusable · fraction 1 · confidence 4/5 · ambiguity Y

**Observed prefix:** Compare small open-weight reasoning models

**Candidate:** Collect independent fixture benchmark records

**Concrete work product:**

```text
Independent lab fixture: Model K 70 points, Model J 72 points, same test and evaluation settings; both small and open-weight.
```

**Full instruction:** Compare small open-weight reasoning models but include only independently reproduced scores and omit vendor-only claims entirely.

**Judge:** The supplied independent lab scores are reusable under the independent-evaluation reading of reproduced scores; the fixture does not document a replication protocol.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F027-K-A1

**Finance-like Read-only Analysis · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Calculate a 7 percent downside scenario for a 100-credit index

**Candidate:** Calculate the requested scenario

**Concrete work product:**

```text
100 × (1 − 0.07) = 93 credits; only the 7% result retained.
```

**Full instruction:** Calculate a 7 percent downside scenario for a 100-credit index and show the hypothetical level without making a trade.

**Judge:** The retained 93-credit result is the requested seven-percent scenario.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F027-K-A2

**Finance-like Read-only Analysis · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Calculate a 7 percent downside scenario for a 100-credit index

**Candidate:** Prepare the scenario formula

**Concrete work product:**

```text
Scenario level = starting level × (1 − decline_fraction); no numeric assumptions embedded.
```

**Full instruction:** Calculate a 7 percent downside scenario for a 100-credit index and show the hypothetical level without making a trade.

**Judge:** The symbolic downside formula supports the hypothetical calculation without trading.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F027-R-A1

**Finance-like Read-only Analysis · non-reusable · fraction 0.25 · confidence 5/5 · ambiguity Y

**Observed prefix:** Calculate a 7 percent downside scenario for a 100-credit index

**Candidate:** Calculate the requested scenario

**Concrete work product:**

```text
100 × (1 − 0.07) = 93 credits; only the 7% result retained.
```

**Full instruction:** Calculate a 7 percent downside scenario for a 100-credit index but use a 12 percent decline instead and omit the 7 percent case.

**Judge:** The 100-credit starting value survives as an operand, but the sole scenario result must be recalculated and excluded.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F027-R-A2

**Finance-like Read-only Analysis · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Calculate a 7 percent downside scenario for a 100-credit index

**Candidate:** Prepare the scenario formula

**Concrete work product:**

```text
Scenario level = starting level × (1 − decline_fraction); no numeric assumptions embedded.
```

**Full instruction:** Calculate a 7 percent downside scenario for a 100-credit index but use a 12 percent decline instead and omit the 7 percent case.

**Judge:** The symbolic formula accommodates twelve percent without retaining the rejected numerical result.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F028-K-A1

**Finance-like Read-only Analysis · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Calculate budget variance from my supplied table

**Candidate:** Compute category variances

**Concrete work product:**

```text
Fixture variances: supplies +20 credits, travel +5 credits, meals −10 credits; positive means overspend.
```

**Full instruction:** Calculate budget variance from my supplied table and identify the largest overspend.

**Judge:** The category variances identify supplies as the largest overspend.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F028-K-A2

**Finance-like Read-only Analysis · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Calculate budget variance from my supplied table

**Candidate:** Aggregate actual category totals

**Concrete work product:**

```text
Fixture actuals: supplies 120 credits, travel 85 credits, meals 40 credits; source-table sums retained.
```

**Full instruction:** Calculate budget variance from my supplied table and identify the largest overspend.

**Judge:** The retained actual totals are inputs to computing each category's overspend.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F028-R-A1

**Finance-like Read-only Analysis · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Calculate budget variance from my supplied table

**Candidate:** Compute category variances

**Concrete work product:**

```text
Fixture variances: supplies +20 credits, travel +5 credits, meals −10 credits; positive means overspend.
```

**Full instruction:** Calculate budget variance from my supplied table but show actual category totals only, without calculating or reporting variances.

**Judge:** Only forbidden variances are retained, with no actual totals to reuse.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F028-R-A2

**Finance-like Read-only Analysis · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Calculate budget variance from my supplied table

**Candidate:** Aggregate actual category totals

**Concrete work product:**

```text
Fixture actuals: supplies 120 credits, travel 85 credits, meals 40 credits; source-table sums retained.
```

**Full instruction:** Calculate budget variance from my supplied table but show actual category totals only, without calculating or reporting variances.

**Judge:** The actual category totals are exactly the revised requested output.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F029-K-A1

**Finance-like Read-only Analysis · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Compare current holdings with the start-of-month snapshot

**Candidate:** Calculate start-of-month concentration

**Concrete work product:**

```text
Start-of-month fixture: asset A 60%, asset B 40%; no other date included.
```

**Full instruction:** Compare current holdings with the start-of-month snapshot and report concentration changes for those two snapshots.

**Judge:** The start-of-month percentages supply the required historical concentration snapshot.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F029-K-A2

**Finance-like Read-only Analysis · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Compare current holdings with the start-of-month snapshot

**Candidate:** Calculate current concentration

**Concrete work product:**

```text
Current fixture: asset A 50%, asset B 50%; values unchanged across comparisons.
```

**Full instruction:** Compare current holdings with the start-of-month snapshot and report concentration changes for those two snapshots.

**Judge:** Current concentration is one of the required comparison snapshots.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F029-R-A1

**Finance-like Read-only Analysis · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Compare current holdings with the start-of-month snapshot

**Candidate:** Calculate start-of-month concentration

**Concrete work product:**

```text
Start-of-month fixture: asset A 60%, asset B 40%; no other date included.
```

**Full instruction:** Compare current holdings with the start-of-month snapshot but compare current holdings with the start-of-year snapshot instead and ignore start-of-month holdings.

**Judge:** The retained start-of-month snapshot is explicitly excluded from the revised comparison.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F029-R-A2

**Finance-like Read-only Analysis · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Compare current holdings with the start-of-month snapshot

**Candidate:** Calculate current concentration

**Concrete work product:**

```text
Current fixture: asset A 50%, asset B 50%; values unchanged across comparisons.
```

**Full instruction:** Compare current holdings with the start-of-month snapshot but compare current holdings with the start-of-year snapshot instead and ignore start-of-month holdings.

**Judge:** The current concentration snapshot remains required when the historical baseline changes.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F030-K-A1

**Finance-like Read-only Analysis · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Calculate breakeven for my debit spread using the supplied values

**Candidate:** Calculate the original breakeven

**Concrete work product:**

```text
For this fixture's specified call debit spread: 100 + 5 = 105 credits.
```

**Full instruction:** Calculate breakeven for my debit spread using the supplied values and use the supplied 5-credit debit and 100-credit lower strike.

**Judge:** The 105-credit calculation uses exactly the final supplied strike and debit.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F030-K-A2

**Finance-like Read-only Analysis · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Calculate breakeven for my debit spread using the supplied values

**Candidate:** Prepare the symbolic breakeven expression

**Concrete work product:**

```text
For the specified call debit spread: lower_strike + net_debit; no prices filled in.
```

**Full instruction:** Calculate breakeven for my debit spread using the supplied values and use the supplied 5-credit debit and 100-credit lower strike.

**Judge:** The symbolic call-spread expression supports substitution of the supplied strike and debit.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F030-R-A1

**Finance-like Read-only Analysis · non-reusable · fraction 0.33 · confidence 5/5 · ambiguity N

**Observed prefix:** Calculate breakeven for my debit spread using the supplied values

**Candidate:** Calculate the original breakeven

**Concrete work product:**

```text
For this fixture's specified call debit spread: 100 + 5 = 105 credits.
```

**Full instruction:** Calculate breakeven for my debit spread using the supplied values but correct the debit to 8 credits while keeping the lower strike at 100 credits.

**Judge:** The lower strike remains 100, but changing the debit invalidates the computed 105-credit result.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F030-R-A2

**Finance-like Read-only Analysis · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Calculate breakeven for my debit spread using the supplied values

**Candidate:** Prepare the symbolic breakeven expression

**Concrete work product:**

```text
For the specified call debit spread: lower_strike + net_debit; no prices filled in.
```

**Full instruction:** Calculate breakeven for my debit spread using the supplied values but correct the debit to 8 credits while keeping the lower strike at 100 credits.

**Judge:** The symbolic expression accepts the corrected debit without revising its formula.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F031-K-A1

**Coding · unresolved · fraction None · confidence 2/5 · ambiguity Y

**Observed prefix:** Write a Python function that counts ERROR lines in the supplied log

**Candidate:** Stage an ERROR-counting function

**Concrete work product:**

```text
def count_lines(lines): return sum(line.startswith('ERROR ') for line in lines)
```

**Full instruction:** Write a Python function that counts ERROR lines in the supplied log and return the count without changing the file.

**Judge:** The item supplies no log format establishing that ERROR lines start with ERROR plus a space, so correctness and required predicate revision remain unresolved.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F031-K-A2

**Coding · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Write a Python function that counts ERROR lines in the supplied log

**Candidate:** Stage a log-reading helper

**Concrete work product:**

```text
def read_lines(path):
    with open(path, encoding='utf-8') as f:
        return f.read().splitlines()
```

**Full instruction:** Write a Python function that counts ERROR lines in the supplied log and return the count without changing the file.

**Judge:** The read-only helper supplies log lines without changing the file.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F031-R-A1

**Coding · non-reusable · fraction 0.5 · confidence 4/5 · ambiguity Y

**Observed prefix:** Write a Python function that counts ERROR lines in the supplied log

**Candidate:** Stage an ERROR-counting function

**Concrete work product:**

```text
def count_lines(lines): return sum(line.startswith('ERROR ') for line in lines)
```

**Full instruction:** Write a Python function that counts ERROR lines in the supplied log but count WARN lines instead and do not count ERROR lines.

**Judge:** The iteration and summation survive, but the ERROR predicate materially contradicts the required WARN count.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F031-R-A2

**Coding · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Write a Python function that counts ERROR lines in the supplied log

**Candidate:** Stage a log-reading helper

**Concrete work product:**

```text
def read_lines(path):
    with open(path, encoding='utf-8') as f:
        return f.read().splitlines()
```

**Full instruction:** Write a Python function that counts ERROR lines in the supplied log but count WARN lines instead and do not count ERROR lines.

**Judge:** The read-only helper supplies lines regardless of the severity ultimately counted.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F032-K-A1

**Coding · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Inspect the client timeout path without changing the code

**Candidate:** Collect a timeout observation

**Concrete work product:**

```text
Fixture client.py line 8: DEFAULT_TIMEOUT = 5; request() passes this constant as its timeout argument.
```

**Full instruction:** Inspect the client timeout path without changing the code and identify where its five-second timeout is set.

**Judge:** The observation identifies both the five-second constant and its request usage.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F032-K-A2

**Coding · unresolved · fraction None · confidence 2/5 · ambiguity Y

**Observed prefix:** Inspect the client timeout path without changing the code

**Candidate:** Stage a ten-second timeout patch

**Concrete work product:**

```text
Unapplied patch replaces DEFAULT_TIMEOUT = 5 with DEFAULT_TIMEOUT = 10; no other edits.
```

**Full instruction:** Inspect the client timeout path without changing the code and identify where its five-second timeout is set.

**Judge:** The patch contains the old five-second constant but no location metadata; the rubric does not settle whether salvaging that observation while discarding the edit avoids material reexecution.

**Author expectation / rater A / rater B:** reusable / non-reusable / non-reusable

## SX1-F032-R-A1

**Coding · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Inspect the client timeout path without changing the code

**Candidate:** Collect a timeout observation

**Concrete work product:**

```text
Fixture client.py line 8: DEFAULT_TIMEOUT = 5; request() passes this constant as its timeout argument.
```

**Full instruction:** Inspect the client timeout path without changing the code but modify the default timeout to ten seconds instead of producing an inspection report.

**Judge:** The observation identifies the exact constant and usage needed for the timeout edit.

**Author expectation / rater A / rater B:** non-reusable / reusable / reusable

## SX1-F032-R-A2

**Coding · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Inspect the client timeout path without changing the code

**Candidate:** Stage a ten-second timeout patch

**Concrete work product:**

```text
Unapplied patch replaces DEFAULT_TIMEOUT = 5 with DEFAULT_TIMEOUT = 10; no other edits.
```

**Full instruction:** Inspect the client timeout path without changing the code but modify the default timeout to ten seconds instead of producing an inspection report.

**Judge:** The unapplied patch makes precisely the revised ten-second default change.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F033-K-A1

**Coding · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Refactor the add function while preserving its public name and behavior

**Candidate:** Stage the preserving refactor

**Concrete work product:**

```text
Replacement definition: def add(a, b): return a + b; public symbol remains add.
```

**Full instruction:** Refactor the add function while preserving its public name and behavior and keep its existing callers compatible.

**Judge:** The replacement retains the add symbol and addition behavior needed by existing callers.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F033-K-A2

**Coding · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Refactor the add function while preserving its public name and behavior

**Candidate:** Stage addition behavior tests

**Concrete work product:**

```text
Assertions: operation(2, 3) == 5; operation(-1, 1) == 0; operation supplied by the test harness, not hardcoded to a name.
```

**Full instruction:** Refactor the add function while preserving its public name and behavior and keep its existing callers compatible.

**Judge:** The name-independent assertions check the addition behavior that must be preserved.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F033-R-A1

**Coding · non-reusable · fraction 0.5 · confidence 4/5 · ambiguity Y

**Observed prefix:** Refactor the add function while preserving its public name and behavior

**Candidate:** Stage the preserving refactor

**Concrete work product:**

```text
Replacement definition: def add(a, b): return a + b; public symbol remains add.
```

**Full instruction:** Refactor the add function while preserving its public name and behavior but rename the public function to total and update callers to use total.

**Judge:** The addition expression survives, but the public symbol must change to total, a functional interface revision rather than cosmetic wording.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F033-R-A2

**Coding · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Refactor the add function while preserving its public name and behavior

**Candidate:** Stage addition behavior tests

**Concrete work product:**

```text
Assertions: operation(2, 3) == 5; operation(-1, 1) == 0; operation supplied by the test harness, not hardcoded to a name.
```

**Full instruction:** Refactor the add function while preserving its public name and behavior but rename the public function to total and update callers to use total.

**Judge:** The behavior assertions use a harness-supplied operation and survive the public-name change.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F034-K-A1

**Coding · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Add malformed-JSON tests to the parser

**Candidate:** Stage malformed-input test cases

**Concrete work product:**

```text
Inputs: an unmatched opening brace, an unfinished numeric array, and an object with an unquoted key; expected outcome for each: parse error.
```

**Full instruction:** Add malformed-JSON tests to the parser and keep this work limited to correctness tests.

**Judge:** The malformed inputs and expected parse errors directly constitute correctness cases.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F034-K-A2

**Coding · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Add malformed-JSON tests to the parser

**Candidate:** Prepare a correctness-test report layout

**Concrete work product:**

```text
Columns: malformed input, expected error, observed error; no timing column.
```

**Full instruction:** Add malformed-JSON tests to the parser and keep this work limited to correctness tests.

**Judge:** Expected and observed error columns organize the requested correctness tests.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F034-R-A1

**Coding · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Add malformed-JSON tests to the parser

**Candidate:** Stage malformed-input test cases

**Concrete work product:**

```text
Inputs: an unmatched opening brace, an unfinished numeric array, and an object with an unquoted key; expected outcome for each: parse error.
```

**Full instruction:** Add malformed-JSON tests to the parser but benchmark parsing speed only and do not add correctness tests.

**Judge:** The staged malformed-input correctness cases do not provide the requested speed measurements.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F034-R-A2

**Coding · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Add malformed-JSON tests to the parser

**Candidate:** Prepare a correctness-test report layout

**Concrete work product:**

```text
Columns: malformed input, expected error, observed error; no timing column.
```

**Full instruction:** Add malformed-JSON tests to the parser but benchmark parsing speed only and do not add correctness tests.

**Judge:** The error-correctness columns omit timing and need redesign for speed benchmarking.

**Author expectation / rater A / rater B:** reusable / non-reusable / non-reusable

## SX1-F035-K-A1

**Document Work · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Rewrite this note for executives while preserving its numbers

**Candidate:** Draft the executive summary

**Concrete work product:**

```text
The project will take 12 weeks with a budget of 30 credits; the decision needed is approval to proceed.
```

**Full instruction:** Rewrite this note for executives while preserving its numbers and keep both the 12-week duration and 30-credit budget.

**Judge:** The executive summary preserves the specified duration and budget.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F035-K-A2

**Document Work · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Rewrite this note for executives while preserving its numbers

**Candidate:** Extract the unchanged duration

**Concrete work product:**

```text
Duration fact from the supplied fixture note: 12 weeks.
```

**Full instruction:** Rewrite this note for executives while preserving its numbers and keep both the 12-week duration and 30-credit budget.

**Judge:** The 12-week duration is explicitly preserved in the rewrite.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F035-R-A1

**Document Work · non-reusable · fraction 0.4 · confidence 4/5 · ambiguity Y

**Observed prefix:** Rewrite this note for executives while preserving its numbers

**Candidate:** Draft the executive summary

**Concrete work product:**

```text
The project will take 12 weeks with a budget of 30 credits; the decision needed is approval to proceed.
```

**Full instruction:** Rewrite this note for executives while preserving its numbers but make it a technical note for engineers and correct the budget to 40 credits.

**Judge:** The 12-week fact survives, but the incorrect budget and executive-oriented framing require revision for the engineering note.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F035-R-A2

**Document Work · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Rewrite this note for executives while preserving its numbers

**Candidate:** Extract the unchanged duration

**Concrete work product:**

```text
Duration fact from the supplied fixture note: 12 weeks.
```

**Full instruction:** Rewrite this note for executives while preserving its numbers but make it a technical note for engineers and correct the budget to 40 credits.

**Judge:** The 12-week fact survives the audience change and budget correction.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F036-K-A1

**Document Work · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Summarize the main report without using the appendix

**Candidate:** Extract main-report finding

**Concrete work product:**

```text
Main report fixture: trial A completed in 8 days with 2 defects. This fact appears only in the main report.
```

**Full instruction:** Summarize the main report without using the appendix and use only the main report findings.

**Judge:** The extracted finding comes from the requested main report.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F036-K-A2

**Document Work · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Summarize the main report without using the appendix

**Candidate:** Stage a summary layout

**Concrete work product:**

```text
Headings: objective, evidence, limitations; no source facts populated.
```

**Full instruction:** Summarize the main report without using the appendix and use only the main report findings.

**Judge:** The empty summary headings can organize main-report findings.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F036-R-A1

**Document Work · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Summarize the main report without using the appendix

**Candidate:** Extract main-report finding

**Concrete work product:**

```text
Main report fixture: trial A completed in 8 days with 2 defects. This fact appears only in the main report.
```

**Full instruction:** Summarize the main report without using the appendix but summarize the appendix only and ignore the main report.

**Judge:** The finding appears only in the main report that must be ignored.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F036-R-A2

**Document Work · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Summarize the main report without using the appendix

**Candidate:** Stage a summary layout

**Concrete work product:**

```text
Headings: objective, evidence, limitations; no source facts populated.
```

**Full instruction:** Summarize the main report without using the appendix but summarize the appendix only and ignore the main report.

**Judge:** The empty summary headings can organize appendix content without carrying main-report facts.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F037-K-A1

**Document Work · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Draft a proposal from these notes and leave pricing undecided

**Candidate:** Stage the pricing section

**Concrete work product:**

```text
Pricing: TBD. No numeric quote is included.
```

**Full instruction:** Draft a proposal from these notes and leave pricing undecided and mark pricing as TBD.

**Judge:** The pricing section marks pricing TBD as requested.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F037-K-A2

**Document Work · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Draft a proposal from these notes and leave pricing undecided

**Candidate:** Stage the scope section

**Concrete work product:**

```text
Scope: deliver one dashboard and its handover guide; no price or schedule included.
```

**Full instruction:** Draft a proposal from these notes and leave pricing undecided and mark pricing as TBD.

**Judge:** Dashboard and handover scope is unaffected by TBD pricing.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F037-R-A1

**Document Work · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Draft a proposal from these notes and leave pricing undecided

**Candidate:** Stage the pricing section

**Concrete work product:**

```text
Pricing: TBD. No numeric quote is included.
```

**Full instruction:** Draft a proposal from these notes and leave pricing undecided but quote the supplied fixed price of 500 credits and remove TBD pricing.

**Judge:** The only pricing content is TBD, which must be removed and replaced with 500 credits.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F037-R-A2

**Document Work · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Draft a proposal from these notes and leave pricing undecided

**Candidate:** Stage the scope section

**Concrete work product:**

```text
Scope: deliver one dashboard and its handover guide; no price or schedule included.
```

**Full instruction:** Draft a proposal from these notes and leave pricing undecided but quote the supplied fixed price of 500 credits and remove TBD pricing.

**Judge:** The dashboard scope survives the change to a fixed numeric price.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F038-K-A1

**Document Work · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Compare these two resumes without recommending a candidate

**Candidate:** Extract resume differences

**Concrete work product:**

```text
Resume A lists Python and 3 years of experience; Resume B lists Java and 5 years. These are fixture facts.
```

**Full instruction:** Compare these two resumes without recommending a candidate and list differences only.

**Judge:** The extracted skills and experience are the requested resume differences.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F038-K-A2

**Document Work · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Compare these two resumes without recommending a candidate

**Candidate:** Stage a comparison-only closing

**Concrete work product:**

```text
These differences are presented without any hiring recommendation.
```

**Full instruction:** Compare these two resumes without recommending a candidate and list differences only.

**Judge:** The closing preserves the comparison-only scope without recommending anyone.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F038-R-A1

**Document Work · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Compare these two resumes without recommending a candidate

**Candidate:** Extract resume differences

**Concrete work product:**

```text
Resume A lists Python and 3 years of experience; Resume B lists Java and 5 years. These are fixture facts.
```

**Full instruction:** Compare these two resumes without recommending a candidate but recommend a candidate using the same resumes and explain the choice.

**Judge:** The resume facts remain evidence for comparing and recommending a candidate.

**Author expectation / rater A / rater B:** non-reusable / reusable / reusable

## SX1-F038-R-A2

**Document Work · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Compare these two resumes without recommending a candidate

**Candidate:** Stage a comparison-only closing

**Concrete work product:**

```text
These differences are presented without any hiring recommendation.
```

**Full instruction:** Compare these two resumes without recommending a candidate but recommend a candidate using the same resumes and explain the choice.

**Judge:** The closing explicitly disclaims the recommendation now required.

**Author expectation / rater A / rater B:** reusable / non-reusable / non-reusable

## SX1-F039-K-A1

**Device/Home Control · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Stage the living-room lights at 30 percent brightness

**Candidate:** Stage the requested lighting command

**Concrete work product:**

```text
Unapplied command: room=living_room, brightness=30, color=unchanged.
```

**Full instruction:** Stage the living-room lights at 30 percent brightness while preserving their current color, without applying changes.

**Judge:** The unapplied command sets living-room brightness while preserving color.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F039-K-A2

**Device/Home Control · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Stage the living-room lights at 30 percent brightness

**Candidate:** Read living-room light state

**Concrete work product:**

```text
Living-room fixture: brightness 80%, color warm white. No bedroom state included.
```

**Full instruction:** Stage the living-room lights at 30 percent brightness while preserving their current color, without applying changes.

**Judge:** The living-room state provides the current color that the staged command must preserve.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F039-R-A1

**Device/Home Control · non-reusable · fraction 0.33 · confidence 5/5 · ambiguity Y

**Observed prefix:** Stage the living-room lights at 30 percent brightness

**Candidate:** Stage the requested lighting command

**Concrete work product:**

```text
Unapplied command: room=living_room, brightness=30, color=unchanged.
```

**Full instruction:** Stage the living-room lights at 30 percent brightness but stage bedroom lights at 60 percent instead and discard the living-room command.

**Judge:** Room and brightness require replacement; the generic unchanged-color argument is the only reusable command component.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F039-R-A2

**Device/Home Control · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Stage the living-room lights at 30 percent brightness

**Candidate:** Read living-room light state

**Concrete work product:**

```text
Living-room fixture: brightness 80%, color warm white. No bedroom state included.
```

**Full instruction:** Stage the living-room lights at 30 percent brightness but stage bedroom lights at 60 percent instead and discard the living-room command.

**Judge:** Living-room brightness and color provide no bedroom state for the replacement command.

**Author expectation / rater A / rater B:** reusable / non-reusable / non-reusable

## SX1-F040-K-A1

**Device/Home Control · unresolved · fraction None · confidence 2/5 · ambiguity Y

**Observed prefix:** Stage a 70 F thermostat setting for tonight

**Candidate:** Stage the 70 F setting

**Concrete work product:**

```text
Unapplied thermostat plan: tonight, target 70 F.
```

**Full instruction:** Stage a 70 F thermostat setting for tonight only if the current setting differs from 70 F; do not apply it.

**Judge:** The current thermostat setting is absent from this item, so the condition permitting any 70 F plan is unresolved and surviving utility cannot be quantified.

**Author expectation / rater A / rater B:** reusable / unresolved / unresolved

## SX1-F040-K-A2

**Device/Home Control · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Stage a 70 F thermostat setting for tonight

**Candidate:** Read current thermostat setting

**Concrete work product:**

```text
Current fixture thermostat setting: 70 F; reading retained for conditional comparison.
```

**Full instruction:** Stage a 70 F thermostat setting for tonight only if the current setting differs from 70 F; do not apply it.

**Judge:** The current 70 F reading resolves whether the conditional staging is needed.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F040-R-A1

**Device/Home Control · non-reusable · fraction None · confidence 5/5 · ambiguity Y

**Observed prefix:** Stage a 70 F thermostat setting for tonight

**Candidate:** Stage the 70 F setting

**Concrete work product:**

```text
Unapplied thermostat plan: tonight, target 70 F.
```

**Full instruction:** Stage a 70 F thermostat setting for tonight but stage 68 F instead, only if the current setting differs from 68 F; do not apply it.

**Judge:** The staged 70 F target is invalid under either branch of the new 68 F condition; missing current state prevents quantifying whether any plan content survives.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F040-R-A2

**Device/Home Control · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Stage a 70 F thermostat setting for tonight

**Candidate:** Read current thermostat setting

**Concrete work product:**

```text
Current fixture thermostat setting: 70 F; reading retained for conditional comparison.
```

**Full instruction:** Stage a 70 F thermostat setting for tonight but stage 68 F instead, only if the current setting differs from 68 F; do not apply it.

**Judge:** The current 70 F reading establishes that the revised 68 F condition is satisfied.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F041-K-A1

**Device/Home Control · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Prepare to lock the back door after I leave

**Candidate:** Read back-door sensor

**Concrete work product:**

```text
Back-door fixture sensor: closed and unlocked; timestamp belongs to the fixed scenario snapshot.
```

**Full instruction:** Prepare to lock the back door after I leave and check the back-door sensor before staging anything.

**Judge:** The back-door reading supplies the expressly requested sensor check.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F041-K-A2

**Device/Home Control · unresolved · fraction None · confidence 2/5 · ambiguity Y

**Observed prefix:** Prepare to lock the back door after I leave

**Candidate:** Stage a departure trigger definition

**Concrete work product:**

```text
Trigger: requester_departed becomes true; no door or lock operation attached.
```

**Full instruction:** Prepare to lock the back door after I leave and check the back-door sensor before staging anything.

**Judge:** The departure trigger content fits, but no prior sensor check is supplied; compliance with checking before staging anything and the resulting need to redo staging remain unresolved.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F041-R-A1

**Device/Home Control · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Prepare to lock the back door after I leave

**Candidate:** Read back-door sensor

**Concrete work product:**

```text
Back-door fixture sensor: closed and unlocked; timestamp belongs to the fixed scenario snapshot.
```

**Full instruction:** Prepare to lock the back door after I leave but prepare to lock the front door instead and do not use the back-door sensor reading.

**Judge:** The back-door sensor reading is explicitly forbidden and provides no front-door state.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F041-R-A2

**Device/Home Control · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Prepare to lock the back door after I leave

**Candidate:** Stage a departure trigger definition

**Concrete work product:**

```text
Trigger: requester_departed becomes true; no door or lock operation attached.
```

**Full instruction:** Prepare to lock the back door after I leave but prepare to lock the front door instead and do not use the back-door sensor reading.

**Judge:** The departure trigger has no back-door binding and still applies to locking the front door.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F042-K-A1

**Device/Home Control · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Stage a kitchen-only vacuum run

**Candidate:** Stage the room-specific cleaning plan

**Concrete work product:**

```text
Unapplied vacuum plan: include kitchen; exclude bedroom, hall and living room.
```

**Full instruction:** Stage a kitchen-only vacuum run and keep all other rooms excluded; do not start cleaning.

**Judge:** The unapplied plan includes only the kitchen and excludes every other named room.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F042-K-A2

**Device/Home Control · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Stage a kitchen-only vacuum run

**Candidate:** Read vacuum battery state

**Concrete work product:**

```text
Fixture vacuum battery: 90%; sufficient for either single-room run in this scenario.
```

**Full instruction:** Stage a kitchen-only vacuum run and keep all other rooms excluded; do not start cleaning.

**Judge:** The frozen battery reading supports staging the kitchen run without starting it.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F042-R-A1

**Device/Home Control · non-reusable · fraction 0.25 · confidence 5/5 · ambiguity Y

**Observed prefix:** Stage a kitchen-only vacuum run

**Candidate:** Stage the room-specific cleaning plan

**Concrete work product:**

```text
Unapplied vacuum plan: include kitchen; exclude bedroom, hall and living room.
```

**Full instruction:** Stage a kitchen-only vacuum run but stage a bedroom-only run instead and discard the kitchen plan.

**Judge:** The kitchen inclusion and bedroom exclusion must be replaced; exclusions of hall and living room provide only minor surviving plan content.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F042-R-A2

**Device/Home Control · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Stage a kitchen-only vacuum run

**Candidate:** Read vacuum battery state

**Concrete work product:**

```text
Fixture vacuum battery: 90%; sufficient for either single-room run in this scenario.
```

**Full instruction:** Stage a kitchen-only vacuum run but stage a bedroom-only run instead and discard the kitchen plan.

**Judge:** The battery reading explicitly remains sufficient for the replacement single-room run.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F043-K-A1

**Media · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find robotics documentaries

**Candidate:** Retrieve robotics documentary cards

**Concrete work product:**

```text
Robot Workshop: robotics, 60 minutes; Machine Motion: robotics, 75 minutes; neither covers astronomy.
```

**Full instruction:** Find robotics documentaries and include only titles under 90 minutes.

**Judge:** Both robotics titles satisfy the under-90-minute requirement.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F043-K-A2

**Media · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find robotics documentaries

**Candidate:** Prepare a runtime filter

**Concrete work product:**

```text
Keep input records whose runtime_minutes < 90; no topic filter or titles embedded.
```

**Full instruction:** Find robotics documentaries and include only titles under 90 minutes.

**Judge:** The runtime predicate implements the requested under-90-minute constraint.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F043-R-A1

**Media · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find robotics documentaries

**Candidate:** Retrieve robotics documentary cards

**Concrete work product:**

```text
Robot Workshop: robotics, 60 minutes; Machine Motion: robotics, 75 minutes; neither covers astronomy.
```

**Full instruction:** Find robotics documentaries but find astronomy documentaries only and exclude robotics titles.

**Judge:** Neither retrieved robotics film covers the required astronomy topic.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F043-R-A2

**Media · non-reusable · fraction 0 · confidence 4/5 · ambiguity Y

**Observed prefix:** Find robotics documentaries

**Candidate:** Prepare a runtime filter

**Concrete work product:**

```text
Keep input records whose runtime_minutes < 90; no topic filter or titles embedded.
```

**Full instruction:** Find robotics documentaries but find astronomy documentaries only and exclude robotics titles.

**Judge:** The runtime exclusion would add an unsupported astronomy constraint; no runtime ceiling is supplied in this item.

**Author expectation / rater A / rater B:** reusable / non-reusable / non-reusable

## SX1-F044-K-A1

**Media · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Build an upbeat instrumental jazz playlist

**Candidate:** Collect instrumental track cards

**Concrete work product:**

```text
Track A and Track B: upbeat jazz, instrumental; no vocals in either fixture track.
```

**Full instruction:** Build an upbeat instrumental jazz playlist and exclude vocal tracks.

**Judge:** Both instrumental jazz tracks satisfy the vocal exclusion.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F044-K-A2

**Media · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Build an upbeat instrumental jazz playlist

**Candidate:** Prepare a vocal-track exclusion predicate

**Concrete work product:**

```text
Keep a supplied track only when has_vocals is false; no titles embedded.
```

**Full instruction:** Build an upbeat instrumental jazz playlist and exclude vocal tracks.

**Judge:** The predicate enforces the final exclusion of vocal tracks.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F044-R-A1

**Media · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Build an upbeat instrumental jazz playlist

**Candidate:** Collect instrumental track cards

**Concrete work product:**

```text
Track A and Track B: upbeat jazz, instrumental; no vocals in either fixture track.
```

**Full instruction:** Build an upbeat instrumental jazz playlist but include only vocal jazz tracks and exclude instrumentals.

**Judge:** Both instrumental tracks fail the vocal-only requirement.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F044-R-A2

**Media · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Build an upbeat instrumental jazz playlist

**Candidate:** Prepare a vocal-track exclusion predicate

**Concrete work product:**

```text
Keep a supplied track only when has_vocals is false; no titles embedded.
```

**Full instruction:** Build an upbeat instrumental jazz playlist but include only vocal jazz tracks and exclude instrumentals.

**Judge:** The predicate excludes the very vocal tracks now required.

**Author expectation / rater A / rater B:** reusable / non-reusable / non-reusable

## SX1-F045-K-A1

**Media · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Choose a non-horror movie under two hours for tonight

**Candidate:** Retrieve movie cards

**Concrete work product:**

```text
Film A: comedy, 90 minutes; Film B: drama, 105 minutes; both explicitly not horror.
```

**Full instruction:** Choose a non-horror movie under two hours for tonight and compare the listed eligible options.

**Judge:** Both retrieved films satisfy the retained genre and runtime requirements.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F045-K-A2

**Media · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Choose a non-horror movie under two hours for tonight

**Candidate:** Stage a generic movie comparison layout

**Concrete work product:**

```text
Columns: title, genre, runtime, availability tonight; no candidate titles or restrictions filled in.
```

**Full instruction:** Choose a non-horror movie under two hours for tonight and compare the listed eligible options.

**Judge:** The movie layout supports comparing the retained title, genre and runtime criteria.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F045-R-A1

**Media · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Choose a non-horror movie under two hours for tonight

**Candidate:** Retrieve movie cards

**Concrete work product:**

```text
Film A: comedy, 90 minutes; Film B: drama, 105 minutes; both explicitly not horror.
```

**Full instruction:** Choose a non-horror movie under two hours for tonight but choose a horror movie longer than two hours instead.

**Judge:** Both short non-horror films fail the reversed genre and duration requirements.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F045-R-A2

**Media · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Choose a non-horror movie under two hours for tonight

**Candidate:** Stage a generic movie comparison layout

**Concrete work product:**

```text
Columns: title, genre, runtime, availability tonight; no candidate titles or restrictions filled in.
```

**Full instruction:** Choose a non-horror movie under two hours for tonight but choose a horror movie longer than two hours instead.

**Judge:** The empty genre and runtime columns accommodate the revised movie requirements.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F046-K-A1

**Media · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find technical podcast interviews about AI agents

**Candidate:** Retrieve interview episode cards

**Concrete work product:**

```text
Episode I and Episode J: technical AI-agent interviews; neither is a news roundup.
```

**Full instruction:** Find technical podcast interviews about AI agents and favor interviews over news roundups.

**Judge:** Both technical AI-agent interviews satisfy the preferred episode format.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F046-K-A2

**Media · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find technical podcast interviews about AI agents

**Candidate:** Prepare the topic query

**Concrete work product:**

```text
Topic query: AI agents; no episode-format restriction.
```

**Full instruction:** Find technical podcast interviews about AI agents and favor interviews over news roundups.

**Judge:** The unrestricted AI-agents topic query remains usable for retrieving interviews.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F046-R-A1

**Media · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find technical podcast interviews about AI agents

**Candidate:** Retrieve interview episode cards

**Concrete work product:**

```text
Episode I and Episode J: technical AI-agent interviews; neither is a news roundup.
```

**Full instruction:** Find technical podcast interviews about AI agents but use only news roundups and exclude interviews.

**Judge:** Both interview cards are explicitly excluded and neither is a news roundup.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F046-R-A2

**Media · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Find technical podcast interviews about AI agents

**Candidate:** Prepare the topic query

**Concrete work product:**

```text
Topic query: AI agents; no episode-format restriction.
```

**Full instruction:** Find technical podcast interviews about AI agents but use only news roundups and exclude interviews.

**Judge:** The AI-agents topic query can retrieve news roundups without removing an interview filter.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F047-K-A1

**General Productivity · reusable · fraction 1 · confidence 5/5 · ambiguity N

**Observed prefix:** Make a three-day business-trip packing checklist

**Candidate:** Draft the clothing checklist

**Concrete work product:**

```text
Two business shirts; one pair of office trousers; office shoes. No formalwear included.
```

**Full instruction:** Make a three-day business-trip packing checklist and omit formalwear.

**Judge:** The stipulated office clothing excludes formalwear and remains a business-trip checklist.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F047-K-A2

**General Productivity · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Make a three-day business-trip packing checklist

**Candidate:** Draft the shared essentials checklist

**Concrete work product:**

```text
Toothbrush; phone charger; personal identification. No destination-specific supplies included.
```

**Full instruction:** Make a three-day business-trip packing checklist and omit formalwear.

**Judge:** The shared essentials are appropriate for the business trip and contain no formalwear.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F047-R-A1

**General Productivity · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Make a three-day business-trip packing checklist

**Candidate:** Draft the clothing checklist

**Concrete work product:**

```text
Two business shirts; one pair of office trousers; office shoes. No formalwear included.
```

**Full instruction:** Make a three-day business-trip packing checklist but make it a three-day camping checklist instead, with no business clothing.

**Judge:** Every listed item is business clothing explicitly excluded from the camping checklist.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F047-R-A2

**General Productivity · reusable · fraction 1 · confidence 4/5 · ambiguity Y

**Observed prefix:** Make a three-day business-trip packing checklist

**Candidate:** Draft the shared essentials checklist

**Concrete work product:**

```text
Toothbrush; phone charger; personal identification. No destination-specific supplies included.
```

**Full instruction:** Make a three-day business-trip packing checklist but make it a three-day camping checklist instead, with no business clothing.

**Judge:** The toothbrush, charger and identification remain reusable camping checklist suggestions; their practical relevance is a contextual judgment.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F048-K-A1

**General Productivity · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Plan my morning around a 9 AM appointment

**Candidate:** Calculate the original departure time

**Concrete work product:**

```text
For a 09:00 arrival and 30 minutes travel, depart at 08:30.
```

**Full instruction:** Plan my morning around a 9 AM appointment and reserve 30 minutes to travel there.

**Judge:** The 08:30 departure implements the stated arrival time and travel duration.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F048-K-A2

**General Productivity · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Plan my morning around a 9 AM appointment

**Candidate:** Prepare the travel-duration field

**Concrete work product:**

```text
Travel duration field: 30 minutes; no appointment or departure time filled in.
```

**Full instruction:** Plan my morning around a 9 AM appointment and reserve 30 minutes to travel there.

**Judge:** The 30-minute field directly supplies the requested travel allowance.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F048-R-A1

**General Productivity · non-reusable · fraction 0.33 · confidence 5/5 · ambiguity N

**Observed prefix:** Plan my morning around a 9 AM appointment

**Candidate:** Calculate the original departure time

**Concrete work product:**

```text
For a 09:00 arrival and 30 minutes travel, depart at 08:30.
```

**Full instruction:** Plan my morning around a 9 AM appointment but move the appointment to 11 AM while retaining the 30-minute travel requirement.

**Judge:** Only the 30-minute travel value survives; the arrival and departure times require a new calculation.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F048-R-A2

**General Productivity · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Plan my morning around a 9 AM appointment

**Candidate:** Prepare the travel-duration field

**Concrete work product:**

```text
Travel duration field: 30 minutes; no appointment or departure time filled in.
```

**Full instruction:** Plan my morning around a 9 AM appointment but move the appointment to 11 AM while retaining the 30-minute travel requirement.

**Judge:** The unchanged 30-minute duration is retained explicitly for the later appointment.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F049-K-A1

**General Productivity · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Build a shopping list for vegetarian tacos

**Candidate:** Draft the protein ingredient

**Concrete work product:**

```text
One tin of beans; no meat.
```

**Full instruction:** Build a shopping list for vegetarian tacos and include beans instead of meat.

**Judge:** Beans supply the expressly requested vegetarian protein.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F049-K-A2

**General Productivity · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Build a shopping list for vegetarian tacos

**Candidate:** Draft the shared taco ingredients

**Concrete work product:**

```text
Tortillas, tomatoes and lettuce; no protein ingredient selected.
```

**Full instruction:** Build a shopping list for vegetarian tacos and include beans instead of meat.

**Judge:** The shared taco ingredients remain usable alongside beans.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F049-R-A1

**General Productivity · non-reusable · fraction 0.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Build a shopping list for vegetarian tacos

**Candidate:** Draft the protein ingredient

**Concrete work product:**

```text
One tin of beans; no meat.
```

**Full instruction:** Build a shopping list for vegetarian tacos but make beef tacos instead and omit beans.

**Judge:** Beans are expressly omitted and the retained protein section contains no beef.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F049-R-A2

**General Productivity · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Build a shopping list for vegetarian tacos

**Candidate:** Draft the shared taco ingredients

**Concrete work product:**

```text
Tortillas, tomatoes and lettuce; no protein ingredient selected.
```

**Full instruction:** Build a shopping list for vegetarian tacos but make beef tacos instead and omit beans.

**Judge:** Tortillas and vegetables remain taco ingredients when beef replaces beans.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F050-K-A1

**General Productivity · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Prioritize today's tasks with the client deadline first

**Candidate:** Stage the original ordering

**Concrete work product:**

```text
1. Client deadline; 2. Server incident; 3. File receipts.
```

**Full instruction:** Prioritize today's tasks with the client deadline first and keep the client deadline at the top.

**Judge:** The staged ordering keeps the client deadline first as requested.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F050-K-A2

**General Productivity · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Prioritize today's tasks with the client deadline first

**Candidate:** Extract today's task inventory

**Concrete work product:**

```text
Tasks due today: client deadline, server incident, file receipts; inventory has no priority ordering.
```

**Full instruction:** Prioritize today's tasks with the client deadline first and keep the client deadline at the top.

**Judge:** The unordered inventory supplies the tasks to prioritize with the deadline first.

**Author expectation / rater A / rater B:** reusable / reusable / reusable

## SX1-F050-R-A1

**General Productivity · non-reusable · fraction 0.5 · confidence 4/5 · ambiguity Y

**Observed prefix:** Prioritize today's tasks with the client deadline first

**Candidate:** Stage the original ordering

**Concrete work product:**

```text
1. Client deadline; 2. Server incident; 3. File receipts.
```

**Full instruction:** Prioritize today's tasks with the client deadline first but put the server incident first and move the client deadline below it.

**Judge:** Task identities survive, but the requested work product is an ordering and its leading priorities must be materially reversed.

**Author expectation / rater A / rater B:** non-reusable / non-reusable / non-reusable

## SX1-F050-R-A2

**General Productivity · reusable · fraction 1.0 · confidence 5/5 · ambiguity N

**Observed prefix:** Prioritize today's tasks with the client deadline first

**Candidate:** Extract today's task inventory

**Concrete work product:**

```text
Tasks due today: client deadline, server incident, file receipts; inventory has no priority ordering.
```

**Full instruction:** Prioritize today's tasks with the client deadline first but put the server incident first and move the client deadline below it.

**Judge:** The unordered task inventory survives the changed priority rule.

**Author expectation / rater A / rater B:** reusable / reusable / reusable
