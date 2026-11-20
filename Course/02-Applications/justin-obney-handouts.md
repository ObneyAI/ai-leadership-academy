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
Recover end-of-term capacity before the new system is ready
At the end of each term, the old school portal could still hold certificates for students who had not finished paying. A back-office staff member opened 200 to 300 student records and deleted each certificate by hand. One cleanup took two to three days.
THE FRICTION
The old portal gave other software no way to delete certificates. Only a person clicking through its screens could do it. The portal team was busy with the replacement system, and the school still used the old portal every day, so any change to it was a risk.
WHAT THEY BUILT
A staff member picks the unpaid students from a list in Salesforce and presses one button. Software then signs in to the portal like a staff member, clicks through the same deletion steps, and marks each student done in Salesforce.
THE DESIGN DECISION
The team built a temporary fix with three limits. It touches only the students on the list. It reports success only after it removes every certificate. The team turns it off when the old portal shuts down.
WHAT LEADERS SHOULD NOTICE
AI helped the team build this tool. Ordinary software runs it, with the same steps each time, and Salesforce picks the students. If a run stops partway, the tool shows an error and staff can run it again.
HOW IT CHECKS ITS WORK
Salesforce picks the students and the certificates to remove.
The software removes each certificate, or confirms that it is already gone.
Then it marks that student done in Salesforce.
UNDERNEATH THE APPLICATION
HOST
Salesforce starts it / Windmill runs a browser
IDENTITY
Salesforce staff login / one portal login for the tool
DATA
Salesforce and the old portal / no new database
THE RESULT
2-3 days
of manual cleanup removed each term
WHAT REPLACES IT
The rebuilt school application does not issue a certificate until the student's payment is complete.
LOOK FOR THIS PATTERN IN YOUR ORGANIZATION
You have a recurring task stuck in an old system, and its replacement is already in progress. Build a temporary fix with clear limits. Check every change it makes, and decide in advance when you will turn it off.

## Page 4 · Case study: Job Shadow Verification

AI LEADERSHIP ACADEMY
CASE STUDY / STUDENT EXPERIENCE
JOB SHADOW VERIFICATION
Turn a job-shadow visit into a trusted Canvas grade
Students complete job-shadow visits in working dental offices. The office manager who confirms the hours has no access to Canvas, the school's learning system. The hours still have to become a Canvas grade: eight hours for half credit and sixteen hours for full credit.
THE FRICTION
A student returned a signed paper form or uploaded a photo. Staff checked each submission, even a four-hour one. They kept track of partial hours and of which students were not done. They entered a grade by hand when a student reached eight or sixteen hours.
WHAT THEY BUILT
The student opens the Canvas assignment and gets a personal QR code. At the office, the office manager scans the code, enters the verified hours, and signs. The tool adds up the visits and posts the grade to Canvas.
THE IDENTITY DECISION
The office manager never gets a Canvas account. When the student opens the assignment, Canvas tells the tool who the student is and where the grade goes. The QR code lets the office manager record one visit for that student and do nothing else. The tool posts the grade itself, with access the school approved.
WHAT LEADERS SHOULD NOTICE
Give an outside person one small job and nothing more. The tool keeps only what it needs: whose visit it was, the hours so far, and where the grade goes. The grade ends up in Canvas, where the school already looks.
THE TRUSTED HANDOFF
The student opens the assignment, and Canvas tells the tool who the student is.
The office manager confirms one visit with the student's QR code.
The tool adds up the hours and posts the correct grade to Canvas.
UNDERNEATH THE APPLICATION
HOST
Railway
IDENTITY
Canvas sign-in / one QR code per student
DATA
PostgreSQL / visits, hours and signatures
THE RESULT
No re-entry
the tool adds up verified visits and posts the correct Canvas grade
WHAT THIS ENABLES NEXT
The team can use this pattern again for any Canvas form that starts or ends outside Canvas.
LOOK FOR THIS PATTERN IN YOUR ORGANIZATION
Someone outside your organization has to confirm a real-world event. Let your system identify the person, give the outside person one action, and write the result back to your system.

## Page 5 · Case study: CPR Instructor Onboarding

AI LEADERSHIP ACADEMY
CASE STUDY / OPERATIONS
CPR INSTRUCTOR ONBOARDING
Onboard more instructors without more back-office staff
Three times a year, a regional dental-education company runs more than 200 classes with more than 85 instructors. Each instructor confirms dates, confirms again before the class, signs an agreement, and then can get paid. Staff ran that process across email, spreadsheets, Salesforce and Bill.com.
THE FRICTION
Every term, staff repeated the same follow-up work. They contacted instructors, updated a spreadsheet and copied information between systems. They tried to keep one shared view of which instructors were ready.
WHAT THEY BUILT
Each instructor gets one personal link. On that page, the instructor reviews their classes and confirms or declines. Fourteen days before a class, the instructor confirms again, then signs once and continues to Bill.com. Staff see the same Salesforce records on one live page, so all instructor data stays in Salesforce.
THE SECURITY DECISION
The team kept instructors out of Salesforce and gave them no new account to manage. Each instructor gets a sign-in link that needs no password and expires soon. The link opens that instructor's classes and nothing else. Staff review anything that looks wrong.
WHAT LEADERS SHOULD NOTICE
AI made it practical for the team to build this exact workflow. Fixed steps in the workflow decide who gets paid, and no AI model makes that choice. The same team can now onboard as many instructors as the business needs, with no extra back-office staff.
"We have something customized exactly to our business that we couldn't have bought. It freed up about 500 hours a year of capacity."
TRAVIS MIGLICCO, CFO
UNDERNEATH THE APPLICATION
HOST
Railway
IDENTITY
personal link for instructors · Google sign-in for staff
DATA
Salesforce · no new database
THE RESULT
≈500
estimated staff hours freed each year
WHAT THIS ENABLES NEXT
The team can use the same approach for other small tools that coordinate outside people.
LOOK FOR THIS PATTERN IN YOUR ORGANIZATION
You work with outside partners on a recurring process. A full company account gives them too much access, and email gives them too little. The data you need is already in systems you trust.
