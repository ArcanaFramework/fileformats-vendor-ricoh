import typing as ty

import mne.io

from fileformats.core import extra_implementation, FileSet
from fileformats.vendor.ricoh.biosig import Kit


@extra_implementation(FileSet.read_metadata)
def kit_read_metadata(kit: Kit, **kwargs: ty.Any) -> ty.Mapping[str, ty.Any]:
    return mne.io.read_raw_kit(kit, mrk=kit.mark_file, verbose=False).info.to_json_dict()  # type: ignore[no-any-return]
