from dataclasses import dataclass
from typing import Dict
 
 
@dataclass
class SeverityResult:
    label: str
    score: int
    color: str
    advice: str
 
 
def classify_severity(
    class_name: str,
    confidence: float,
    area_pct: float,
    aspect_ratio: float = 1.0 
) -> SeverityResult:
    """
    Multi-factor severity classification.
    Combines: damage type, area, confidence, shape.
    """
    if area_pct > 5.0:    base = 8
    elif area_pct > 2.5:  base = 5
    elif area_pct > 1.0:  base = 3
    else:                  base = 1

    type_mod = 2 if class_name == 'pothole' else 0
 
    conf_mod = 1 if confidence > 0.7 else 0
 
    shape_mod = 1 if (class_name == 'pothole' and 0.5 < aspect_ratio < 2.0) else 0
 
    score = min(10, base + type_mod + conf_mod + shape_mod)
 
    if score >= 7:
        return SeverityResult(
            label='Severe', score=score, color='#CC0000',
            advice='Immediate repair required. Hazardous to vehicles.'
        )
    elif score >= 4:
        return SeverityResult(
            label='Moderate', score=score, color='#E07000',
            advice='Schedule repair within 2 weeks.'
        )
    else:
        return SeverityResult(
            label='Minor', score=score, color='#2E7D32',
            advice='Monitor and schedule routine maintenance.'
        )