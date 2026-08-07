from __future__ import annotations

import numpy as np

def triangular(x: float, a: float, b: float, c: float) -> float:
    if x <= a or x >= c:
        return 0.0
    if x == b:
        return 1.0
    if x < b:
        return (x - a) / (b - a)
    return (c - x) / (c - b)

def left_shoulder(x: float, a: float, b: float) -> float:
    if x <= a:
        return 1.0
    if x >= b:
        return 0.0
    return (b - x) / (b - a)


def right_shoulder(x: float, a: float, b: float) -> float:
    if x <= a:
        return 0.0

    if x >= b:
        return 1.0

    return (x - a) / (b - a)

def fuzzify_pitch(pitch_difference: float) -> dict[str, float]:
    return {
        "perfect": left_shoulder(
            pitch_difference,
            0.0,
            0.5
        ),

        "good": triangular(
            pitch_difference,
            0.25,
            0.75,
            1.5
        ),

        "off": right_shoulder(
            pitch_difference,
            1.0,
            3.0
        )
    }


def fuzzify_timing(timing_difference: float) -> dict[str, float]:
    return {
        "accurate": left_shoulder(
            timing_difference,
            0.02,
            0.08
        ),

        "slightly_off": triangular(
            timing_difference,
            0.04,
            0.12,
            0.25
        ),

        "badly_off": right_shoulder(
            timing_difference,
            0.18,
            0.40
        )
    }


def fuzzify_loudness(loudness_difference: float) -> dict[str, float]:
    return {
        "good": left_shoulder(
            loudness_difference,
            0.05,
            0.20
        ),

        "slightly_off": triangular(
            loudness_difference,
            0.10,
            0.25,
            0.45
        ),

        "bad": right_shoulder(
            loudness_difference,
            0.35,
            0.60
        )
    }

def output_memberships(score: np.ndarray) -> dict[str, np.ndarray]:
    return {
        "poor": np.array([
            left_shoulder(value, 0, 35)
            for value in score
        ]),

        "okay": np.array([
            triangular(value, 20, 45, 65)
            for value in score
        ]),

        "good": np.array([
            triangular(value, 50, 70, 85)
            for value in score
        ]),

        "excellent": np.array([
            right_shoulder(value, 75, 95)
            for value in score
        ])
    }

def evaluate_rules(pitch: dict[str, float], timing: dict[str, float], loudness: dict[str, float]) -> dict[str, float]:
    rules = []

    # --------------------------------------------------------
    # EXCELLENT
    # --------------------------------------------------------

    rules.append(
        min(
            pitch["perfect"],
            timing["accurate"],
            loudness["good"]
        )
    )

    rules.append(
        min(
            pitch["perfect"],
            timing["accurate"]
        )
    )

    # --------------------------------------------------------
    # GOOD
    # --------------------------------------------------------

    rules.append(
        min(
            pitch["good"],
            timing["accurate"]
        )
    )

    rules.append(
        min(
            pitch["perfect"],
            timing["slightly_off"]
        )
    )
    rules.append(
        min(
            pitch["good"],
            timing["slightly_off"],
            loudness["good"]
        )
    )
    rules.append(
        min(
            pitch["perfect"],
            loudness["slightly_off"]
        )
    )
    # --------------------------------------------------------
    # OKAY
    # --------------------------------------------------------
    rules.append(
        min(
            pitch["good"],
            timing["badly_off"]
        )
    )
    rules.append(
        min(
            pitch["off"],
            timing["accurate"]
        )
    )
    rules.append(
        min(
            pitch["good"],
            loudness["slightly_off"]
        )
    )
    rules.append(
        min(
            pitch["perfect"],
            loudness["bad"]
        )
    )
    # --------------------------------------------------------
    # POOR
    # --------------------------------------------------------
    rules.append(
        pitch["off"]
    )
    rules.append(
        timing["badly_off"]
    )
    rules.append(
        loudness["bad"]
    )
    excellent = max(
        rules[0],
        rules[1]
    )
    good = max(
        rules[2],
        rules[3],
        rules[4],
        rules[5]
    )
    okay = max(
        rules[6],
        rules[7],
        rules[8],
        rules[9]
    )
    poor = max(
        rules[10],
        rules[11],
        rules[12]
    )
    return {
        "poor": poor,
        "okay": okay,
        "good": good,
        "excellent": excellent
    }

def defuzzify(aggregated_memberships: dict[str, float], resolution: int = 1001) -> float:
    universe = np.linspace(0, 100, resolution)
    output_sets = output_memberships(universe)
    aggregated = np.zeros_like(universe)
    for name, firing_strength in aggregated_memberships.items():
        clipped = np.minimum(output_sets[name], firing_strength)
        aggregated = np.maximum(aggregated, clipped)
    denominator = np.sum(aggregated)
    if denominator == 0:
        return 0.0
    numerator = np.sum(universe * aggregated)
    return float(numerator / denominator)

def fuzzy_note_score(pitch_difference: float, timing_difference: float, loudness_difference: float) -> float:
    pitch = fuzzify_pitch(max(0.0, pitch_difference))
    timing = fuzzify_timing(max(0.0, timing_difference))
    loudness = fuzzify_loudness(max(0.0, loudness_difference))
    rule_results = evaluate_rules(pitch, timing, loudness)
    score = defuzzify(rule_results)
    print(f"\nPitch difference:    {pitch_difference:.3f}")
    print(f"Timing difference:   {timing_difference:.3f}")
    print(f"Loudness difference: {loudness_difference:.3f}")
    print("\nMemberships:")
    print(f"Pitch:    {pitch}")
    print(f"Timing:   {timing}")
    print(f"Loudness: {loudness}")
    print("\nRule output:")
    print(rule_results)
    print(f"\nFuzzy score: {score:.2f}")
    print("------------------")
    return round(max(0.0, min(100.0, score)), 2)