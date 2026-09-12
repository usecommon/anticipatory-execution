# AI judge review of 220 frozen cases

Keep away from independent human annotators. One AI rating per case; main and boundary cases separated below.

# Main review cases

## CP1-SP1-S-SX1-F004-K-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Compare nonstop flights to Eastport and

**Action:** Prepare nonstop-flight comparison algorithm

```text
Given candidate flight records, retain destination Eastport and stops==0; normalize fare components into one currency and keep baggage fees separately when unknown. Group equivalent departure dates, origins, and passenger counts; compare total known cost, departure/arrival times, and elapsed duration. Mark missing costs unknown rather than zero.
```

**Full instruction:** Compare nonstop flights to Eastport and list only nonstop itineraries.

**Sufficiency:** substantive — Prepare nonstop-flight comparison algorithm: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The nonstop Eastport filter and fare comparison remain applicable.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_12-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** Pop on over to the 'Documents' directory and craft a new file dubbed 'summary.txt', would you? If it

**Action:** Draft non-overwriting file creation command

```text
if [ -d Documents ]; then
  (set -C; : > Documents/summary.txt)
else
  printf '%s\n' 'Documents directory not found' >&2
fi
# Noclobber protects any existing summary.txt; draft only.
```

**Full instruction:** Pop on over to the 'Documents' directory and craft a new file dubbed 'summary.txt', would you? If it already exists, return an error

**Sufficiency:** substantive — Draft non-overwriting file creation command: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

Noclobber creation already errors on an existing summary.txt.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F008-R-W12

**Source:** synthetic · **Words:** 12 · **Disposition:** reusable

**Prefix:** Find pharmacies in Brookfield that are open now but only list hospital

**Action:** Draft hospital-pharmacy discovery query

```text
"Brookfield" "hospital pharmacy" (hours OR "open now") -jobs -careers
```

**Full instruction:** Find pharmacies in Brookfield that are open now but only list hospital pharmacies that are closed now and open tomorrow.

**Sufficiency:** substantive — Draft hospital-pharmacy discovery query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** Y

Hospital-pharmacy hours discovery survives; current-versus-tomorrow filtering remains to be added despite contradictory wording.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_0-W6

**Source:** public_bfcl · **Words:** 6 · **Disposition:** reusable

**Prefix:** Move 'final_report.pdf' within document directory to

**Action:** Draft a guarded move plan for final_report.pdf.

```text
Unexecuted algorithm: resolve document-directory/final_report.pdf as the source; require a regular file; resolve the eventual destination; reject a destination equal to the source or an already-existing target; record source and destination in an unsent move plan. If later authorized, use an exclusive no-overwrite move and verify source absence plus destination presence. Destination is absent, so no move is attempted.
```

**Full instruction:** Move 'final_report.pdf' within document directory to 'temp' directory in document. Make sure to create the directory

**Sufficiency:** substantive — Draft a guarded move plan for final_report.pdf: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

Source checks and exclusive move staging survive destination binding and adding directory creation.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F010-K-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** non_reusable

**Prefix:** Compare 15-litre shoulder bags and rank

**Action:** Prepare 15-litre bag ranking method

```text
Filter candidates to shoulder-carry bags with documented 15 L capacity. For candidates with known comparable attributes, define dominance as no higher price or empty weight and no smaller opening width, with one strict advantage. Return Pareto layers; flag incomparable or missing-attribute candidates rather than inventing weighted rankings.
```

**Full instruction:** Compare 15-litre shoulder bags and rank the two listed bags by lower weight.

**Sufficiency:** substantive — Prepare 15-litre bag ranking method: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

Pareto ranking across price, opening and weight must become a weight-only ordering; capacity filtering survives.

Substantive preparation requires material replacement or has no established role in the final task.

## CP1-SP1-P-multi_turn_base_59-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** I recently moved to San Francisco and I’m planning a trip to Rivermist. How far apart are these

**Action:** Draft a route-distance search

```text
"San Francisco" "Rivermist" ("road distance" OR "driving distance" OR "straight line distance")
```

**Full instruction:** I recently moved to San Francisco and I’m planning a trip to Rivermist. How far apart are these places? I'd like to gauge the distance before setting off on this adventure.

**Sufficiency:** substantive — Draft a route-distance search: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

The named route-distance search directly supports the distance request.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_3-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** As part of my latest photography project, I need to gather files that have 'test' in their name

**Action:** Draft a filename collection command

```text
find . -type f -iname '*test*' -print
```

**Full instruction:** As part of my latest photography project, I need to gather files that have 'test' in their name from any folder in my current directory. Could you help me locate those?

**Sufficiency:** substantive — Draft a filename collection command: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

Recursive filename matching remains the requested discovery step.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F020-R-W12

**Source:** synthetic · **Words:** 12 · **Disposition:** reusable

**Prefix:** Draft a message declining dinner tonight but accept dinner tonight instead and

**Action:** Draft a dinner acceptance

```text
I'd be happy to join you for dinner tonight. Looking forward to seeing you!
```

**Full instruction:** Draft a message declining dinner tonight but accept dinner tonight instead and do not suggest another date.

**Sufficiency:** substantive — Draft a dinner acceptance: concrete draft content establishes preparation beyond copied inputs.

**Ambiguity:** N

The acceptance text already avoids suggesting another date.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_33-W12

**Source:** public_bfcl · **Words:** 12 · **Disposition:** unresolved_reuse

**Prefix:** What's the name of the python file my current directory? There should

**Action:** Draft Python-file discovery command

```text
find . -maxdepth 1 -type f -name '*.py' -print
# Report every match; if multiple match, do not choose an arbitrary file.
```

**Full instruction:** What's the name of the python file my current directory? There should be only one and. Do not list hidden files. 

**Sufficiency:** substantive — Draft Python-file discovery command: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

The command includes hidden Python files; whether any would require correction is unknown.

Substantive preparation; reuse remains unresolved.

## CP1-SP1-S-SX1-F005-K-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Find Italian restaurants around Cedar Square

**Action:** Prepare restaurant discovery query

```text
"Cedar Square" ("Italian restaurant" OR trattoria OR osteria) -jobs -careers
```

**Full instruction:** Find Italian restaurants around Cedar Square and choose places with outdoor seating.

**Sufficiency:** substantive — Prepare restaurant discovery query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

Italian restaurant discovery can be narrowed to outdoor seating.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_128-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** Could you ascertain the current time? It seems vital for aligning my stock market ventures seamlessly. Additionally, could

**Action:** Draft a timestamp command for market-time checks

```text
python3 -c 'from datetime import datetime, timezone; print(datetime.now(timezone.utc).isoformat()); print(datetime.now().astimezone().isoformat())'
```

**Full instruction:** Could you ascertain the current time? It seems vital for aligning my stock market ventures seamlessly. Additionally, could you do me the favor of identifying which stocks in the Technology sector are currently offered?

**Sufficiency:** substantive — Draft a timestamp command for market-time checks: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The timezone-aware timestamp command survives the additional sector-stock request.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F018-K-W12

**Source:** synthetic · **Words:** 12 · **Disposition:** reusable

**Prefix:** Draft a reply thanking Morgan for the introduction and offer to provide

**Action:** Draft unsent introduction reply

```text
Hi Morgan, thank you for making the introduction. I appreciate you connecting us and look forward to learning more about their work. I’m happy to share some background on my work to help get the conversation started. Best,
```

**Full instruction:** Draft a reply thanking Morgan for the introduction and offer to provide more information.

**Sufficiency:** substantive — Draft unsent introduction reply: concrete draft content establishes preparation beyond copied inputs.

**Ambiguity:** N

The thanks and offer to share background satisfy the requested reply.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_32-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** I would like to peek the content of 'Spring2023Draft' for review, and could you also provide a comprehensive

**Action:** Draft a read-only document preview

```text
from pathlib import Path
p = Path('Spring2023Draft')
if not p.is_file(): raise FileNotFoundError(p)
print(p.read_text())
```

**Full instruction:** I would like to peek the content of 'Spring2023Draft' for review, and could you also provide a comprehensive character count of that same file for thorough assessment?

**Sufficiency:** substantive — Draft a read-only document preview: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

Reading the named document remains useful before counting its characters.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_175-W12

**Source:** public_bfcl · **Words:** 12 · **Disposition:** reusable

**Prefix:** How much would a flight from SF to LA even cost? It's

**Action:** Draft airfare search

```text
("SFO" OR "San Francisco") ("LAX" OR "Los Angeles") (airfare OR "flight price") -hotel -cruise
Treat airport codes as candidate city-airport mappings to confirm before pricing.
```

**Full instruction:** How much would a flight from SF to LA even cost? It's probably cheap. That's it, let me just do it. I need to arrange a business class flight for Robert Trenton from San Francisco to Los Angeles on November 25th 2026. The reservation should be made using his travel card with id card_3487 and access code 1293. Following the booking, I have to ensure an invoice is issued to verify the charges.

**Sufficiency:** substantive — Draft airfare search: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

The route search remains reusable after adding cabin and date constraints.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F007-K-W12

**Source:** synthetic · **Words:** 12 · **Disposition:** reusable

**Prefix:** Find gyms in Riverton that sell day passes and prioritize day-pass gyms

**Action:** Draft a day-pass gym search

```text
"Riverton" (gym OR "fitness center") ("day pass" OR "single visit") (price OR access)
```

**Full instruction:** Find gyms in Riverton that sell day passes and prioritize day-pass gyms with a sauna.

**Sufficiency:** substantive — Draft a day-pass gym search: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

Day-pass gym discovery supports later sauna prioritization.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_61-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** Could you map out the precise mileage from San Francisco to Rivermist for me, along with an assessment

**Action:** Draft a driving-mileage query

```text
"San Francisco" "Rivermist" ("driving distance" OR "road distance") (miles OR mileage)
```

**Full instruction:** Could you map out the precise mileage from San Francisco to Rivermist for me, along with an assessment of whether my current fuel should suffice the journey?

**Sufficiency:** substantive — Draft a driving-mileage query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

Driving mileage remains necessary for the later fuel assessment.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F013-K-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Find freestanding desk converters under 250

**Action:** Prepare desk-converter discovery query

```text
("desk converter" OR "desktop riser") (freestanding OR "free standing") -"wall mounted" -"desk frame"
```

**Full instruction:** Find freestanding desk converters under 250 credits and exclude permanently mounted converters.

**Sufficiency:** substantive — Prepare desk-converter discovery query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

The query already seeks freestanding converters and can be price-filtered.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_44-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** non_reusable

**Prefix:** Could you populate 'annual_report.txt' with data on quarterly revenue: 'Q1: $5000, Q2: $7000, Q3: $6000, Q4: $8000'? I

**Action:** Draft annual revenue report

```text
Quarterly Revenue
Q1: $5,000
Q2: $7,000
Q3: $6,000
Q4: $8,000
Annual total: $26,000
Quarterly average: $6,500
Highest quarter: Q4 ($8,000)
Lowest quarter: Q1 ($5,000)
Q4 versus Q1: +$3,000 (+60%).
```

**Full instruction:** Could you populate 'annual_report.txt' with data on quarterly revenue: 'Q1: $5000, Q2: $7000, Q3: $6000, Q4: $8000'? I only want to store the quoted text in my file. The file is somehwhere inside the file system.

**Sufficiency:** substantive — Draft annual revenue report: concrete draft content establishes preparation beyond copied inputs.

**Ambiguity:** N

Added analysis and reformatted amounts conflict with storing only the exact quoted text.

Substantive preparation requires material replacement or has no established role in the final task.

## CP1-SP1-P-multi_turn_base_18-W12

**Source:** public_bfcl · **Words:** 12 · **Disposition:** reusable

**Prefix:** Copy all the text files of the 'Quarter1_Reports' directory and place it

**Action:** Draft text-copy collision plan

```text
Enumerate immediate regular *.txt files in Quarter1_Reports, including names beginning with a dot. Map each basename into a destination directory once specified. Abort if any target exists; otherwise copy and compare source/target bytes before declaring success. Preserve the source files.
```

**Full instruction:** Copy all the text files of the 'Quarter1_Reports' directory and place it in a new directory naming it 'Archived_Quarter1.

**Sufficiency:** substantive — Draft text-copy collision plan: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The collision-aware text-copy plan survives binding the archive destination.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F011-R-W12

**Source:** synthetic · **Words:** 12 · **Disposition:** reusable

**Prefix:** Find brown faux-suede jackets with stand collars but use black cotton jackets

**Action:** Draft revised jacket search

```text
"black" "cotton" jacket -brown -"faux suede"
```

**Full instruction:** Find brown faux-suede jackets with stand collars but use black cotton jackets with lapels instead and discard the original options.

**Sufficiency:** substantive — Draft revised jacket search: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

The corrected black-cotton search can be narrowed to lapels.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F027-K-W12

**Source:** synthetic · **Words:** 12 · **Disposition:** reusable

**Prefix:** Calculate a 7 percent downside scenario for a 100-credit index and show

**Action:** Compute downside scenario

```text
100-credit base × (1 − 0.07) = 93 credits; hypothetical decline = 7 credits.
```

**Full instruction:** Calculate a 7 percent downside scenario for a 100-credit index and show the hypothetical level without making a trade.

**Sufficiency:** substantive — Compute downside scenario: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The 93-credit hypothetical result is exactly the requested scenario.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F044-R-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** non_reusable

**Prefix:** Build an upbeat instrumental jazz playlist

**Action:** Draft upbeat instrumental jazz playlist

```text
Candidate sequence: Art Blakey & The Jazz Messengers — Moanin’; Dave Brubeck Quartet — Take Five; Duke Ellington — C Jam Blues; Sonny Rollins — St. Thomas; Cannonball Adderley — Work Song. Select instrumental recordings of these tunes and audition tempo/energy before finalizing.
```

**Full instruction:** Build an upbeat instrumental jazz playlist but include only vocal jazz tracks and exclude instrumentals.

**Sufficiency:** substantive — Draft upbeat instrumental jazz playlist: concrete draft content establishes preparation beyond copied inputs.

**Ambiguity:** N

An instrumental recording playlist must be replaced with vocal tracks.

Substantive preparation requires material replacement or has no established role in the final task.

## CP1-SP1-S-SX1-F024-R-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Compare Acme's revenue in its two

**Action:** Prepare a two-observation revenue comparison algorithm.

```text
Given two supplied revenue observations R1 and R2, first require matching currency, scale, accounting scope, and comparable period lengths. Normalize numeric scale, compute absolute change Δ = R2 − R1, and compute percentage change 100 × Δ/R1 only when R1 ≠ 0; otherwise report the percentage as undefined. Label observations with their supplied periods and avoid calling the result growth until chronological order is confirmed. No Acme figures are assumed.
```

**Full instruction:** Compare Acme's revenue in its two annual releases but compare Beacon's releases instead, with no Acme figures.

**Sufficiency:** substantive — Prepare a two-observation revenue comparison algorithm: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

The company-independent two-value comparison accepts Beacon observations without rewriting its arithmetic.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F040-K-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Stage a 70 F thermostat setting

**Action:** Prepare a thermostat temperature conversion and unsent staging rule.

```text
Requested temperature: 70 °F. Equivalent Celsius: (70 − 32) × 5/9 = 190/9 °C ≈ 21.111 °C. Unexecuted staging logic: read the target device’s native unit and allowed setpoint increment; represent this temperature in that unit; report any rounding difference; retain as an unsent draft. Device identity and operating mode must come from the completed request.
```

**Full instruction:** Stage a 70 F thermostat setting for tonight only if the current setting differs from 70 F; do not apply it.

**Sufficiency:** substantive — Prepare a thermostat temperature conversion and unsent staging rule: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The temperature conversion and unsent staging logic survive adding the current-setting condition.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_31-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** Hey there, I need to set up a directory titled 'Reports' in my current workspace. Once that's in

**Action:** Draft safe directory creation command

```text
if [ -e Reports ] && [ ! -d Reports ]; then
  printf '%s\n' 'Reports exists and is not a directory' >&2
else
  mkdir -p -- Reports
fi
```

**Full instruction:** Hey there, I need to set up a directory titled 'Reports' in my current workspace. Once that's in place, could you help me locate a file called 'summary.doc' in this vicinity and transfer it to the new 'Reports' folder? After that, I'd appreciate if you could find and open up 'data.txt', then scan through it to identify lines that mention 'Q4 financials'. Also, could you let me know the total number of lines in 'data.txt'?

**Sufficiency:** substantive — Draft safe directory creation command: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

Guarded Reports creation remains a required first step.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F019-K-W18

**Source:** synthetic · **Words:** 18 · **Disposition:** reusable

**Prefix:** Draft a team update saying the build is delayed and keep the cause neutral because it is not

**Action:** Draft a neutral build-delay update

```text
Team, the build is delayed. The cause has not been established in the information available for this update. No revised completion date is confirmed here.
```

**Full instruction:** Draft a team update saying the build is delayed and keep the cause neutral because it is not yet known.

**Sufficiency:** substantive — Draft a neutral build-delay update: concrete draft content establishes preparation beyond copied inputs.

**Ambiguity:** N

The delay update leaves its cause unasserted as requested.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_5-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** Find analysis_report.csv and upon locating it, ensure you move it to the 'archive' directory in the same directory

**Action:** Draft guarded archive-move algorithm

```text
Recursively locate exact filename analysis_report.csv. Require exactly one source; otherwise report ambiguity. Set destination to source.parent/archive/analysis_report.csv. Reject if target exists or source is already inside an archive directory. Plan directory creation and a non-overwriting move; retain the original path as a rollback record. No changes applied.
```

**Full instruction:** Find analysis_report.csv and upon locating it, ensure you move it to the 'archive' directory in the same directory of analysis report for safekeeping.

**Sufficiency:** substantive — Draft guarded archive-move algorithm: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The source-relative archive destination and guarded move match the full request.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_113-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** It would mean a lot if you could include Quasar Ltd.'s stock in my watchlist. After that's completed,

**Action:** Draft company identity discovery query

```text
"Quasar Ltd" ("investor relations" OR ticker OR exchange) -quasarframework -astronomy
```

**Full instruction:** It would mean a lot if you could include Quasar Ltd.'s stock in my watchlist. After that's completed, please let me know what's on the list so I can have a look.

**Sufficiency:** substantive — Draft company identity discovery query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

Issuer identity discovery supports adding the correct Quasar instrument.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_87-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** As I gear up for another delightful journey exploring the captivating waterways, I'm looking to convert 60 gallons

**Action:** Calculate both gallon conventions

```text
60 US liquid gallons × 3.785411784 = 227.12470704 liters.
60 imperial gallons × 4.54609 = 272.7654 liters.
Select the convention before using the result.
```

**Full instruction:** As I gear up for another delightful journey exploring the captivating waterways, I'm looking to convert 60 gallons of fuel into liters. Could you assist me with that conversion? I tend to work more comfortably with liters.

**Sufficiency:** substantive — Calculate both gallon conventions: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

Both gallon-convention calculations survive; the intended convention remains unspecified.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_19-W6

**Source:** public_bfcl · **Words:** 6 · **Disposition:** reusable

**Prefix:** Find every file with the name

**Action:** Draft exact-name file search skeleton

```text
find "$SEARCH_ROOT" -type f -name "$EXACT_FILENAME" -print
```

**Full instruction:** Find every file with the name 'test_document.txt' nestled within the current directory.

**Sufficiency:** substantive — Draft exact-name file search skeleton: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The parameterized exact-name find command needs only supplied argument binding.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F021-R-W18

**Source:** synthetic · **Words:** 18 · **Disposition:** reusable

**Prefix:** Draft a refund approval message but the refund is denied, so explain the denial and do not promise

**Action:** Draft a denial without promising a refund

```text
Your refund request has been denied. The information provided here does not specify the reason, so I cannot give a reliable explanation of the decision. Please refer to the decision notice for the applicable grounds.
```

**Full instruction:** Draft a refund approval message but the refund is denied, so explain the denial and do not promise payment.

**Sufficiency:** substantive — Draft a denial without promising a refund: concrete draft content establishes preparation beyond copied inputs.

**Ambiguity:** Y

Denial wording survives, but the missing denial grounds prevent a factual explanation.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F005-R-W12

**Source:** synthetic · **Words:** 12 · **Disposition:** reusable

**Prefix:** Find Italian restaurants around Cedar Square but change the cuisine to Thai

**Action:** Draft the corrected cuisine search

```text
"Cedar Square" ("Thai restaurant" OR "Thai food") (menu OR location) -"Italian restaurant"
```

**Full instruction:** Find Italian restaurants around Cedar Square but change the cuisine to Thai and exclude Italian restaurants.

**Sufficiency:** substantive — Draft the corrected cuisine search: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

The corrected Thai query excludes the superseded cuisine.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F031-K-W12

**Source:** synthetic · **Words:** 12 · **Disposition:** reusable

**Prefix:** Write a Python function that counts ERROR lines in the supplied log

**Action:** Draft ERROR-line counting function

```text
def count_error_lines(log_text: str) -> int:
    import re
    error = re.compile(r"\bERROR\b")
    return sum(bool(error.search(line)) for line in log_text.splitlines())
# Counts each line once, case-sensitively, when ERROR occurs as a word.
```

**Full instruction:** Write a Python function that counts ERROR lines in the supplied log and return the count without changing the file.

**Sufficiency:** substantive — Draft ERROR-line counting function: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The function counts ERROR lines without writing to the log.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_85-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** I’m planning a trip from Rivermist to San Francisco, and I need to see if my current fuel

**Action:** Draft fuel sufficiency calculation

```text
Given road distance d, current fuel f and economy e in distance per fuel unit: usable range = f*e; trip fuel = d/e; shortfall = max(0,d/e-f). Require e>0, d>=0, f>=0 and consistent units; mark sufficiency unknown until route distance and readings are supplied.
```

**Full instruction:** I’m planning a trip from Rivermist to San Francisco, and I need to see if my current fuel situation will get me there. Could you work out the distance?

**Sufficiency:** substantive — Draft fuel sufficiency calculation: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

The fuel-sufficiency formulas serve the stated trip concern once distance and readings arrive.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F032-K-W12

**Source:** synthetic · **Words:** 12 · **Disposition:** reusable

**Prefix:** Inspect the client timeout path without changing the code and identify where

**Action:** Draft read-only timeout-path search

```text
rg -n --glob '*.{py,js,ts,go,rs,java}' 'timeout|deadline|ETIMEDOUT|TimeoutError' .
# Follow matches from client request creation through exception handling; distinguish connect, read and total deadlines before attributing the timeout.
```

**Full instruction:** Inspect the client timeout path without changing the code and identify where its five-second timeout is set.

**Sufficiency:** substantive — Draft read-only timeout-path search: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

Read-only timeout discovery remains useful for locating the five-second setting.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_9-W12

**Source:** public_bfcl · **Words:** 12 · **Disposition:** reusable

**Prefix:** I remember I should have a document called 'FinalReport.txt' in the 'Documentation'

**Action:** Draft document-location command

```text
find Documentation -type f -name 'FinalReport.txt' -print
# Report all exact-name matches; do not silently pick one.
```

**Full instruction:** I remember I should have a document called 'FinalReport.txt' in the 'Documentation' folder. 

**Sufficiency:** substantive — Draft document-location command: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The exact filename search uses the requested Documentation directory.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F023-K-W12

**Source:** synthetic · **Words:** 12 · **Disposition:** reusable

**Prefix:** Find version 3 documentation for Library L and use only the official

**Action:** Draft official version-documentation query

```text
"Library L" ("version 3" OR "v3") (documentation OR reference) -tutorial -stackoverflow
Accept a later result only if hosted by the library publisher and explicitly scoped to version 3.
```

**Full instruction:** Find version 3 documentation for Library L and use only the official version 3 material.

**Sufficiency:** substantive — Draft official version-documentation query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

The official-source and version-three checks remain required.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_116-W6

**Source:** public_bfcl · **Words:** 6 · **Disposition:** reusable

**Prefix:** Could you peruse my stock watchlist

**Action:** Prepare stock-watchlist descriptive analysis

```text
Deduplicate entries by exchange plus ticker, retaining display names. For supplied observations with positive reference price p0, compute change_pct=100*(p1-p0)/p0. Mark stale timestamps and missing reference prices; sort observations by timestamp then ticker, without adding securities or trade advice.
```

**Full instruction:** Could you peruse my stock watchlist and share what's on my radar right now, please?

**Sufficiency:** substantive — Prepare stock-watchlist descriptive analysis: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

Watchlist identity deduplication survives, while performance calculations exceed a contents listing.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_138-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** I just tracked down an intriguing company named Synex Solutions, and I'm eager to delve into its financial

**Action:** Draft issuer financial-source query

```text
"Synex Solutions" ("annual report" OR "financial statements" OR "investor relations") -jobs -careers
```

**Full instruction:** I just tracked down an intriguing company named Synex Solutions, and I'm eager to delve into its financial performance. Would you mind providing a comprehensive analysis of its latest stock status?

**Sufficiency:** substantive — Draft issuer financial-source query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

Issuer financial-source discovery remains a useful part of stock-status analysis.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F038-R-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Compare these two resumes without recommending

**Action:** Draft evidence-based resume comparison algorithm

```text
Extract each resume’s explicitly stated roles, dates, skills, education, and accomplishments. Pair claims by category, preserve source excerpts, and mark unstated items as not provided. Calculate durations only for unambiguous dates; present differences without scoring, selecting a candidate, or inferring protected traits.
```

**Full instruction:** Compare these two resumes without recommending a candidate but recommend a candidate using the same resumes and explain the choice.

**Sufficiency:** substantive — Draft evidence-based resume comparison algorithm: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

Evidence extraction and comparison survive adding a recommendation; the no-selection presentation rule changes.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F034-R-W12

**Source:** synthetic · **Words:** 12 · **Disposition:** reusable

**Prefix:** Add malformed-JSON tests to the parser but benchmark parsing speed only and

**Action:** Draft parser benchmark skeleton

```text
def benchmark(parse, documents, repeats=5):
    from time import perf_counter
    if not documents: raise ValueError("nonempty corpus required")
    samples=[]
    for _ in range(repeats):
        start=perf_counter()
        for text in documents: parse(text)
        samples.append((perf_counter()-start)/len(documents))
    return {"seconds_per_document": samples}
# Use a fixed valid-JSON corpus; preparation is outside the timed loop.
```

**Full instruction:** Add malformed-JSON tests to the parser but benchmark parsing speed only and do not add correctness tests.

**Sufficiency:** substantive — Draft parser benchmark skeleton: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The valid-corpus timing function supports benchmarking without correctness tests.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F003-R-W18

**Source:** synthetic · **Words:** 18 · **Disposition:** reusable

**Prefix:** Compare Friday car rentals at North Terminal but pickup must be at South Terminal instead, with no North

**Action:** Draft revised rental query

```text
"South Terminal" "Friday" ("car rental" OR "rental car") -"North Terminal"
```

**Full instruction:** Compare Friday car rentals at North Terminal but pickup must be at South Terminal instead, with no North Terminal results.

**Sufficiency:** substantive — Draft revised rental query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

The query uses South Terminal and excludes North Terminal.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_13-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** In documents directory, there's a file that piques my curiosity regarding its contents. It's alphabetically first file in

**Action:** Draft alphabetical-first file read algorithm

```text
Enumerate immediate regular files in documents, including hidden files. Sort basenames by Unicode code-point order, explicitly reporting that ordering convention. If none exist, return an empty-directory result; otherwise read only the first file as text, reporting decode errors instead of substituting another file.
```

**Full instruction:** In documents directory, there's a file that piques my curiosity regarding its contents. It's alphabetically first file in that directory. Could you display the last line of that file for me?

**Sufficiency:** substantive — Draft alphabetical-first file read algorithm: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

Selecting and reading the first file survives extracting its final line; alphabetical convention is explicit.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_112-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** Wonderful, in light of the prevailing market landscape, could we dive into the Technology sector for a bit?

**Action:** Draft a technology-sector research query

```text
"technology sector" ("sector index" OR "sector performance") (methodology OR constituents)
```

**Full instruction:** Wonderful, in light of the prevailing market landscape, could we dive into the Technology sector for a bit? Compiling a list of stock symbols would be incredibly useful.

**Sufficiency:** substantive — Draft a technology-sector research query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

Sector constituent discovery can supply symbols for the requested technology list.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_102-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** Having assessed the market status, I've resolved to initiate a purchase of 100 shares of Tesla at $700

**Action:** Calculate proposed Tesla order notional

```text
100 shares × $700 per share = $70,000 gross notional. This excludes fees and does not establish execution price, buying power or an executed order.
```

**Full instruction:** Having assessed the market status, I've resolved to initiate a purchase of 100 shares of Tesla at $700 per share. Kindly proceed with executing this transaction on my behalf.

**Sufficiency:** substantive — Calculate proposed Tesla order notional: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The 70000-dollar notional remains valid preparation for the specified order.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_2-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** Go into document folder and Could you draft up a create a document titled 'TeamNotes.txt' for keeping track

**Action:** Draft useful team-notes conventions

```text
# Team Notes

Record decisions with the reason they were chosen and the person responsible for follow-through. Separate agreed decisions from ideas still under discussion. For each action, write a concrete deliverable and due date; carry unresolved actions into the next meeting. When a decision changes, append the new decision and reference the earlier entry so the history remains readable.
```

**Full instruction:** Go into document folder and Could you draft up a create a document titled 'TeamNotes.txt' for keeping track of all the fresh ideas?

**Sufficiency:** substantive — Draft useful team-notes conventions: concrete draft content establishes preparation beyond copied inputs.

**Ambiguity:** Y

Concrete note-taking conventions can seed the ideas document, though much concerns decisions and actions.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F015-K-W18

**Source:** synthetic · **Words:** 18 · **Disposition:** reusable

**Prefix:** Check whether my dentist can see me on Friday and keep my existing appointment if Friday has no

**Action:** Draft a conditional dentist-appointment plan

```text
def friday_plan(friday_slots, existing_appointment):
    if not friday_slots: return {"retain": existing_appointment, "proposed_change": None}
    return {"retain": existing_appointment, "candidate_slots": friday_slots, "status": "review_before_change"}
```

**Full instruction:** Check whether my dentist can see me on Friday and keep my existing appointment if Friday has no openings.

**Sufficiency:** substantive — Draft a conditional dentist-appointment plan: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The conditional plan retains the appointment when Friday has no slots.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F006-R-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** non_reusable

**Prefix:** Find bakeries around Birch Park but

**Action:** Prepare bakery discovery query

```text
"Birch Park" (bakery OR bakeries OR patisserie) -jobs -careers
```

**Full instruction:** Find bakeries around Birch Park but I meant pharmacies around Birch Park, not bakeries.

**Sufficiency:** substantive — Prepare bakery discovery query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

Bakery discovery is superseded by pharmacy discovery.

Substantive preparation requires material replacement or has no established role in the final task.

## CP1-SP1-S-SX1-F043-K-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Find robotics documentaries and include only

**Action:** Prepare robotics documentary query

```text
(robotics OR "robot engineering") (documentary OR "documentary film") -fiction -trailer
```

**Full instruction:** Find robotics documentaries and include only titles under 90 minutes.

**Sufficiency:** substantive — Prepare robotics documentary query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

Robotics documentary discovery can be filtered by runtime.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F029-R-W18

**Source:** synthetic · **Words:** 18 · **Disposition:** reusable

**Prefix:** Compare current holdings with the start-of-month snapshot but compare current holdings with the start-of-year snapshot instead and ignore

**Action:** Draft revised portfolio comparison

```text
Use start-of-year as baseline. Align instruments by stable ID; mark missing prices instead of treating them as zero. For each complete snapshot calculate weights from market values; report value change and 100*(current_weight-start_year_weight) percentage points. Added/removed instruments have zero weight only when their absence is confirmed.
```

**Full instruction:** Compare current holdings with the start-of-month snapshot but compare current holdings with the start-of-year snapshot instead and ignore start-of-month holdings.

**Sufficiency:** substantive — Draft revised portfolio comparison: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The comparison already uses the corrected start-of-year baseline.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F016-R-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Find team meeting slots this week

**Action:** Draft free-slot intersection algorithm

```text
Within this week in the team timezone, intersect participant working-hour intervals. Subtract the union of all busy intervals, merging overlaps first. Return each remaining interval with its duration; do not assume meeting duration, attendees, or calendar availability.
```

**Full instruction:** Find team meeting slots this week after 10 AM but only consider slots before 10 AM this week.

**Sufficiency:** substantive — Draft free-slot intersection algorithm: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

The free-interval algorithm has no after-10 restriction and supports filtering to before 10.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F001-R-W12

**Source:** synthetic · **Words:** 12 · **Disposition:** reusable

**Prefix:** Compare flights from Harborview to Eastport but change the destination to Westhaven

**Action:** Draft revised flight query

```text
"Harborview" "Westhaven" (flight OR airfare) -"Eastport"
```

**Full instruction:** Compare flights from Harborview to Eastport but change the destination to Westhaven and discard the Eastport options.

**Sufficiency:** substantive — Draft revised flight query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

The flight query targets Westhaven and excludes Eastport.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F038-K-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Compare these two resumes without recommending

**Action:** Draft evidence-based resume comparison algorithm

```text
Extract each resume’s explicitly stated roles, dates, skills, education, and accomplishments. Pair claims by category, preserve source excerpts, and mark unstated items as not provided. Calculate durations only for unambiguous dates; present differences without scoring, selecting a candidate, or inferring protected traits.
```

**Full instruction:** Compare these two resumes without recommending a candidate and list differences only.

**Sufficiency:** substantive — Draft evidence-based resume comparison algorithm: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

Evidence-only resume comparison matches the differences-only request.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F028-R-W12

**Source:** synthetic · **Words:** 12 · **Disposition:** reusable

**Prefix:** Calculate budget variance from my supplied table but show actual category totals

**Action:** Draft actual-category aggregation logic

```text
def actual_totals(rows):
    from decimal import Decimal
    totals = {}
    for row in rows:
        category = row["category"]
        totals[category] = totals.get(category, Decimal(0)) + Decimal(str(row["actual"]))
    return totals
```

**Full instruction:** Calculate budget variance from my supplied table but show actual category totals only, without calculating or reporting variances.

**Sufficiency:** substantive — Draft actual-category aggregation logic: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

Actual-category aggregation computes no variances.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_122-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** I noticed some promising trends and want to proceed with a 'Buy' order for 100 shares of AAPL

**Action:** Draft uncommitted order guard

```text
Draft intent: BUY 100 AAPL shares. Before any submission, resolve venue/currency and order type, then require a current quote. At proposed price p and fees f, estimated debit = 100*p+f. Reject fractional/nonpositive quantity or insufficient available funds; keep status DRAFT with submission disabled.
```

**Full instruction:** I noticed some promising trends and want to proceed with a 'Buy' order for 100 shares of AAPL at a price of $150 each. Let's ensure the order is placed correctly.

**Sufficiency:** substantive — Draft uncommitted order guard: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The 100-share AAPL draft and debit formula survive binding the 150-dollar price.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_140-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** I'm contemplating whether adding Zeta Corp's stock to my watchlist is the right move. It sounds like it's

**Action:** Draft watchlist research query

```text
"Zeta Corp" ("investor relations" OR "annual report" OR "stock exchange") -rumor -forum
```

**Full instruction:** I'm contemplating whether adding Zeta Corp's stock to my watchlist is the right move. It sounds like it's on a noteworthy upward trend. Could you add that to my watchlist?

**Sufficiency:** substantive — Draft watchlist research query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

Issuer-source research can resolve Zeta's instrument before a watchlist addition.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F022-K-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Find peer-reviewed papers about hidden-state probing

**Action:** Prepare literature queries and a publication-status filter.

```text
Unsubmitted queries: ("hidden-state probing" OR "hidden state probing" OR "probing hidden representations") ("language model" OR "neural network") (proceedings OR journal); ("probing classifiers" OR "diagnostic classifiers") ("hidden states" OR representations) (ACL OR EMNLP OR ICLR). For each candidate, verify an actual journal or conference publication record; an arXiv listing alone does not establish peer review.
```

**Full instruction:** Find peer-reviewed papers about hidden-state probing and use only peer-reviewed sources.

**Sufficiency:** substantive — Prepare literature queries and a publication-status filter: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

Literature queries and publication verification implement the peer-review requirement.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F006-K-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Find bakeries around Birch Park that

**Action:** Prepare a bakery discovery query for Birch Park.

```text
Unsubmitted query: (bakery OR bakeries OR patisserie) "Birch Park" (address OR location OR directions) -recipe -recipes. Geographic identity and the unfinished qualifying condition remain unverified.
```

**Full instruction:** Find bakeries around Birch Park that serve coffee, including the two listed options.

**Sufficiency:** substantive — Prepare a bakery discovery query for Birch Park: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

Bakery location discovery survives adding the coffee filter and listed candidates.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_199-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** I'm planning a journey from Los Angeles to New York on the morning of April 15th 2026, preferring

**Action:** Draft a route/date search query

```text
("Los Angeles" OR LAX) ("New York" OR JFK OR EWR) "April 15 2026" (morning OR departure)
```

**Full instruction:** I'm planning a journey from Los Angeles to New York on the morning of April 15th 2026, preferring to fly business class. Check the flight cost and then please arrange this flight using my pre-linked credit card with id 'card_123456789' and access token 'abc123xyz'.

**Sufficiency:** substantive — Draft a route/date search query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

The route, morning and date remain correct when business class is specified.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_49-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** Within the temp directory, could you list all the current files directly in the terminal including all the

**Action:** Draft a complete temp-directory listing

```text
find ./temp -mindepth 1 -maxdepth 1 -print | sort
```

**Full instruction:** Within the temp directory, could you list all the current files directly in the terminal including all the hidden files, ensuring we maintain the present directory structure intact and refrain from generating any additional directories or files?

**Sufficiency:** substantive — Draft a complete temp-directory listing: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The temp listing includes hidden entries and makes no filesystem changes.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F009-K-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Research local robotic actuator manufacturers and

**Action:** Prepare an actuator-manufacturer research query.

```text
Unsubmitted query: ("robotic actuator" OR "robotics actuators" OR "servo actuator") (manufacturer OR manufacturing) (factory OR "contact us") -distributor -reseller. When locality is specified, add its quoted city or region and verify the manufacturing address rather than relying on a sales-office address.
```

**Full instruction:** Research local robotic actuator manufacturers and retain the manufacturers while adding distributors separately.

**Sufficiency:** substantive — Prepare an actuator-manufacturer research query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** Y

Manufacturer discovery survives because manufacturers remain required; distributors can be researched separately.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F011-R-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** non_reusable

**Prefix:** Find brown faux-suede jackets with stand

**Action:** Prepare apparel query

```text
("faux suede" OR "faux-suede") brown jacket ("stand collar" OR "stand-up collar") -"genuine suede"
```

**Full instruction:** Find brown faux-suede jackets with stand collars but use black cotton jackets with lapels instead and discard the original options.

**Sufficiency:** substantive — Prepare apparel query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

The brown faux-suede stand-collar target is expressly discarded.

Substantive preparation requires material replacement or has no established role in the final task.

## CP1-SP1-S-SX1-F013-R-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** non_reusable

**Prefix:** Find freestanding desk converters under 250

**Action:** Prepare desk-converter discovery query

```text
("desk converter" OR "desktop riser") (freestanding OR "free standing") -"wall mounted" -"desk frame"
```

**Full instruction:** Find freestanding desk converters under 250 credits but only show permanently mounted converters and discard freestanding ones.

**Sufficiency:** substantive — Prepare desk-converter discovery query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

Freestanding-only discovery conflicts with permanently mounted-only results.

Substantive preparation requires material replacement or has no established role in the final task.

## CP1-SP1-P-multi_turn_base_58-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** I am planning a road trip from Rivermist to San Francisco, and I need to know how far

**Action:** Draft road-distance discovery query

```text
"Rivermist" "San Francisco" ("driving distance" OR "road distance") -flight -airfare
```

**Full instruction:** I am planning a road trip from Rivermist to San Francisco, and I need to know how far I will be traveling. This would help me ensure that my car is sufficiently fueled for the journey.

**Sufficiency:** substantive — Draft road-distance discovery query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

The road-distance search supports the unchanged fuel-planning journey.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_30-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** Search for test result of Apollo Project which is supposed to be in the project directory. It's likely

**Action:** Draft an Apollo test-result discovery command

```text
rg --files --hidden -g '!.git' | rg -i '(apollo.*(test|result)|(test|result).*apollo)'
```

**Full instruction:** Search for test result of Apollo Project which is supposed to be in the project directory. It's likely a JSON file. While it's a secret file, please take a look and tell me what's inside.

**Sufficiency:** substantive — Draft an Apollo test-result discovery command: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The hidden-inclusive Apollo filename search supports discovering secret test results.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_17-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** Could you provide me with an inventory of files that are currently visible and hidden in the directory

**Action:** Draft directory inventory command

```text
find "$TARGET_DIR" -mindepth 1 -maxdepth 1 -print
# Includes dotfiles and dot-directories; does not recurse or modify entries.
```

**Full instruction:** Could you provide me with an inventory of files that are currently visible and hidden in the directory I'm working in at the moment?

**Sufficiency:** substantive — Draft directory inventory command: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The parameterized inventory includes hidden entries and can use the current directory.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F015-R-W18

**Source:** synthetic · **Words:** 18 · **Disposition:** reusable

**Prefix:** Check whether my dentist can see me on Friday but check Monday instead and ignore Friday openings, keeping

**Action:** Draft unsent dentist inquiry

```text
Hello, could you let me know your available appointment times on Monday? Please consider Monday availability only; I no longer need Friday openings. Thank you.
```

**Full instruction:** Check whether my dentist can see me on Friday but check Monday instead and ignore Friday openings, keeping my existing appointment as fallback.

**Sufficiency:** substantive — Draft unsent dentist inquiry: concrete draft content establishes preparation beyond copied inputs.

**Ambiguity:** N

The Monday inquiry remains reusable while the existing appointment is retained separately.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F024-K-W12

**Source:** synthetic · **Words:** 12 · **Disposition:** reusable

**Prefix:** Compare Acme's revenue in its two annual releases and report company-stated actual

**Action:** Draft reported-revenue comparison rule

```text
Extract revenue, period length, currency, units and restatement status from each company annual release. Compare like-for-like company-stated actuals only. Difference = later-earlier; growth_pct = 100*(later-earlier)/earlier when earlier != 0. If periods or currencies differ, report incompatibility rather than silently normalize.
```

**Full instruction:** Compare Acme's revenue in its two annual releases and report company-stated actual revenue only.

**Sufficiency:** substantive — Draft reported-revenue comparison rule: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

Like-for-like company-stated revenue comparison matches the final constraint.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_26-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** unresolved_reuse

**Prefix:** Could you kindly navigate to the temporary directory and list all the files available there right in the

**Action:** Draft a temporary-directory listing

```text
find ./temp -mindepth 1 -maxdepth 1 -print | sort
```

**Full instruction:** Could you kindly navigate to the temporary directory and list all the files available there right in the terminal for me? I would like to quickly skim through them and all the hidden files.

**Sufficiency:** substantive — Draft a temporary-directory listing: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

The command assumes ./temp, but the intended temporary directory location is unspecified.

Substantive preparation; reuse remains unresolved.

## CP1-SP1-S-SX1-F031-R-W18

**Source:** synthetic · **Words:** 18 · **Disposition:** reusable

**Prefix:** Write a Python function that counts ERROR lines in the supplied log but count WARN lines instead and

**Action:** Draft a WARN-line counter

```text
import re
def count_warn_lines(log_text):
    return sum(bool(re.search(r"\bWARN\b", line)) for line in log_text.splitlines())
```

**Full instruction:** Write a Python function that counts ERROR lines in the supplied log but count WARN lines instead and do not count ERROR lines.

**Sufficiency:** substantive — Draft a WARN-line counter: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The counter targets WARN rather than ERROR.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_133-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** Could you kindly integrate Apple's stock into my current watchlist and subsequently provide me with a detailed breakdown

**Action:** Draft Apple watchlist update algorithm

```text
Resolve Apple to a verified listed instrument identifier, then compare against existing watchlist IDs. If already present, do not duplicate; otherwise stage one addition. For the requested breakdown, join the resolved ID to timestamped price and issuer-disclosure data, preserving missing values as unknown. Keep update uncommitted.
```

**Full instruction:** Could you kindly integrate Apple's stock into my current watchlist and subsequently provide me with a detailed breakdown of the watchlist's contents?

**Sufficiency:** substantive — Draft Apple watchlist update algorithm: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

Identity resolution, deduplication and uncommitted addition support the watchlist request.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F001-R-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Compare flights from Harborview to Eastport

**Action:** Draft flight-comparison procedure

```text
Keep flight records whose origin is Harborview and destination Eastport. Group by travel date, passenger count, and fare cabin. Within each group compare total fare including known mandatory fees, stop count, elapsed duration, and baggage allowance; retain missing fees as unknown and flag differing airport identifiers for review.
```

**Full instruction:** Compare flights from Harborview to Eastport but change the destination to Westhaven and discard the Eastport options.

**Sufficiency:** substantive — Draft flight-comparison procedure: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

The unexecuted comparison procedure survives a destination-constant substitution; no Eastport results exist to discard.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F029-R-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Compare current holdings with the start-of-month

**Action:** Draft holdings reconciliation algorithm

```text
Outer-join current and start-of-month position snapshots on account plus instrument identifier. Compute quantity_delta=q_now-q_start with absent positions treated as zero only for complete snapshots. Label new, closed, increased, decreased, and unchanged positions. If prices are present in the same currency, compute value_delta=q_now*p_now-q_start*p_start and separate quantity and price effects using (q_now-q_start)*p_start + q_now*(p_now-p_start). Flag corporate actions rather than treating every quantity change as a trade.
```

**Full instruction:** Compare current holdings with the start-of-month snapshot but compare current holdings with the start-of-year snapshot instead and ignore start-of-month holdings.

**Sufficiency:** substantive — Draft holdings reconciliation algorithm: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

Snapshot reconciliation arithmetic survives binding the start-of-year input and relabeling its baseline.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F034-K-W12

**Source:** synthetic · **Words:** 12 · **Disposition:** reusable

**Prefix:** Add malformed-JSON tests to the parser and keep this work limited to

**Action:** Draft malformed-JSON test cases

```text
Malformed inputs: {"a":1,} (trailing comma); {"a":} (missing value); {"a" 1} (missing colon); [1,2 (unclosed array); {"a":"unterminated} (unclosed string). For each, assert parsing raises the parser’s documented parse-error type and never returns a partial successful object. Do not assert implementation-specific error wording.
```

**Full instruction:** Add malformed-JSON tests to the parser and keep this work limited to correctness tests.

**Sufficiency:** substantive — Draft malformed-JSON test cases: concrete draft content establishes preparation beyond copied inputs.

**Ambiguity:** N

The malformed inputs and rejection assertions remain correctness tests.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_115-W12

**Source:** public_bfcl · **Words:** 12 · **Disposition:** reusable

**Prefix:** I require a comprehensive analysis of the stock with Amazon, as it

**Action:** Draft an Amazon stock-analysis source query

```text
Amazon ("investor relations" OR "Form 10-K" OR "quarterly results") (revenue OR "operating income" OR "cash flow")
```

**Full instruction:** I require a comprehensive analysis of the stock with Amazon, as it will inform my subsequent decision-making.

**Sufficiency:** substantive — Draft an Amazon stock-analysis source query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

Amazon disclosure discovery supports the requested stock analysis.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_25-W12

**Source:** public_bfcl · **Words:** 12 · **Disposition:** reusable

**Prefix:** Examine current directory for any presence of the file named 'summary.txt'. If

**Action:** Draft an existence check for summary.txt

```text
from pathlib import Path
p = Path('summary.txt')
print('regular file present' if p.is_file() else 'no regular file at summary.txt')
```

**Full instruction:** Examine current directory for any presence of the file named 'summary.txt'. If there is one, What's inside?

**Sufficiency:** substantive — Draft an existence check for summary.txt: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The summary.txt existence check remains needed before conditional reading.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F023-R-W12

**Source:** synthetic · **Words:** 12 · **Disposition:** reusable

**Prefix:** Find version 3 documentation for Library L but use version 4 instead

**Action:** Draft a version-filtered documentation query

```text
"Library L" ("version 4" OR "v4") (documentation OR reference) -"version 3" -"v3"
```

**Full instruction:** Find version 3 documentation for Library L but use version 4 instead and exclude all version 3 documentation.

**Sufficiency:** substantive — Draft a version-filtered documentation query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

The query correctly switches to version four and excludes version three.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_33-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** unresolved_reuse

**Prefix:** What's the name of the python file my current directory? There should be only one and. Do not

**Action:** Draft a top-level Python filename check

```text
from pathlib import Path
files = sorted(p.name for p in Path('.').iterdir() if p.is_file() and p.suffix == '.py')
print(files[0] if len(files) == 1 else f'Expected one Python file; found {len(files)}: {files}')
```

**Full instruction:** What's the name of the python file my current directory? There should be only one and. Do not list hidden files. 

**Sufficiency:** substantive — Draft a top-level Python filename check: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

Hidden Python files are not excluded; their presence and effect on the single-file result are unknown.

Substantive preparation; reuse remains unresolved.

## CP1-SP1-S-SX1-F001-K-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Compare flights from Harborview to Eastport

**Action:** Draft flight-comparison procedure

```text
Keep flight records whose origin is Harborview and destination Eastport. Group by travel date, passenger count, and fare cabin. Within each group compare total fare including known mandatory fees, stop count, elapsed duration, and baggage allowance; retain missing fees as unknown and flag differing airport identifiers for review.
```

**Full instruction:** Compare flights from Harborview to Eastport and show the two listed morning options.

**Sufficiency:** substantive — Draft flight-comparison procedure: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The route comparison can be restricted to the listed morning flights.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F027-R-W18

**Source:** synthetic · **Words:** 18 · **Disposition:** reusable

**Prefix:** Calculate a 7 percent downside scenario for a 100-credit index but use a 12 percent decline instead and

**Action:** Calculate the corrected downside scenario

```text
Starting index: 100 credits. Decline: 100 × 0.12 = 12 credits. Scenario level: 100 − 12 = 88 credits.
```

**Full instruction:** Calculate a 7 percent downside scenario for a 100-credit index but use a 12 percent decline instead and omit the 7 percent case.

**Sufficiency:** substantive — Calculate the corrected downside scenario: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The corrected 12-percent decline yields the required 88-credit level.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_90-W6

**Source:** public_bfcl · **Words:** 6 · **Disposition:** reusable

**Prefix:** I need to fill 150 liters

**Action:** Prepare the fuel-volume conversion and cost expression.

```text
150 liters = 0.150 cubic meters. Using 1 US liquid gallon = 3.785411784 liters, 150 liters ≈ 39.6258 US gallons. Using 1 imperial gallon = 4.54609 liters, 150 liters ≈ 32.9954 imperial gallons. At a quoted price p per liter, total cost is 150p; no price, tank capacity, or purchase is inferred.
```

**Full instruction:** I need to fill 150 liters of gasoline into my vehicle for today's trip and then start the engine using the standard start mode to ensure everything is operational before departure. How much is that in gallon? Round it to the nearest integer and fill that amount.

**Sufficiency:** substantive — Prepare the fuel-volume conversion and cost expression: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

Both gallon conversions survive rounding; the intended gallon convention remains unresolved.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F028-K-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Calculate budget variance from my supplied

**Action:** Draft a budget-variance calculation function.

```text
Unexecuted Python draft:
def budget_variance(actual, budget):
    delta = actual - budget
    percent = None if budget == 0 else 100 * delta / budget
    return {"actual_minus_budget": delta, "variance_percent": percent}

Apply only to supplied pairs in matching units and periods. Positive delta means actual exceeds budget; whether that is favorable depends on whether the line is revenue or expense. With a zero budget, the percentage is undefined.
```

**Full instruction:** Calculate budget variance from my supplied table and identify the largest overspend.

**Sufficiency:** substantive — Draft a budget-variance calculation function: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The variance function remains useful before selecting the largest overspend.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_7-W6

**Source:** public_bfcl · **Words:** 6 · **Disposition:** reusable

**Prefix:** Directly open the academic_venture folder and

**Action:** Draft guarded academic folder navigation

```text
if [ -d ./academic_venture ]; then cd -- ./academic_venture && pwd; else printf "%s\n" "academic_venture directory absent" >&2; fi
```

**Full instruction:** Directly open the academic_venture folder and employ precise commands to generate a new directory for our upcoming academic venture, ensuring its exact placement in our present work directory. It's name should be academic_hub

**Sufficiency:** substantive — Draft guarded academic folder navigation: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

Guarded navigation remains the requested first step before directory creation.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_1-W12

**Source:** public_bfcl · **Words:** 12 · **Disposition:** reusable

**Prefix:** I am alex. Check if the current directory is under my name

**Action:** Draft current-path name checks

```text
from pathlib import Path
p = Path.cwd()
print({'leaf_named_alex': p.name.casefold() == 'alex', 'beneath_alex_component': any(x.name.casefold() == 'alex' for x in p.parents)})
# A path-name match is not proof of account ownership.
```

**Full instruction:** I am alex. Check if the current directory is under my name and list all the visible and hidden contents in the current directory now, please.

**Sufficiency:** substantive — Draft current-path name checks: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

The name checks remain reusable, with filesystem ownership explicitly distinguished from path names.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F046-R-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** non_reusable

**Prefix:** Find technical podcast interviews about AI

**Action:** Prepare technical podcast search query

```text
(AI OR "artificial intelligence") (podcast OR "podcast transcript") (interview OR conversation) (architecture OR training OR inference) -"AI generated podcast"
```

**Full instruction:** Find technical podcast interviews about AI agents but use only news roundups and exclude interviews.

**Sufficiency:** substantive — Prepare technical podcast search query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

Interview-specific discovery conflicts with news-only selection.

Substantive preparation requires material replacement or has no established role in the final task.

## CP1-SP1-S-SX1-F011-K-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Find brown faux-suede jackets with stand

**Action:** Prepare apparel query

```text
("faux suede" OR "faux-suede") brown jacket ("stand collar" OR "stand-up collar") -"genuine suede"
```

**Full instruction:** Find brown faux-suede jackets with stand collars and compare the listed options under 200 credits.

**Sufficiency:** substantive — Prepare apparel query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

The jacket query remains useful under the price cap.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F012-K-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Compare robotics synthetic-data tools that support

**Action:** Draft a robotics synthetic-data comparison method.

```text
For each eventual candidate, run the same scene specification and compare: sensor outputs and label types; control of geometry, materials, lighting, and random seeds; robot/kinematic model import; reproducibility of a generated sample from its seed; and export schema compatibility. Record whether each capability is native, requires custom code, or is unsupported. Apply the missing must-support condition as a hard filter before scoring remaining tools. This is an unexecuted comparison protocol.
```

**Full instruction:** Compare robotics synthetic-data tools that support Engine R and keep Engine R support mandatory.

**Sufficiency:** substantive — Draft a robotics synthetic-data comparison method: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The parameterized capability protocol accepts Engine R as its hard filter.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F044-K-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Build an upbeat instrumental jazz playlist

**Action:** Draft upbeat instrumental jazz playlist

```text
Candidate sequence: Art Blakey & The Jazz Messengers — Moanin’; Dave Brubeck Quartet — Take Five; Duke Ellington — C Jam Blues; Sonny Rollins — St. Thomas; Cannonball Adderley — Work Song. Select instrumental recordings of these tunes and audition tempo/energy before finalizing.
```

**Full instruction:** Build an upbeat instrumental jazz playlist and exclude vocal tracks.

**Sufficiency:** substantive — Draft upbeat instrumental jazz playlist: concrete draft content establishes preparation beyond copied inputs.

**Ambiguity:** N

The instrumental candidate playlist survives excluding vocal recordings.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_38-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** I've misplaced a vital document inclusive of extensive research. Assist in locating a file named 'findings_report' within this

**Action:** Draft exact research-file discovery command

```text
find "$SEARCH_ROOT" -type f \( -name 'findings_report' -o -name 'findings_report.*' \) -print
# Report all matches, including extension variants; do not choose an arbitrary duplicate.
```

**Full instruction:** I've misplaced a vital document inclusive of extensive research. Assist in locating a file named 'findings_report' within this 'SuperResearch'. Could you remove it and the directory.

**Sufficiency:** substantive — Draft exact research-file discovery command: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The filename search survives binding SuperResearch and supports locating the deletion target.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_107-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** Before purchasing shares in Zeta Corp, I am curious about their recent stock performance. Could you provide their

**Action:** Draft stock-performance disclosure query

```text
"Zeta Corp" ("historical stock prices" OR "quarterly results" OR "investor relations") -forum -rumor
```

**Full instruction:** Before purchasing shares in Zeta Corp, I am curious about their recent stock performance. Could you provide their stock symbol and detail their market activity?

**Sufficiency:** substantive — Draft stock-performance disclosure query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

Issuer and price-source discovery supports symbol and market-activity reporting.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F045-R-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** non_reusable

**Prefix:** Choose a non-horror movie under two

**Action:** Prepare non-horror movie filter

```text
Given movie metadata, remove entries whose genre tags contain Horror, and hold untagged entries for review. Preserve titles, runtime, and genre evidence for remaining candidates. Do not apply a numeric runtime cutoff until the unit after "two" is known.
```

**Full instruction:** Choose a non-horror movie under two hours for tonight but choose a horror movie longer than two hours instead.

**Sufficiency:** substantive — Prepare non-horror movie filter: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

The central non-horror exclusion must reverse; metadata handling alone survives.

Substantive preparation requires material replacement or has no established role in the final task.

## CP1-SP1-S-SX1-F014-K-W12

**Source:** synthetic · **Words:** 12 · **Disposition:** reusable

**Prefix:** Find a 30-minute meeting for Sam and me on Tuesday and use

**Action:** Draft a Tuesday common-slot algorithm

```text
def common_half_hours(sam_free, my_free):
    from datetime import timedelta
    slots = []
    for a,b in sam_free:
        for c,d in my_free:
            start,end = max(a,c),min(b,d)
            if start.weekday() == 1 and end-start >= timedelta(minutes=30):
                slots.append((start,start+timedelta(minutes=30)))
    return sorted(set(slots))
# Supply intervals on the intended Tuesday in one timezone.
```

**Full instruction:** Find a 30-minute meeting for Sam and me on Tuesday and use either of the two listed Tuesday slots.

**Sufficiency:** substantive — Draft a Tuesday common-slot algorithm: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

Tuesday half-hour intersection supports choosing a listed Tuesday slot.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_80-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** You're planning an extended expedition from Rivermist to San Francisco. Could you determine the travel distance between these

**Action:** Draft a route-distance query

```text
"Rivermist" "San Francisco" ("driving distance" OR "road distance") (miles OR kilometers)
```

**Full instruction:** You're planning an extended expedition from Rivermist to San Francisco. Could you determine the travel distance between these two locations for me?

**Sufficiency:** substantive — Draft a route-distance query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

The query covers the unchanged route-distance request.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_35-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** Find a file named 'config.py' somewhere deep in the file system and once you have located it, display

**Action:** Draft filename discovery command

```text
find "$SEARCH_ROOT" -type f -name 'config.py' -print
# Preserve every matching path; select a unique intended match before any display step.
```

**Full instruction:** Find a file named 'config.py' somewhere deep in the file system and once you have located it, display the last line of the first occuring file.

**Sufficiency:** substantive — Draft filename discovery command: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

All config.py paths remain useful, although the later first-occurrence rule replaces unique-match selection.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_169-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** I just relocated to Rivermist and I'm looking to book a flight to Los Angeles for a crucial

**Action:** Draft flight discovery query

```text
"Rivermist" "Los Angeles" (flight OR airline OR airport) -hotel -cruise
```

**Full instruction:** I just relocated to Rivermist and I'm looking to book a flight to Los Angeles for a crucial business meeting. Could you arrange the flight for me, using my credit card with id 'card_6789'? I need it booked for next Tuesday 2026-11-10, in business class, with a cost under $1200. Additionally, I have received my new access token: 2278-9812-3456-4567. Once the flight is confirmed, please ensure you acquire the invoice for this transaction as it's necessary for my reimbursement.

**Sufficiency:** substantive — Draft flight discovery query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

The same flight route can be narrowed by date, cabin and budget.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_166-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** I'm setting sail on an adventure from Crescent Hollow to Rivermist and need the scoop on flight costs

**Action:** Draft airfare discovery query

```text
"Crescent Hollow" "Rivermist" (flight OR airfare) (fare OR price) -hotel -cruise
```

**Full instruction:** I'm setting sail on an adventure from Crescent Hollow to Rivermist and need the scoop on flight costs for my journey. My takeoff is scheduled for 2026-07-15, and luxury's the name of the game, so I'll be in business class.

**Sufficiency:** substantive — Draft airfare discovery query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

Airfare discovery survives adding the travel date and cabin.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F047-K-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Make a three-day business-trip packing checklist

**Action:** Draft a three-day business-trip packing checklist.

```text
Three-day business-trip packing checklist:
• Wear one business outfit in transit if suitable; pack two coordinating work tops, one extra pair of trousers or a skirt, and one blazer that works with all outfits.
• Pack three sets of underwear and socks, sleepwear, a casual outfit, and comfortable shoes; reuse business shoes to reduce bulk.
• Pack laptop, its charger, phone charger, headphones, and any presentation adapter needed by your own equipment. Save offline copies of your presentation and itinerary.
• Pack identification, payment card, required work access badge, and travel documents applicable to the itinerary.
• Pack toiletries, personal medication for the trip, and a small spare supply if available.
• Keep essential documents, medication, and one change of clothes in your carry-on if checking a bag. Adjust outerwear to the forecast once the destination is known.
```

**Full instruction:** Make a three-day business-trip packing checklist and omit formalwear.

**Sufficiency:** substantive — Draft a three-day business-trip packing checklist: concrete draft content establishes preparation beyond copied inputs.

**Ambiguity:** Y

Travel essentials survive; business clothing may need trimming depending on the meaning of formalwear.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F034-R-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** non_reusable

**Prefix:** Add malformed-JSON tests to the parser

**Action:** Draft malformed-JSON test vectors

```text
Invalid input cases: {"a":1,} (trailing comma); {"a" 1} (missing colon); {"a":"unterminated} (unclosed string); [1,,2] (empty element); {"a":tru} (invalid literal); {"a":1} trailing (extra input). For each, assert parse rejection with the parser’s documented error type, no partially accepted value, and no crash. Include valid controls {} and {"a":[1,true,null]} to ensure rejection is not unconditional.
```

**Full instruction:** Add malformed-JSON tests to the parser but benchmark parsing speed only and do not add correctness tests.

**Sufficiency:** substantive — Draft malformed-JSON test vectors: concrete draft content establishes preparation beyond copied inputs.

**Ambiguity:** N

Correctness vectors and assertions are expressly excluded by speed-only benchmarking.

Substantive preparation requires material replacement or has no established role in the final task.

## CP1-SP1-P-multi_turn_base_28-W6

**Source:** public_bfcl · **Words:** 6 · **Disposition:** unresolved_reuse

**Prefix:** Where is my analysis? Locate any

**Action:** Draft a local analysis-file discovery command.

```text
Unexecuted command: rg --files --hidden -g '!.git/**' -g '*[Aa]nalys*' <chosen-search-root>
Retain full paths for every match and distinguish files from different directories. Filename matches are candidates, not proof that the desired analysis has been found.
```

**Full instruction:** Where is my analysis? Locate any file with analysis in it.

**Sufficiency:** substantive — Draft a local analysis-file discovery command: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

Filename discovery is concrete, but 'analysis in it' could require content search instead.

Substantive preparation; reuse remains unresolved.

## CP1-SP1-S-SX1-F021-K-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Draft a refund approval message and

**Action:** Draft uncommitted refund approval wording

```text
Your refund request is approved. We will confirm the refund amount, payment method, and expected processing time separately. Thank you for your patience. [Draft only; verify actual approval before sending.]
```

**Full instruction:** Draft a refund approval message and avoid promising a payment date.

**Sufficiency:** substantive — Draft uncommitted refund approval wording: concrete draft content establishes preparation beyond copied inputs.

**Ambiguity:** N

The approval draft promises no payment date.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_54-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** Would you be able to convert 20 liters of gasoline into gallons for me? Afterwards, starting the engine

**Action:** Convert the specified gasoline volume

```text
20 liters = 5.28344 US gallons (20 ÷ 3.785411784), or 4.39938 Imperial gallons (20 ÷ 4.54609).
```

**Full instruction:** Would you be able to convert 20 liters of gasoline into gallons for me? Afterwards, starting the engine to check for smooth operation would be appreciated.

**Sufficiency:** substantive — Convert the specified gasoline volume: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

Both volume conversions survive the separate engine-start request; gallon convention is unspecified.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F040-R-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** non_reusable

**Prefix:** Stage a 70 F thermostat setting

**Action:** Prepare a thermostat temperature conversion and unsent staging rule.

```text
Requested temperature: 70 °F. Equivalent Celsius: (70 − 32) × 5/9 = 190/9 °C ≈ 21.111 °C. Unexecuted staging logic: read the target device’s native unit and allowed setpoint increment; represent this temperature in that unit; report any rounding difference; retain as an unsent draft. Device identity and operating mode must come from the completed request.
```

**Full instruction:** Stage a 70 F thermostat setting for tonight but stage 68 F instead, only if the current setting differs from 68 F; do not apply it.

**Sufficiency:** substantive — Prepare a thermostat temperature conversion and unsent staging rule: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The numeric 70-degree conversion must be recalculated for 68 degrees, though staging logic survives.

Substantive preparation requires material replacement or has no established role in the final task.

## CP1-SP1-S-SX1-F030-K-W18

**Source:** synthetic · **Words:** 18 · **Disposition:** reusable

**Prefix:** Calculate breakeven for my debit spread using the supplied values and use the supplied 5-credit debit and 100-credit

**Action:** Draft conditional debit-spread breakeven arithmetic

```text
With debit 5 credits and a 100-credit strike: if 100 is the lower long-call strike, call-spread breakeven = 100 + 5 = 105. If 100 is the higher long-put strike, put-spread breakeven = 100 − 5 = 95. The truncated prefix does not identify spread direction or the role of 100.
```

**Full instruction:** Calculate breakeven for my debit spread using the supplied values and use the supplied 5-credit debit and 100-credit lower strike.

**Sufficiency:** substantive — Draft conditional debit-spread breakeven arithmetic: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

The conditional 105 call breakeven survives; the put result assumes 100 is the higher strike, which the full text excludes.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F014-R-W18

**Source:** synthetic · **Words:** 18 · **Disposition:** reusable

**Prefix:** Find a 30-minute meeting for Sam and me on Tuesday but switch the meeting to Wednesday and ignore

**Action:** Draft availability intersection algorithm

```text
For Wednesday only, intersect Sam’s and my free intervals in a shared timezone. For each overlap [s,e), retain it if e-s >= 30 minutes; propose [s,s+30 minutes). Do not reserve a slot.
```

**Full instruction:** Find a 30-minute meeting for Sam and me on Tuesday but switch the meeting to Wednesday and ignore Tuesday availability.

**Sufficiency:** substantive — Draft availability intersection algorithm: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

Wednesday-only intersection matches the revised meeting day.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F039-R-W18

**Source:** synthetic · **Words:** 18 · **Disposition:** reusable

**Prefix:** Stage the living-room lights at 30 percent brightness but stage bedroom lights at 60 percent instead and discard

**Action:** Draft a replacement lighting plan

```text
def replacement_lighting_plan():
    return {"pending_actions": [{"room": "bedroom", "brightness_percent": 60}], "discard_pending": [{"room": "living-room", "brightness_percent": 30}]}
# Returns local data only.
```

**Full instruction:** Stage the living-room lights at 30 percent brightness but stage bedroom lights at 60 percent instead and discard the living-room command.

**Sufficiency:** substantive — Draft a replacement lighting plan: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

The returned pending-action and discard lists operationalize replacement of the living-room plan.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F008-R-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Find pharmacies in Brookfield that are

**Action:** Prepare pharmacy location discovery for Brookfield.

```text
Unsubmitted query: (pharmacy OR pharmacies) "Brookfield" (address OR location OR hours) -jobs -careers. Confirm which Brookfield and the unfinished qualifying condition before filtering candidates or making a recommendation.
```

**Full instruction:** Find pharmacies in Brookfield that are open now but only list hospital pharmacies that are closed now and open tomorrow.

**Sufficiency:** substantive — Prepare pharmacy location discovery for Brookfield: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** Y

Broad pharmacy and hours discovery survives hospital, closed-now and tomorrow filtering.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_35-W6

**Source:** public_bfcl · **Words:** 6 · **Disposition:** reusable

**Prefix:** Find a file named 'config.py' somewhere

**Action:** Draft config.py file search

```text
find "$SEARCH_ROOT" -type f -name config.py -print
```

**Full instruction:** Find a file named 'config.py' somewhere deep in the file system and once you have located it, display the last line of the first occuring file.

**Sufficiency:** substantive — Draft config.py file search: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

Exact config.py discovery remains needed before selecting and reading a match.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_47-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** I have a list of student record in this directory, could you find me where is it by

**Action:** Draft a student-record discovery command

```text
find . -type f \( -iname '*student*' -o -iname '*enrol*' -o -iname '*roster*' \) -print
```

**Full instruction:** I have a list of student record in this directory, could you find me where is it by telling me its name and using 'find'?

**Sufficiency:** substantive — Draft a student-record discovery command: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The find-based filename candidates directly support locating a student record.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F043-R-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Find robotics documentaries but find astronomy

**Action:** Prepare separate documentary search expressions.

```text
Unsubmitted queries: (robotics OR robots) (documentary OR documentaries) -fiction -"movie review"; (astronomy OR astrophysics) (documentary OR documentaries) -astrology. Keep the result sets separate because the conjunction may introduce an additional requirement.
```

**Full instruction:** Find robotics documentaries but find astronomy documentaries only and exclude robotics titles.

**Sufficiency:** substantive — Prepare separate documentary search expressions: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** Y

The separate astronomy query survives intact; the robotics query can be discarded.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_119-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** Could you provide me with the latest stock information for Zeta Corp, including its current price and the

**Action:** Draft stock-quote source query

```text
"Zeta Corp" ("stock quote" OR "investor relations") (price OR exchange) -forum -rumor
```

**Full instruction:** Could you provide me with the latest stock information for Zeta Corp, including its current price and the performance metrics?

**Sufficiency:** substantive — Draft stock-quote source query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

Zeta quote-source discovery supports current price and metrics.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F012-R-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Compare robotics synthetic-data tools that support

**Action:** Draft a robotics synthetic-data comparison method.

```text
For each eventual candidate, run the same scene specification and compare: sensor outputs and label types; control of geometry, materials, lighting, and random seeds; robot/kinematic model import; reproducibility of a generated sample from its seed; and export schema compatibility. Record whether each capability is native, requires custom code, or is unsupported. Apply the missing must-support condition as a hard filter before scoring remaining tools. This is an unexecuted comparison protocol.
```

**Full instruction:** Compare robotics synthetic-data tools that support Engine R but only consider tools for Engine S that do not support Engine R.

**Sufficiency:** substantive — Draft a robotics synthetic-data comparison method: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The comparison protocol has no bound engine and can accept Engine S plus the Engine R exclusion.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_43-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** Arrange a complete listing of all files and directories presently located here, making sure you don't overlook the

**Action:** Draft a full current-directory inventory

```text
find . -mindepth 1 -maxdepth 1 -print | sort
```

**Full instruction:** Arrange a complete listing of all files and directories presently located here, making sure you don't overlook the hidden ones too.

**Sufficiency:** substantive — Draft a full current-directory inventory: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The directory inventory includes hidden files and directories.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F025-R-W18

**Source:** synthetic · **Words:** 18 · **Disposition:** reusable

**Prefix:** Find primary rules for Region A consumer AI systems but use Region B rules only and exclude Region

**Action:** Draft primary-source search

```text
"Region B" ("consumer AI" OR "consumer artificial intelligence") (legislation OR regulation OR statute) -commentary -opinion
```

**Full instruction:** Find primary rules for Region A consumer AI systems but use Region B rules only and exclude Region A rules.

**Sufficiency:** substantive — Draft primary-source search: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

The query targets the corrected Region B primary rules.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F026-K-W12

**Source:** synthetic · **Words:** 12 · **Disposition:** reusable

**Prefix:** Compare small open-weight reasoning models and flag vendor-only scores as unverified rather

**Action:** Draft score-provenance annotation logic

```text
def annotate_score(row):
    result = dict(row)
    result["verification"] = "independently reproduced" if row.get("independent_reproduction_url") else "unverified: vendor-only" if row.get("vendor_score_url") else "unverified: no source"
    return result
# Benchmark versions and evaluation settings must match before scores are ranked.
```

**Full instruction:** Compare small open-weight reasoning models and flag vendor-only scores as unverified rather than treating them as evidence.

**Sufficiency:** substantive — Draft score-provenance annotation logic: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

Vendor-only annotation logic survives, though a reproduction URL itself still needs verification.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F049-K-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** non_reusable

**Prefix:** Build a shopping list for vegetarian

**Action:** Draft vegetarian shopping-list candidate

```text
Candidate staples: lentils, chickpeas, tofu, brown rice, oats, whole-grain bread, spinach, broccoli, carrots, tomatoes, onions, fruit, olive oil, and nuts or seeds. Group legumes/tofu together as protein sources, rice/oats/bread as grains, and vegetables/fruit as produce; quantities depend on meals and servings.
```

**Full instruction:** Build a shopping list for vegetarian tacos and include beans instead of meat.

**Sufficiency:** substantive — Draft vegetarian shopping-list candidate: concrete draft content establishes preparation beyond copied inputs.

**Ambiguity:** Y

A broad staples list needs substantial replacement for bean tacos, with only some produce and grains reusable.

Substantive preparation requires material replacement or has no established role in the final task.

## CP1-SP1-P-multi_turn_base_100-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** I'm contemplating enhancing my investment portfolio with some tech industry assets, and I've got my eye on Nvidia.

**Action:** Draft Nvidia disclosure discovery query

```text
"Nvidia" ("annual report" OR "quarterly results" OR "investor relations") -rumor -forum
```

**Full instruction:** I'm contemplating enhancing my investment portfolio with some tech industry assets, and I've got my eye on Nvidia. I'm keen to know its current stock price, and would appreciate if you could source this information for me.

**Sufficiency:** substantive — Draft Nvidia disclosure discovery query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** Y

The investor-relations branch can lead to a current quote; annual-report branches are not current pricing.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F016-K-W12

**Source:** synthetic · **Words:** 12 · **Disposition:** reusable

**Prefix:** Find team meeting slots this week after 10 AM and show the

**Action:** Draft a team-slot intersection algorithm

```text
def intersect_free_windows(team_windows):
    from datetime import time
    common = team_windows[0] if team_windows else []
    for windows in team_windows[1:]:
        common = [(max(a,c),min(b,d)) for a,b in common for c,d in windows if max(a,c)<min(b,d)]
    return [(max(a,a.replace(hour=10,minute=0,second=0,microsecond=0)),b) for a,b in common if b.time()>time(10)]
# Inputs: same-day free intervals already scoped to this week and one timezone.
```

**Full instruction:** Find team meeting slots this week after 10 AM and show the two listed afternoon slots.

**Sufficiency:** substantive — Draft a team-slot intersection algorithm: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The common-window algorithm retains the requested afternoon availability.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_30-W6

**Source:** public_bfcl · **Words:** 6 · **Disposition:** unresolved_reuse

**Prefix:** Search for test result of Apollo

**Action:** Prepare a local Apollo test-result discovery query.

```text
Unexecuted command: rg -n -i -l -g '*.xml' -g '*.json' -g '*.log' -g '*.txt' -g '*.md' 'Apollo' <chosen-results-root>
Within each resulting candidate, search for test evidence using: rg -n -i 'testsuite|testcase|passed|failed|failure|error|skipped' <candidate-path>
Treat Apollo mentions without test evidence as nonmatches; do not infer a result status.
```

**Full instruction:** Search for test result of Apollo Project which is supposed to be in the project directory. It's likely a JSON file. While it's a secret file, please take a look and tell me what's inside.

**Sufficiency:** substantive — Prepare a local Apollo test-result discovery query: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

The content search omits hidden-file inclusion despite a secret target; the target's visibility and contents are unknown.

Substantive preparation; reuse remains unresolved.

## CP1-SP1-S-SX1-F042-K-W12

**Source:** synthetic · **Words:** 12 · **Disposition:** reusable

**Prefix:** Stage a kitchen-only vacuum run and keep all other rooms excluded; do

**Action:** Draft vacuum scope-validation rule

```text
Unsubmitted run configuration: include only kitchen. Resolve kitchen to exactly one saved room ID; reject zero or multiple matches. Compute excluded rooms = all mapped room IDs minus kitchen ID, and reject any plan whose selected-room set differs from {kitchen ID}. Do not dispatch.
```

**Full instruction:** Stage a kitchen-only vacuum run and keep all other rooms excluded; do not start cleaning.

**Sufficiency:** substantive — Draft vacuum scope-validation rule: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

Unique kitchen resolution and scope rejection satisfy unsent kitchen-only staging.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_4-W12

**Source:** public_bfcl · **Words:** 12 · **Disposition:** unresolved_reuse

**Prefix:** Could you kindly show me the list of files in tmp directory

**Action:** Draft a tmp inventory command

```text
find ./tmp -mindepth 1 -maxdepth 1 -print | sort
```

**Full instruction:** Could you kindly show me the list of files in tmp directory in my file system including the hidden one?

**Sufficiency:** substantive — Draft a tmp inventory command: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

The command assumes ./tmp, while the tmp directory's actual filesystem location is unspecified.

Substantive preparation; reuse remains unresolved.

## CP1-SP1-S-SX1-F047-R-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** non_reusable

**Prefix:** Make a three-day business-trip packing checklist

**Action:** Draft a three-day business-trip packing checklist.

```text
Three-day business-trip packing checklist:
• Wear one business outfit in transit if suitable; pack two coordinating work tops, one extra pair of trousers or a skirt, and one blazer that works with all outfits.
• Pack three sets of underwear and socks, sleepwear, a casual outfit, and comfortable shoes; reuse business shoes to reduce bulk.
• Pack laptop, its charger, phone charger, headphones, and any presentation adapter needed by your own equipment. Save offline copies of your presentation and itinerary.
• Pack identification, payment card, required work access badge, and travel documents applicable to the itinerary.
• Pack toiletries, personal medication for the trip, and a small spare supply if available.
• Keep essential documents, medication, and one change of clothes in your carry-on if checking a bag. Adjust outerwear to the forecast once the destination is known.
```

**Full instruction:** Make a three-day business-trip packing checklist but make it a three-day camping checklist instead, with no business clothing.

**Sufficiency:** substantive — Draft a three-day business-trip packing checklist: concrete draft content establishes preparation beyond copied inputs.

**Ambiguity:** N

Camping requires substantial gear replacement and removal of business clothing, though personal essentials survive.

Substantive preparation requires material replacement or has no established role in the final task.

## CP1-SP1-S-SX1-F006-R-W12

**Source:** synthetic · **Words:** 12 · **Disposition:** reusable

**Prefix:** Find bakeries around Birch Park but I meant pharmacies around Birch Park,

**Action:** Draft the corrected pharmacy search

```text
"Birch Park" (pharmacy OR chemist) (address OR hours) -bakery -bakeries
```

**Full instruction:** Find bakeries around Birch Park but I meant pharmacies around Birch Park, not bakeries.

**Sufficiency:** substantive — Draft the corrected pharmacy search: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

The corrected pharmacy query replaces bakery discovery.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_48-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** In my workspace folder, direct your attention to the initial directory we have access to and list out

**Action:** Draft a workspace-root listing command

```text
find . -mindepth 1 -maxdepth 1 -print | sort
```

**Full instruction:** In my workspace folder, direct your attention to the initial directory we have access to and list out the files present including the hidden files. Should you stumble upon a directory named 'test', go into there, dive deep and identify any files with 'test' in their names using 'ls'. Keeping tabs on details is key.

**Sufficiency:** substantive — Draft a workspace-root listing command: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

The initial hidden-inclusive inventory survives; the later ls requirement appears to govern the test-directory step.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F020-K-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Draft a message declining dinner tonight

**Action:** Draft dinner-decline message

```text
Thanks for inviting me to dinner tonight. I won’t be able to make it, but I appreciate the invitation. I hope you have a lovely evening.
```

**Full instruction:** Draft a message declining dinner tonight and suggest meeting next weekend.

**Sufficiency:** substantive — Draft dinner-decline message: concrete draft content establishes preparation beyond copied inputs.

**Ambiguity:** N

The decline message remains reusable with an added next-weekend suggestion.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_5-W12

**Source:** public_bfcl · **Words:** 12 · **Disposition:** reusable

**Prefix:** Find analysis_report.csv and upon locating it, ensure you move it to the

**Action:** Draft a filename discovery command

```text
find . -type f -name 'analysis_report.csv' -print
```

**Full instruction:** Find analysis_report.csv and upon locating it, ensure you move it to the 'archive' directory in the same directory of analysis report for safekeeping.

**Sufficiency:** substantive — Draft a filename discovery command: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

Exact filename discovery remains needed before the archive move.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_148-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** I'd appreciate if you could initiate an order, purchasing 100 shares of the company under the symbol AAPL

**Action:** Draft unsubmitted order validation

```text
DRAFT BUY: AAPL, quantity 100 shares. For price p and fees f, estimate 100*p+f in the instrument currency. Require a resolved venue, order type, valid quote timestamp and sufficient funds before any executable order can be created. Submission remains disabled.
```

**Full instruction:** I'd appreciate if you could initiate an order, purchasing 100 shares of the company under the symbol AAPL at the market's current rate. I've assessed it as a promising chance.

**Sufficiency:** substantive — Draft unsubmitted order validation: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

Order validation and the 100-share debit formula remain applicable to the market-price purchase.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F041-R-W18

**Source:** synthetic · **Words:** 18 · **Disposition:** reusable

**Prefix:** Prepare to lock the back door after I leave but prepare to lock the front door instead and

**Action:** Draft a replacement front-door locking plan

```text
def prepare_lock_plan():
    return {"pending_actions": [{"door": "front", "action": "lock", "trigger": "after departure"}], "discard_pending": [{"door": "back", "action": "lock"}]}
# Local staging data; no lock operation.
```

**Full instruction:** Prepare to lock the back door after I leave but prepare to lock the front door instead and do not use the back-door sensor reading.

**Sufficiency:** substantive — Draft a replacement front-door locking plan: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

The replacement action list stages the front lock without using a back-door reading.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F006-K-W12

**Source:** synthetic · **Words:** 12 · **Disposition:** reusable

**Prefix:** Find bakeries around Birch Park that serve coffee, including the two listed

**Action:** Draft bakery search

```text
"Birch Park" (bakery OR bakeries) (coffee OR espresso) -jobs -careers
```

**Full instruction:** Find bakeries around Birch Park that serve coffee, including the two listed options.

**Sufficiency:** substantive — Draft bakery search: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

Bakery-plus-coffee discovery matches the completed request.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_128-W6

**Source:** public_bfcl · **Words:** 6 · **Disposition:** reusable

**Prefix:** Could you ascertain the current time?

**Action:** Draft timezone-aware clock command

```text
date "+%Y-%m-%d %H:%M:%S %Z (%z)"
```

**Full instruction:** Could you ascertain the current time? It seems vital for aligning my stock market ventures seamlessly. Additionally, could you do me the favor of identifying which stocks in the Technology sector are currently offered?

**Sufficiency:** substantive — Draft timezone-aware clock command: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The timestamp command remains required despite the added stock-list request.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_131-W6

**Source:** public_bfcl · **Words:** 6 · **Disposition:** reusable

**Prefix:** Could you provide the current time?

**Action:** Draft current-time formatting command

```text
date "+%Y-%m-%d %H:%M:%S %Z (%z)"
```

**Full instruction:** Could you provide the current time? I need to assess market conditions before proceeding with trades.

**Sufficiency:** substantive — Draft current-time formatting command: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The current-time command directly supports the final request.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F029-K-W12

**Source:** synthetic · **Words:** 12 · **Disposition:** reusable

**Prefix:** Compare current holdings with the start-of-month snapshot and report concentration changes for

**Action:** Draft concentration-change calculation

```text
For each snapshot independently, weight_i = market_value_i / sum(market_value). Align holdings on stable identifiers, filling absent positions with zero weight. Report change_pp = 100*(current_weight_i-start_month_weight_i); also report HHI = sum(weight_i**2) and its change. Reject a zero denominator and disclose unpriced positions.
```

**Full instruction:** Compare current holdings with the start-of-month snapshot and report concentration changes for those two snapshots.

**Sufficiency:** substantive — Draft concentration-change calculation: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

The concentration arithmetic matches the snapshots, but zero-filling requires confirmed snapshot completeness.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F010-R-W12

**Source:** synthetic · **Words:** 12 · **Disposition:** reusable

**Prefix:** Compare 15-litre shoulder bags but compare 30-litre backpacks instead and do not

**Action:** Draft a corrected backpack search

```text
"30 litre" backpack (dimensions OR weight OR review) -"15 litre" -"shoulder bag"
```

**Full instruction:** Compare 15-litre shoulder bags but compare 30-litre backpacks instead and do not include shoulder bags.

**Sufficiency:** substantive — Draft a corrected backpack search: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

The search correctly targets 30-litre backpacks and excludes shoulder bags.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_179-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** I plan to book a flight from Crescent Hollow to New York, aimed at a business endeavor. Utilize

**Action:** Draft flight route discovery query

```text
"Crescent Hollow" "New York" (flight OR airport OR airline) -hotel -cruise
```

**Full instruction:** I plan to book a flight from Crescent Hollow to New York, aimed at a business endeavor. Utilize my typical credit card (ID=card_6789) and access token 'abc123xyz' for the payment. Schedule it for economy class on November 12th 2026, making sure my frequent flyer discount is applied, ensuring the total fee is $850.

**Sufficiency:** substantive — Draft flight route discovery query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

Route discovery survives later fare, date and payment requirements.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_55-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** If the fuel level is lower than 10, then go ahead and add double that amount. Let's assume

**Action:** Draft conditional refueling calculation

```text
def planned_addition(level):
    if level < 0: raise ValueError("fuel level must be nonnegative")
    return 2*level if level < 10 else 0
# Predicted final amount is level + planned_addition(level). Units must match the threshold; this calculates only and operates no vehicle.
```

**Full instruction:** If the fuel level is lower than 10, then go ahead and add double that amount. Let's assume I will also head out right after, so feel free to start the engine using the necessary mode.

**Sufficiency:** substantive — Draft conditional refueling calculation: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

The conditional doubling calculation remains reusable without presuming a current fuel reading.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_163-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** I have to arrange a flight from San Francisco to Los Angeles for my journey next month November

**Action:** Draft November route search

```text
"San Francisco" "Los Angeles" "November" (flight OR airfare) -hotel -cruise
```

**Full instruction:** I have to arrange a flight from San Francisco to Los Angeles for my journey next month November on two days after close of the 14th day in the year 2026. I'll be flying business class, and I'll be settling the payment using my American Express card with id 'AMEX123456789'. Would you be able to take care of this reservation using access token 'abc123xyz' for me? Just make sure I have enough money for the cost of the flight. I have around $8,000.

**Sufficiency:** substantive — Draft November route search: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

November route discovery survives the later exact date and cabin constraints.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_104-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** non_reusable

**Prefix:** I'm interested in keeping up with Lulu Qian and her impressive achievements in the tech world, even if

**Action:** Draft person-specific updates query

```text
"Lulu Qian" (research OR publication OR award OR interview) -"people search" -address
```

**Full instruction:** I'm interested in keeping up with Lulu Qian and her impressive achievements in the tech world, even if it's all a bit over my head! One company I've heard about lately that caught my attention because of its innovative tech solutions is 'Quasar Ltd.'. I've become quite intrigued by what they offer. Could you help me out by finding the current price and trading details for 'Quasar Ltd.'. so I can better understand their market position?

**Sufficiency:** substantive — Draft person-specific updates query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** Y

Person-specific achievement research does not support the eventual Quasar price and trading request.

Substantive preparation requires material replacement or has no established role in the final task.

## CP1-SP1-P-multi_turn_base_120-W12

**Source:** public_bfcl · **Words:** 12 · **Disposition:** reusable

**Prefix:** After confirming the market's operational status, proceed to purchase 100 Apple shares

**Action:** Draft an Apple share cost estimator

```text
def apple_cost(quoted_price):
    if quoted_price <= 0: raise ValueError("Positive quote required")
    return 100 * quoted_price
# Gross estimate for 100 shares; fees omitted; no order submission.
```

**Full instruction:** After confirming the market's operational status, proceed to purchase 100 Apple shares at the prevailing market price.

**Sufficiency:** substantive — Draft an Apple share cost estimator: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The 100-share cost estimator remains useful with a current quote.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F008-R-W18

**Source:** synthetic · **Words:** 18 · **Disposition:** reusable

**Prefix:** Find pharmacies in Brookfield that are open now but only list hospital pharmacies that are closed now and

**Action:** Draft the corrected pharmacy query and filter

```text
Search: "Brookfield" "hospital pharmacy" (hours OR schedule). Retain only hospital pharmacies whose published schedule excludes the relevant local current time; exclude open pharmacies and pharmacies without verifiable hours.
```

**Full instruction:** Find pharmacies in Brookfield that are open now but only list hospital pharmacies that are closed now and open tomorrow.

**Sufficiency:** substantive — Draft the corrected pharmacy query and filter: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** Y

Closed hospital-pharmacy filtering survives adding tomorrow opening verification.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_69-W12

**Source:** public_bfcl · **Words:** 12 · **Disposition:** reusable

**Prefix:** Estimate the distance between San Francisco and Rivermist. Afterwards, fill the tank

**Action:** Draft driving-distance query

```text
"San Francisco" "Rivermist" ("driving distance" OR "road distance") -airfare -flight
```

**Full instruction:** Estimate the distance between San Francisco and Rivermist. Afterwards, fill the tank with 40 additional liters of gasoline for my quick trip. Round the fill amount to two decimal places

**Sufficiency:** substantive — Draft driving-distance query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

Distance discovery remains requested alongside the separate refueling action.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F040-K-W12

**Source:** synthetic · **Words:** 12 · **Disposition:** reusable

**Prefix:** Stage a 70 F thermostat setting for tonight only if the current

**Action:** Draft a thermostat conversion reference

```text
70 °F = (70 − 32) × 5/9 = 21.111… °C, approximately 21.1 °C.
```

**Full instruction:** Stage a 70 F thermostat setting for tonight only if the current setting differs from 70 F; do not apply it.

**Sufficiency:** substantive — Draft a thermostat conversion reference: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

The conversion remains a reusable temperature reference; actual device units and current setting are unknown.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F004-R-W12

**Source:** synthetic · **Words:** 12 · **Disposition:** reusable

**Prefix:** Compare nonstop flights to Eastport but I now want only one-stop itineraries

**Action:** Draft a one-stop itinerary filter

```text
def one_stop_to_eastport(itineraries):
    return [i for i in itineraries if i["destination"] == "Eastport" and len(i["segments"]) == 2 and i["segments"][0]["arrival_airport"] == i["segments"][1]["departure_airport"]]
# Two connected flight segments encode one stop; origin/date remain unspecified.
```

**Full instruction:** Compare nonstop flights to Eastport but I now want only one-stop itineraries to Eastport.

**Sufficiency:** substantive — Draft a one-stop itinerary filter: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The two-connected-segment filter implements the revised one-stop requirement.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_32-W12

**Source:** public_bfcl · **Words:** 12 · **Disposition:** reusable

**Prefix:** I would like to peek the content of 'Spring2023Draft' for review, and

**Action:** Draft a read-only Spring2023Draft preview

```text
from pathlib import Path
p = Path('Spring2023Draft')
if not p.is_file(): raise FileNotFoundError(p)
print(p.read_text())
```

**Full instruction:** I would like to peek the content of 'Spring2023Draft' for review, and could you also provide a comprehensive character count of that same file for thorough assessment?

**Sufficiency:** substantive — Draft a read-only Spring2023Draft preview: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The document read remains useful for preview and later character counting.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_109-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** I heard that the technology sector is booming these days. Get me a list of potential tech stocks

**Action:** Draft technology equity screening rule

```text
Within a verified listed-equity universe, filter sector=Technology; exclude delisted instruments and missing recent filings. Rank candidates separately by revenue growth, operating cash flow margin and debt burden; report valuation alongside each, without collapsing unlike measures into an unexplained score. Record source dates and treat missing data as unknown.
```

**Full instruction:** I heard that the technology sector is booming these days. Get me a list of potential tech stocks I could invest in.

**Sufficiency:** substantive — Draft technology equity screening rule: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The technology screening and separate metric rankings support the requested candidate list.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_34-W12

**Source:** public_bfcl · **Words:** 12 · **Disposition:** reusable

**Prefix:** I'd like to take a look at the finance_report.txt. Would you send

**Action:** Draft local report-read command

```text
if [ -f finance_report.txt ] && [ -r finance_report.txt ]; then
  cat -- finance_report.txt
else
  printf '%s\n' 'Readable finance_report.txt not found' >&2
fi
# Local display only; no send operation.
```

**Full instruction:** I'd like to take a look at the finance_report.txt. Would you send me the content of the last line.

**Sufficiency:** substantive — Draft local report-read command: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

Guarded reading remains reusable with final-line extraction; the entire file need not be shown to the user.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F045-K-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Choose a non-horror movie under two

**Action:** Prepare non-horror movie filter

```text
Given movie metadata, remove entries whose genre tags contain Horror, and hold untagged entries for review. Preserve titles, runtime, and genre evidence for remaining candidates. Do not apply a numeric runtime cutoff until the unit after "two" is known.
```

**Full instruction:** Choose a non-horror movie under two hours for tonight and compare the listed eligible options.

**Sufficiency:** substantive — Prepare non-horror movie filter: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

Non-horror filtering survives adding a two-hour runtime constraint.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F030-K-W12

**Source:** synthetic · **Words:** 12 · **Disposition:** reusable

**Prefix:** Calculate breakeven for my debit spread using the supplied values and use

**Action:** Draft a debit-spread breakeven function

```text
def debit_breakeven(kind, long_strike, debit):
    if debit <= 0: raise ValueError("Debit must be positive")
    if kind == "call": return long_strike + debit
    if kind == "put": return long_strike - debit
    raise ValueError("Expected call or put debit spread")
```

**Full instruction:** Calculate breakeven for my debit spread using the supplied values and use the supplied 5-credit debit and 100-credit lower strike.

**Sufficiency:** substantive — Draft a debit-spread breakeven function: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

The parameterized call/put function survives; spread direction and the put long strike still need specification.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F002-K-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Find hotels near Maple Station and

**Action:** Prepare hotel discovery query

```text
"Maple Station" (hotel OR accommodation) (near OR walking) -jobs -careers
```

**Full instruction:** Find hotels near Maple Station and compare the two listed hotels by walking distance.

**Sufficiency:** substantive — Prepare hotel discovery query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

Hotel discovery near Maple remains reusable for walking-distance comparison.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_127-W6

**Source:** public_bfcl · **Words:** 6 · **Disposition:** non_reusable

**Prefix:** I’m re-evaluating my current investment portfolio

**Action:** Prepare portfolio exposure calculations

```text
For positions with quantity q_i and same-currency price p_i, compute v_i=q_i*p_i, total V=sum(v_i), and weight w_i=v_i/V if V>0. Sum weights by sector and asset class; compute concentration H=sum(w_i**2) and effective holding count 1/H. Report missing prices separately and do not calculate weights from an incomplete total.
```

**Full instruction:** I’m re-evaluating my current investment portfolio and need to make informed decisions. Could you display the current stocks I am monitoring?

**Sufficiency:** substantive — Prepare portfolio exposure calculations: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

Held-position exposure calculations do not produce a list of monitored watchlist stocks.

Substantive preparation requires material replacement or has no established role in the final task.

## CP1-SP1-P-multi_turn_base_131-W12

**Source:** public_bfcl · **Words:** 12 · **Disposition:** reusable

**Prefix:** Could you provide the current time? I need to assess market conditions

**Action:** Draft a timestamp command

```text
python3 -c 'from datetime import datetime, timezone; print(datetime.now(timezone.utc).isoformat()); print(datetime.now().astimezone().isoformat())'
```

**Full instruction:** Could you provide the current time? I need to assess market conditions before proceeding with trades.

**Sufficiency:** substantive — Draft a timestamp command: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

Timezone-aware timestamp preparation directly supports the current-time request.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_189-W12

**Source:** public_bfcl · **Words:** 12 · **Disposition:** reusable

**Prefix:** Planning an incredible journey from NYC to Tokyo on December 24th 2026

**Action:** Draft holiday flight query

```text
("NYC" OR "New York") "Tokyo" "2026-12-24" (flight OR airfare) -hotel
```

**Full instruction:** Planning an incredible journey from NYC to Tokyo on December 24th 2026 in first class! I have my credit card ready with the id card_5678, which is expiring soon, and I'd like to allocate business expenses wisely. The cardholder's name matches mine, Michael Thompson, and I can provide the CVV when needed, which is 456. Just double check how much the flight costs for me and then could you make the booking using access token 'abc123xyz'?

**Sufficiency:** substantive — Draft holiday flight query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

The NYC-Tokyo dated route search survives first-class narrowing.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_30-W12

**Source:** public_bfcl · **Words:** 12 · **Disposition:** unresolved_reuse

**Prefix:** Search for test result of Apollo Project which is supposed to be

**Action:** Draft project-results search

```text
"Apollo Project" ("test result" OR "test results" OR "test report") -jobs -careers
```

**Full instruction:** Search for test result of Apollo Project which is supposed to be in the project directory. It's likely a JSON file. While it's a secret file, please take a look and tell me what's inside.

**Sufficiency:** substantive — Draft project-results search: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** Y

The web-style query is substantive, but no search interface is supplied for the requested local secret file.

Substantive preparation; reuse remains unresolved.

## CP1-SP1-S-SX1-F032-K-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Inspect the client timeout path without

**Action:** Draft a read-only client-timeout inspection search.

```text
Unexecuted search: rg -n -i 'timeout|timed.?out|deadline|ETIMEDOUT|AbortController' <client-source-root>
Trace matches from timeout configuration to request creation, cancellation/error conversion, retry handling, and caller-visible propagation. Check whether retries reuse an exhausted overall deadline and whether cancellation releases timers. Preserve the unfinished without constraint before doing any inspection.
```

**Full instruction:** Inspect the client timeout path without changing the code and identify where its five-second timeout is set.

**Sufficiency:** substantive — Draft a read-only client-timeout inspection search: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

Read-only timeout tracing remains useful to locate the five-second configuration.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F002-R-W12

**Source:** synthetic · **Words:** 12 · **Disposition:** reusable

**Prefix:** Find hotels near Maple Station but use Pine Station instead and omit

**Action:** Draft revised hotel query

```text
"Pine Station" (hotel OR lodging) (near OR walking) -"Maple Station"
```

**Full instruction:** Find hotels near Maple Station but use Pine Station instead and omit Maple Station hotels.

**Sufficiency:** substantive — Draft revised hotel query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

The corrected Pine Station hotel query matches the final location.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_24-W6

**Source:** public_bfcl · **Words:** 6 · **Disposition:** reusable

**Prefix:** Look for draft and final report

**Action:** Draft report-file discovery command

```text
rg --files --hidden -g "!.git" | rg -i "(^|/)[^/]*((draft|final)[^/]*report|report[^/]*(draft|final))[^/]*$"
```

**Full instruction:** Look for draft and final report in my current directory. Compare the content difference of both.

**Sufficiency:** substantive — Draft report-file discovery command: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

Draft/final report discovery remains useful before comparing contents.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F012-K-W12

**Source:** synthetic · **Words:** 12 · **Disposition:** reusable

**Prefix:** Compare robotics synthetic-data tools that support Engine R and keep Engine R

**Action:** Draft Engine R tool-discovery query

```text
"Engine R" ("synthetic data" OR "synthetic-data") robotics (tool OR integration OR documentation) -jobs
```

**Full instruction:** Compare robotics synthetic-data tools that support Engine R and keep Engine R support mandatory.

**Sufficiency:** substantive — Draft Engine R tool-discovery query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

Engine R integration discovery supports mandatory Engine R compatibility.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F008-K-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Find pharmacies in Brookfield that are

**Action:** Prepare pharmacy location discovery for Brookfield.

```text
Unsubmitted query: (pharmacy OR pharmacies) "Brookfield" (address OR location OR hours) -jobs -careers. Confirm which Brookfield and the unfinished qualifying condition before filtering candidates or making a recommendation.
```

**Full instruction:** Find pharmacies in Brookfield that are open now and omit hospital-based pharmacies.

**Sufficiency:** substantive — Prepare pharmacy location discovery for Brookfield: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

Broad pharmacy discovery can be filtered for open non-hospital pharmacies.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F048-R-W18

**Source:** synthetic · **Words:** 18 · **Disposition:** reusable

**Prefix:** Plan my morning around a 9 AM appointment but move the appointment to 11 AM while retaining the

**Action:** Draft a revised appointment-centered morning

```text
09:00–10:00: Keep available for personal preparation.
10:00–11:00: Reserve as a flexible preparation/travel buffer; actual travel duration is not supplied.
11:00: Appointment (revised from 09:00).
```

**Full instruction:** Plan my morning around a 9 AM appointment but move the appointment to 11 AM while retaining the 30-minute travel requirement.

**Sufficiency:** substantive — Draft a revised appointment-centered morning: concrete draft content establishes preparation beyond copied inputs.

**Ambiguity:** Y

The 11 AM plan and hour buffer can accommodate the specified 30-minute journey.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_130-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** Having established the market scenario, imagine you're poised to place an order to acquire 150 shares of 'NEPT'

**Action:** Draft an order-notional calculator

```text
def nept_notional(price_per_share):
    if price_per_share <= 0: raise ValueError("Positive quoted price required")
    return 150 * price_per_share
# Estimate only; excludes fees and submits no order.
```

**Full instruction:** Having established the market scenario, imagine you're poised to place an order to acquire 150 shares of 'NEPT' at 25.50 USD per share. Would you initiate this order for me?

**Sufficiency:** substantive — Draft an order-notional calculator: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The 150-share notional function survives binding the 25.50-dollar price.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_137-W12

**Source:** public_bfcl · **Words:** 12 · **Disposition:** reusable

**Prefix:** I reckon it's about time to track Zeta Corp's stock performance closely,

**Action:** Draft performance-source query

```text
"Zeta Corp" ("historical prices" OR "investor relations" OR "stock quote") -rumor -forum
```

**Full instruction:** I reckon it's about time to track Zeta Corp's stock performance closely, so it'd be great if you could add it to my watchlist, please.

**Sufficiency:** substantive — Draft performance-source query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

Issuer and quote-source discovery can resolve the watchlist instrument.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F032-R-W18

**Source:** synthetic · **Words:** 18 · **Disposition:** reusable

**Prefix:** Inspect the client timeout path without changing the code but modify the default timeout to ten seconds instead

**Action:** Draft a timeout-change inspection query

```text
rg -n -i 'timeout|time_out|request_timeout' --glob '*client*' --glob '!*.lock' .
```

**Full instruction:** Inspect the client timeout path without changing the code but modify the default timeout to ten seconds instead of producing an inspection report.

**Sufficiency:** substantive — Draft a timeout-change inspection query: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

Timeout configuration discovery remains necessary before changing the default.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_168-W12

**Source:** public_bfcl · **Words:** 12 · **Disposition:** reusable

**Prefix:** Calculate the exchange rate for 1500 USD to EUR for me, I

**Action:** Draft exchange conversion calculation

```text
Given a verified rate r EUR per USD, gross proceeds = 1500*r EUR. If percentage fee p and fixed EUR fee f apply, net = 1500*r*(1-p)-f. If rate is quoted as USD per EUR, use r=1/quote. Store quote timestamp; do not present an unverified numeric rate.
```

**Full instruction:** Calculate the exchange rate for 1500 USD to EUR for me, I have some funds to convert quickly.

**Sufficiency:** substantive — Draft exchange conversion calculation: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The rate-direction and fee-aware EUR conversion formulas remain applicable.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_18-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** Copy all the text files of the 'Quarter1_Reports' directory and place it in a new directory naming it

**Action:** Draft non-overwriting text-copy algorithm

```text
For each immediate regular file in Quarter1_Reports whose suffix is .txt, add (source, NEW_DIRECTORY/source.name) to a copy plan. Reject a destination equal to the source directory or any existing target. Create the new destination only when its name is resolved; copy metadata and bytes, verify byte equality, retain all originals. No operations executed.
```

**Full instruction:** Copy all the text files of the 'Quarter1_Reports' directory and place it in a new directory naming it 'Archived_Quarter1.

**Sufficiency:** substantive — Draft non-overwriting text-copy algorithm: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The non-overwriting copy algorithm survives binding Archived_Quarter1.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F005-R-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** non_reusable

**Prefix:** Find Italian restaurants around Cedar Square

**Action:** Prepare restaurant discovery query

```text
"Cedar Square" ("Italian restaurant" OR trattoria OR osteria) -jobs -careers
```

**Full instruction:** Find Italian restaurants around Cedar Square but change the cuisine to Thai and exclude Italian restaurants.

**Sufficiency:** substantive — Prepare restaurant discovery query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

Italian-specific discovery is excluded by the Thai-only correction.

Substantive preparation requires material replacement or has no established role in the final task.

## CP1-SP1-S-SX1-F010-R-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Compare 15-litre shoulder bags but compare

**Action:** Prepare bag comparison normalization

```text
Retain documented 15 L shoulder bags. Normalize dimensions to cm and empty weight to g; preserve source currency for prices. Compare capacity, closure, strap adjustability, empty weight, and price only where values are documented; distinguish unavailable values from zero and refrain from aggregate ranking until comparison constraints arrive.
```

**Full instruction:** Compare 15-litre shoulder bags but compare 30-litre backpacks instead and do not include shoulder bags.

**Sufficiency:** substantive — Prepare bag comparison normalization: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

The unexecuted normalization and comparison protocol survives substituting backpack capacity and carry type.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F007-R-W18

**Source:** synthetic · **Words:** 18 · **Disposition:** reusable

**Prefix:** Find gyms in Riverton that sell day passes but only consider members-only gyms that do not sell day

**Action:** Draft the corrected gym search

```text
"Riverton" gym ("members only" OR "membership required") ("no day passes" OR "day passes not available")
```

**Full instruction:** Find gyms in Riverton that sell day passes but only consider members-only gyms that do not sell day passes.

**Sufficiency:** substantive — Draft the corrected gym search: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

The revised query seeks members-only gyms without day passes.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F022-R-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** non_reusable

**Prefix:** Find peer-reviewed papers about hidden-state probing

**Action:** Prepare literature queries and a publication-status filter.

```text
Unsubmitted queries: ("hidden-state probing" OR "hidden state probing" OR "probing hidden representations") ("language model" OR "neural network") (proceedings OR journal); ("probing classifiers" OR "diagnostic classifiers") ("hidden states" OR representations) (ACL OR EMNLP OR ICLR). For each candidate, verify an actual journal or conference publication record; an arXiv listing alone does not establish peer review.
```

**Full instruction:** Find peer-reviewed papers about hidden-state probing but use only non-peer-reviewed technical reports about hidden-state probing.

**Sufficiency:** substantive — Prepare literature queries and a publication-status filter: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** Y

The required peer-reviewed publication filter conflicts with technical-report-only selection; topic expressions survive.

Substantive preparation requires material replacement or has no established role in the final task.

## CP1-SP1-S-SX1-F009-R-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** non_reusable

**Prefix:** Research local robotic actuator manufacturers but

**Action:** Prepare manufacturer discovery query

```text
("robotic actuator" OR "robotics actuator") (manufacturer OR factory) -distributor -reseller
```

**Full instruction:** Research local robotic actuator manufacturers but list distributors only and exclude manufacturers.

**Sufficiency:** substantive — Prepare manufacturer discovery query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

Manufacturer-only discovery explicitly excludes the now-required distributors.

Substantive preparation requires material replacement or has no established role in the final task.

## CP1-SP1-S-SX1-F026-R-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Compare small open-weight reasoning models but

**Action:** Draft an open-weight reasoning-model comparison protocol.

```text
For each eventual small-model candidate, verify downloadable weights and license terms, parameter count and architecture, quantized memory needs, and maximum supported context from its model card. Compare on the same task set with fixed prompt, sampling settings, and output-token budget; report accuracy alongside latency and output length so extra reasoning tokens do not hide compute costs. Treat the missing but clause as unresolved before selecting candidates.
```

**Full instruction:** Compare small open-weight reasoning models but include only independently reproduced scores and omit vendor-only claims entirely.

**Sufficiency:** substantive — Draft an open-weight reasoning-model comparison protocol: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The controlled comparison protocol survives requiring independently reproduced scores.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F020-R-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** non_reusable

**Prefix:** Draft a message declining dinner tonight

**Action:** Draft dinner-decline message

```text
Thanks for inviting me to dinner tonight. I won’t be able to make it, but I appreciate the invitation. I hope you have a lovely evening.
```

**Full instruction:** Draft a message declining dinner tonight but accept dinner tonight instead and do not suggest another date.

**Sufficiency:** substantive — Draft dinner-decline message: concrete draft content establishes preparation beyond copied inputs.

**Ambiguity:** N

The refusal must be replaced by acceptance, though a thank-you phrase survives.

Substantive preparation requires material replacement or has no established role in the final task.

## CP1-SP1-P-multi_turn_base_92-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** Could you provide me with a rough distance from Rivermist (zip 83214) to Greenway (zip 74532)? I'm eager

**Action:** Draft zip-constrained route query

```text
"Rivermist" "83214" "Greenway" "74532" ("driving distance" OR route)
```

**Full instruction:** Could you provide me with a rough distance from Rivermist (zip 83214) to Greenway (zip 74532)? I'm eager to plan a visit and need to know the travel distance.

**Sufficiency:** substantive — Draft zip-constrained route query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

The zip-constrained route search directly supports the distance estimate.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_132-W12

**Source:** public_bfcl · **Words:** 12 · **Disposition:** reusable

**Prefix:** I need details on the performance of a particular stock, 'SYNX', can

**Action:** Draft a security-performance source query

```text
"SYNX" ("stock performance" OR "historical prices") (exchange OR "investor relations")
```

**Full instruction:** I need details on the performance of a particular stock, 'SYNX', can you provide me with the critical information? It should be added to my watchlist.

**Sufficiency:** substantive — Draft a security-performance source query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

Security-performance discovery remains requested before watchlist addition.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_174-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** I'm organizing a trip from San Francisco to Rome on October 10th 2026 and considering to fly business

**Action:** Draft a dated business-class flight query

```text
("San Francisco" OR SFO) (Rome OR FCO) "October 10 2026" "business class" flights
```

**Full instruction:** I'm organizing a trip from San Francisco to Rome on October 10th 2026 and considering to fly business class. Secure a flight reservation that aligns with my financial constraints using my card with id card_7243 and access token 'abc123xyz'. Be sure to convert the ticket cost to EUR for an accurate currency reference.

**Sufficiency:** substantive — Draft a dated business-class flight query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

The dated business-class route query survives currency and funding checks.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_11-W12

**Source:** public_bfcl · **Words:** 12 · **Disposition:** reusable

**Prefix:** Display all the available files located within the '/temp' directory including hidden

**Action:** Draft hidden-inclusive file listing

```text
find /temp -mindepth 1 -maxdepth 1 -type f -print
# Includes hidden regular files and does not recurse or modify entries.
```

**Full instruction:** Display all the available files located within the '/temp' directory including hidden one using the terminal interface .

**Sufficiency:** substantive — Draft hidden-inclusive file listing: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The exact /temp hidden-inclusive regular-file listing matches the request.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_89-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** I'm planning a road trip from Rivermist to Stonebrook and would love an estimate on how far this

**Action:** Draft a road-distance query

```text
"Rivermist" "Stonebrook" ("driving distance" OR "road distance") (miles OR kilometers)
```

**Full instruction:** I'm planning a road trip from Rivermist to Stonebrook and would love an estimate on how far this journey will take me.

**Sufficiency:** substantive — Draft a road-distance query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

The route-distance query addresses the unchanged road trip.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_180-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** non_reusable

**Prefix:** I need to cap my travel expenses at 20,000 RMB. Sort out everything to make sure this limit

**Action:** Draft travel budget constraint

```text
Let confirmed transport, lodging, meals, local travel and fees be T,L,M,G,F in RMB. Remaining budget = 20000-(T+L+M+G+F). Accept a plan only when every component is priced and remaining budget >= 0; rank feasible substitutions by savings and retain an explicit unpriced status for missing costs.
```

**Full instruction:** I need to cap my travel expenses at 20,000 RMB. Sort out everything to make sure this limit is correctly set up. Around it to have tenth and hundredth digit. Like 12.34 as the input. My access token is abc123xyz if you need.

**Sufficiency:** substantive — Draft travel budget constraint: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

Expense optimization does not implement setting a budget limit formatted to two decimals; the ceiling value survives.

Substantive preparation requires material replacement or has no established role in the final task.

## CP1-SP1-P-multi_turn_base_20-W6

**Source:** public_bfcl · **Words:** 6 · **Disposition:** reusable

**Prefix:** Go to documents folder in CWD.

**Action:** Draft guarded directory navigation command

```text
target="$PWD/documents"; if [ -d "$target" ]; then cd -- "$target" && pwd; else printf "%s\n" "documents directory absent" >&2; fi
```

**Full instruction:** Go to documents folder in CWD. Next, from the first document in current folder. What does the last line look like?

**Sufficiency:** substantive — Draft guarded directory navigation command: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

Guarded documents navigation remains needed before reading the first document.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F019-R-W18

**Source:** synthetic · **Words:** 18 · **Disposition:** reusable

**Prefix:** Draft a team update saying the build is delayed but the build is on schedule, so report that

**Action:** Draft the corrected build-status update

```text
Team, the build is on schedule. We are continuing against the planned timeline.
```

**Full instruction:** Draft a team update saying the build is delayed but the build is on schedule, so report that and do not mention a delay.

**Sufficiency:** substantive — Draft the corrected build-status update: concrete draft content establishes preparation beyond copied inputs.

**Ambiguity:** N

The corrected update reports on-schedule status without mentioning delay.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_136-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** Give me an update on where Zeta Corp's stock stands right now and proceed with purchasing 50 shares

**Action:** Draft purchase cost and validation rule

```text
Unsubmitted intent: buy 50 shares of Zeta Corp. Resolve the exact listed instrument before attaching a quote. Record quote timestamp and currency; calculate estimated debit = 50*price + fees. Do not generate an executable order until instrument, order type and funding are resolved.
```

**Full instruction:** Give me an update on where Zeta Corp's stock stands right now and proceed with purchasing 50 shares at the ongoing rate.

**Sufficiency:** substantive — Draft purchase cost and validation rule: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

Instrument validation and the 50-share debit formula support the requested market-rate purchase.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F049-R-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** non_reusable

**Prefix:** Build a shopping list for vegetarian

**Action:** Draft vegetarian shopping-list candidate

```text
Candidate staples: lentils, chickpeas, tofu, brown rice, oats, whole-grain bread, spinach, broccoli, carrots, tomatoes, onions, fruit, olive oil, and nuts or seeds. Group legumes/tofu together as protein sources, rice/oats/bread as grains, and vegetables/fruit as produce; quantities depend on meals and servings.
```

**Full instruction:** Build a shopping list for vegetarian tacos but make beef tacos instead and omit beans.

**Sufficiency:** substantive — Draft vegetarian shopping-list candidate: concrete draft content establishes preparation beyond copied inputs.

**Ambiguity:** Y

Vegetarian staples require substantial replacement for beef tacos, though some produce remains useful.

Substantive preparation requires material replacement or has no established role in the final task.

## CP1-SP1-P-multi_turn_base_171-W6

**Source:** public_bfcl · **Words:** 6 · **Disposition:** non_reusable

**Prefix:** I'm planning an expedition to Beijing

**Action:** Prepare Beijing trip research query

```text
("Beijing" OR "北京") ("visitor guide" OR "getting around") ("official" OR "tourism")
```

**Full instruction:** I'm planning an expedition to Beijing and I want to ensure my financial strategy is well-prepared for the adventure. Budget me sufficiently to meet the target of 10000 RMB and ensure the flight cost checks out to be under my budget? Thanks! Now, let's arrange for a luxurious first-class flight from JFK to Beijing Capital Airport for June 15th 2026 utilizing my primary card with id 'card_8283'. Oh, and here's my access code 897362.

**Sufficiency:** substantive — Prepare Beijing trip research query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** Y

Beijing visitor-guide discovery does not establish flight pricing or the specified budget; incidental travel context is marginal.

Substantive preparation requires material replacement or has no established role in the final task.

## CP1-SP1-S-SX1-F046-K-W12

**Source:** synthetic · **Words:** 12 · **Disposition:** reusable

**Prefix:** Find technical podcast interviews about AI agents and favor interviews over news

**Action:** Draft interview-focused podcast search

```text
"AI agents" podcast (interview OR "in conversation") (technical OR engineering) -"news roundup"
```

**Full instruction:** Find technical podcast interviews about AI agents and favor interviews over news roundups.

**Sufficiency:** substantive — Draft interview-focused podcast search: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

The interview-focused technical podcast query matches the preference.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F040-K-W18

**Source:** synthetic · **Words:** 18 · **Disposition:** reusable

**Prefix:** Stage a 70 F thermostat setting for tonight only if the current setting differs from 70 F; do

**Action:** Draft thermostat staging logic

```text
def stage_tonight(current_f):
    if current_f is None: return {"status": "needs_current_setting"}
    if current_f == 70: return {"status": "no_change"}
    return {"status": "draft", "target_f": 70, "scope": "tonight", "restore_f": current_f}
# Local plan only; no device calls.
```

**Full instruction:** Stage a 70 F thermostat setting for tonight only if the current setting differs from 70 F; do not apply it.

**Sufficiency:** substantive — Draft thermostat staging logic: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The staging function handles unknown/current-equal settings and leaves the change unsubmitted.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_99-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** I'm planning a road trip to the Grand Canyon and need to drive a distance of 380 miles.

**Action:** Draft fuel calculation for stated distance

```text
For 380 miles and economy e miles/gallon, required fuel = 380/e gallons (e>0). With current fuel f gallons, additional fuel = max(0,380/e-f). No numeric fuel quantity can be concluded until economy and current fuel are supplied.
```

**Full instruction:** I'm planning a road trip to the Grand Canyon and need to drive a distance of 380 miles. You could assist me in determining whether my vehicle has sufficient fuel for this journey, please? If it is not sufficient, fill the fuel tank completely.

**Sufficiency:** substantive — Draft fuel calculation for stated distance: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The 380-mile sufficiency formula evaluates the condition before any full-tank fill.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F042-R-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Stage a kitchen-only vacuum run but

**Action:** Draft kitchen-only run staging logic

```text
Resolve the exact kitchen room label to one unique map room ID. If missing or ambiguous, return no candidate. Otherwise construct an unsubmitted plan {operation: vacuum, room_ids: [kitchen_id]}; reject any plan that contains additional room IDs or whole-home scope. Preserve this as a preview pending the unfinished constraint.
```

**Full instruction:** Stage a kitchen-only vacuum run but stage a bedroom-only run instead and discard the kitchen plan.

**Sufficiency:** substantive — Draft kitchen-only run staging logic: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

The unexecuted unique-room and single-room staging logic survives substituting bedroom for kitchen.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_119-W12

**Source:** public_bfcl · **Words:** 12 · **Disposition:** reusable

**Prefix:** Could you provide me with the latest stock information for Zeta Corp,

**Action:** Draft a current-stock source query

```text
"Zeta Corp" ("stock quote" OR "investor relations") (exchange OR ticker)
```

**Full instruction:** Could you provide me with the latest stock information for Zeta Corp, including its current price and the performance metrics?

**Sufficiency:** substantive — Draft a current-stock source query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

Issuer and quote discovery support current Zeta price and performance reporting.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F050-R-W18

**Source:** synthetic · **Words:** 18 · **Disposition:** reusable

**Prefix:** Prioritize today's tasks with the client deadline first but put the server incident first and move the client

**Action:** Draft partial task-priority rule

```text
Place the server incident first. Order remaining tasks by earliest hard deadline, using dependency prerequisites before blocked work. Put the client deadline task after the incident; do not assign its final rank until the unfinished move instruction is resolved.
```

**Full instruction:** Prioritize today's tasks with the client deadline first but put the server incident first and move the client deadline below it.

**Sufficiency:** substantive — Draft partial task-priority rule: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The priority rule already puts the incident ahead of the client deadline.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_155-W12

**Source:** public_bfcl · **Words:** 12 · **Disposition:** reusable

**Prefix:** I'm planning to fly from LAX to JFK on November 15th 2026

**Action:** Draft a dated airport-route search

```text
"LAX" "JFK" "November 15 2026" (flight OR schedule)
```

**Full instruction:** I'm planning to fly from LAX to JFK on November 15th 2026 and aim to travel in business class with a budget of $2400. Could you please book a seat for this flight? I'll be using my access token 'abc123xyz' and Mastercard with id 'id15583' for payment.

**Sufficiency:** substantive — Draft a dated airport-route search: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

The dated LAX-JFK search remains reusable under business-class and budget constraints.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_134-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** I'm keen to gather comprehensive insights regarding a company trading under 'Quasar Ltd.'. Specifically, I'm looking for its

**Action:** Draft a company-source search query

```text
"Quasar Ltd." ("annual report" OR "investor relations" OR "stock exchange")
```

**Full instruction:** I'm keen to gather comprehensive insights regarding a company trading under 'Quasar Ltd.'. Specifically, I'm looking for its up-to-the-minute stock price, crucial market performance metrics, and the volume of its recent trading activities. Once you have that sorted out, kindly include this company on my watchlist.

**Sufficiency:** substantive — Draft a company-source search query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

Issuer and exchange discovery support the quote, trading metrics and instrument identity.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_14-W6

**Source:** public_bfcl · **Words:** 6 · **Disposition:** reusable

**Prefix:** First cd within the 'ResearchDocs' directory

**Action:** Draft guarded ResearchDocs navigation

```text
if [ -d ./ResearchDocs ]; then cd -- ./ResearchDocs && pwd; else printf "%s\n" "ResearchDocs directory absent" >&2; fi
```

**Full instruction:** First cd within the 'ResearchDocs' directory and then locate any files titled 'report.csv'.

**Sufficiency:** substantive — Draft guarded ResearchDocs navigation: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

ResearchDocs navigation remains the required first step before report.csv discovery.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_29-W12

**Source:** public_bfcl · **Words:** 12 · **Disposition:** reusable

**Prefix:** Open up 'VisionX' folder. What's the human readible disk usage of that

**Action:** Draft human-readable directory usage command

```text
if [ -d VisionX ]; then
  (cd -- VisionX && du -sh .)
else
  printf '%s\n' 'VisionX directory not found' >&2
fi
```

**Full instruction:** Open up 'VisionX' folder. What's the human readible disk usage of that folder?

**Sufficiency:** substantive — Draft human-readable directory usage command: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The guarded du command computes the requested human-readable VisionX usage.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_189-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** Planning an incredible journey from NYC to Tokyo on December 24th 2026 in first class! I have my

**Action:** Draft first-class route search

```text
("NYC" OR "New York") "Tokyo" "2026-12-24" "first class" (flight OR fare) -hotel
```

**Full instruction:** Planning an incredible journey from NYC to Tokyo on December 24th 2026 in first class! I have my credit card ready with the id card_5678, which is expiring soon, and I'd like to allocate business expenses wisely. The cardholder's name matches mine, Michael Thompson, and I can provide the CVV when needed, which is 456. Just double check how much the flight costs for me and then could you make the booking using access token 'abc123xyz'?

**Sufficiency:** substantive — Draft first-class route search: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

The route, date and first-class fare query remain aligned with booking preparation.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_1-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** I am alex. Check if the current directory is under my name and list all the visible and

**Action:** Draft a directory-name check and inventory

```text
from pathlib import Path
p = Path.cwd()
print({'directory': str(p), 'leaf_name_matches_alex': p.name.casefold() == 'alex', 'has_alex_ancestor': any(x.name.casefold() == 'alex' for x in p.parents)})
for child in sorted(p.iterdir()): print(child.name)
# Name checks do not establish filesystem ownership.
```

**Full instruction:** I am alex. Check if the current directory is under my name and list all the visible and hidden contents in the current directory now, please.

**Sufficiency:** substantive — Draft a directory-name check and inventory: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

Path-name checks and hidden-inclusive inventory survive; account ownership is not established by names.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_163-W12

**Source:** public_bfcl · **Words:** 12 · **Disposition:** reusable

**Prefix:** I have to arrange a flight from San Francisco to Los Angeles

**Action:** Draft route discovery query

```text
"San Francisco" "Los Angeles" ("nonstop flight" OR "flight schedule") -hotel -cruise
```

**Full instruction:** I have to arrange a flight from San Francisco to Los Angeles for my journey next month November on two days after close of the 14th day in the year 2026. I'll be flying business class, and I'll be settling the payment using my American Express card with id 'AMEX123456789'. Would you be able to take care of this reservation using access token 'abc123xyz' for me? Just make sure I have enough money for the cost of the flight. I have around $8,000.

**Sufficiency:** substantive — Draft route discovery query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

The route and schedule query remains reusable with the later date and cabin.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_40-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** Arrange a complete listing of all files and directories presently located here, making sure you don't overlook the

**Action:** Draft a full current-directory inventory

```text
find . -mindepth 1 -maxdepth 1 -print | sort
```

**Full instruction:** Arrange a complete listing of all files and directories presently located here, making sure you don't overlook the hidden ones too.

**Sufficiency:** substantive — Draft a full current-directory inventory: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

The hidden-inclusive current-directory inventory exactly matches the request.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_156-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** I'm planning to fly from San Francisco to Los Angeles on October 15, 2026. Could you assist in

**Action:** Draft dated route query

```text
"San Francisco" "Los Angeles" "2026-10-15" (flight OR fare) -hotel -cruise
```

**Full instruction:** I'm planning to fly from San Francisco to Los Angeles on October 15, 2026. Could you assist in securing a first-class seat using my travel card with id 'travel_card_12345'? Everything you need—access token (abc123xyz456), traveler details—are at the ready. Just make sure that I can afford it because I only have 6000 dollars to spend for this flight.

**Sufficiency:** substantive — Draft dated route query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

The dated route query remains reusable before first-class affordability checks.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F030-R-W18

**Source:** synthetic · **Words:** 18 · **Disposition:** reusable

**Prefix:** Calculate breakeven for my debit spread using the supplied values but correct the debit to 8 credits while

**Action:** Draft the corrected debit calculation

```text
def corrected_breakeven(kind, long_strike):
    if kind == "call": return long_strike + 8
    if kind == "put": return long_strike - 8
    raise ValueError("Specify call or put debit spread")
```

**Full instruction:** Calculate breakeven for my debit spread using the supplied values but correct the debit to 8 credits while keeping the lower strike at 100 credits.

**Sufficiency:** substantive — Draft the corrected debit calculation: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** Y

The corrected eight-credit function survives, while spread direction and relevant long strike remain unspecified.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_199-W12

**Source:** public_bfcl · **Words:** 12 · **Disposition:** reusable

**Prefix:** I'm planning a journey from Los Angeles to New York on the

**Action:** Draft route search

```text
"Los Angeles" "New York" ("nonstop flight" OR "flight schedule") -hotel -cruise
```

**Full instruction:** I'm planning a journey from Los Angeles to New York on the morning of April 15th 2026, preferring to fly business class. Check the flight cost and then please arrange this flight using my pre-linked credit card with id 'card_123456789' and access token 'abc123xyz'.

**Sufficiency:** substantive — Draft route search: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

Los Angeles-New York schedule discovery survives date, morning and cabin narrowing.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_62-W18

**Source:** public_bfcl · **Words:** 18 · **Disposition:** reusable

**Prefix:** I'm currently in Rivermist planning a trip to Stonebrook. Could you provide an estimate of the distance and

**Action:** Draft road-distance discovery query

```text
"Rivermist" "Stonebrook" ("driving distance" OR "road distance") -flight -airfare
```

**Full instruction:** I'm currently in Rivermist planning a trip to Stonebrook. Could you provide an estimate of the distance and forward this info to my cousin Bob via text, in the format 'The distance from Rivermist to Stonebrook is xxx km.', where xxx is replaced by the distance value, in one decimal place)?

**Sufficiency:** substantive — Draft road-distance discovery query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** N

Distance discovery remains necessary before formatting and texting the route information.

Substantive preparation survives without material re-execution.

## CP1-SP1-S-SX1-F042-K-W6

**Source:** synthetic · **Words:** 6 · **Disposition:** reusable

**Prefix:** Stage a kitchen-only vacuum run and

**Action:** Draft kitchen-only vacuum staging logic.

```text
Unexecuted staging algorithm: look up the mapped room whose verified label is kitchen; require exactly one matching room ID; construct a draft cleaning target containing only that ID; reject any whole-home flag or additional room target; keep the run unsent. If mapping is missing or ambiguous, return no staged target. The trailing and may add another constraint.
```

**Full instruction:** Stage a kitchen-only vacuum run and keep all other rooms excluded; do not start cleaning.

**Sufficiency:** substantive — Draft kitchen-only vacuum staging logic: concrete operational logic establishes preparation beyond copied inputs.

**Ambiguity:** N

Unique kitchen-room staging already enforces unsent kitchen-only scope.

Substantive preparation survives without material re-execution.

## CP1-SP1-P-multi_turn_base_106-W6

**Source:** public_bfcl · **Words:** 6 · **Disposition:** unresolved_reuse

**Prefix:** I'm looking into investing in technology

**Action:** Prepare a technology-investment research query.

```text
Unsubmitted query: ("technology sector" OR "information technology") ("annual report" OR "10-K") ("risk factors" OR "segment revenue") -"stock picks" -"get rich". Use the resulting filings for exposure and risk research; this supplies no investment recommendation.
```

**Full instruction:** I'm looking into investing in technology stocks and I'm drawn to the company with the ticker AAPL. Could you get its present stock performance for me and proceed with purchasing 100 shares at the prevailing market rate?

**Sufficiency:** substantive — Prepare a technology-investment research query: concrete query construction establishes preparation beyond copied inputs.

**Ambiguity:** Y

Broad sector filing research might help, but no supplied results establish reuse for current AAPL performance and purchase.

Substantive preparation; reuse remains unresolved.

# Boundary diagnostics

## BOUNDARY-015

**Source:** public_bfcl · **Words:** 6 · **Disposition:** invalid_candidate

**Prefix:** I'm looking into investing in technology

**Action:** List unresolved fields for later filling.

```text
{"target":null,"operation":null,"arguments":null,"result":null}
```

**Full instruction:** I'm looking into investing in technology stocks and I'm drawn to the company with the ticker AAPL. Could you get its present stock performance for me and proceed with purchasing 100 shares at the prevailing market rate?

**Sufficiency:** no_material_work — All fields are null, so no work unit is established.

**Ambiguity:** N

All fields are null, so no work unit is established.

No established work unit; survival utility is not scored.

## BOUNDARY-012

**Source:** public_bfcl · **Words:** 18 · **Disposition:** invalid_candidate

**Prefix:** I am alex. Check if the current directory is under my name and list all the visible and

**Action:** Write a generic task checklist.

```text
1. Identify the task.
2. Collect missing details.
3. Complete the task.
```

**Full instruction:** I am alex. Check if the current directory is under my name and list all the visible and hidden contents in the current directory now, please.

**Sufficiency:** no_material_work — The generic three-step checklist performs no task-specific preparation.

**Ambiguity:** N

The generic three-step checklist performs no task-specific preparation.

No established work unit; survival utility is not scored.

## BOUNDARY-018

**Source:** synthetic · **Words:** 6 · **Disposition:** invalid_candidate

**Prefix:** Draft a refund approval message and

**Action:** Prepare an empty results table.

```text
| Item | Result |
|---|---|
| | |
```

**Full instruction:** Draft a refund approval message and avoid promising a payment date.

**Sufficiency:** no_material_work — An empty results table contains no refund wording or operation.

**Ambiguity:** N

An empty results table contains no refund wording or operation.

No established work unit; survival utility is not scored.

## BOUNDARY-005

**Source:** synthetic · **Words:** 18 · **Disposition:** invalid_candidate

**Prefix:** Draft a team update saying the build is delayed but the build is on schedule, so report that

**Action:** Copy the observed instruction into a note.

```text
Draft a team update saying the build is delayed but the build is on schedule, so report that
```

**Full instruction:** Draft a team update saying the build is delayed but the build is on schedule, so report that and do not mention a delay.

**Sufficiency:** no_material_work — The note only copies the partial instruction.

**Ambiguity:** N

The note only copies the partial instruction.

No established work unit; survival utility is not scored.

## BOUNDARY-011

**Source:** synthetic · **Words:** 6 · **Disposition:** invalid_candidate

**Prefix:** Find hotels near Maple Station and

**Action:** List unresolved fields for later filling.

```text
{"target":null,"operation":null,"arguments":null,"result":null}
```

**Full instruction:** Find hotels near Maple Station and compare the two listed hotels by walking distance.

**Sufficiency:** no_material_work — Null slots contain no hotel discovery or comparison work.

**Ambiguity:** N

Null slots contain no hotel discovery or comparison work.

No established work unit; survival utility is not scored.

## BOUNDARY-006

**Source:** synthetic · **Words:** 12 · **Disposition:** invalid_candidate

**Prefix:** Stage a kitchen-only vacuum run and keep all other rooms excluded; do

**Action:** Prepare an empty results table.

```text
| Item | Result |
|---|---|
| | |
```

**Full instruction:** Stage a kitchen-only vacuum run and keep all other rooms excluded; do not start cleaning.

**Sufficiency:** no_material_work — The empty table contains no vacuum staging logic.

**Ambiguity:** N

The empty table contains no vacuum staging logic.

No established work unit; survival utility is not scored.

## BOUNDARY-007

**Source:** synthetic · **Words:** 6 · **Disposition:** invalid_candidate

**Prefix:** Compare nonstop flights to Eastport and

**Action:** List unresolved fields for later filling.

```text
{"target":null,"operation":null,"arguments":null,"result":null}
```

**Full instruction:** Compare nonstop flights to Eastport and list only nonstop itineraries.

**Sufficiency:** no_material_work — Null slots establish no flight comparison artifact.

**Ambiguity:** N

Null slots establish no flight comparison artifact.

No established work unit; survival utility is not scored.

## BOUNDARY-014

**Source:** synthetic · **Words:** 12 · **Disposition:** invalid_candidate

**Prefix:** Find hotels near Maple Station but use Pine Station instead and omit

**Action:** Prepare an empty results table.

```text
| Item | Result |
|---|---|
| | |
```

**Full instruction:** Find hotels near Maple Station but use Pine Station instead and omit Maple Station hotels.

**Sufficiency:** no_material_work — The empty hotel table contains no discovery or transformation.

**Ambiguity:** N

The empty hotel table contains no discovery or transformation.

No established work unit; survival utility is not scored.

## BOUNDARY-010

**Source:** public_bfcl · **Words:** 18 · **Disposition:** invalid_candidate

**Prefix:** I'm planning a road trip from Rivermist to Stonebrook and would love an estimate on how far this

**Action:** Prepare an empty results table.

```text
| Item | Result |
|---|---|
| | |
```

**Full instruction:** I'm planning a road trip from Rivermist to Stonebrook and would love an estimate on how far this journey will take me.

**Sufficiency:** no_material_work — An empty table performs no distance preparation.

**Ambiguity:** N

An empty table performs no distance preparation.

No established work unit; survival utility is not scored.

## BOUNDARY-017

**Source:** public_bfcl · **Words:** 18 · **Disposition:** invalid_candidate

**Prefix:** I'm contemplating enhancing my investment portfolio with some tech industry assets, and I've got my eye on Nvidia.

**Action:** Copy the observed instruction into a note.

```text
I'm contemplating enhancing my investment portfolio with some tech industry assets, and I've got my eye on Nvidia.
```

**Full instruction:** I'm contemplating enhancing my investment portfolio with some tech industry assets, and I've got my eye on Nvidia. I'm keen to know its current stock price, and would appreciate if you could source this information for me.

**Sufficiency:** no_material_work — The note repeats the prefix without creating research work.

**Ambiguity:** N

The note repeats the prefix without creating research work.

No established work unit; survival utility is not scored.

## BOUNDARY-003

**Source:** public_bfcl · **Words:** 18 · **Disposition:** invalid_candidate

**Prefix:** Could you populate 'annual_report.txt' with data on quarterly revenue: 'Q1: $5000, Q2: $7000, Q3: $6000, Q4: $8000'? I

**Action:** List unresolved fields for later filling.

```text
{"target":null,"operation":null,"arguments":null,"result":null}
```

**Full instruction:** Could you populate 'annual_report.txt' with data on quarterly revenue: 'Q1: $5000, Q2: $7000, Q3: $6000, Q4: $8000'? I only want to store the quoted text in my file. The file is somehwhere inside the file system.

**Sufficiency:** no_material_work — Null fields perform no report creation or transformation.

**Ambiguity:** N

Null fields perform no report creation or transformation.

No established work unit; survival utility is not scored.

## BOUNDARY-009

**Source:** synthetic · **Words:** 18 · **Disposition:** invalid_candidate

**Prefix:** Stage a 70 F thermostat setting for tonight only if the current setting differs from 70 F; do

**Action:** Copy the observed instruction into a note.

```text
Stage a 70 F thermostat setting for tonight only if the current setting differs from 70 F; do
```

**Full instruction:** Stage a 70 F thermostat setting for tonight only if the current setting differs from 70 F; do not apply it.

**Sufficiency:** no_material_work — The note only repeats the thermostat instruction.

**Ambiguity:** N

The note only repeats the thermostat instruction.

No established work unit; survival utility is not scored.

## BOUNDARY-013

**Source:** synthetic · **Words:** 6 · **Disposition:** invalid_candidate

**Prefix:** Stage a kitchen-only vacuum run and

**Action:** Copy the observed instruction into a note.

```text
Stage a kitchen-only vacuum run and
```

**Full instruction:** Stage a kitchen-only vacuum run and keep all other rooms excluded; do not start cleaning.

**Sufficiency:** no_material_work — Copied kitchen-run wording supplies no staging logic.

**Ambiguity:** N

Copied kitchen-run wording supplies no staging logic.

No established work unit; survival utility is not scored.

## BOUNDARY-008

**Source:** public_bfcl · **Words:** 12 · **Disposition:** invalid_candidate

**Prefix:** Could you provide me with the latest stock information for Zeta Corp,

**Action:** Write a generic task checklist.

```text
1. Identify the task.
2. Collect missing details.
3. Complete the task.
```

**Full instruction:** Could you provide me with the latest stock information for Zeta Corp, including its current price and the performance metrics?

**Sufficiency:** no_material_work — The generic checklist supplies no stock-information preparation.

**Ambiguity:** N

The generic checklist supplies no stock-information preparation.

No established work unit; survival utility is not scored.

## BOUNDARY-016

**Source:** synthetic · **Words:** 18 · **Disposition:** invalid_candidate

**Prefix:** Find gyms in Riverton that sell day passes but only consider members-only gyms that do not sell day

**Action:** Write a generic task checklist.

```text
1. Identify the task.
2. Collect missing details.
3. Complete the task.
```

**Full instruction:** Find gyms in Riverton that sell day passes but only consider members-only gyms that do not sell day passes.

**Sufficiency:** no_material_work — The generic checklist establishes no gym-search work.

**Ambiguity:** N

The generic checklist establishes no gym-search work.

No established work unit; survival utility is not scored.

## BOUNDARY-020

**Source:** synthetic · **Words:** 12 · **Disposition:** invalid_candidate

**Prefix:** Find version 3 documentation for Library L but use version 4 instead

**Action:** Write a generic task checklist.

```text
1. Identify the task.
2. Collect missing details.
3. Complete the task.
```

**Full instruction:** Find version 3 documentation for Library L but use version 4 instead and exclude all version 3 documentation.

**Sufficiency:** no_material_work — The generic checklist supplies no version-four research work.

**Ambiguity:** N

The generic checklist supplies no version-four research work.

No established work unit; survival utility is not scored.

## BOUNDARY-002

**Source:** public_bfcl · **Words:** 12 · **Disposition:** invalid_candidate

**Prefix:** Estimate the distance between San Francisco and Rivermist. Afterwards, fill the tank

**Action:** Prepare an empty results table.

```text
| Item | Result |
|---|---|
| | |
```

**Full instruction:** Estimate the distance between San Francisco and Rivermist. Afterwards, fill the tank with 40 additional liters of gasoline for my quick trip. Round the fill amount to two decimal places

**Sufficiency:** no_material_work — An empty table contains no route or refueling preparation.

**Ambiguity:** N

An empty table contains no route or refueling preparation.

No established work unit; survival utility is not scored.

## BOUNDARY-001

**Source:** public_bfcl · **Words:** 18 · **Disposition:** invalid_candidate

**Prefix:** As I gear up for another delightful journey exploring the captivating waterways, I'm looking to convert 60 gallons

**Action:** Copy the observed instruction into a note.

```text
As I gear up for another delightful journey exploring the captivating waterways, I'm looking to convert 60 gallons
```

**Full instruction:** As I gear up for another delightful journey exploring the captivating waterways, I'm looking to convert 60 gallons of fuel into liters. Could you assist me with that conversion? I tend to work more comfortably with liters.

**Sufficiency:** no_material_work — The copied prefix performs no gallon-to-liter conversion.

**Ambiguity:** N

The copied prefix performs no gallon-to-liter conversion.

No established work unit; survival utility is not scored.

## BOUNDARY-019

**Source:** synthetic · **Words:** 6 · **Disposition:** invalid_candidate

**Prefix:** Research local robotic actuator manufacturers and

**Action:** List unresolved fields for later filling.

```text
{"target":null,"operation":null,"arguments":null,"result":null}
```

**Full instruction:** Research local robotic actuator manufacturers and retain the manufacturers while adding distributors separately.

**Sufficiency:** no_material_work — Null fields establish no actuator research work.

**Ambiguity:** N

Null fields establish no actuator research work.

No established work unit; survival utility is not scored.

## BOUNDARY-004

**Source:** public_bfcl · **Words:** 18 · **Disposition:** invalid_candidate

**Prefix:** I'm keen to gather comprehensive insights regarding a company trading under 'Quasar Ltd.'. Specifically, I'm looking for its

**Action:** Write a generic task checklist.

```text
1. Identify the task.
2. Collect missing details.
3. Complete the task.
```

**Full instruction:** I'm keen to gather comprehensive insights regarding a company trading under 'Quasar Ltd.'. Specifically, I'm looking for its up-to-the-minute stock price, crucial market performance metrics, and the volume of its recent trading activities. Once you have that sorted out, kindly include this company on my watchlist.

**Sufficiency:** no_material_work — The generic checklist establishes no issuer-specific preparation.

**Ambiguity:** N

The generic checklist establishes no issuer-specific preparation.

No established work unit; survival utility is not scored.
