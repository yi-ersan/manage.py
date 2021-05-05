from django.db import models

# Create your models here.
class Task(models.Model):
    task_code = models.CharField(max_length=16, null=True)
    weld_method = models.CharField(max_length=32, null=True)
    worker_code = models.CharField(max_length=32, null=True)
    machine_code = models.CharField(max_length=32, null=True)
    product_code = models.CharField(max_length=32, null=True)
    process_card = models.CharField(max_length=256, null=True)
    weld_current = models.FloatField(null=True)
    weld_vol = models.FloatField(null=True)
    weld_power = models.FloatField(null=True)
    weld_speed = models.FloatField(null=True)
    weld_gas = models.CharField(max_length=16, null=True)
    app_test = models.NullBooleanField(null=True)
    ray_test = models.NullBooleanField(null=True)
    ray_test_prop = models.FloatField(null=True)
    other_test = models.NullBooleanField(null=True)
    other_test_method = models.CharField(max_length=32, null=True)


class Spot(models.Model):
    spot_code = models.CharField(max_length=32, null=True)
    task_code = models.ForeignKey('Task', on_delete=models.CASCADE)
    app_test_status = models.NullBooleanField(null=True)
    app_inspector_code = models.CharField(max_length=32, null=True, default='')
    app_defect_type = models.CharField(max_length=32, null=True, default='')
    app_test_result = models.CharField(max_length=16, null=True, default='')
    app_test_notes = models.TextField(null=True, default='')
    ray_test_status = models.NullBooleanField(null=True)
    ray_inspector_code = models.CharField(max_length=32, null=True, default='')
    ray_defect_type = models.CharField(max_length=32, null=True, default='')
    ray_test_result = models.CharField(max_length=16, null=True, default='')
    ray_test_notes = models.TextField(null=True, default='')
    app_defect_type_0 = models.NullBooleanField(null=True)
    app_defect_type_1 = models.NullBooleanField(null=True)
    app_defect_type_2 = models.NullBooleanField(null=True)
    app_defect_type_3 = models.NullBooleanField(null=True)
    app_defect_type_4 = models.NullBooleanField(null=True)
    app_defect_type_5 = models.NullBooleanField(null=True)


class WeldSpot(models.Model):
    spot_code = models.CharField(max_length=32, null=True)
    task_code = models.ForeignKey('Task', on_delete=models.CASCADE)
    app_test_status = models.NullBooleanField(null=True)
    app_inspector_code = models.CharField(max_length=32, null=True, default='')
    app_defect_type = models.CharField(max_length=32, null=True, default='')
    app_test_result = models.CharField(max_length=16, null=True, default='')
    app_test_notes = models.TextField(null=True, default='')
    ray_test_status = models.NullBooleanField(null=True)
    ray_inspector_code = models.CharField(max_length=32, null=True, default='')
    ray_defect_type = models.CharField(max_length=32, null=True, default='')
    ray_test_result = models.CharField(max_length=16, null=True, default='')
    ray_test_notes = models.TextField(null=True, default='')
    app_defect_type_0 = models.NullBooleanField(null=True)
    app_defect_type_1 = models.NullBooleanField(null=True)
    app_defect_type_2 = models.NullBooleanField(null=True)
    app_defect_type_3 = models.NullBooleanField(null=True)
    app_defect_type_4 = models.NullBooleanField(null=True)
    app_defect_type_5 = models.NullBooleanField(null=True)
