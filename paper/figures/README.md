# Figure 1 reproduction

From the manuscript source-tree root, run:

```text
<PYTHON_EXECUTABLE> figures/+generate_theory_summary.py
```

The script requires Python with NumPy and Matplotlib. It writes the analytic
ray data to `+rate_ray_data.csv` and figures to `theory_summary.pdf`,
`+theory_summary.svg`, and `+theory_summary.png` in `figures/`. It also copies
the SVG and PNG outputs byte-for-byte to the existing `theory_summary.svg`
and `theory_summary.png` counterparts, so every figure copy shows the current result. The CSV and raster PNG
are expected to reproduce byte-for-byte in the audited environment. PDF
creation timestamps and automatically generated SVG element identifiers may
differ without changing plotted content.

The figure contains analytic formulas only. It contains no empirical
measurements or simulated performance evidence.

Panel (a) retains the exact analytic ray formulas and data. Panel (b) shows
the three envelope strata and the uniform numerical upper bound
`q/sqrt(2) + 4*omega`, with `omega = 1 - v_-/B_0^2`, for the fixed-denominator
clipped moment estimator under the average-variance condition. Interior rate
constants remain pointwise; a matching joint transition is not claimed.
