import os
from enum import Enum
from scripts.copy_kb import copy_kb


class CopyKbPaths(Enum):
    KB = os.path.dirname(os.path.abspath(__file__))
    OSTIS = os.path.split(KB)[0]
    KB_COPY = os.path.join(OSTIS, 'ims.ostis.kb_copy')
    SCRIPTS = os.path.join(KB, 'scripts')

copy_kb(CopyKbPaths.KB.value, CopyKbPaths.KB_COPY.value)
scripts = [os.path.join(CopyKbPaths.SCRIPTS.value, 'remove_scsi.py')]
for script in scripts:
    if os.path.isfile(script) and script != 'copy_kb.py' and script.endswith('.py'):
        os.system("python3 " + script + ' ' + CopyKbPaths.KB_COPY.value)

