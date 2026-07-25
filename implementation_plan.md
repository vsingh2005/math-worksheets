# Implementation Plan - Track Selection Page, Grade Questions Bank Expansion & Hover Fixes

This plan outlines the enhancements to allow users to select from three different placement test tracks (Grades 3–4, Grades 5–6, and Grades 7–8) after clicking "Begin Math Assessment". It also covers expanding the question pool with 45 new questions for Grades 3, 4, and 5, adapting the dynamic difficulty bounds to respect the chosen track, and repairing the hover color text contrast on the "View Past Results" button.

## Proposed Changes

### [HTML Component]

#### [MODIFY] [index.html](file:///c:/Users/singh/Downloads/math_worksheets_repo/index.html)
- Add a new **Track Selection Panel** (`track-selection-panel`) within the landing screen (`landing-screen`), initially hidden.
- Alter the click action of "Begin Math Assessment" to trigger showing this track selection panel rather than moving immediately to the general instructions screen.
- Set up cards for:
  - **Grades 3–4 Placement Test** (Elementary Track)
  - **Grades 5–6 Placement Test** (Intermediate Track)
  - **Grades 7–8 Placement Test** (Middle School Track)
- Clicking a track sets the selection and transitions to the Instructions step.
- Add a `save-exit-confirm-modal` dialog layout (already implemented in index.html, but double check it integrates cleanly with the tracks).

### [CSS Stylesheet]

#### [MODIFY] [index.css](file:///c:/Users/singh/Downloads/math_worksheets_repo/index.css)
- Add hover override classes for `button.hover\:bg-slate-100` to prevent the WordPress white-text hover styling from rendering the text invisible on hover.

### [JavaScript Controller]

#### [MODIFY] [app_tabs.js](file:///c:/Users/singh/Downloads/math_worksheets_repo/app_tabs.js)
- Inject **45 new math questions** (15 for Grade 3, 15 for Grade 4, 15 for Grade 5) into the `questions` array. All new questions will follow the exact multiple-choice or numeric format with explanations.
- Update the app `state` to include `selectedTrack` (defaults to `'7-8'`).
- In `startExam()`, initialize `state.activeDifficulty` based on the chosen track:
  - Track `'3-4'` starts at Grade 3.
  - Track `'5-6'` starts at Grade 5.
  - Track `'7-8'` starts at Grade 7.
- In `nextQuestion()`, constrain the dynamic difficulty progression:
  - Track `'3-4'`: bounded between 3 and 4.
  - Track `'5-6'`: bounded between 5 and 6.
  - Track `'7-8'`: bounded between 7 and 8.
- In `finishExam()`, adjust the padding queue (if ended early) and the recommended placement logic to map correctly to the chosen track bounds.
- Update `showTrackSelection()` and `selectTrack(track)` helpers.

#### [MODIFY] [app.js](file:///c:/Users/singh/Downloads/math_worksheets_repo/app.js)
- Sync the identical question bank, state settings, difficulty track boundaries, and helpers as modified in `app_tabs.js` (keeping them functional duplicates).

---

## Verification Plan

### Automated/Localhost Tests
- Run the local server and verify using the browser subagent that:
  - Clicking "Begin Math Assessment" shows the three track options.
  - Selecting "Grades 3–4" starts a test serving Grade 3 questions, and dynamic difficulty oscillates correctly between Grades 3 and 4 without exceeding those limits.
  - Selecting "Grades 5–6" starts a test serving Grade 5 and 6 questions.
  - The "View Past Results" button remains fully readable on hover.
