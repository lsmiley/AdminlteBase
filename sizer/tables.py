import django_tables2 as tables

from product.models import Product
from .models import SizerItem, Sizer


class SizerTable(tables.Table):
    tag_final_value = tables.Column(orderable=False, verbose_name='Value')
    action = tables.TemplateColumn(
        '<a href="{{ record.get_edit_url }}" <i class="fa fa-edit"></i></a>', orderable=False)

    class Meta:
        model = Sizer
        template_name = 'django_tables2/bootstrap.html'
        fields = ['date', 'title', 'tag_final_value']


# noinspection PyPackageRequirements
class ProductTable(tables.Table):
    tag_final_value = tables.Column(orderable=False, verbose_name='Base Hrs:')
    action = tables.TemplateColumn(

        '<a <button class="btn btn-info add_button" data-href="{% url "ajax_add" instance.id record.id %}">Add!</a>',
        # '<button class="btn btn-info add_button" "onclick="window.location= {% url "ajax_add" instance.id record.id %}">Add!</a>',
        orderable=False
    )

    class Meta:
        model = Product
        template_name = 'django_tables2/bootstrap.html'
        fields = ['title', 'category', 'tag_final_value']



class SizerItemTable(tables.Table):
    numworkstation = tables.Column(orderable=False, verbose_name='# Wkstn.')
    wkstnshourscalc = tables.Column(orderable=False, verbose_name='Wkstn/Hrs.')
    numserver = tables.Column(orderable=False, verbose_name='# Svrs')
    srvshourscalc = tables.Column(orderable=False, verbose_name='Svr/Hrs.')
    numipaddress = tables.Column(orderable=False, verbose_name='# IP/EP')
    ipshourscalc = tables.Column(orderable=False, verbose_name='IP/Hrs.')
    tag_final_totalhourscalc = tables.Column(orderable=False, verbose_name='Ttl/Hrs.')
    total_endpoints = tables.Column(orderable=False, verbose_name='# Endpoints')
    qty = tables.Column(orderable=False, verbose_name='# Consoles')
    # price = tables.Column(orderable=False, verbose_name='Base')
    # tag_line_base_hours = tables.Column(orderable=False, verbose_name='Hrs.')

    # tag_final_price = tables.Column(orderable=False, verbose_name='Price')

    Options = tables.TemplateColumn('''

           
           
    ''', orderable=False)

    class Meta:
        model = SizerItem
        template_name = 'django_tables2/bootstrap.html'
        fields = ['product', 'qty']
