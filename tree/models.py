from django.core.exceptions import ValidationError
from django.db import models


class Node(models.Model):
    parent = models.ForeignKey('tree.Node', on_delete=models.CASCADE, related_name='children', null=True)

    def save(self, *args, **kwargs):
        if self.parent and self.parent.children.count() >= 3 and self.pk is None:
            raise ValidationError("Too many children")
        #
        # if self.children.count() > 3:
        #     raise ValidationError("Too many children")

        return super(Node, self).save(*args, **kwargs)


class Tree(models.Model):
    parent_node = models.OneToOneField('tree.Node', on_delete=models.CASCADE)
