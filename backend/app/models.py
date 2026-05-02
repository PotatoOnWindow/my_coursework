from tortoise import fields, models


class News(models.Model):
    id = fields.IntField(pk=True)

    title = fields.CharField(max_length=255)
    content = fields.TextField()

    source = fields.CharField(max_length=100, null=True)
    url = fields.CharField(max_length=500, null=True)

    tags = fields.CharField(max_length=255, null=True)  # "tech,ai,python"

    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.title
