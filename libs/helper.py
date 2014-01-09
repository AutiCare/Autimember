

import settings as settings
mainapp = settings.appsettings()

def debugprint(debugtext):
    if (settings.ENABLE_DEBUG == 1):
        print(debugtext)

