# Session 2 handouts: field guide and case studies

Justin Obney's Session 2 handouts for the AI Leadership Academy. This is the text of `justin-obney-handouts.pdf`, in order, for assistants to read. Page 2 is a worksheet; its blanks are for the participant to fill in.

## Pages 1–2 · The AI application field guide

THE AI APPLICATION FIELD GUIDE
From useful idea to
organizational software
A model can answer. Software gives it tools, access to information, and the ability to act.
THE FIVE RUNGS
1
Thought Partner & Assistant
A new way to use a computer.
2
AI Workflows
Routines and scheduled tasks you set up once.
3
Tool Builder
Describe a tool; a teammate starts using it.
4
Bots & Agents
Set up for a job, it acts on its own.
5
Systems of Record
AI built into the records the business runs on.
THE RISK SPECTRUM
Low stakes and reversible
Core and mission-critical
CAPABILITY GATE
Can we design, secure, operate, and maintain it responsibly?
VERIFICATION GATE
Who must validate it before the business depends on it?
You can build more than ever. The stakes decide who should own it.
AI Applications Across the Enterprise
Field Guide / Map
FIND YOUR FIRST APPLICATION
Start with the work, not the tool
01
Look for friction
Where are people...
copying or retyping information?
chasing status or approvals?
reconciling multiple systems?
drafting the same kind of work again?
deciding without enough context?
02
Describe the smallest useful outcome
When  happens, we want  to take  action
using information from , while  verifies .
03
Understand the reach
People affected
Systems touched
Information accessed
How often it happens
If it is wrong
Reversible?
04
Choose the first responsible
step
Ladder rung
Experiment owner
Verification owner
Evidence it worked
Date to stop or expand
Notes
Start small enough to learn. Bring engineering depth when the work becomes load-bearing.
WHEN AN EXPERIMENT STARTS BECOMING REAL SOFTWARE
Justin Obney - justin@obney.ai
Field Guide / Worksheet

## Page 3 · Case study: Certificate Cleanup

AI LEADERSHIP ACADEMY
CASE STUDY / ADMIN AND OPERATIONS
CERTIFICATE CLEANUP
Recover end-of-semester capacity without waiting for the ideal rebuild
At the end of a semester, the legacy school portal could still hold certificates for students whose payment was incomplete. A back-office operator worked through roughly 200-300 student records, opening files and deleting certificates one at a time. A normal cleanup consumed two to three days.
THE FRICTION
The portal had no deletion endpoint. Its team was already focused on a mission-critical replacement, and the legacy application still carried enough production traffic that even a small change deserved caution.
WHAT THEY BUILT
Staff select payment-incomplete students from an existing Salesforce list. Windmill signs into the school portal, follows the known deletion steps, and reports completion back to the exact Salesforce student record.
THE ARCHITECTURE DECISION
The team did not wait for the future rebuild, and it did not pretend the browser bridge should last forever. It bounded the automation to a known list, required complete deletion before success, and tied retirement to the legacy system's own decommissioning.
WHAT LEADERS SHOULD NOTICE
AI helped write this workflow; it does not decide whom to touch. Salesforce supplies the eligibility rule, the worker executes known steps, and a partial failure remains an error that is safe to rerun.
THE VERIFICATION BOUNDARY
Salesforce selects the students and document types.
The worker deletes every targeted file or confirms it is already absent.
Only then does one completion flag return to that student's Salesforce record.
UNDERNEATH THE APPLICATION
HOST
Salesforce initiates / Windmill and Chromium execute
IDENTITY
Salesforce staff / portal worker credential
DATA
Salesforce and the legacy portal / no new database
THE RESULT
2-3 days
of recurring manual cleanup removed each semester
WHAT REPLACES IT
The rebuilt school application prevents the affected certificates from being generated until payment is resolved.
LOOK FOR THIS PATTERN IN YOUR ORGANIZATION
A recurring task is trapped behind a legacy interface while its durable replacement is already underway. Use a bounded bridge, verify every mutation, and define how the bridge disappears.

## Page 4 · Case study: Job Shadow Verification

AI LEADERSHIP ACADEMY
CASE STUDY / STUDENT EXPERIENCE
JOB SHADOW VERIFICATION
Turn a real-world visit into a trusted Canvas gradebook record
Students complete job-shadow visits inside working dental offices. The person who witnesses those hours is outside the school's learning system, but the result still has to become a Canvas grade: eight hours for half credit and sixteen hours for full credit.
THE FRICTION
A student returned a signed paper form or uploaded a photo. Even a four-hour submission created work: staff inspected it, retained the partial progress, remembered who was incomplete, and manually entered a grade only after a threshold was reached.
WHAT THEY BUILT
The student opens the existing Canvas assignment and receives a personal QR code. While the student is at the office, a manager scans it, enters verified hours, and signs. The application accumulates visits and posts the grade back to Canvas automatically.
THE IDENTITY DECISION
The verifier does not need a Canvas account and never receives Canvas authority. Canvas identifies the student and supplies the future grade destination. The QR permits only a visit submission for that student; the application uses its own trusted connection when it writes the grade.
WHAT LEADERS SHOULD NOTICE
The QR does not replace trust; it narrows the handoff. The application owns only the state needed to connect a real-world verification to the right student, preserve partial visits, and write the result into the system the school already uses.
THE TRUSTED HANDOFF
Canvas launches the identified student and deposits the grade destination.
The office manager verifies one visit through the student's scoped QR.
The application totals hours and posts the correct threshold back to Canvas.
UNDERNEATH THE APPLICATION
HOST
Railway
IDENTITY
Canvas LTI / revocable student-specific QR
DATA
PostgreSQL / visits, hours, signature, write-back address
THE RESULT
No re-entry
verified visits accumulate and become the correct Canvas grade automatically
WHAT THIS ENABLES NEXT
The team now has a reusable pattern for Canvas-connected forms that begin or end outside Canvas.
LOOK FOR THIS PATTERN IN YOUR ORGANIZATION
A trusted person outside your core system must verify a real-world event. Let the system identify the participant, give the verifier only the action they need, and write the result back automatically.

## Page 5 · Case study: CPR Instructor Onboarding

AI LEADERSHIP ACADEMY
CASE STUDY / OPERATIONS
CPR INSTRUCTOR ONBOARDING
Scale instructor onboarding without scaling back-office headcount
Three times a year, a regional dental-education company coordinates more than 200 classes across 85+ instructors. Each person confirms dates, reconfirms before the event, signs an agreement, and becomes eligible for payment. That process ran across email, spreadsheets, Salesforce, and Bill.com.
THE FRICTION
Every term restarted the same chase. Staff followed up with instructors, updated a spreadsheet, moved information between systems, and tried to maintain one shared picture of who was ready.
WHAT THEY BUILT
Each instructor gets one personal link. From that page they review their classes, confirm or decline, reconfirm 14 days out, sign once, and continue into Bill.com. Staff manage the same Salesforce records from one live view; the portal does not create another system of record.
THE SECURITY DECISION
The team did not want instructors inside Salesforce. Instructors did not need another account to manage. So it chose a short-lived, narrowly scoped magic link: enough access to review and respond to class details, no privileged system access, and staff review for anything questionable.
WHAT LEADERS SHOULD NOTICE
AI is not deciding who gets paid. It made this precise custom workflow practical to build. The return is capacity: the same team can onboard as many instructors as the business needs without adding back-office staff.
"We have something customized exactly to our business that we couldn't have bought. It freed up about 500 hours a year of capacity."
TRAVIS MIGLICCO, CFO
UNDERNEATH THE APPLICATION
HOST
Railway
IDENTITY
personal link · Google for staff
DATA
Salesforce · no new app database
THE RESULT
≈500
estimated staff hours freed each year
WHAT THIS ENABLES NEXT
The team now has a reusable pattern for simple, scoped group-coordination tools.
LOOK FOR THIS PATTERN IN YOUR ORGANIZATION
A recurring partner workflow where a full company account is too much, email is too little, and the data already lives inside systems the organization trusts.
