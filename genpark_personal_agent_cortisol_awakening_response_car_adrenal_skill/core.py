# -*- coding: utf-8 -*-
"""Cortisol Awakening Response (CAR) & Adrenal Rhythm for GenPark Personal Agent."""
import json
from typing import Dict, Any

class CortisolAwakeningResponseAdrenalCopilot:
    """HPA axis diurnal rhythm, Cortisol Awakening Response (CAR), and photoperiod entrainment engine."""

    @staticmethod
    def audit_cortisol_awakening_curve(wake_cortisol_nmol_l: float, wake_plus_30m_cortisol_nmol_l: float, afternoon_cortisol_nmol_l: float, night_cortisol_nmol_l: float) -> Dict[str, Any]:
        """Assess the natural 50-75% morning cortisol rise (CAR) that energizes the body for the day."""
        car_delta = wake_plus_30m_cortisol_nmol_l - wake_cortisol_nmol_l
        car_rise_pct = round((car_delta / max(0.1, wake_cortisol_nmol_l)) * 100.0, 1)

        # Diurnal slope check: night cortisol should drop below 2.0 nmol/L
        elevated_nocturnal = night_cortisol_nmol_l > 3.5

        if car_rise_pct < 20.0:
            status = "FLATTENED_BURNOUT"
            clinical_risk = "Chronic exhaustion, hypocortisolemia, or severe burnout."
        elif car_rise_pct > 120.0 or wake_plus_30m_cortisol_nmol_l > 30.0:
            status = "HYPER_REACTIVE_ACUTE_STRESS"
            clinical_risk = "Hyperarousal, acute panic state, or chronic sympathetic overdrive."
        else:
            status = "NORMAL_HEALTHY"
            clinical_risk = "Robust resilient diurnal HPA axis dynamic."

        return {
            "wake_cortisol": wake_cortisol_nmol_l,
            "peak_30m_cortisol": wake_plus_30m_cortisol_nmol_l,
            "car_rise_percentage": car_rise_pct,
            "night_cortisol": night_cortisol_nmol_l,
            "rhythm_status": status,
            "nocturnal_suppression_ok": not elevated_nocturnal,
            "assessment": clinical_risk
        }

    @staticmethod
    def prescribe_circadian_light_pacing(car_curve_status: str, wake_time_hh_mm: str) -> Dict[str, Any]:
        """Deliver lux photon pacing protocol to re-calibrate retinal ipRGC ganglion cell signaling."""
        return {
            "status": car_curve_status,
            "morning_phototherapy": {
                "window": f"Within 30 minutes of waking ({wake_time_hh_mm})",
                "intensity_lux": "10,000 lux lamp (or 30 mins direct outdoor natural daylight)",
                "mechanism": "Suppresses melatonin synthesis and stimulates pituitary ACTH for healthy CAR spike."
            },
            "evening_blue_blocker_cadence": {
                "start_time": "T-3 hours before planned sleep",
                "spectral_notch": "Block 450-480nm melanopic wavelengths",
                "ambient_ceiling": "< 50 lux red/amber dim illumination"
            },
            "adrenal_support_recommendations": [
                "Ashwagandha (KSM-66 300mg) in evening if hyper-reactive night cortisol is elevated.",
                "Delay caffeine intake until 90-120 minutes post-waking to allow adenosine clearance."
            ]
        }
