from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.name


class Paint(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='paints', verbose_name="Категорія")
    title = models.CharField(max_length=200, verbose_name="Назва фарби")
    brand = models.CharField(max_length=100, verbose_name="Бренд")
    color_code = models.CharField(max_length=50, verbose_name="Код кольору (RAL/HEX)")
    volume = models.FloatField(verbose_name="Об'єм (л)")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна (грн)")
    description = models.TextField(blank=True, verbose_name="Опис")
    # ВИПРАВЛЕНО: замінено upload_url на upload_to
    image = models.ImageField(upload_to='paints/', blank=True, verbose_name="Зображення")
    in_stock = models.BooleanField(default=True, verbose_name="В наявності")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Фарба"
        verbose_name_plural = "Фарби"

    def __str__(self):
        return f"{self.brand} {self.title} ({self.volume}л)"