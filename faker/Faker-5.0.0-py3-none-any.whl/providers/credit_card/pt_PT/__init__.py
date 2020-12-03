from collections import OrderedDict

from .. import CreditCard
from .. import Provider as CreditCardProvider


class Provider(CreditCardProvider):
    """Implementation of ``pt_PT`` locale credit card

    For all methods that take ``card_type`` as an argument a random card type
    will be used if the supplied value is ``None``. The list of valid card types
    includes ``'visa'``, ``'mastercard'`` and ``'maestro'``.

    Source: https://bincheck.org/portugal
    """

    prefix_visa = ['400131', '400190', '400817', '402192', '402947', '402956', '403005', '403006', '403007',
                   '403008', '403271', '404520', '404530', '405758', '406170', '406475', '407548', '407549',
                   '407575', '408237', '408239', '409842', '409843', '410000', '410344', '410345', '410553',
                   '410557', '411635', '411700', '411701', '411869', '412487', '412488', '412489', '412657',
                   '412782', '412990', '413014', '413793', '413871', '415158', '415159', '415170', '415171',
                   '415174', '415175', '415194', '415195', '415238', '415272', '415273', '415403', '415404',
                   '415405', '415440', '415441', '415569', '415920', '415961', '416952', '416963', '416970',
                   '417005', '417091', '417092', '417337', '418847', '419022', '419682', '419683', '419684',
                   '421149', '421510', '422080', '422240', '422241', '422414', '422417', '422597', '422869',
                   '423392', '423393', '424118', '424184', '424208', '424661', '425509', '425510', '425906',
                   '426150', '426360', '426370', '427256', '427304', '427729', '427770', '427867', '428139',
                   '428184', '428185', '428186', '428187', '429711', '430240', '430241', '431926', '433390',
                   '433391', '433511', '433512', '433513', '433599', '433618', '433622', '433966', '437886',
                   '438257', '439070', '440637', '440644', '440645', '442664', '443977', '443978', '444224',
                   '444227', '445961', '445962', '446140', '446144', '449389', '450915', '451156', '451166',
                   '454755', '455250', '455290', '455292', '455658', '456811', '456812', '457031', '458058',
                   '458059', '459432', '459433', '459449', '460340', '460341', '460342', '461247', '461248',
                   '461249', '462731', '462732', '464406', '465964', '476066', '476067', '476068', '476069',
                   '476070', '476071', '476329', '477920', '477921', '477922', '477947', '477989', '478062',
                   '478063', '479702', '479736', '483088', '485672', '486449', '486457', '489434', '489485',
                   '490772', '490830', '490831', '490832', '490841', '490863', '491213', '491546', '491547',
                   '491613', '492194', '493402', '493480', '493800', '493801', '493830', '498800', '499968',
                   '499969', '499986', '422239', '422041', '464409', '464408']

    prefix_mastercard = ['510122', '510123', '512556', '518772', '519744', '519774', '520342', '524552',
                         '524878', '525625', '525808', '526819', '527014', '528024', '529119', '530267',
                         '530770', '532355', '536468', '541171', '541557', '542081', '542098', '542858',
                         '543099', '543116', '543123', '544051', '544052', '544233', '547260', '547459',
                         '548168', '548169', '552727', '552755', '553057', '554506', '554517', '554518',
                         '556660', '557836', '557882', '557883', '557888']

    prefix_maestro = ['501654', '501659', '670530', '670811', '670812', '676938', '676938', '677393',
                      '677707', '670835', '670817']

    credit_card_types = OrderedDict((
        ('maestro', CreditCard('Maestro', prefix_maestro, 16, security_code='CVV2')),
        ('mastercard', CreditCard('Mastercard', prefix_mastercard, 16, security_code='CVV2')),
        ('visa', CreditCard('Visa', prefix_visa, 16, security_code='CVV2')),
    ))

    def credit_card_expire(self, start='now', end='+4y', date_format='%m/%y'):
        """Generate a credit card expiry date.

        This method uses |date_time_between| under the hood to generate the
        expiry date, so the ``start`` and ``end`` arguments work in the same way
        here as it would in that method. For the actual formatting of the expiry
        date, |strftime| is used and ``date_format`` is simply passed
        to that method.
        """

        expire_date = self.generator.date_time_between(start, end)
        return expire_date.strftime(date_format)
