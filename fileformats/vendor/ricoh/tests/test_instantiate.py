"""
Pytest tests for EEG/MEG file format validation and metadata reading.

Test data is downloaded via MNE's dataset utilities and cached for the session.

Authors:
- Miao Cao

Email:
- miaocao@swin.edu.au
"""

from fileformats.vendor.ricoh.biosig import Kit

# ------------------------------
# MEG: KIT
# ------------------------------


def test_kit_instantiate(kit_sqd_path):
    Kit(kit_sqd_path)
