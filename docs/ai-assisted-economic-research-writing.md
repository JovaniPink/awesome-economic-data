# AI-Assisted Economic Research and Writing

Reviewed August 30, 2026.

## Provenance and rights boundary

This is an original English guide, not a translation or republication.

Its workflow categories were inspired by [uinue2010/awesome-ai-research-writing-economics](https://github.com/uinue2010/awesome-ai-research-writing-economics), which identifies [Leey21/awesome-ai-research-writing](https://github.com/Leey21/awesome-ai-research-writing) as its upstream source. Neither repository exposed a recognized license during the August 30, 2026 review. This guide therefore does not copy their prompts, translate their prose, or reproduce their collections.

The templates below were written for this catalog. They add explicit evidence, privacy, causal-language, and verification boundaries. A later license or permission change should be reviewed separately before any direct translation is considered.

## Operating principles

AI can help reorganize, edit, question, and check supplied material. It is not the authority for a dataset, result, citation, institutional fact, or journal rule.

- Do not invent citations, DOI values, BibTeX, data, coefficients, or significance.
- Preserve the research question, sample, period, geography, units, variable definitions, model, and uncertainty supplied by the researcher.
- Use causal language only when the identification design and assumptions support it.
- Distinguish statistical significance, economic magnitude, prediction quality, and causal identification.
- Mark missing evidence instead of filling a gap with a plausible statement.
- Verify every citation, quotation, calculation, and factual claim against a primary source.
- Do not submit confidential, embargoed, proprietary, personally identifiable, or restricted data to an unapproved model or service.
- Check the current disclosure, authorship, data-use, and AI-assistance rules of the target journal and institution.
- Retain a human-readable change log for material edits and analytical suggestions.
- AI-assisted reviewer output is diagnostic feedback, not peer review.

## Recommended workflow

Use AI only after establishing the source and research boundaries.

1. Record the research question, population, period, estimand, identification strategy, and claim type.
2. Verify the data authority, units, revisions, access terms, and reproducible analysis path.
3. Build a claim-to-evidence table before drafting conclusions.
4. Use the narrowest writing or review template that fits the task.
5. Compare the output with the original text, tables, code, and sources.
6. Reject unsupported additions and restore any lost limitation or uncertainty.
7. Apply journal-specific formatting and disclosure rules only after checking their current primary documentation.

## Chinese Draft to English Economics Prose

Use this pattern to turn a researcher-supplied Chinese draft into restrained English economics prose. The researcher remains responsible for verifying the Chinese source, terminology, and evidence.

```text
Task: Rewrite the supplied Chinese draft as clear English economics prose.

Preserve exactly:
- Research question, population, geography, period, and units.
- Variable names, equations, estimates, uncertainty, and citation keys.
- Whether each statement is descriptive, predictive, associational, or causal.

Rules:
- Do not add evidence, citations, mechanisms, robustness checks, or policy claims.
- Use causal terms only when the input states a credible identification strategy.
- Keep LaTeX commands and mathematical notation intact.
- List any ambiguous term or missing definition after the draft instead of guessing.

Output:
1. Revised English text.
2. Ambiguities requiring author review.
3. Material wording changes that altered emphasis but not meaning.

Input:
[Paste the authorized Chinese draft and its research context.]
```

## English Economics Prose to a Chinese Reading Copy

Use this pattern to create a reading aid, not a substitute for the cited English source.

```text
Task: Produce a faithful Chinese reading copy of the supplied English economics text.

Rules:
- Preserve the direction and strength of every claim.
- Keep sample, period, units, variable names, estimates, and uncertainty visible.
- Do not strengthen association into causation or rewrite an author limitation.
- Preserve citation keys and identify any term without a clear conventional translation.
- Describe equations in readable language only when the user requests it; otherwise retain them.

Output:
1. Chinese reading copy.
2. Terminology choices requiring author confirmation.

Input:
[Paste the authorized English text.]
```

## Chinese Academic Rewriting

Use this pattern when the content is already in Chinese but needs a clearer economic argument.

```text
Task: Reorganize the supplied Chinese draft into concise academic prose.

Required sequence:
1. Research question or proposition.
2. Data or theoretical setting.
3. Identification or logical basis.
4. Result or implication.
5. Limitation where material.

Rules:
- Retain every supplied fact and qualification.
- Do not manufacture institutional background or literature support.
- Keep descriptive, predictive, and causal claims distinct.
- Flag missing definitions or logical steps for the author.

Input:
[Paste the draft, intended section, audience, and required terminology.]
```

## Careful Condensation

Use this pattern to reduce length without deleting evidence or changing the claim.

```text
Task: Reduce the supplied passage by the requested word or character target.

Must retain:
- Population, period, geography, units, and comparison group.
- Estimand, model, identification assumptions, and uncertainty.
- Main estimate, meaningful null result, limitation, and citation keys.

Remove first:
- Repeated transitions, duplicated definitions, and unsupported emphasis.
- Generic statements that do not change the argument.

Output:
1. Condensed text.
2. Exact items removed or combined.
3. Warning if the requested reduction cannot preserve the evidence contract.

Input:
[Paste the text and target length.]
```

## Evidence-Bounded Expansion

Expansion should clarify supplied reasoning, not create new findings.

```text
Task: Expand the supplied passage only by making its existing logic explicit.

Allowed additions:
- Definitions already supported by the supplied context.
- A clearer comparison, mechanism hypothesis, or limitation already present in the input.
- Transitions that connect the research question, design, and result.

Prohibited additions:
- New facts, citations, data, estimates, significance, mechanisms, or policy effects.
- Causal language stronger than the identification strategy supports.

Output:
1. Expanded text.
2. Added sentences mapped to their supporting input.
3. Evidence gaps that require research rather than prose expansion.

Input:
[Paste the passage and all authorized supporting context.]
```

## English Economics Editing

This pattern improves readability while retaining the analytical contract.

```text
Task: Edit the supplied English economics prose for clarity, precision, and flow.

Check:
- Research question and contribution are specific rather than promotional.
- Data, sample, period, and variables are defined before interpretation.
- Identification language matches the design.
- Estimates include units and an appropriate uncertainty statement.
- Statistical and economic significance are not conflated.
- Limitations remain visible.

Do not change citation keys, equations, variable names, numerical values, or claim strength without flagging the change.

Output:
1. Edited prose.
2. Claim-strength changes for author approval.
3. Missing evidence or definitions.

Input:
[Paste the passage and identify its paper section.]
```

## Chinese Economics Editing

Use this pattern for a Chinese-language economics paper or policy research document.

```text
Task: Edit the supplied Chinese economics text for formal, direct, evidence-bounded prose.

Check:
- One principal claim per paragraph.
- Consistent economic terminology and variable names.
- Clear distinction among institutional background, empirical design, result, and interpretation.
- No causal wording beyond the supplied identification design.
- No unsupported adjectives about novelty, importance, or policy effectiveness.

Output:
1. Edited Chinese text.
2. Terminology and logic questions.
3. Any sentence whose original meaning could not be preserved confidently.

Input:
[Paste the authorized text and target publication type.]
```

## Logic and Identification Review

Run this before polishing prose. Clear language cannot repair a missing comparison or invalid design.

```text
Task: Audit the supplied research argument and identification logic.

For every major claim, report:
- Claim type: descriptive, predictive, associational, causal, structural, or simulated.
- Supporting data, equation, design element, or cited authority.
- Required assumption.
- Main threat, such as confounding, reverse causality, selection, measurement error, leakage, or post-treatment control.
- Evidence that addresses the threat.
- Unresolved gap.

For DID, event study, IV, RDD, panel, forecasting, or simulation designs, apply the design-specific assumptions supplied by the researcher. Do not infer that an assumption passed merely because a method name appears.

Input:
[Paste the research question, design, data description, and claims.]
```

## Removing Formulaic AI Style from LaTeX Prose

The purpose is better writing, not concealment of prohibited AI use.

```text
Task: Revise the supplied LaTeX prose to remove repetition, vague transitions, generic praise, and formulaic phrasing.

Rules:
- Preserve commands, labels, references, equations, tables, citation keys, and escaped characters.
- Prefer concrete nouns and verbs tied to the research design.
- Do not add stylistic variation that changes the claim or hides uncertainty.
- Do not remove required AI-use disclosures, acknowledgments, or provenance.
- Return a change log for every sentence whose analytical emphasis changed.

Input:
[Paste the LaTeX passage and current disclosure requirements.]
```

## Removing Formulaic AI Style from Word Prose

Use this for plain text intended for Word or another rich-text editor.

```text
Task: Make the supplied prose direct and specific without changing its evidence.

Remove:
- Repeated summaries, empty topic sentences, exaggerated novelty, and generic conclusions.
- Unnecessary headings or list fragments when a paragraph is clearer.

Preserve:
- Numbers, units, citations, uncertainty, qualifications, and disclosure language.
- Author terminology unless a proposed replacement is listed for approval.

Output:
1. Clean plain text.
2. Change log.
3. Claims that still need evidence.

Input:
[Paste the passage and intended audience.]
```

## Research-Design Figures

A design figure should expose the source of variation and limits, not decorate the paper.

```text
Task: Specify a research-design figure from the supplied study design.

Include only supported elements:
- Units, treatment or exposure, comparison, timing, assignment rule, mechanism hypothesis, and outcome.
- Identification source for DID, event study, IV, RDD, panel, experiment, forecast, or simulation.
- Dashed or otherwise qualified arrows for hypotheses or associations that are not identified causal paths.

Return:
1. Recommended diagram type and reading order.
2. Nodes, arrows, labels, and legend.
3. Accessibility requirements, including grayscale distinction and alt text.
4. Claims the figure must not imply.

Input:
[Paste the verified research design and claim boundary.]
```

## Empirical Chart Selection

Choose a chart from the inferential task, not from visual novelty.

```text
Task: Recommend one primary and, if necessary, one supporting empirical chart.

Match the chart to the question:
- Event-study estimates with confidence intervals for dynamic treatment effects and pre-trends.
- Treatment and comparison trends for descriptive DID context.
- Binned or raw scatterplots with bandwidth and fit details for RDD.
- Coefficient or forest plots for estimates across outcomes or subgroups.
- Histograms, densities, or empirical distributions for sample and placebo diagnostics.
- Time series, maps, or small multiples for descriptive temporal and geographic structure.

Report axes, units, uncertainty, reference category, weighting, sample restrictions, and accessibility. Do not add significance markers when the input lacks the required statistics.

Input:
[Paste the verified data description, estimates, and communication goal.]
```

## Figure Titles

Titles should name the quantity and comparison without announcing a conclusion the figure cannot prove.

```text
Task: Draft three concise English figure titles.

Each title must identify the outcome, comparison or design, and period or geography when needed. Prefer established forms such as Event-Study Estimates of, Trends in, Distribution of, or Binned Relationship Between. Avoid claims such as proves, drives, or causes unless the supplied design supports them.

Input:
[Paste the figure content, units, population, and claim type.]
```

## Table Titles

Table titles should distinguish descriptive statistics, estimates, and robustness evidence.

```text
Task: Draft three concise English table titles.

Use a title family that matches the content, such as Summary Statistics, Baseline Estimates, First-Stage Estimates, Robustness Checks, Heterogeneous Associations, or Forecast Evaluation. Include the outcome, population, or period when omission would make the title ambiguous. Do not imply causality or statistical significance not established in the table.

Input:
[Paste the table purpose, columns, sample, and design.]
```

## Empirical-Results Analysis

The model may organize supplied results but must not infer unavailable statistics.

```text
Task: Analyze the supplied empirical table or machine-readable results.

For each main estimate, report:
- Direction, magnitude, unit, comparison, and uncertainty.
- Statistical significance only from supplied standard errors, intervals, or tests.
- Economic magnitude relative to a stated baseline when available.
- Stability across prespecified specifications or samples.
- Whether the design supports descriptive, predictive, associational, or causal language.

State null, unstable, or contradictory findings directly. Do not calculate missing standard errors, invent a reference mean, or choose a preferred specification after seeing outcomes.

Output:
1. Evidence table.
2. Draft results prose.
3. Verification checklist tied to table cells or artifact paths.

Input:
[Paste the verified table and its variable dictionary.]
```

## Reviewer Simulation

AI-assisted reviewer output is diagnostic feedback, not peer review.

```text
Task: Produce a constructive pre-submission review of the supplied manuscript and evidence package.

Separate:
- Fatal or design-level concerns.
- Important but repairable analysis gaps.
- Reporting, reproducibility, and exposition problems.
- Minor presentation issues.

Evaluate the research question, contribution, data authority, measurement, identification, specification, uncertainty, robustness, mechanism evidence, external validity, reproducibility, and claim boundaries. Cite page, section, table, figure, equation, or artifact locations for each concern. Do not invent journal policy or predict acceptance.

Input:
[Provide the authorized manuscript, appendix, code and data notes, and target-audience criteria.]
```

## Model and Tool Selection

Choose tools by task, authority, privacy, and verification needs rather than popularity.

```text
Task: Recommend an AI-assisted workflow for the supplied economics research task.

For each proposed tool or model, report:
- Narrow task it may perform.
- Inputs it may receive and data it must not receive.
- Required human verification.
- Citation, privacy, reproducibility, and disclosure risks.
- Non-AI alternative when the task requires exact computation or source authority.

Prefer deterministic code for transformations, estimates, tables, and figures. Use retrieval only against authorized sources. Do not ask a language model to supply missing observations, citations, identification, or statistical evidence.

Input:
[Describe the task, data classification, software environment, output, and governing rules.]
```

## Final verification checklist

Before using any AI-assisted output in research:

- Compare all numbers with the authoritative table, data artifact, or executed code.
- Open every citation and confirm authors, title, venue, date, DOI, and supported claim.
- Recheck equations, signs, units, samples, reference groups, and uncertainty.
- Confirm that predictive accuracy has not been rewritten as causal evidence.
- Confirm that simulated behavior has not been rewritten as observed behavior.
- Confirm that limitations, null results, and contradictory evidence remain visible.
- Review tracked changes and retain author responsibility for the final text.
- Follow current journal, employer, funder, data-provider, and institutional rules.
