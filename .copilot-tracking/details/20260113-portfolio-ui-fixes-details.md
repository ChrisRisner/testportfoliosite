<!-- markdownlint-disable-file -->
# Task Details: Portfolio UI Fixes

## Research Reference

**Source Research**: .copilot-tracking/research/20260113-portfolio-ui-fixes-research.md

## Phase 1: Style Updates

### Task 1.1: Reposition Social Links in CSS

Remove the auto margin from social links to prevent them from sticking to the bottom of the sidebar.

* **Files**:
  * [src/static/style.css](src/static/style.css) - Main stylesheet
* **Success**:
  * Social links section follows the flow of the document (appears after navigation)
* **Research References**:
  * .copilot-tracking/research/20260113-portfolio-ui-fixes-research.md (Lines 61-69) - CSS Fix Example
  * .copilot-tracking/research/20260113-portfolio-ui-fixes-research.md (Lines 80-87) - Technical Scenario 1
* **Dependencies**:
  * None

## Phase 2: Template Updates

### Task 2.1: Add Active Class Logic to Navigation

Update the navigation loop in the main template to strictly apply the 'active' class when the current album matches the link.

* **Files**:
  * [src/templates/index.html](src/templates/index.html) - Main layout template
* **Success**:
  * Navigation link for the current album has `class="nav-link active"`
  * Other navigation links have `class="nav-link"`
* **Research References**:
  * .copilot-tracking/research/20260113-portfolio-ui-fixes-research.md (Lines 72-76) - Template Fix Example
  * .copilot-tracking/research/20260113-portfolio-ui-fixes-research.md (Lines 89-95) - Technical Scenario 2
* **Dependencies**:
  * `current_album` context variable availability (Confirmed in Research)

## Dependencies

* Python Environment

## Success Criteria

* Visual inspection shows social links moved up
* Visual inspection shows active link highlighted
