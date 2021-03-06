# Generated by Django 2.2.7 on 2020-04-04 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perimeter_core', '0007_nodeinterfaceipaddress_is_default'),
    ]

    operations = [
        migrations.CreateModel(
            name='NodeInterfaceAvailabilityCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('total_number_of_bound_ip_addresses', models.IntegerField(default=0)),
                ('node_interface', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perimeter_core.NodeInterface')),
            ],
        ),
        migrations.CreateModel(
            name='NodeInterfaceIPAddressAvailabilityCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('total_number_of_bound_ip_addresses', models.IntegerField(default=0)),
                ('interface_availability_cache', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infrastructure_monitoring_api.NodeInterfaceAvailabilityCache')),
                ('ip_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perimeter_core.NodeInterfaceIPAddress')),
            ],
        ),
        migrations.CreateModel(
            name='NodeInterfaceIPAddressServiceAvailabilityCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('ip_address_availability_cache', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infrastructure_monitoring_api.NodeInterfaceIPAddressAvailabilityCache')),
                ('node_interface_ip_address_service_mapping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perimeter_core.NodeInterfaceIPAddressServiceMapping')),
            ],
        ),
        migrations.CreateModel(
            name='NodeAvailabilityCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('total_number_of_bound_ip_addresses', models.IntegerField(default=0)),
                ('number_of_nodes_online', models.IntegerField(default=0)),
                ('number_of_nodes_offline', models.IntegerField(default=0)),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perimeter_core.Node')),
            ],
        ),
        migrations.CreateModel(
            name='NetworkAvailabilityCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('total_number_of_bound_ip_addresses', models.IntegerField(default=0)),
                ('number_of_nodes_online', models.IntegerField(default=0)),
                ('number_of_nodes_offline', models.IntegerField(default=0)),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perimeter_core.Network')),
            ],
        ),
        migrations.CreateModel(
            name='ClusterAvailabilityCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('total_number_of_nodes', models.IntegerField(default=0)),
                ('number_of_nodes_online', models.IntegerField(default=0)),
                ('number_of_nodes_offline', models.IntegerField(default=0)),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perimeter_core.Cluster')),
            ],
        ),
    ]
