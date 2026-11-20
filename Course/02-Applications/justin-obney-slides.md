# Session 2 slides: Applications

Justin Obney's slides from Session 2 of the AI Leadership Academy, November 20, 2026. This is the visible text of each slide in `justin-obney-slides.pdf`, in order, for assistants to read. Page numbers match the PDF. Pages marked "Underneath" are the diagram or detail opened beneath the slide before them. Speaker notes are not included.

## Page 1 · Slide 1

BEFORE WE START
Set up your Academy folder
links.obney.ai/c2-setup
Unzip it, connect it to your assistant (Claude Cowork, ChatGPT Work or Grok Bot), allow access, then paste:
“Read ACADEMY.md and help me get started.”
THE FOUR CHECKS
It opens your folder
It quotes a course file
It saves a note
A new chat finds it

## Page 2 · Slide 2

BEFORE WE START · RECONNECT
Ask what you should work on
Your assistant has your folder and whatever it already knows about you. Let it suggest where to start.
1
Ask for your opportunities
From your folder, Session 1 and what it knows about you.
2
Pick two
The one you could start soonest, and the ambitious one you really want.
3
Save them
Name the ambitious goal. Start with the attainable step toward it.
TRY ASKING
“From what you know about me and what’s in my Academy folder, what might my opportunity statements be? Help me pick the most attainable one and the most ambitious one, then save both.”
Before moving on: A few of you will share what it told you back.

## Page 3 · Slide 3

Let's talk about AI
 Software
JUSTIN OBNEY

## Page 4 · Slide 4

AI is Software

## Page 5 · Slide 5

Spot the difference?
ANTHROPIC
Claude
CHAT
Claude
WORK
CoWork
CODE
Claude Code
OPENAI
ChatGPT
CHAT
ChatGPT
WORK
ChatGPT Work
CODE
Codex

## Page 6 · Underneath slide 5

SEEN ON X
[Image: Tweet from @james406: 'seriously be careful out there everyone — i had 2 Microsoft Copilot licenses in my car, and someone broke in and left 4 more']

## Page 7 · Slide 6

THE HARNESS
The model is only one part.
A MODEL ALONE
MODEL
Answers, then stops.
→
A MODEL IN A HARNESS
Context + memory
What it knows
Tools + integrations
What it can reach
Guardrails + permissions
What it may do
Validation + feedback
How it improves
MODEL
Useful. Reliable. Safe.

## Page 8 · Slide 7

WHERE AI WORKS
Where does your assistant run?
No computer
A CHATBOT
Your computer
WHERE WE WORK TODAY
Its own computer
IT RUNS BY ITSELF
IT WORKS WITH
What you paste in
Your files, while you watch
What you connect, on a schedule
CLOSE YOUR LAPTOP
It waits
It stops
It keeps going

## Page 9 · Slide 8

YOUR ASSISTANT · FILES ON YOUR COMPUTER
Describe the outcome. Get finished work back.
Claude · Cowork
Turn our Q3 numbers into a board update, one deck and a one-page summary.
Pulled the sheet, built the deck, wrote the recap.
Here's the board update. Three slides on revenue and retention, plus a one-page summary you can send as-is.
PPT
Q3 Board Update
3 slides · updated just now
Open
Progress
4 of 4
Outputs 3
PPT
Q3-board-update.pptx
DOC
board-summary.docx
CSV
q3-metrics.csv
Context
📁
Q3 financials

## Page 10 · Slide 9

PRACTICE · BUILD
We’re going to build a dashboard
Building something is the fastest way to get fluent with AI. This is the muscle we’re exercising:
Describe what you want
→
Inspect the result
→
Ask for changes
THE SCENE
You run an HVAC service company with six branches. Complaints are up, and customers say they’re waiting too long. You have a hunch and two weekly reports.
FOLLOW ALONG
links.obney.ai/c2-build
The data files and every prompt to copy. Start a new chat for it. No new-chat button? Tell it you’re starting a class exercise.

## Page 11 · Slide 10

LIVE BUILD · ONE REPORT
Start with the problem
Say what’s wrong before you ask for anything. One report is enough to start.
1
Save the report first
Download it from the page into your Academy folder, not Downloads.
2
Say the problem
Complaints are up. Have it read the report and help you visualize it.
3
Ask to see it
Name the view you want. If it doesn’t point at the problem, say so.
TRY ASKING
“Show me complaints, response time and same-day completion by branch, week by week. Make the problem jump out.”
Before moving on: Switch to the editor. Open the result, and push back if it doesn’t point at the problem.

## Page 12 · Slide 11

LIVE BUILD · A SECOND SOURCE
Test your hunch
A second report lets you check the story you already suspect.
1
Say your hunch
Lake Charles is short on techs. Save the staffing report in the same folder.
2
Put them on one timeline
Does staffing line up with when service got worse?
3
Try to break it
Ask what else changed around those weeks before you believe the first story.
TRY ASKING
“My hunch is Lake Charles is short on techs. Here’s our staffing report. Does staffing line up with when service got worse? Put them on one timeline.”
Before moving on: What else could explain it? Ask before you act on the first answer.

## Page 13 · Slide 12

PRACTICE · CHECK
Check what the dashboard claims
A convincing dashboard still needs its numbers and interpretations checked.
1
Trace a claim to the source
Check a total, a trend and something unusual against the CSV rows.
2
Check the match
Did combining the files drop branches, duplicate rows or turn gaps into zeros?
3
Correct a copy and rebuild
Keep the original files and leave unknowns visibly unknown. Save the result in Builds/.
TRY ASKING
“Before I take this to my managers, what in here could be wrong? Show me the rows behind each number.”
Before moving on: What would you need to check before putting this in front of your leadership team?

## Page 14 · Slide 13

FROM A DASHBOARD TO A RECURRING WORKFLOW
Where does next Monday’s data come from?
1
A report arrives
An export, an email or a shared folder
→
2
A trigger starts the work
One you approved
→
3
The files are checked
The same checks as today
→
4
The dashboard refreshes
New numbers, same view
→
5
A person reviews it
Before anyone relies on it
Each step needs a connection, permissions and somewhere to run. Your dashboard has none of these yet.

## Page 15 · Slide 14

LOOKING AHEAD · SESSIONS 3–5
Where could this help in your work?
What do you repeatedly gather, compare or explain?
In Sessions 3–5, you’ll explore your own opportunities and what it would take to pursue them.
TRY ASKING
“Help me think about where something like this could help in my work. Ask me one question at a time, then save a short note of the idea.”

## Page 16 · Slide 15

THE CODING AGENT
Like it or not, you're all coders now
onboard.py
✳
written by Claude
1# "onboard the instructors" is just this
2from org import salesforce, billcom, mail
3
4def onboard(person):
5    who  = salesforce.get(person, ["name", "classes"])
6    link = personal_link(who)        # no account
7    mail.send(who.email, link)     # one link
8    if who.confirmed:
9        billcom.invite(who)         # so they get paid
10    return link

## Page 17 · Underneath slide 15

THE REALIZATION · TOKEN BY TOKEN
Same stream of tokens, two very different results.
[Image: The completed program and its list of pending instructors.]

## Page 18 · Slide 16

AI wrote both. Only one calls a model.
DETERMINISTIC
dashboard.ts
✳ written by Claude
1const rows = await readReports()
2const result = summarize(rows)
3dashboard.draw(result)
Rules decide
Same input → same path
NON-DETERMINISTIC
weekly-note.ts
✳ written by Claude
1const rows = await readReports()
2const result = await model.generate(rows)
3dashboard.addNote(result)
The model decides
The output can vary
How it was built ≠ how it runs.

## Page 19 · Slide 17

THE LADDER
From thought partner to systems of record
1
Thought Partner & Assistant
A new way to use a computer.
2
AI Workflows
Routines and scheduled tasks you set up once.
MAKING THE ASSISTANT YOURS
OTHERS RELY ON IT
3
Tool Builder
Describe a tool; a teammate starts using it.
4
Bots & Agents
Set up for a job, it acts on its own.
5
Systems of Record
AI built into the records the business runs on.
MADE FOR OTHERS TO RELY ON

## Page 20 · Slide 18

CONCEPT · THE HOST
Where does it run when you’re not there?
THE DASHBOARD
Somewhere your team can open it
Not a file on one laptop.
THE UPDATES
Somewhere the recurring work can run
Even while your laptop is closed.
That somewhere is a host: an always-on computer you rent.

## Page 21 · Slide 19

CONCEPT · AUTHENTICATION
Reachable is not the same as allowed.
A LINK
Where the tool is
It makes the tool reachable.
≠
AUTHENTICATION
Who is asking
What they can do—and when access ends.

## Page 22 · Slide 20

The stakes change who should own the work.
LOW STAKES
A useful tool for me
MISSION-CRITICAL
The core student platform
PERSONAL AND CONTAINED
COMPLIANCE & FINANCE

## Page 23 · Slide 21

CASE STUDY · THE THREAD THROUGH THIS SESSION
A local dental-education company
12+
SaaS systems of record it runs on
3 terms
a year, region-wide clinics and classes
2 builders
the COO and a CPA, neither an engineer

## Page 24 · Slide 22

MCP FLEET · CROSS-FUNCTION
One question used to require five exports.
“What did we spend on ads versus enrollments?”
FIVE EXPORTS
→
TWELVE CONNECTORS
→
ONE LIVE ANSWER

## Page 25 · Slide 23

MCP FLEET · CROSS-FUNCTION
Every system they run on, reachable in one sentence.
Salesforce
QuickBooks
Bill.com
Authorize.Net
ADP
BerniePortal
Bloom Growth
Canvas LMS
Digital Ads
Google Business
Marketing Cloud
Webflow

## Page 26 · Slide 24

MCP FLEET · ACCESS TO DATA
Whose permissions does the model use?
PERSONAL CONNECTION
As you
Only what you can see
SERVICE ACCOUNT
As the system
Potentially everything

## Page 27 · Slide 25

MCP FLEET · INFRASTRUCTURE
Twelve connectors. No new system of record.
WHAT IT NEEDED
HOST
via Railway
AUTHENTICATION

## Page 28 · Slide 26

Tool Builder
Describe a tool. A teammate starts using it.
1
Thought Partner & Assistant
2
AI Workflows
3
Tool Builder
4
Bots & Agents
5
Systems of Record

## Page 29 · Slide 27

CPR INSTRUCTOR ONBOARDING · OPERATIONS
Every term starts the same scramble
3×
terms each year
200+
classes each term
85+
instructors region-wide
1
spreadsheet holding it together

## Page 30 · Slide 28

CPR INSTRUCTOR ONBOARDING · THE RESULT
One page for instructors. ≈500 hours back for staff.
🎓
Dental Academy
CPR INSTRUCTOR PORTAL
Claim your CPR classes
Hi there! Confirm the classes you can teach below.
YOUR REQUESTED CLASSES
Family Dentistry
Practice address
SAT
Sep 19
TIME
9:00 AM
Confirm I'll be there
I can't make this one
Family Dentistry
Practice address
SAT
Sep 19
TIME
2:00 PM
Confirm I'll be there
I can't make this one
🎓
Dental Academy
· CPR Scheduling · Staff View
Signed in as staff
CPR Instructor Portal
272 active + draft courses · 272 shifts · 223 covered · 85+ instructors
272
Courses
246
Invites sent
239
Links opened
223
First confirms
26
Unassigned
COURSE
PRACTICE
INSTRUCTOR
STATUS
1ST CONFIRM
CONTRACT
Birmingham, AL — AM
Practice A
Instructor A
Active
Confirmed
Yes
Bloomington, IN — AM
Practice B
Instructor B
Active
Confirmed
Yes
Boone, NC — AM
Practice C
Instructor C
Active
Pending
Pending
Brandon, FL — AM
Practice D
(unassigned)
Draft
—
—

## Page 31 · Underneath slide 28

CPR INSTRUCTOR ONBOARDING · STATE MACHINE
One Salesforce record moves from invitation through payment.
[Image: CPR instructor lifecycle from invitation through payment]

## Page 32 · Slide 29

CPR INSTRUCTOR ONBOARDING · INFRASTRUCTURE
A hosted page over the records they already had.
WHAT IT NEEDED
HOST
via Railway
AUTHENTICATION
via magic links
DATABASE
via Salesforce
Staff access through Google OAuth
SYSTEMS IT TOUCHED
Salesforce
Bill.com

## Page 33 · Slide 30

JOB SHADOW · STUDENT EXPERIENCE
A QR code turns signed hours into a Canvas grade.
STUDENT
Shows the QR
→
HOST OFFICE
Signs + enters hours
→
CANVAS
Posts the grade
8 hours = 50%
·
16 hours = 100%

## Page 34 · Underneath slide 30

JOB SHADOW · THE WRITE-BACK UNDERNEATH
The verifier never logs into Canvas. The student's launch already deposited the address.
[Image: Job shadow verification sequence from Canvas launch through gradebook update]

## Page 35 · Slide 31

JOB SHADOW · INFRASTRUCTURE
The first build that needed its own database.
WHAT IT NEEDED
HOST
via Railway
AUTHENTICATION
via Canvas + QR
DATABASE
via PostgreSQL
NEW IN THIS BUILD
LTI 1.3
SYSTEMS IT TOUCHED
Canvas
Canvas authenticates the student and receives the grade write-back.

## Page 36 · Slide 32

CERTIFICATE CLEANUP · ADMIN & OPS
Two days of clicking became one Salesforce button.
BEFORE
2–3 days
each term
→
NOW
One button
Windmill runs the work
AI helped build it. Windmill runs it.

## Page 37 · Underneath slide 32

CERTIFICATE CLEANUP · THE WINDMILL RUN UNDERNEATH
Salesforce decides who to touch; headless browsers do the clicking.
[Image: Certificate cleanup sequence across Salesforce, Windmill, a robot browser, and the admin portal]

## Page 38 · Slide 33

CERTIFICATE CLEANUP · INFRASTRUCTURE
No API put a browser in the stack.
WHAT IT NEEDED
HOST
via Railway
AUTHENTICATION
via staff login
DATABASE
via Salesforce
Windmill + Chromium · staff login because the portal has no API
SYSTEMS IT TOUCHED
Salesforce
Admin portal

## Page 39 · Slide 34

Bots & Agents
Bots run one job on their own. Agents carry context and choose what happens next.
1
Thought Partner & Assistant
2
AI Workflows
3
Tool Builder
4
Bots & Agents
5
Systems of Record

## Page 40 · Slide 35

AVA · SALES
The COO's first build booked 50 calls no one would have chased.
50
CALLS BOOKED
from dormant leads
Lead arrives
→
Ava texts
→
Call booked

## Page 41 · Underneath slide 35

REPORT CARD
The operator's first version graded 68 (D+); rebuilt with obney's engineers, it graded 90 (A−).
OPERATOR BUILD · JUL 2
68
D+
Booking core action · 25%
58
·
D+
Safety & compliance TCPA · 20%
60
·
D+
Architecture design intent · 15%
80
·
B−
Conversational quality · 15%
82
·
B−
Reliability robustness · 10%
78
·
C+
Observability explainability · 10%
63
·
D
Cadence proactive · 5%
55
·
D
AFTER OBNEY'S ENGINEERS · JUL 31
90
A−
Booking core action · 25%
90
·
A−
Safety & compliance TCPA · 20%
88
·
B+
Architecture design intent · 15%
93
·
A
Conversational quality · 15%
90
·
A−
Reliability robustness · 10%
90
·
A−
Observability explainability · 10%
93
·
A
Cadence proactive · 5%
85
·
B
Biggest moves on the two dimensions the audit weighted heaviest: Booking 58→90 and Compliance 60→88.

## Page 42 · Slide 36

AVA · INFRASTRUCTURE
Salesforce became the entire application.
WHAT IT NEEDED
HOST
via Salesforce
AUTHENTICATION
via Salesforce
DATABASE
via Salesforce
Apex + LWC · platform permissions · SOQL
SYSTEMS IT TOUCHED
Salesforce
Anthropic
OpenRouter
SMS

## Page 43 · Slide 37

THE OBNEY.AI VAULT · 1,791 CONNECTED NOTES
CARL · CHIEF OF STAFF
Context is what makes Carl an assistant.

## Page 44 · Slide 38

CARL · CHIEF OF STAFF
You text him like a teammate.
C
Carl
carl@obney.ai
Carl — join the team Slack and say hi 👋
On it. Slack emailed a code to carl@obney.ai. Grabbing it.
In 🤖 Joined #all-obney and introduced myself.
Nice. Brief me before my 9?
Sent your day-start: 3 meetings, 2 client replies waiting, 1 invoice overdue.
Text Message

## Page 45 · Slide 39

BEFORE WE CLOSE
Who would fix it?
If the dashboard you built today broke next Monday.
ILLUSTRATION, NOT DATA
Things people rely on
People who could fix them
Time →

## Page 46 · Slide 40

WHO DOES THIS WORK NOW
Operators start it. Engineers make it safe to scale.
FDO
Forward-Deployed Operator
Runs the business and builds the first version.
FDE
Forward-Deployed Engineer
Hardens the operator's build for production.
PRO SWE
Professional Software / AI Engineer
Owns the platform and standards underneath.

## Page 47 · Slide 41

THE PAVED ROAD
People will build. Give them a road.
THE PIECES, DECIDED ONE AT A TIME
Hosting
Identity & permissions
Data & connectors
Logging & monitoring
Tests & environments
BROUGHT TOGETHER: THE PAVED ROAD
Reliable · Secure · Yours

## Page 48 · Slide 42

IF SOMEONE ELSE SETS THE ROAD
One skill, two places to use it
AT WORK, INSIDE THE WALLS
Get very good
1
Know the toolset
What’s approved, and what your admins have turned on.
2
Go deep on what’s allowed
Master the approved tools before reaching for others.
3
Stay close to IT
Or whichever group is making progress. Bring them what you learn.
EVERYWHERE ELSE
Build freely
The same understanding works across the rest of your life: home, side projects, the things you run.
This is a new way to use a computer.

## Page 49 · Slide 43

SYSTEMS OF RECORD
The stakes decide who should own it.
01
CAPABILITY GATE
Can we operate it responsibly?
02
VERIFICATION GATE
Who must validate it before the business depends on it?
LOW STAKES · REVERSIBLE
Explore internally
CORE · MISSION-CRITICAL
Bring engineering depth
1
Thought Partner & Assistant
2
AI Workflows
3
Tool Builder
4
Bots & Agents
5
Systems of Record

## Page 50 · Slide 44

THE AI-NATIVE TURN
Built with AI, or built for it?
Everything today used AI to build largely traditional software. AI-native software is the next turn: built for the agents that are coming.
TRADITIONAL · BUILT WITH AI
The agent finds your data and guesses what you meant.
your unstructured data
→
an intent it made up
AI-NATIVE · BUILT FOR AGENTS
The agent reads your intent and acts like you would.
YOUR SYSTEM DECLARES
INTENT
GUARDRAILS
ACCESS PATTERNS
PURPOSE
Agents will reach your data either way. AI-native software decides whose intent they act on.

## Page 51 · Slide 45

COMING OUT OF SESSION 2
Your next three actions.
3
Use AI to think it through.
Have your assistant ask questions, challenge assumptions and help you explore possible approaches.
4
Build something useful and check it.
Describe what you need, create a first version, and verify that it works.
5
Choose an opportunity to explore further.
Save what you want to pursue, what information or access you need, and where you may need help. Bring that into Session 3.
