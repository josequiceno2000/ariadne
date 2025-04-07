---
name: Bug Report
about: Report something not working as expected
title: "[BUG] <short description>"
labels: [bug]
assignees: []
---

body:
  - type: markdown
    attributes:
      value: |
        Thanks for helping improve **Ariadne**! Please fill out the form below so we can address the bug as soon as possible.

  - type: input
    id: summary
    attributes:
      label: Bug Summary
      description: What went wrong? Be clear and concise.
      placeholder: "The maze solver crashes when selecting A* on 50x50 grid"
    validations:
      required: true
  
  - type: textarea
    id: steps
    attributes:
      label: Steps to Reproduce
      description: Please describe how to trigger the bug
      placeholder: |
        1. Go to 'Maze Settings'
        2. Set Maze Size to 50x50
        3. Select 'A* Algorithm'
        4. Click 'Solve'
        5. App crashes
    validations:
      required: true

  - type: textarea
    id: expected
    attributes:
      label: What Should Have Happened?
      description: Tell us the expected outcome.
      placeholder: "I expected the maze to be solved visually with A*."

  - type: textarea
    id: logs
    attributes:
      label: Relevant Logs / Screenshots
      description: Paste error logs, traceback, or attach screenshots if helpful.
      placeholder: |
        ```
        Traceback (most recent call last):
        File "main.py", line 88...
        ```

  - type: dropdown
    id: platform
    attributes:
      label: What OS/Platform Are You Using?
      options:
        - Windows
        - macOS
        - Linux
        - Other
      description: This helps reproduce platform-specific bugs

  - type: input
    id: version
    attributes:
      label: Ariadne Version
      placeholder: "v1.0.0 (or commit SHA)"