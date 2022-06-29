# Generated by Django 4.0.3 on 2022-06-29 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PaymentManagement', '0001_initial'),
        ('AdminManagement', '0002_remove_contrato_clienteid_remove_contrato_parqueid_and_more'),
        ('OperationManagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='contratoid',
            field=models.ForeignKey(db_column='ContratoID', null=True, on_delete=django.db.models.deletion.CASCADE, to='PaymentManagement.contrato'),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='reservaid',
            field=models.ForeignKey(db_column='ReservaID', null=True, on_delete=django.db.models.deletion.CASCADE, to='PaymentManagement.reserva'),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='viaturaid',
            field=models.ForeignKey(db_column='ViaturaID', null=True, on_delete=django.db.models.deletion.CASCADE, to='OperationManagement.viatura'),
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Contrato',
        ),
        migrations.DeleteModel(
            name='Dia',
        ),
        migrations.DeleteModel(
            name='Fatura',
        ),
        migrations.DeleteModel(
            name='Pagamento',
        ),
        migrations.DeleteModel(
            name='Periodicidade',
        ),
        migrations.DeleteModel(
            name='Reclamacao',
        ),
        migrations.DeleteModel(
            name='RegistoMovimento',
        ),
        migrations.DeleteModel(
            name='Reserva',
        ),
        migrations.DeleteModel(
            name='TabelaPrecos',
        ),
        migrations.DeleteModel(
            name='Viatura',
        ),
    ]