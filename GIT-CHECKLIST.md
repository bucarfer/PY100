✅ Git Workflow Checklist for VS Code
🔄 Before You Start Coding (Optional but Good Habit)
Open Terminal in VS Code.
Run:
bash
Copy
Edit
git pull --no-rebase
This ensures you have the latest version from GitHub before you start working.

📝 While You Work
Make changes to your files.
Save often (Cmd+S or Ctrl+S).
💾 After You Finish a Session (Commit + Push)
1️⃣ Stage your changes
bash
Copy
Edit
git add .
2️⃣ Commit with a helpful message
bash
Copy
Edit
git commit -m "Short description of what you did"
3️⃣ Push to GitHub
bash
Copy
Edit
git push
🔄 When Switching Devices (or Collaborating)
If you work on this repo from another device, always pull first:
bash
Copy
Edit
git pull --no-rebase
🚨 If Git Refuses to Pull (Conflicts or Divergence)
Check if you have uncommitted changes.
Either:
Commit your changes.
Or stash your changes:
bash
Copy
Edit
git stash
Then try:
bash
Copy
Edit
git pull --no-rebase
If you stashed changes, bring them back:
bash
Copy
Edit
git stash pop