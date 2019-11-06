#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# Copyright 2019 Fabian Binder, comNET GmbH <fabian.binder@comnetgmbh.com>
#
# This file is part of braintower_notifications.
#
# braintower_notifications is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# braintower_notifications is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with braintower_notifications.  If not, see <http://www.gnu.org/licenses/>.
#

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
