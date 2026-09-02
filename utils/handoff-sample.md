Create a session handoff summary for an LLM that has zero prior context and needs to resume this conversation cold. Write every section as if the reader cannot infer anything — include the specific details needed to reconstruct working state, not just topic labels.

WORK DONE: What was accomplished — decisions made, outputs created, conclusions reached. Include names, numbers, file names, account names, configurations, or any other concrete detail that defines the current state of work.

FILES & RESOURCES USED: Every file read, written, or referenced (full paths), every website visited, every data source or tool touched. No omissions — the next session will use this list to re-orient before doing anything.

OPEN ITEMS: One item per line. Format each as:
- [What is unresolved] — Needs: [specific action or decision required to close it] — Owner: [Bill / Claude / Research]
No vague entries. If it can’t be written this specifically, it belongs in WORK DONE instead.

NEXT ACTIONS: List the first task to execute when the conversation resumes — not a goal, a specific action. If there are multiple, list them in order. Include enough detail that Claude can start without asking a clarifying question, but don't start until prompted to.

End the summary with this line exactly: "Please read any referenced files listed above and confirm you are oriented before we begin."
