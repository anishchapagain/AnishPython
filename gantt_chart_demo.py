import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Define milestones and timelines
milestones = [
    ("RFP Released", "2025-06-10", "2025-06-10"),
    ("Proposal Submission Deadline", "2025-06-25", "2025-06-25"),
    ("Evaluation & Shortlisting", "2025-06-26", "2025-07-05"),
    ("Project Kickoff", "2025-07-10", "2025-07-10"),
    ("Phase 1: Chatbot + Ticket Classifier", "2025-07-11", "2025-09-10"),
    ("Phase 2: Loan Risk + Fraud Detection", "2025-09-11", "2025-11-15"),
    ("Phase 3: Staff Tools + Summarizer", "2025-11-16", "2026-01-15"),
    ("UAT & Staff Training", "2026-01-16", "2026-02-10"),
    ("Full System Go-Live", "2026-02-15", "2026-02-15"),
    ("Support & Maintenance Begins", "2026-02-16", "2027-02-16")
]

# Convert to DataFrame
df = pd.DataFrame(milestones, columns=["Task", "Start", "End"])
df["Start"] = pd.to_datetime(df["Start"])
df["End"] = pd.to_datetime(df["End"])
df["Duration"] = df["End"] - df["Start"]

# Create Gantt chart
fig, ax = plt.subplots(figsize=(12, 6))
for i, row in df.iterrows():
    ax.barh(row["Task"], row["Duration"].days, left=row["Start"], color='skyblue' if row["Duration"].days > 0 else 'lightgreen')

# Format date axis
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
plt.xticks(rotation=45)
plt.xlabel("Timeline")
plt.title("AI/ML Banking Project - Milestone Gantt Chart")
plt.tight_layout()

plt.grid(True, axis='x', linestyle='--', alpha=0.6)
plt.show()
