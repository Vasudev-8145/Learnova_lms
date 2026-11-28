from django.db import models

from units.models import Modules

class Lessons(models.Model):

    lesson_number = models.PositiveIntegerField()

    module = models.ForeignKey(Modules,on_delete=models.CASCADE)

    title = models.CharField(max_length=200)

    description = models.TextField()

    duration = models.CharField(max_length=200)

    video_url = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):

        if not self.pk:

            last_lesson_object = Lessons.objects.filter(module=self.module).last()

            if last_lesson_object:

                self.lesson_number = last_lesson_object.lesson_number+1

            else:

                self.lesson_number = 1

        return super().save(*args,**kwargs)
    