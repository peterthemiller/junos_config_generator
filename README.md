# junos_config_generator
Generates Juniper configuration files for easy deployment to a lab environment

Main device template (device_template.j2) contains basic system host-name and root-authentication configuration
Other templates add on vlans, routed interfaces, ntp, etc.
Future lab features, such as OSPF, are planned for future templates.

The lab devices used are QFX-RE vms in Cisco CML. This limits the interfaces available, and cannot properly simulate any hosts, only the switch to switch connectivity.

