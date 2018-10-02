from django.contrib import admin

from .models import Setor
from .models import Pessoas
from .models import Porta
from .models import Acesso
from .models import Registro
###################
from .models import Botao
from .models import Status
from .models import Registrobotao
###################

admin.site.register(Setor)
admin.site.register(Pessoas)
admin.site.register(Porta)
admin.site.register(Acesso)
admin.site.register(Registro)
admin.site.register(Botao)
admin.site.register(Status)
admin.site.register(Registrobotao)