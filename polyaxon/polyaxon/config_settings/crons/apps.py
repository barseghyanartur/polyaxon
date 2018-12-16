from ..apps import *
from ..auditor_apps import AUDITOR_APPS

PROJECT_APPS = AUDITOR_APPS + (
    'stores.apps.StoresConfig',
    'crons.apps.CronsConfig',
)

INSTALLED_APPS += PROJECT_APPS
