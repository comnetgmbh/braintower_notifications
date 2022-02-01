# Braintower Notification Plugin for checkmk

Note: This notification plugin is outdated and has been replaced by the brevis.one plugin at https://github.com/comnetgmbh/brevis_one_notifications

This plugin for checkmk allows users to configure notification rules using Braintower SMS gateways.

To connect to the Braintower SMS gateway, a Web-API user has to be configured via the Braintower web interface.

Multiple Braintower SMS gateways can be configured as a fallback solution. Each configured SMS gateway will be checked for error messages and the next one will be used if an error occured.
