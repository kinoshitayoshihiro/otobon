# --- START OF FILE utilities/__init__.py (役割特化・修正版) ---
"""
utilities package -- 音楽生成プロジェクト全体で利用されるコアユーティリティ群
--------------------------------------------------------------------------
公開API:
    - core_music_utils:
        - MIN_NOTE_DURATION_QL
        - get_time_signature_object
        - sanitize_chord_label
        - get_music21_chord_object (sanitize_chord_label を内部で使用)
    - scale_registry:
        - build_scale_object
        - ScaleRegistry (クラス)
    - humanizer:
        - generate_fractional_noise
        - apply_humanization_to_element
        - apply_humanization_to_part
        - HUMANIZATION_TEMPLATES
        - NUMPY_AVAILABLE
"""

from .core_music_utils import (
    MIN_NOTE_DURATION_QL,
    get_time_signature_object,
    sanitize_chord_label,
    get_music21_chord_object # これも公開すると便利
)

from .scale_registry import (
    build_scale_object,
    ScaleRegistry
)

from .humanizer import (
    generate_fractional_noise,
    apply_humanization_to_element,
    apply_humanization_to_part,
    HUMANIZATION_TEMPLATES,
    NUMPY_AVAILABLE,
)

__all__ = [
    "MIN_NOTE_DURATION_QL", "get_time_signature_object", "sanitize_chord_label", "get_music21_chord_object",
    "build_scale_object", "ScaleRegistry",
    "generate_fractional_noise", "apply_humanization_to_element", "apply_humanization_to_part",
    "HUMANIZATION_TEMPLATES", "NUMPY_AVAILABLE",
]
# --- END OF FILE utilities/__init__.py ---