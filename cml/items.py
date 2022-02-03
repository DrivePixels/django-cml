# -*- coding: utf-8 -
from __future__ import absolute_import
from decimal import Decimal
from datetime import datetime

PROCESSED_ITEMS = ('Group', 'PropertyVariant', 'Property', 'PropertyVariant', 'Sku', 'Tax', 'Product', 'Offer', 'Order')


class BaseItem(object):

    def __init__(self, xml_element=None):
        self.xml_element = xml_element


class Group(BaseItem):

    def __init__(self, *args, **kwargs):
        super(Group, self).__init__(*args, **kwargs)
        self.id = u''
        self.name = u''
        self.groups = []

    def __repr__(self):
        return '<Group object:'\
                '\nid: {id}' \
                '\nname: {name}' \
                '\ngroups: {groups}>'.format(
                    id=self.id.encode('utf-8') if self.id else '',
                    name=self.name.encode('utf-8') if self.name else '',
                    groups=self.groups
                )


class Property(BaseItem):

    def __init__(self, *args, **kwargs):
        super(Property, self).__init__(*args, **kwargs)
        self.id = u''
        self.name = u''
        self.value_type = u''
        self.for_products = False

    def __repr__(self):
        return '<Property object:'\
                '\nid: {id}' \
                '\nname: {name}' \
                '\nvalue_type: {value_type}' \
                '\nfor_products: {for_products}>'.format(
                    id=self.id.encode('utf-8') if self.id else '',
                    name=self.name.encode('utf-8') if self.name else '',
                    value_type=self.value_type.encode('utf-8') if self.value_type else '',
                    for_products=self.for_products
                )


class PropertyVariant(BaseItem):

    def __init__(self, *args, **kwargs):
        super(PropertyVariant, self).__init__(*args, **kwargs)
        self.id = u''
        self.value = u''
        self.property_id = u''

    def __repr__(self):
        return '<PropertyVariant object:'\
                '\nid: {id}' \
                '\nvalue: {value}' \
                '\nproperty_id: {property_id}>'.format(
                    id=self.id.encode('utf-8') if self.id else '',
                    value=self.value.encode('utf-8') if self.value else '',
                    property_id=self.property_id.encode('utf-8') if self.property_id else ''
                )


class Sku(BaseItem):

    def __init__(self, *args, **kwargs):
        super(Sku, self).__init__(*args, **kwargs)
        self.id = u''
        self.name = u''
        self.name_full = u''
        self.international_abbr = u''

    def __repr__(self):
        return '<Sku object:'\
                '\nid: {id}' \
                '\nname: {name}' \
                '\nname_full: {name_full}' \
                '\ninternational_abbr: {international_abbr}>'.format(
                    id=self.id.encode('utf-8') if self.id else '',
                    name=self.name.encode('utf-8') if self.name else '',
                    name_full=self.name_full.encode('utf-8') if self.name_full else '',
                    international_abbr=self.international_abbr.encode('utf-8') if self.international_abbr else ''
                )


class Tax(BaseItem):

    def __init__(self, *args, **kwargs):
        super(Tax, self).__init__(*args, **kwargs)
        self.name = u''
        self.value = Decimal()

    def __repr__(self):
        return '<Tax object:'\
                '\nname: {name}' \
                '\nvalue: {value}>'.format(
                    name=self.name.encode('utf-8') if self.name else '',
                    value=self.value
                )


class AdditionalField(BaseItem):

    def __init__(self, *args, **kwargs):
        super(AdditionalField, self).__init__(*args, **kwargs)
        self.name = u''
        self.value = u''

    def __repr__(self):
        return '<AdditionalField object:'\
                '\nname: {name}' \
                '\nvalue: {value}>'.format(
                    name=self.name.encode('utf-8') if self.name else '',
                    value=self.value.encode('utf-8') if self.value else ''
                )


class Product(BaseItem):

    def __init__(self, *args, **kwargs):
        super(Product, self).__init__(*args, **kwargs)
        self.id = u''
        self.name = u''
        self.sku_id = u''
        self.group_ids = []
        self.properties = []
        self.tax_name = u''
        self.image_path = u''
        self.additional_fields = []

    def __repr__(self):
        return '<Product object:'\
                '\nid: {id}' \
                '\nname: {name}' \
                '\nsku_id: {sku_id}' \
                '\ngroup_ids: {group_ids}' \
                '\nproperties: {properties}' \
                '\ntax_name: {tax_name}' \
                '\nimage_path: {image_path}' \
                '\nadditional_fields: {additional_fields}>'.format(
                    id=self.id.encode('utf-8') if self.id else '',
                    name=self.name.encode('utf-8') if self.name else '',
                    sku_id=self.sku_id.encode('utf-8') if self.sku_id else '',
                    group_ids=self.group_ids,
                    properties=self.properties,
                    tax_name=self.tax_name.encode('utf-8') if self.tax_name else '',
                    image_path=self.image_path.encode('utf-8') if self.image_path else '',
                    additional_fields=self.additional_fields
                )


class PriceType(BaseItem):

    def __init__(self, *args, **kwargs):
        super(PriceType, self).__init__(*args, **kwargs)
        self.id = u''
        self.name = u''
        self.currency = u''
        self.tax_name = u''
        self.tax_in_sum = False

    def __repr__(self):
        return '<PriceType object:'\
                '\nid: {id}'\
                '\nname: {name}'\
                '\ncurrency: {currency}'\
                '\ntax_name: {tax_name}'\
                '\ntax_in_sum: {tax_in_sum}>'.format(
                    id=self.id.encode('utf-8') if self.id else '',
                    name=self.name.encode('utf-8') if self.name else '',
                    currency=self.currency.encode('utf-8') if self.currency else '',
                    tax_name=self.tax_name.encode('utf-8') if self.tax_name else '',
                    tax_in_sum=self.tax_in_sum
                )


class Price(BaseItem):

    def __init__(self, *args, **kwargs):
        super(Price, self).__init__(*args, **kwargs)
        self.representation = u''
        self.price_type_id = u''
        self.price_for_sku = Decimal()
        self.currency_name = u''
        self.sku_name = u''
        self.sku_ratio = Decimal()

    def __repr__(self):
        return '<Price object:'\
                '\nrepresentation: {representation}'\
                '\nprice_type_id: {price_type_id}'\
                '\nprice_for_sku: {price_for_sku}'\
                '\ncurrency_name: {currency_name}'\
                '\nsku_name: {sku_name}'\
                '\nsku_ratio: {sku_ratio}>'.format(
                    representation=self.representation.encode('utf-8') if self.representation else '',
                    price_type_id=self.price_type_id.encode('utf-8') if self.price_type_id else '',
                    price_for_sku=self.price_for_sku,
                    currency_name=self.currency_name.encode('utf-8') if self.currency_name else '',
                    sku_name=self.sku_name.encode('utf-8') if self.sku_name else '',
                    sku_ratio=self.sku_ratio
                )


class Offer(BaseItem):

    def __init__(self, *args, **kwargs):
        super(Offer, self).__init__(*args, **kwargs)
        self.id = u''
        self.name = u''
        self.sku_id = u''
        self.prices = []
        self.quantity = Decimal()

    def __repr__(self):
        return '<Offer object:'\
                '\nid: {id}'\
                '\nname: {name}'\
                '\nsku_id: {sku_id}'\
                '\nprices: {prices}>'.format(
                    id=self.id.encode('utf-8') if self.id else '',
                    name=self.name.encode('utf-8') if self.name else '',
                    sku_id=self.sku_id.encode('utf-8') if self.sku_id else '',
                    prices=self.prices
                )


class Client(BaseItem):

    def __init__(self):
        self.id = u''
        self.name = u''
        self.role = u'Покупатель'
        self.full_name = u''
        self.first_name = u''
        self.last_name = u''
        self.address = u''


class OrderItem(BaseItem):

    def __init__(self):
        self.id = u''
        self.name = u''
        self.sku = Sku(None)
        self.price = Decimal()
        self.quant = Decimal()
        self.sum = Decimal()


class Order(BaseItem):

    def __init__(self, *args, **kwargs):
        super(Order, self).__init__(*args, **kwargs)
        self.id = u''
        self.number = u''
        self.date = datetime.now().date()
        self.currency_name = u''
        self.currency_rate = Decimal()
        self.operation = u'Заказ товара'
        self.role = u'Продавец'
        self.sum = Decimal()
        self.client = Client()
        self.time = datetime.now().time()
        self.comment = u''
        self.items = []
        self.additional_fields = []
