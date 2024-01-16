from django.contrib import admin

from controlnes.models import nesModel


class nesModelAdmin(admin.ModelAdmin):
    fields = ['id','f_reg','aspirante','categoria','cel1','cel2','apoyo','observaciones','zona','status','f_exam','f_env_admi','r_exam','solicitud','f_audiencia','paq']
    list_display = ['id','f_reg','aspirante','categoria']
    search_fields = ['id','f_reg','aspirante','categoria','cel1','cel2','apoyo','observaciones','zona','status','f_exam','f_env_admi','r_exam','solicitud','f_audiencia','paq']



admin.site.register(nesModel, nesModelAdmin)
