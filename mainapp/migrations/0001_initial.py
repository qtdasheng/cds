# Generated by Django 2.0.1 on 2020-02-28 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TCaipu',
            fields=[
                ('cpid', models.AutoField(primary_key=True, serialize=False)),
                ('cp_title', models.CharField(max_length=50)),
                ('cpimg', models.CharField(max_length=100)),
                ('cp_info', models.CharField(blank=True, max_length=200, null=True)),
                ('cp_url', models.CharField(max_length=200)),
                ('cp_cretime', models.DateTimeField()),
            ],
            options={
                'db_table': 't_caipu',
            },
        ),
        migrations.CreateModel(
            name='TCpfenlei',
            fields=[
                ('flid', models.AutoField(primary_key=True, serialize=False)),
                ('flname', models.CharField(max_length=50)),
                ('flnote', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 't_cpfenlei',
            },
        ),
        migrations.CreateModel(
            name='TDianzan',
            fields=[
                ('dzid', models.AutoField(primary_key=True, serialize=False)),
                ('cpid', models.ForeignKey(blank=True, db_column='cpid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.TCaipu')),
            ],
            options={
                'db_table': 't_dianzan',
            },
        ),
        migrations.CreateModel(
            name='TFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fkcontent', models.CharField(max_length=200)),
                ('fkcretime', models.DateTimeField()),
            ],
            options={
                'db_table': 't_feedback',
            },
        ),
        migrations.CreateModel(
            name='TGoods',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('gname', models.CharField(max_length=50)),
                ('gimg', models.CharField(max_length=100)),
                ('gpreprice', models.FloatField()),
                ('gprice', models.FloatField()),
                ('gnum', models.IntegerField()),
                ('gcretime', models.DateTimeField()),
            ],
            options={
                'db_table': 't_goods',
            },
        ),
        migrations.CreateModel(
            name='THistory',
            fields=[
                ('hid', models.AutoField(primary_key=True, serialize=False)),
                ('hcre_time', models.DateTimeField()),
                ('cpid', models.ForeignKey(blank=True, db_column='cpid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.TCaipu')),
            ],
            options={
                'db_table': 't_history',
            },
        ),
        migrations.CreateModel(
            name='TMessage',
            fields=[
                ('create_time', models.DateTimeField(auto_created=True, blank=True)),
                ('message_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('link_url', models.CharField(blank=True, max_length=100, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('state', models.IntegerField(choices=[(0, '审核中'), (1, '已通过'), (2, '未通过')], default=0)),
            ],
            options={
                'db_table': 't_message',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='TOrder',
            fields=[
                ('oid', models.AutoField(primary_key=True, serialize=False)),
                ('oprice', models.FloatField()),
                ('ocretime', models.DateTimeField()),
                ('ostate', models.IntegerField()),
            ],
            options={
                'db_table': 't_order',
            },
        ),
        migrations.CreateModel(
            name='TOrdergoods',
            fields=[
                ('ogid', models.AutoField(primary_key=True, serialize=False)),
                ('ognum', models.IntegerField()),
                ('gid', models.ForeignKey(db_column='gid', on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.TGoods')),
                ('oid', models.ForeignKey(db_column='oid', on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.TOrder')),
            ],
            options={
                'db_table': 't_ordergoods',
            },
        ),
        migrations.CreateModel(
            name='TPinglun',
            fields=[
                ('plid', models.AutoField(primary_key=True, serialize=False)),
                ('pl_text', models.CharField(blank=True, max_length=200, null=True)),
                ('cpid', models.ForeignKey(blank=True, db_column='cpid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.TCaipu')),
            ],
            options={
                'db_table': 't_pinglun',
            },
        ),
        migrations.CreateModel(
            name='TRel',
            fields=[
                ('rel_id', models.AutoField(primary_key=True, serialize=False)),
                ('fans_id', models.IntegerField(blank=True, null=True)),
                ('followed_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_rel',
            },
        ),
        migrations.CreateModel(
            name='TRenwu',
            fields=[
                ('rwid', models.AutoField(primary_key=True, serialize=False)),
                ('rwname', models.IntegerField(blank=True, null=True)),
                ('rwexp', models.IntegerField(blank=True, null=True)),
                ('note', models.CharField(blank=True, max_length=200, null=True)),
                ('cpid', models.ForeignKey(blank=True, db_column='cpid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.TCaipu')),
            ],
            options={
                'db_table': 't_renwu',
            },
        ),
        migrations.CreateModel(
            name='TShoucang',
            fields=[
                ('scid', models.AutoField(primary_key=True, serialize=False)),
                ('sccretime', models.DateTimeField()),
                ('cpid', models.ForeignKey(db_column='cpid', on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.TCaipu')),
            ],
            options={
                'db_table': 't_shoucang',
            },
        ),
        migrations.CreateModel(
            name='TSysMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('parent_id', models.IntegerField(blank=True, null=True)),
                ('ord', models.IntegerField(blank=True, null=True)),
                ('url', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 't_sys_menu',
            },
        ),
        migrations.CreateModel(
            name='TSysRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('code', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'db_table': 't_sys_role',
            },
        ),
        migrations.CreateModel(
            name='TSysRoleMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_id', models.IntegerField(blank=True, null=True)),
                ('menu_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_sys_role_menu',
            },
        ),
        migrations.CreateModel(
            name='TSysUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('auth_string', models.CharField(max_length=32)),
                ('nick_name', models.CharField(blank=True, max_length=20, null=True)),
                ('role_id', models.IntegerField()),
            ],
            options={
                'db_table': 't_sys_user',
            },
        ),
        migrations.CreateModel(
            name='TUser',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('head', models.CharField(blank=True, max_length=100, null=True)),
                ('ucretime', models.DateTimeField()),
                ('note', models.CharField(blank=True, max_length=200, null=True)),
                ('exp', models.IntegerField(blank=True, null=True)),
                ('level', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_user',
            },
        ),
        migrations.CreateModel(
            name='TVendor',
            fields=[
                ('vid', models.AutoField(primary_key=True, serialize=False)),
                ('vname', models.CharField(blank=True, max_length=50, null=True)),
                ('vpassword', models.CharField(blank=True, max_length=50, null=True)),
                ('vphone', models.CharField(blank=True, max_length=50, null=True)),
                ('vaddress', models.CharField(blank=True, max_length=100, null=True)),
                ('v_cretime', models.DateTimeField()),
            ],
            options={
                'db_table': 't_vendor',
            },
        ),
        migrations.CreateModel(
            name='TZhuanfa',
            fields=[
                ('zfid', models.AutoField(primary_key=True, serialize=False)),
                ('cpid', models.ForeignKey(db_column='cpid', on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.TCaipu')),
                ('uid', models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.TUser')),
            ],
            options={
                'db_table': 't_zhuanfa',
            },
        ),
        migrations.AddField(
            model_name='tshoucang',
            name='uid',
            field=models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.TUser'),
        ),
        migrations.AddField(
            model_name='tpinglun',
            name='uid',
            field=models.ForeignKey(blank=True, db_column='uid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.TUser'),
        ),
        migrations.AddField(
            model_name='torder',
            name='uid',
            field=models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.TUser'),
        ),
        migrations.AddField(
            model_name='thistory',
            name='uid',
            field=models.ForeignKey(blank=True, db_column='uid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.TUser'),
        ),
        migrations.AddField(
            model_name='tgoods',
            name='vid',
            field=models.ForeignKey(blank=True, db_column='vid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.TVendor'),
        ),
        migrations.AddField(
            model_name='tfeedback',
            name='uid',
            field=models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.TUser'),
        ),
        migrations.AddField(
            model_name='tdianzan',
            name='uid',
            field=models.ForeignKey(blank=True, db_column='uid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.TUser'),
        ),
        migrations.AddField(
            model_name='tcaipu',
            name='flid',
            field=models.ForeignKey(blank=True, db_column='flid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.TCpfenlei'),
        ),
        migrations.AddField(
            model_name='tcaipu',
            name='uid',
            field=models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.TUser'),
        ),
    ]
