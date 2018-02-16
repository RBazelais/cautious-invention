from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Ninjas(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo_id = models.IntegerField()    def __str__(self):
        return self.first_name

# >>> from apps.dojo_ninjas.models import *
# >>> Dojo.objects.create(name="CodingDojo Silicon Valley", city="Mountain View", state="CA")
# <Dojo: CodingDojo Silicon Valley>
# >>> Dojo.objects.create(name="CodingDojo Seattle", city="Seattle", state="WA")
# <Dojo: CodingDojo Seattle>
# >>> Dojo.objects.create(name="CodingDojo New York", city="New York", state="NY")
# <Dojo: CodingDojo New York>
# >>> Ninjas.objects.create(first_name="Jim", last_name="Henson", dojo_id=0)
# <Ninjas: Jim>
# >>> Ninjas.objects.create(first_name="Chris", last_name="Benot", dojo_id=0)
# <Ninjas: Chris>
# >>> Ninjas.objects.create(first_name="Cherrise", last_name="Varga", dojo_id=0)
# <Ninjas: Cherrise>
# >>> Ninjas.objects.create(first_name="Omar", last_name="Shah", dojo_id=0)
# <Ninjas: Omar>
# >>> Ninjas.objects.create(first_name="Yuri", last_name="Puletski", dojo_id=0)
# <Ninjas: Yuri>
# >>> Ninjas.objects.create(first_name="Rebecca", last_name="Owens", dojo_id=0)
# <Ninjas: Rebecca>
# >>> Ninjas.objects.create(first_name="T'Challa", last_name="Black", dojo_id=0)
# <Ninjas: T'Challa>
# >>> Ninjas.objects.create(first_name="Sombra", last_name="Hernandez", dojo_id=0)
# <Ninjas: Sombra>
# >>> Ninjas.objects.create(first_name="Shakia", last_name="Brown", dojo_id=0)
# <Ninjas: Shakia>
# >>> Dojo.objects.create(name="CodingDojo Chicago", city="Chicago", state="IL")
# <Dojo: CodingDojo Chicago>
# >>> Dojo.objects.create(name="CodingDojo Los Angeles", city="Los Angeles", state="CA")
# <Dojo: CodingDojo Los Angeles>
# >>> Dojo.objects.create(name="CodingDojo Washington D.C.", city="Washington D.C.", state="DC")
# <Dojo: CodingDojo Washington D.C.>
# >>> Dojo.objects.all()
# <QuerySet [<Dojo: CodingDojo Silicon Valley>, <Dojo: CodingDojo Seattle>, <Dojo: CodingDojo New York>, <Dojo: CodingDojo Chicago>, <Dojo: CodingDojo Los Angeles>, <Dojo: CodingDojo Washington D.C.>]>
# >>> Dojo.objects.get(id=1).delete())

# >>> Dojo.objects.get(id=1).delete()
# (1, {u'dojo_ninjas.Dojo': 1})
# >>> Dojo.objects.get(id=4).delete()
# (1, {u'dojo_ninjas.Dojo': 1})
# >>> Dojo.objects.get(id=6).delete()
# (1, {u'dojo_ninjas.Dojo': 1})
# >>> Dojo.objects.all()
# <QuerySet [<Dojo: CodingDojo Seattle>, <Dojo: CodingDojo New York>, <Dojo: CodingDojo Los Angeles>]>
# >>> Ninjas.objects.all()
# <QuerySet [<Ninjas: Jim>, <Ninjas: Chris>, <Ninjas: Cherrise>, <Ninjas: Omar>, <Ninjas: Yuri>, <Ninjas: Rebecca>, <Ninjas: T'Challa>, <Ninjas: Sombra>, <Ninjas: Shakia>]>
# >>> Ninjas.objects.get(id=1).update(dojo_id=1)

# >>> jim = Ninjas.objects.get(id=1)
# >>> jim.dojo_id = 1
# >>> jim.save()
# >>> chris = Ninjas.objects.get(id=2)
# >>> chris.dojo_id = 2
# >>> chris.save()
# >>> cherisse = Ninjas.objects.get(id=3)
# >>> cherisse.dojo_id = 1
# >>> cherisee.save()

# >>> cherisse.save()
# >>> Omar = Ninjas.object.get(id=4)

# >>> Omar = Ninjas.objects.get(id=4)
# >>> Omar.dojo_id =1
# >>> Omar.save()
# >>> Ninjas.objects.all()
# <QuerySet [<Ninjas: Jim>, <Ninjas: Chris>, <Ninjas: Cherrise>, <Ninjas: Omar>, <Ninjas: Yuri>, <Ninjas: Rebecca>, <Ninjas: T'Challa>, <Ninjas: Sombra>, <Ninjas: Shakia>]>
# >>> yuri = Ninjas.objects.get(id=5)
# >>> yrui.dojo_id=2

# >>> yuri.dojo_id=2
# >>> yuri.save()
# >>> reb = Ninjas.objects.get(id=6)
# >>> reb.dojo_id=2
# >>> reb.save()

# >>> tchalla = Ninjas.objects.get(id=7)
# >>> tchalla.dojo_id=3
# >>> tchalla.save()
# >>> sombra = Ninjas.objects.get(id=8)
# >>> sombra.dojo_id = 3
# >>> sombra.save()

# >>> sakia = Ninjas.objects.get(id=9)
# >>> sakia.dojo_id = 3
# >>> sakia.save()
# >>> Dojo.Objects.all()

# Dojo.objects.all()
# <QuerySet [<Dojo: CodingDojo Seattle>, <Dojo: CodingDojo New York>, <Dojo: CodingDojo Los Angeles>]>
# >>> Dojo.objects.first().get(Ninjas.objects.get(dojo_id=1)