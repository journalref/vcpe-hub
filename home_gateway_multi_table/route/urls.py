# service control
get_sc_sequence = '/service-control/sequence'
get_sc_priority = '/service-control/priority'
get_sc_status = '/service-control/status'
put_service_enable = '/service-control/enable'
put_service_disable = '/service-control/disable'

# firewall
get_fw_rules = '/firewall/rules'
put_fw_knownport_add = '/firewall/known-port/add'
put_fw_knownport_delete = '/firewall/known-port/delete'
put_fw_customport_add = '/firewall/custom-port/add'
put_fw_customport_delete = '/firewall/custom-port/delete'

# nat + dhcp
post_nat_config_init = '/nat/config/init'
put_nat_config_save = '/nat/config/save'
get_nat_config = '/nat/config'
get_dhcp_config = '/dhcp/config'

# qos
# meter
get_qos_meter = '/qos/meter'
put_qos_meter_add = '/qos/meter/add'
put_qos_meter_delete = '/qos/meter/delete'
put_qos_meter_modify = '/qos/meter/modify'
# topology
get_qos_topology = '/qos/topology'
# application(W.I.P.)
# rate-limit
get_qos_rate_limit_member = '/qos/rate-limit/member'
put_qos_rate_limit_member = '/qos/rate-limit/member'
get_qos_rate_limit_app = '/qos/rate-limit/application'
put_qos_rate_limit_app = '/qos/rate-limit/application'
