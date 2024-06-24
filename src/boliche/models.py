# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Barra(models.Model):
    id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    nombre = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'barra'


class Bebida(models.Model):
    id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    nombre = models.CharField(max_length=100)
    cantidad_ml = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'bebida'


class DetalleBarra(models.Model):
    id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    empleado = models.ForeignKey('Empleado', models.DO_NOTHING, db_column='empleado', blank=True, null=True)
    barra = models.ForeignKey(Barra, models.DO_NOTHING, db_column='barra', blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.barra)

    class Meta:
        managed = False
        db_table = 'detalle_barra'


class DetalleTrago(models.Model):
    id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    bebida = models.ForeignKey(Bebida, models.DO_NOTHING, db_column='bebida', blank=True, null=True)
    trago = models.ForeignKey('Trago', models.DO_NOTHING, db_column='trago', blank=True, null=True)
    
    def __str__(self):
        return '{}'.format(self.trago)

    class Meta:
        managed = False
        db_table = 'detalle_trago'


class DetalleVenta(models.Model):
    id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    cantidad = models.IntegerField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='venta', blank=True, null=True)
    trago = models.ForeignKey('Trago', models.DO_NOTHING, db_column='trago', blank=True, null=True)

    def __str__(self):
        return 'Detalle venta {}'.format(self.id)

    class Meta:
        managed = False
        db_table = 'detalle_venta'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empleado(models.Model):
    id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    nombre = models.CharField(max_length=100)
    nro_documento = models.BigIntegerField()
    telefono = models.BigIntegerField()

    def __str__(self):
        return '{}'.format(self.nombre)

    class Meta:
        managed = False
        db_table = 'empleado'


class Pista(models.Model):
    id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pista'


class Trago(models.Model):
    id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    nombre = models.CharField(max_length=30)
    volumen_ml = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'trago'


class Venta(models.Model):
    id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    fecha = models.DateField(blank=True, null=True)
    barra = models.ForeignKey(Barra, models.DO_NOTHING, db_column='barra', blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.fecha, self.barra)

    class Meta:
        managed = False
        db_table = 'venta'
