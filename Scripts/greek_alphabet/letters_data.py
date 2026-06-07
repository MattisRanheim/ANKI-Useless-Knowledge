# -*- coding: utf-8 -*-
"""
Greek letters as used in mathematics.

Each entry: (symbol, name, form, latex)

Scope (a math-relevant subset of the Greek alphabet, 40 symbols):
  * 23 lowercase letters — the full lowercase alphabet except omicron, which is
    identical to a Latin 'o' and is not used in mathematics.
  * 10 uppercase letters whose glyph is distinct from a Latin letter and is
    actually used in math (Gamma, Delta, Theta, Lambda, Xi, Pi, Sigma, Phi,
    Psi, Omega). The other capitals (Alpha=A, Beta=B, ...) are omitted because
    they are indistinguishable from Roman letters.
  * 7 variant lowercase forms that math uses as separate symbols (e.g. the
    lunate epsilon, the script theta, the final sigma).

The `latex` field gives the command that renders each glyph: note that the
plain lowercase epsilon/phi here are the \\var- forms (the shapes most people
hand-write), and the lunate/straight shapes are the variants.
"""

LETTERS = [
    # ── Lowercase alphabet (omicron omitted: identical to Latin 'o') ──────────
    ("α", "Alpha",   "lowercase", "\\alpha"),
    ("β", "Beta",    "lowercase", "\\beta"),
    ("γ", "Gamma",   "lowercase", "\\gamma"),
    ("δ", "Delta",   "lowercase", "\\delta"),
    ("ε", "Epsilon", "lowercase", "\\varepsilon"),
    ("ζ", "Zeta",    "lowercase", "\\zeta"),
    ("η", "Eta",     "lowercase", "\\eta"),
    ("θ", "Theta",   "lowercase", "\\theta"),
    ("ι", "Iota",    "lowercase", "\\iota"),
    ("κ", "Kappa",   "lowercase", "\\kappa"),
    ("λ", "Lambda",  "lowercase", "\\lambda"),
    ("μ", "Mu",      "lowercase", "\\mu"),
    ("ν", "Nu",      "lowercase", "\\nu"),
    ("ξ", "Xi",      "lowercase", "\\xi"),
    ("π", "Pi",      "lowercase", "\\pi"),
    ("ρ", "Rho",     "lowercase", "\\rho"),
    ("σ", "Sigma",   "lowercase", "\\sigma"),
    ("τ", "Tau",     "lowercase", "\\tau"),
    ("υ", "Upsilon", "lowercase", "\\upsilon"),
    ("φ", "Phi",     "lowercase", "\\varphi"),
    ("χ", "Chi",     "lowercase", "\\chi"),
    ("ψ", "Psi",     "lowercase", "\\psi"),
    ("ω", "Omega",   "lowercase", "\\omega"),

    # ── Uppercase (distinct from Latin, used in math) ────────────────────────
    ("Γ", "Gamma",   "uppercase", "\\Gamma"),
    ("Δ", "Delta",   "uppercase", "\\Delta"),
    ("Θ", "Theta",   "uppercase", "\\Theta"),
    ("Λ", "Lambda",  "uppercase", "\\Lambda"),
    ("Ξ", "Xi",      "uppercase", "\\Xi"),
    ("Π", "Pi",      "uppercase", "\\Pi"),
    ("Σ", "Sigma",   "uppercase", "\\Sigma"),
    ("Φ", "Phi",     "uppercase", "\\Phi"),
    ("Ψ", "Psi",     "uppercase", "\\Psi"),
    ("Ω", "Omega",   "uppercase", "\\Omega"),

    # ── Variant lowercase forms used as distinct math symbols ─────────────────
    ("ϵ", "Epsilon", "lowercase variant (lunate)", "\\epsilon"),
    ("ϑ", "Theta",   "lowercase variant (script)", "\\vartheta"),
    ("ϰ", "Kappa",   "lowercase variant",          "\\varkappa"),
    ("ϖ", "Pi",      "lowercase variant",          "\\varpi"),
    ("ϱ", "Rho",     "lowercase variant",          "\\varrho"),
    ("ς", "Sigma",   "lowercase (final form)",     "\\varsigma"),
    ("ϕ", "Phi",     "lowercase variant (straight)", "\\phi"),
]
