# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime
from common import md5_


class TCaipu(models.Model):
    cpid = models.AutoField(primary_key=True)
    uid = models.ForeignKey('TUser', models.DO_NOTHING, db_column='uid')
    cp_title = models.CharField(max_length=50)
    cpimg = models.CharField(max_length=100)
    cp_info = models.CharField(max_length=200, blank=True, null=True)
    cp_url = models.CharField(max_length=200)
    cp_cretime = models.DateTimeField()
    flid = models.ForeignKey('TCpfenlei', models.DO_NOTHING, db_column='flid', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_caipu'


class TCpfenlei(models.Model):
    flid = models.AutoField(primary_key=True)
    flname = models.CharField(max_length=50)
    flnote = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_cpfenlei'


class TDianzan(models.Model):
    dzid = models.AutoField(primary_key=True)
    uid = models.ForeignKey('TUser', models.DO_NOTHING, db_column='uid', blank=True, null=True)
    cpid = models.ForeignKey(TCaipu, models.DO_NOTHING, db_column='cpid', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_dianzan'


class TFeedback(models.Model):
    uid = models.ForeignKey('TUser', models.DO_NOTHING, db_column='uid')
    fkcontent = models.CharField(max_length=200)
    fkcretime = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 't_feedback'


class TGoods(models.Model):
    gid = models.AutoField(primary_key=True)
    vid = models.ForeignKey('TVendor', models.DO_NOTHING, db_column='vid', blank=True, null=True)
    gname = models.CharField(max_length=50)
    gimg = models.CharField(max_length=100)
    gpreprice = models.FloatField()
    gprice = models.FloatField()
    gnum = models.IntegerField()
    gcretime = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 't_goods'


class THistory(models.Model):
    hid = models.AutoField(primary_key=True)
    cpid = models.ForeignKey(TCaipu, models.DO_NOTHING, db_column='cpid', blank=True, null=True)
    uid = models.ForeignKey('TUser', models.DO_NOTHING, db_column='uid', blank=True, null=True)
    hcre_time = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 't_history'


class TOrder(models.Model):
    oid = models.AutoField(primary_key=True)
    oprice = models.FloatField()
    ocretime = models.DateTimeField()
    ostate = models.IntegerField()
    uid = models.ForeignKey('TUser', models.DO_NOTHING, db_column='uid')

    class Meta:
        # managed = False
        db_table = 't_order'


class TOrdergoods(models.Model):
    ogid = models.AutoField(primary_key=True)
    gid = models.ForeignKey(TGoods, models.DO_NOTHING, db_column='gid')
    ognum = models.IntegerField()
    oid = models.ForeignKey(TOrder, models.DO_NOTHING, db_column='oid')

    class Meta:
        # managed = False
        db_table = 't_ordergoods'


class TPinglun(models.Model):
    plid = models.AutoField(primary_key=True)
    uid = models.ForeignKey('TUser', models.DO_NOTHING, db_column='uid', blank=True, null=True)
    cpid = models.ForeignKey(TCaipu, models.DO_NOTHING, db_column='cpid', blank=True, null=True)
    pl_text = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_pinglun'


class TRel(models.Model):
    rel_id = models.AutoField(primary_key=True)
    fans_id = models.IntegerField(blank=True, null=True)
    followed_id = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_rel'


class TRenwu(models.Model):
    rwid = models.AutoField(primary_key=True)
    rwname = models.IntegerField(blank=True, null=True)
    rwexp = models.IntegerField(blank=True, null=True)
    note = models.CharField(max_length=200, blank=True, null=True)
    cpid = models.ForeignKey(TCaipu, models.DO_NOTHING, db_column='cpid', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_renwu'


class TShoucang(models.Model):
    scid = models.AutoField(primary_key=True)
    uid = models.ForeignKey('TUser', models.DO_NOTHING, db_column='uid')
    cpid = models.ForeignKey(TCaipu, models.DO_NOTHING, db_column='cpid')
    sccretime = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 't_shoucang'


class TUser(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    head = models.CharField(max_length=100, blank=True, null=True)
    ucretime = models.DateTimeField()
    note = models.CharField(max_length=200, blank=True, null=True)
    exp = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_user'


class TVendor(models.Model):
    vid = models.AutoField(primary_key=True)
    vname = models.CharField(max_length=50, blank=True, null=True)
    vpassword = models.CharField(max_length=50, blank=True, null=True)
    vphone = models.CharField(max_length=50, blank=True, null=True)
    vaddress = models.CharField(max_length=100, blank=True, null=True)
    v_cretime = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 't_vendor'


class TZhuanfa(models.Model):
    zfid = models.AutoField(primary_key=True)
    uid = models.ForeignKey(TUser, models.DO_NOTHING, db_column='uid')
    cpid = models.ForeignKey(TCaipu, models.DO_NOTHING, db_column='cpid')

    class Meta:
        # managed = False
        db_table = 't_zhuanfa'


class TSysMenu(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    ord = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_sys_menu'


class TSysRole(models.Model):
    name = models.CharField(unique=True, max_length=20)
    code = models.CharField(unique=True, max_length=10)

    class Meta:
        # managed = False
        db_table = 't_sys_role'


class TSysRoleMenu(models.Model):
    role_id = models.IntegerField(blank=True, null=True)
    menu_id = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_sys_role_menu'


class TSysUser(models.Model):
    username = models.CharField(unique=True, max_length=20)
    auth_string = models.CharField(max_length=32)
    nick_name = models.CharField(max_length=20, blank=True, null=True)
    role_id = models.IntegerField()

    @property
    def role(self):
        return TSysRole.objects.get(pk=self.role_id)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if len(self.auth_string) != 32:
            self.auth_string = md5_.hash_encode(self.auth_string)

        super(TSysUser, self).save()

    class Meta:
        # managed = False
        db_table = 't_sys_user'


class TMessage(models.Model):
    message_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    link_url = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(auto_created=True, blank=True)
    note = models.TextField(blank=True, null=True)

    states = (
        (0, '审核中'),
        (1, '已通过'),
        (2, '未通过')
    )
    state = models.IntegerField(choices=states, default=0)

    @property
    def state_label(self):
        return self.states[self.state][-1]

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.create_time is None:
            self.create_time = datetime.now()

        super(TMessage, self).save()

    class Meta:
        # managed = False
        db_table = 't_message'
        ordering = ['-create_time']
