"""Prototype DSP utilities for HearForge.

The functions here are safe, testable Python prototypes. Production live audio
should move the low-latency loop to native Android audio such as Oboe/AAudio.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List


@dataclass
class DSPSettings:
    gain_db: float = 6.0
    speech_boost: bool = True
    noise_reduction: bool = True
    safety_limiter: bool = True
    limiter_ceiling: float = 0.85
    compressor_threshold: float = 0.35
    compressor_ratio: float = 4.0


def db_to_linear(db: float) -> float:
    return 10 ** (db / 20.0)


def clamp(sample: float, ceiling: float = 0.85) -> float:
    return max(-ceiling, min(ceiling, sample))


def noise_gate(sample: float, floor: float = 0.015, attenuation: float = 0.25) -> float:
    if abs(sample) < floor:
        return sample * attenuation
    return sample


def compressor(sample: float, threshold: float = 0.35, ratio: float = 4.0) -> float:
    sign = 1.0 if sample >= 0 else -1.0
    x = abs(sample)
    if x <= threshold:
        return sample
    compressed = threshold + (x - threshold) / max(ratio, 1.0)
    return sign * compressed


def speech_presence_boost(sample: float, amount: float = 1.12) -> float:
    """Simple scalar placeholder for speech band enhancement.

    Real implementation should use band-pass filters around voice frequencies.
    """
    return sample * amount


def process_frame(samples: Iterable[float], settings: DSPSettings | None = None) -> List[float]:
    settings = settings or DSPSettings()
    gain = db_to_linear(settings.gain_db)
    processed: List[float] = []

    for raw in samples:
        sample = float(raw)
        if settings.noise_reduction:
            sample = noise_gate(sample)
        sample *= gain
        if settings.speech_boost:
            sample = speech_presence_boost(sample)
        sample = compressor(sample, settings.compressor_threshold, settings.compressor_ratio)
        if settings.safety_limiter:
            sample = clamp(sample, settings.limiter_ceiling)
        processed.append(sample)

    return processed
