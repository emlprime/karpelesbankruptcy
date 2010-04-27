from django.contrib import admin

from karpelesbankruptcy.content.models import HomeText, AboutBankruptcyText, LoanModificationsText, AboutText, ResourcesText, ContactText, Chapter13Text, Chapter11Text, Chapter7Text, ReliefFromStayText, DisclaimerText

class HomeTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(HomeText, HomeTextAdmin)

class AboutTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(AboutText, AboutTextAdmin)

class LoanModificationsTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(LoanModificationsText, LoanModificationsTextAdmin)

class ReliefFromStayTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(ReliefFromStayText, ReliefFromStayTextAdmin)

class AboutBankruptcyTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(AboutBankruptcyText, AboutBankruptcyTextAdmin)

class ContactTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(ContactText, ContactTextAdmin)

class Chapter7TextAdmin(admin.ModelAdmin):
    pass
admin.site.register(Chapter7Text, Chapter7TextAdmin)

class Chapter11TextAdmin(admin.ModelAdmin):
    pass
admin.site.register(Chapter11Text, Chapter11TextAdmin)

class Chapter13TextAdmin(admin.ModelAdmin):
    pass
admin.site.register(Chapter13Text, Chapter13TextAdmin)

class DisclaimerTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(DisclaimerText, DisclaimerTextAdmin)

class ResourcesTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(ResourcesText, ResourcesTextAdmin)
