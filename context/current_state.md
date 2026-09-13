# Current Research State

_Last updated: 2026-09-13_

## Active investigation

Understand the origin and structure of the one-loop corrections to the
Newtonian gravitational potential in effective quantum gravity.

The current reference point is Eq. 20 in Donoghue's treatment and the
calculation underlying it.

## Current conceptual focus

Important issues currently being investigated include:

- the relationship between scattering amplitudes and effective potentials;
- the origin of classical contributions from loop diagrams;
- the distinction between analytic and nonanalytic momentum dependence;
- triangle, bubble, box, and related one-loop topologies;
- Passarino-Veltman loop-integral notation;
- how the specific scattering process determines where classical and quantum
  pieces appear in perturbation theory.

## Computational status

Mathematica is being used for the calculation.

FeynCalc and FeynGrav are relevant computational tools.

Some loop-integral exploration has already been performed, including scalar
triangle integrals and Passarino-Veltman representations.

The new VS Code-centered environment is being established so calculations can
be edited, executed, version controlled, and connected directly to the
research notes.

## Next physics direction

After the standard one-loop correction is understood sufficiently well,
investigate how additional terms allowed in the gravitational EFT Lagrangian
affect the correction to the potential.

In particular:

1. identify relevant higher-derivative / curvature operators;
2. determine how they modify vertices and propagators;
3. identify which one-loop amplitudes are affected;
4. isolate long-distance nonanalytic contributions;
5. determine whether they modify classical terms, quantum terms, or only
   short-distance/contact contributions.

## Immediate infrastructure task

Finish constructing the VS Code research environment.

Next setup stages:

1. establish project context files;
2. establish backup/version control for the Obsidian vault;
3. install and configure an AI coding agent;
4. connect Mathematica execution through `wolframscript`.