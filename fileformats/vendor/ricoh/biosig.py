from fileformats.core.mixin import WithAdjacentFiles
from fileformats.core.exceptions import FormatMismatchError
from fileformats.generic import File, BinaryFile, UnicodeFile

from fileformats.biosig import Meg


class KitMark(BinaryFile):
    """Marker"""

    ext = ".mrk"


class KitHeadPosition(UnicodeFile):
    ext = ".elp"


class KitSensorInfo(File):
    ext = ".hsj"


class Kit(WithAdjacentFiles, Meg, BinaryFile):
    """
    KIT/RIKEN (Ricon) MEG format (directory-based)
    Required files:
    - Main data file (.sqd or .con)
    Optional files: .mrk (marker/coregistration), .elp (head position), .hsj (sensor info)
    """

    ext = ".sqd"
    alternate_exts = (".con",)

    marker_generic_names = ("marker.mrk", "markers.mrk", "kit.mrk")

    @property
    def mark_file(self) -> KitMark | None:
        try:
            mrk_path = self.select_by_ext(KitMark)
            return KitMark(mrk_path)
        except FormatMismatchError:
            pass
        for cand in self.marker_generic_names:
            mrk_path = self.parent / cand
            if mrk_path.exists():
                return KitMark(mrk_path)
        return None

    @property
    def head_position_file(self) -> KitHeadPosition | None:
        try:
            return KitHeadPosition(self.select_by_ext(KitHeadPosition))
        except FormatMismatchError as e:
            if e.args[0].startswith("No matching files"):
                return None
            raise

    @property
    def sensor_info_file(self) -> KitSensorInfo | None:
        try:
            return KitSensorInfo(self.select_by_ext(KitSensorInfo))
        except FormatMismatchError as e:
            if e.args[0].startswith("No matching files"):
                return None
            raise
