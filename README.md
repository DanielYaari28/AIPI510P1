# AIPI510P1

# Rethinking University Rankings: The Untold Stories in Public Data

## Overview

Traditional university rankings often emphasize prestige, selectivity, and institutional reputation. This project explores the same question but in a different and more equitable light: how do university rankings change when we prioritize measurable student outcomes, affordability, accessibility, and student success?

Using publicly available higher-education data, the team developed a custom university ranking system based on four dimensions:

- Student Success — 40%
- Student Outcomes — 35%
- Affordability — 20%
- Accessibility — 5%

Each component is normalized so universities can be compared across different measures. These components are then combined into a single baseline score used to rank institutions based on the weifghts provided above.

The analysis also tests alternative scenarios (i.e. different weights based on the categories) to demonstrate how ranking methodology influences university rankings. Additionally, the project examines Duke University as a case study to show how dramatically an institution's position can change when different priorities are emphasized. This draws direct parallels to how US universities come out in rankings in other sites and publications, indicating biased looks on the universities.

### Key Questions

This project explores:

1. Which universities rank highest under the baseline methodology (top 10)?
2. What factors drive those rankings?
3. What is the relationship between affordability and student outcomes?
4. How sensitive are rankings to the weights assigned to different priorities?
5. Where does an individual university, such as Duke, fall under different ranking prioritiies?

---

## Dataset

This project uses publicly available data from the **U.S. Department of Education College Scorecard**.

The College Scorecard provides information about U.S. colleges and universities. The data that was utalized includes measures related to:

- Student outcomes
- Cost and affordability
- Graduation and retention
- Admissions and accessibility
- Earnings and other post-college outcomes

**Source:** U.S. Department of Education, College Scorecard.

The raw variables were cleaned and transformed into four primary ranking dimensions:

| Dimension | Description |
| --- | --- |
| Student Success | Measures related to students progressing through and completing college |
| Outcomes | Measures of student outcomes after attending the institution (via salary) |
| Affordability | Measures representing the financial accessibility/cost of attending and living |
| Accessibility | Measures representing how accessible an institution is to prospective students (via Pellgrants and a diversity index) |

---

## Ranking Methodology

The baseline university score is calculated as:

**Final Score = 0.40(Student Success) + 0.35(Outcomes) + 0.20(Affordability) + 0.05(Accessibility)**

Universities are then ranked from highest to lowest final score.

To test how subjective weighting decisions affect the rankings, the analysis also evaluates several alternative scenarios:

| Scenario | Success | Outcomes | Affordability | Accessibility |
| --- | ---: | ---: | ---: | ---: |
| Baseline | 40% | 35% | 20% | 5% |
| Equal | 25% | 25% | 25% | 25% |
| Success-focused | 70% | 20% | 5% | 5% |
| Outcome-focused | 30% | 45% | 15% | 10% |
| Affordability-focused | 30% | 20% | 40% | 10% |
| Accessibility-focused | 20% | 20% | 20% | 40% |

This sensitivity analysis illustrates that university rankings are not purely objective: the priorities chosen by the ranking methodology can materially change where an institution ranks.

---

## Visual Analysis

The project includes several visualizations designed to tell different parts of the ranking story.

Top 10 Universities: Shows the ten highest-ranked universities under the baseline system.

Category Breakdown: Compares the four categories for the Top 10 universities to show what drives their overall scores.

Affordability vs. Outcomes: Shows the relationship between affordability and student outcomes across universities and highlights where these top 10 institutions fall.

Duke Ranking Sensitivity: Shows how Duke University's rank changes when different ranking dimensions receive greater weight.

Score Distribution: Shows how baseline scores are distributed across all universities.

---

## Reproducing the Analysis

### 1. Clone the repository

```bash
git clone https://github.com/DanielYaari28/AIPI510P1.git
cd AIPI510P1
