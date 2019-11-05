# Braintower Notification Plugin for checkmk

This plugin for checkmk allows users to configure notification rules using Braintower SMS gateways.

To connect to the Braintower SMS gateway, a Web-API user has to be configured via the Braintower web interface.

Multiple Braintower SMS gateways can be configured as a fallback solution. Each configured SMS gateway will be checked for error messages and the next one will be used if an error occured.