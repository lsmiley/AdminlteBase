# Generated by Django 3.2.5 on 2022-05-10 16:22

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('labordelivery', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testquestionnaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('title', models.CharField(blank=True, max_length=150)),
                ('rfs_num', models.CharField(blank=True, max_length=150)),
                ('sales_connect_num', models.CharField(blank=True, max_length=150)),
                ('appttus_num', models.CharField(blank=True, max_length=150)),
                ('sizingtype', models.CharField(blank=True, max_length=150)),
                ('due_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('PricingStructureSelect', models.CharField(choices=[('Standard', 'Standard'), ('Firm', 'Firm'), ('NBIE', 'NBIE')], default='Select-One', max_length=150)),
                ('team', models.CharField(blank=True, max_length=150)),
                ('assigned_by', models.CharField(blank=True, max_length=150)),
                ('assigned_to', models.CharField(blank=True, max_length=150)),
                ('RequesterFirstName', models.CharField(blank=True, max_length=150)),
                ('RequesterLastName', models.CharField(blank=True, max_length=150)),
                ('RequesterRole', models.CharField(blank=True, max_length=150)),
                ('RequesterEmail', models.CharField(blank=True, max_length=150)),
                ('CustomerName', models.CharField(blank=True, max_length=150)),
                ('CustomerStatus', models.CharField(choices=[('---Select one ---', '---Select one ---'), ('New Customer', 'New Customer'), ('Existing Customer', 'Existing Customer'), ('Returning Customer', 'Returning Customer')], default='Select-One', max_length=150)),
                ('Solution_Design', models.CharField(choices=[('---Select one ---', '---Select one ---'), ('Priyadarshi Achar - AP', 'Asia/Pacific'), ('David Lugg - Europe', 'David Lugg - Europe'), ('Julie Keane - Europe', 'Julie Keane - Europe'), ('Marek Wolsan - Europe', 'Marek Wolsan'), ('Steve Chew - Europe', 'Steve Chew'), ('Kiyomi Miura - Japan', 'Kiyomi Miura - Japan'), ('Marcello Belloni Gomes - LA', 'Marcello Belloni Gomes'), ('Greg Sinclair - MEA', 'Greg Sinclair - MEA'), ('David Cunningham - NA', 'David Cunningham - NA'), ('Page Farmer - NA', 'Page Farmer - NA'), ('Gerry Comeau - WW', 'Gerry Comeau - WW'), ('Jonathan Planko - WW', 'Jonathan Planko - WW'), ('None', 'None')], default='Select-One', max_length=150)),
                ('SalesContactName', models.CharField(blank=True, max_length=150)),
                ('SalesContactEmail', models.CharField(blank=True, max_length=150)),
                ('TranStartDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('Firm_Price_or_NBIE', models.CharField(choices=[('Firm', 'Firm'), ('NBIE', 'NBIE')], default='Select-One', max_length=150)),
                ('Service_Delivery_Requirements', models.CharField(choices=[('---Select one ---', '---Select one ---'), ('Asia/Pacific', 'Asia/Pacific'), ('Europe', 'Europe'), ('Latin America', 'latin America'), ('North America', 'North America'), ('None', 'None')], default='Select-One', max_length=150)),
                ('Solution_Owner', models.CharField(blank=True, max_length=150)),
                ('Revenue_Structure_Select', models.CharField(choices=[('---Select one ---', '---Select one ---'), ('Cost Recovery', 'Cost Recovery'), ('Revenue Share', 'Revenue Share')], default='Select-One', max_length=150)),
                ('Revenue_Structure_Cost_Explain', models.CharField(blank=True, max_length=150)),
                ('Restricted_Delivery', models.BooleanField(default=False)),
                ('Restricted_Delivery_Explanation', models.CharField(blank=True, max_length=150)),
                ('Questionnaire_num_consoles', models.IntegerField(default='0')),
                ('Questionnaire_num_workstation', models.IntegerField(default='0')),
                ('Questionnaire_num_server', models.IntegerField(db_column='Numserver', default='0')),
                ('Questionnaire_num_ipaddress', models.IntegerField(default='0')),
                ('Questionnaire_num_total_endpoints', models.IntegerField(default='0')),
                ('AntiVirusMalware', models.BooleanField(default=False)),
                ('DLP_on_Workstations', models.BooleanField(default=False)),
                ('DLP_on_Servers', models.BooleanField(default=False)),
                ('Encryption_on_Workstations', models.BooleanField(default=False)),
                ('Encryption_on_Servers', models.BooleanField(default=False)),
                ('prodcomponent1_wkstn', models.BooleanField(default=False)),
                ('NAS_Storage', models.BooleanField(default=False)),
                ('Windows', models.BooleanField(default=False)),
                ('AIX', models.BooleanField(default=False)),
                ('VDI', models.BooleanField(default=False)),
                ('URL_Filtering', models.BooleanField(default=False)),
                ('HIPs_on_Workstations', models.BooleanField(default=False)),
                ('HIPs_on_Servers', models.BooleanField(default=False)),
                ('Firewall_on_Workstations', models.BooleanField(default=False)),
                ('Firewall_on_Servers', models.BooleanField(default=False)),
                ('BigFix_Patching_Scanning', models.BooleanField(default=False)),
                ('Linux', models.BooleanField(default=False)),
                ('Integrity_Monitoring', models.BooleanField(default=False)),
                ('Citrix', models.BooleanField(default=False)),
                ('Other_Features_or_Platforms', models.BooleanField(default=False)),
                ('Other_Features_or_Platforms_Note', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=' Explain Other Features and Platform Requirements?', null=True)),
                ('Environment_and_Platforms_Note', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('EmsServiceRequested', models.BooleanField(default=False)),
                ('prepardedby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='testquestionnaires', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='TestquestionnaireItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('discount_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('final_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('total_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('base', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('discount_base', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('final_base', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('total_base', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('fte', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('discount_fte', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('final_fte', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('total_fte', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('productcomplexityfac', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('numworkstation', models.IntegerField(default='0')),
                ('numserver', models.IntegerField(db_column='Numserver', default='0')),
                ('numipaddress', models.IntegerField(default='0')),
                ('total_endpoints', models.IntegerField(default='0')),
                ('desc', models.CharField(blank=True, max_length=150)),
                ('numappchange', models.IntegerField(default='0')),
                ('srvshourscalc', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('wkstnshourscalc', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('ipshourscalc', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('addlconhourscalc', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('appchangehourscalc', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('totalhourscalc', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('appchangefac', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('serverfte', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('workstationfte', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('ipendpointfte', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('addlconfte', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('deliveryoption', models.CharField(blank=True, max_length=150)),
                ('regions', models.CharField(blank=True, max_length=150)),
                ('currencytype', models.CharField(blank=True, max_length=150)),
                ('defaultfte_year', models.CharField(blank=True, max_length=150)),
                ('workweek', models.CharField(blank=True, max_length=150)),
                ('deliveryctrcostfactor', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('band2count', models.FloatField(default='0.0')),
                ('band2percentage', models.FloatField(default='0.0')),
                ('band3count', models.FloatField(default='0.0')),
                ('band3percentage', models.FloatField(default='0.0')),
                ('band4count', models.FloatField(default='0.0')),
                ('band4percentage', models.FloatField(default='0.0')),
                ('band5count', models.FloatField(default='0.0')),
                ('band5percentage', models.FloatField(default='0.0')),
                ('band6count', models.FloatField(default='0.0')),
                ('band6percentage', models.FloatField(default='0.0')),
                ('band7count', models.FloatField(default='0.0')),
                ('band7percentage', models.FloatField(default='0.0')),
                ('band8count', models.FloatField(default='0.0')),
                ('band8percentage', models.FloatField(default='0.0')),
                ('band9count', models.FloatField(default='0.0')),
                ('band9percentage', models.FloatField(default='0.0')),
                ('band10count', models.FloatField(default='0.0')),
                ('band10percentage', models.FloatField(default='0.0')),
                ('bandstotalcount', models.FloatField(default='0.0')),
                ('bandstotalpercentage', models.FloatField(default='0.0')),
                ('nummonths', models.IntegerField(default='12')),
                ('prodcomponent1_desc', models.CharField(blank=True, max_length=150, null=True)),
                ('prodcomponent1_wkstn', models.BooleanField(default=False)),
                ('prodcomponent1_wkstnhours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent1_svr', models.BooleanField(default=False)),
                ('prodcomponent1_svrHours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent1_IP', models.BooleanField(default=False)),
                ('prodcomponent1_iphours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent1_ttl_hours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent1_ttl_fte', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent2_desc', models.CharField(blank=True, max_length=150, null=True)),
                ('prodcomponent2_wkstn', models.BooleanField(default=False)),
                ('prodcomponent2_wkstnhours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent2_svr', models.BooleanField(default=False)),
                ('prodcomponent2_svrHours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent2_IP', models.BooleanField(default=False)),
                ('prodcomponent2_iphours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent2_ttl_hours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent2_ttl_fte', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent3_desc', models.CharField(blank=True, max_length=150, null=True)),
                ('prodcomponent3_wkstn', models.BooleanField(default=False)),
                ('prodcomponent3_wkstnhours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent3_svr', models.BooleanField(default=False)),
                ('prodcomponent3_svrHours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent3_IP', models.BooleanField(default=False)),
                ('prodcomponent3_iphours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent3_ttl_hours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent3_ttl_fte', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent4_desc', models.CharField(blank=True, max_length=150, null=True)),
                ('prodcomponent4_wkstn', models.BooleanField(default=False)),
                ('prodcomponent4_wkstnhours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent4_svr', models.BooleanField(default=False)),
                ('prodcomponent4_svrHours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent4_IP', models.BooleanField(default=False)),
                ('prodcomponent4_iphours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent4_ttl_hours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent4_ttl_fte', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent5_desc', models.CharField(blank=True, max_length=150, null=True)),
                ('prodcomponent5_wkstn', models.BooleanField(default=False)),
                ('prodcomponent5_wkstnhours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent5_svr', models.BooleanField(default=False)),
                ('prodcomponent5_svrHours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent5_IP', models.BooleanField(default=False)),
                ('prodcomponent5_iphours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent5_ttl_hours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent5_ttl_fte', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent6_desc', models.CharField(blank=True, max_length=150, null=True)),
                ('prodcomponent6_wkstn', models.BooleanField(default=False)),
                ('prodcomponent6_wkstnhours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent6_svr', models.BooleanField(default=False)),
                ('prodcomponent6_svrHours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent6_IP', models.BooleanField(default=False)),
                ('prodcomponent6_iphours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent6_ttl_hours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent6_ttl_fte', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent7_desc', models.CharField(blank=True, max_length=150, null=True)),
                ('prodcomponent7_wkstn', models.BooleanField(default=False)),
                ('prodcomponent7_wkstnhours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent7_svr', models.BooleanField(default=False)),
                ('prodcomponent7_svrHours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent7_IP', models.BooleanField(default=False)),
                ('prodcomponent7_iphours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent7_ttl_hours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent7_ttl_fte', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent8_desc', models.CharField(blank=True, max_length=150, null=True)),
                ('prodcomponent8_wkstn', models.BooleanField(default=False)),
                ('prodcomponent8_wkstnhours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent8_svr', models.BooleanField(default=False)),
                ('prodcomponent8_svrHours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent8_IP', models.BooleanField(default=False)),
                ('prodcomponent8_iphours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent8_ttl_hours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent8_ttl_fte', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent9_desc', models.CharField(blank=True, max_length=150, null=True)),
                ('prodcomponent9_wkstn', models.BooleanField(default=False)),
                ('prodcomponent9_wkstnhours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent9_svr', models.BooleanField(default=False)),
                ('prodcomponent9_svrHours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent9_IP', models.BooleanField(default=False)),
                ('prodcomponent9_iphours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent9_ttl_hours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent9_ttl_fte', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent10_desc', models.CharField(blank=True, max_length=150, null=True)),
                ('prodcomponent10_wkstn', models.BooleanField(default=False)),
                ('prodcomponent10_wkstnhours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent10_svr', models.BooleanField(default=False)),
                ('prodcomponent10_svrHours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent10_IP', models.BooleanField(default=False)),
                ('prodcomponent10_iphours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent10_ttl_hours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent10_ttl_fte', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent11_desc', models.CharField(blank=True, max_length=150, null=True)),
                ('prodcomponent11_wkstn', models.BooleanField(default=False)),
                ('prodcomponent11_wkstnhours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent11_svr', models.BooleanField(default=False)),
                ('prodcomponent11_svrHours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent11_IP', models.BooleanField(default=False)),
                ('prodcomponent11_iphours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent11_ttl_hours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent11_ttl_fte', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent12_desc', models.CharField(blank=True, max_length=150, null=True)),
                ('prodcomponent12_wkstn', models.BooleanField(default=False)),
                ('prodcomponent12_wkstnhours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent12_svr', models.BooleanField(default=False)),
                ('prodcomponent12_svrHours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent12_IP', models.BooleanField(default=False)),
                ('prodcomponent12_iphours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent12_ttl_hours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent12_ttl_fte', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent13_desc', models.CharField(blank=True, max_length=150, null=True)),
                ('prodcomponent13_wkstn', models.BooleanField(default=False)),
                ('prodcomponent13_wkstnhours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent13_svr', models.BooleanField(default=False)),
                ('prodcomponent13_svrHours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent13_IP', models.BooleanField(default=False)),
                ('prodcomponent13_iphours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent13_ttl_hours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent13_ttl_fte', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent14_desc', models.CharField(blank=True, max_length=150, null=True)),
                ('prodcomponent14_wkstn', models.BooleanField(default=False)),
                ('prodcomponent14_wkstnhours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent14_svr', models.BooleanField(default=False)),
                ('prodcomponent14_svrHours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent14_IP', models.BooleanField(default=False)),
                ('prodcomponent14_iphours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent14_ttl_hours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent14_ttl_fte', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent15_desc', models.CharField(blank=True, max_length=150, null=True)),
                ('prodcomponent15_wkstn', models.BooleanField(default=False)),
                ('prodcomponent15_wkstnhours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent15_svr', models.BooleanField(default=False)),
                ('prodcomponent15_svrHours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent15_IP', models.BooleanField(default=False)),
                ('prodcomponent15_iphours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent15_ttl_hours', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodcomponent15_ttl_fte', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('softlifesvryesno', models.BooleanField(default=False)),
                ('softlifesrvhourscalc', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('softlifesvrfte', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('prodimage', models.ImageField(blank=True, null=True, upload_to='')),
                ('labordelivery', models.ForeignKey(default=5, on_delete=django.db.models.deletion.PROTECT, to='labordelivery.labordelivery')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product')),
                ('testquestionnaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionnaire_items', to='testquestionnaire.testquestionnaire')),
            ],
        ),
    ]
