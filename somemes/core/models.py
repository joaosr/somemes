from django.db import models
from django.core.urlresolvers import reverse


def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


class Meme(models.Model):
    descricao = models.TextField('Descrição')
    imagem = models.ImageField('Imagem', upload_to=upload_location,
                               null=True,
                               blank=True,
                               default='no-img-professor.png')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Memes'
        verbose_name = 'Meme'

    def __str__(self):
        return self.descricao

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})

    @staticmethod
    def list_all():
        return Meme.objects.all().values()
