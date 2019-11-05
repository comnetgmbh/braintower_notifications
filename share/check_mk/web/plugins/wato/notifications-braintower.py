#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

register_notification_parameters(
    'braintower',
    Dictionary(
        required_keys = ['host'],
        elements = [
            ( 'host',
                ListOfStrings(
                    title = _('Braintower gateways'),
                    help = _('Hostname, IPv4 or IPv6 address of the Braintower systems. '
                             'If the connection to the first gateway fails, the notification'
                             'script will try to send the notification using the next gateway.'),
                    size = 40,
                    allow_empty = False,
                )
            ),
            ( 'username',
                TextAscii(
                    title = _('Username'),
                    help = _('Username used for authentication at the Braintower Web-API'),
                    default_value = 'braintower',
                    size = 40,
                    allow_empty = False,
                )
            ),
            ( 'password',
                Password(
                    title = _('Password'),
                    help = _('Password used for authentication at the Braintower Web-API'),
                    default_value = 'braintower',
                    size = 40,
                    allow_empty = False,
                )
            ),
        ]
    )
)
