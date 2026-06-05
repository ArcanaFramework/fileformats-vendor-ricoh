"""
Pytest tests for EEG/MEG file format validation and metadata reading.

Test data is downloaded via MNE's dataset utilities and cached for the session.

Authors:
- Miao Cao

Email:
- miaocao@swin.edu.au
"""

from fileformats.biosig import Kit

# ------------------------------
# MEG: KIT
# ------------------------------


def test_kit_read_metadata(kit_sqd_path):
    metadata = Kit(kit_sqd_path).metadata
    assert isinstance(metadata, dict)
    assert metadata["sfreq"] is not None
