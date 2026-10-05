from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUT = Path(__file__).resolve().parent


def main() -> None:
    r = np.geomspace(0.01, 1.0, 240)
    inherited = r**3
    directional = r**2
    ratio = (inherited + directional) / inherited
    np.savetxt(
        OUT / "+rate_ray_data.csv",
        np.column_stack([r, inherited, directional, ratio]),
        delimiter=",",
        header="r,inherited_nuisance_lower_r3,directional_term_r2,full_to_inherited_ratio",
        comments="",
    )

    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 8.2,
            "axes.titlesize": 9,
            "axes.labelsize": 8.2,
            "legend.fontsize": 7.3,
            "xtick.labelsize": 7.3,
            "ytick.labelsize": 7.3,
            "axes.linewidth": 0.7,
        }
    )
    fig, axes = plt.subplots(1, 2, figsize=(6.55, 2.30), gridspec_kw={"width_ratios": [1.15, 1]})

    ax = axes[0]
    ax.loglog(r, inherited, color="#4C78A8", lw=1.8, label=r"Inherited $AB+M=r^3$")
    ax.loglog(r, directional, color="#E45756", lw=1.8, label=r"Missing $O$ or $P=r^2$")
    ax.fill_between(r, inherited, directional, color="#F2CF5B", alpha=0.27, linewidth=0)
    ax.set_xlabel(r"ray scale $r$")
    ax.set_ylabel("nuisance lower-bound order")
    ax.set_title("(a) Directional terms change the order", loc="left", fontweight="bold")
    ax.grid(True, which="major", lw=0.45, alpha=0.28)
    ax.legend(frameon=False, loc="lower right")
    ax.text(
        0.025,
        0.62,
        r"full / inherited $=1+r^{-1}$",
        transform=ax.transAxes,
        fontsize=7.4,
        bbox={"boxstyle": "round,pad=0.25", "facecolor": "white", "edgecolor": "0.75"},
    )
    ax.text(
        0.025,
        0.04,
        r"O-ray: $(a,t)=(r,r),\ b=s=0$" + "\n" + r"P-ray: $(b,s)=(r,r),\ a=t=0$",
        transform=ax.transAxes,
        fontsize=6.9,
    )

    ax = axes[1]
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 1)
    ax.axis("off")
    colors = ["#BAB0AC", "#59A14F", "#4C78A8"]
    labels = [
        ("E", r"$v_->B_0^2$", "empty\nexperiment"),
        ("I", r"$0<v_-<B_0^2$", r"$q+AB+M+O+P$"),
        ("S", r"$v_-=B_0^2$", "$\\pi_0=0$\nrate $q$"),
    ]
    for index, (short, condition, consequence) in enumerate(labels):
        x = index + 0.08
        rect = plt.Rectangle((x, 0.25), 0.84, 0.48, facecolor=colors[index], alpha=0.18, edgecolor=colors[index], lw=1.4)
        ax.add_patch(rect)
        ax.text(x + 0.42, 0.63, short, ha="center", va="center", fontsize=12, fontweight="bold", color=colors[index])
        ax.text(x + 0.42, 0.49, condition, ha="center", va="center", fontsize=7.2)
        ax.text(x + 0.42, 0.34, consequence, ha="center", va="center", fontsize=5.9, linespacing=1.0)
    ax.annotate("", xy=(1.02, 0.49), xytext=(0.92, 0.49), arrowprops={"arrowstyle": "-", "lw": 1, "color": "0.45"})
    ax.annotate("", xy=(2.02, 0.49), xytext=(1.92, 0.49), arrowprops={"arrowstyle": "-", "lw": 1, "color": "0.45"})
    ax.set_title("(b) Envelope geometry creates three strata", loc="left", fontweight="bold")
    ax.text(
        1.5,
        0.11,
        r"Uniform upper bound: $q/\sqrt{2}+4\omega$"
        + "\n"
        + r"$\omega=1-v_-/B_0^2$; no matching joint transition."
        + "\nInterior rate constants remain pointwise.",
        ha="center",
        va="center",
        fontsize=6.8,
        linespacing=1.2,
    )

    fig.tight_layout(pad=0.55, w_pad=1.2)
    for suffix in ("pdf", "svg", "png"):
        name = "theory_summary.pdf" if suffix == "pdf" else f"+theory_summary.{suffix}"
        fig.savefig(OUT / name, dpi=300, bbox_inches="tight")
        if suffix in ("svg", "png"):
            (OUT / f"theory_summary.{suffix}").write_bytes((OUT / name).read_bytes())
    plt.close(fig)


if __name__ == "__main__":
    main()
