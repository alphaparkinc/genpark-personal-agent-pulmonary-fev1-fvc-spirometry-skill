# -*- coding: utf-8 -*-
"""Pulmonary Spirometry & Vital Capacity Screener for GenPark Personal Agent."""
import json
from typing import Dict, Any

class PulmonarySpirometryVitalCapacityScreener:
    @staticmethod
    def calculate_tiffeneau_spirometry_index(fev1_liters: float, fvc_liters: float, predicted_fev1_liters: float = 3.8) -> Dict[str, Any]:
        ratio_pct = round((fev1_liters / max(0.1, fvc_liters)) * 100.0, 1)
        fev1_pct_predicted = round((fev1_liters / max(0.1, predicted_fev1_liters)) * 100.0, 1)
        
        # GOLD Criteria: FEV1/FVC < 70% defines obstructive limitation
        if ratio_pct < 70.0:
            pattern = "OBSTRUCTIVE_AIRWAY_DEFICIT (Asthma / COPD Pattern)"
        elif fev1_pct_predicted < 80.0 and ratio_pct >= 70.0:
            pattern = "RESTRICTIVE_VENTILATORY_PATTERN_SUSPECTED"
        else:
            pattern = "NORMAL_PULMONARY_VENTILATORY_FUNCTION"
            
        return {
            "fev1_liters": fev1_liters,
            "fvc_liters": fvc_liters,
            "tiffeneau_index_fev1_fvc_pct": ratio_pct,
            "fev1_pct_of_predicted": fev1_pct_predicted,
            "clinical_spirometry_classification": pattern
        }

    @staticmethod
    def synthesize_respiratory_muscle_training_protocol(fev1_pct_predicted: float) -> Dict[str, Any]:
        return {
            "inspiratory_muscle_training_imt": [
                "Inspiratory threshold device (PowerBreathe) set to 40% maximal inspiratory pressure (MIP)",
                "30 breaths twice daily for 6 weeks",
                "Diaphragmatic box breathing (4s in, 4s hold, 4s out, 4s hold) for autonomic regulation"
            ],
            "expected_functional_gain": "5-12% improvement in maximal voluntary ventilation and reduced perception of exertional dyspnea."
        }
