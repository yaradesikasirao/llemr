# Generated by Django 3.1.2 on 2020-12-04 01:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_encounter_encounterstatus'),
        ('workup', '0006_auto_20201114_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='attestablebasicnote',
            name='encounter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.encounter'),
        ),
        migrations.AddField(
            model_name='basicnote',
            name='encounter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.encounter'),
        ),
        migrations.AddField(
            model_name='historicalattestablebasicnote',
            name='encounter',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.encounter'),
        ),
        migrations.AddField(
            model_name='historicalbasicnote',
            name='encounter',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.encounter'),
        ),
        migrations.AddField(
            model_name='historicalworkup',
            name='encounter',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.encounter'),
        ),
        migrations.AddField(
            model_name='workup',
            name='encounter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.encounter'),
        ),
    ]
