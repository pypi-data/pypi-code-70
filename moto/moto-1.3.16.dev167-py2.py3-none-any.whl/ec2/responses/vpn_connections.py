from __future__ import unicode_literals
from moto.core.responses import BaseResponse
from moto.ec2.utils import filters_from_querystring


class VPNConnections(BaseResponse):
    def create_vpn_connection(self):
        type = self._get_param("Type")
        cgw_id = self._get_param("CustomerGatewayId")
        vgw_id = self._get_param("VpnGatewayId")
        static_routes = self._get_param("StaticRoutesOnly")
        vpn_connection = self.ec2_backend.create_vpn_connection(
            type, cgw_id, vgw_id, static_routes_only=static_routes
        )
        template = self.response_template(CREATE_VPN_CONNECTION_RESPONSE)
        return template.render(vpn_connection=vpn_connection)

    def delete_vpn_connection(self):
        vpn_connection_id = self._get_param("VpnConnectionId")
        vpn_connection = self.ec2_backend.delete_vpn_connection(vpn_connection_id)
        template = self.response_template(DELETE_VPN_CONNECTION_RESPONSE)
        return template.render(vpn_connection=vpn_connection)

    def describe_vpn_connections(self):
        vpn_connection_ids = self._get_multi_param("VpnConnectionId")
        filters = filters_from_querystring(self.querystring)
        vpn_connections = self.ec2_backend.get_all_vpn_connections(
            vpn_connection_ids=vpn_connection_ids, filters=filters
        )
        template = self.response_template(DESCRIBE_VPN_CONNECTION_RESPONSE)
        return template.render(vpn_connections=vpn_connections)


CREATE_VPN_CONNECTION_RESPONSE = """
<CreateVpnConnectionResponse xmlns="http://ec2.amazonaws.com/doc/2013-10-15/">
  <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
  <vpnConnection>
    <vpnConnectionId>{{ vpn_connection.id }}</vpnConnectionId>
    <state>pending</state>
      <customerGatewayConfiguration>
        <vpn_connection id="{{ vpn_connection.id }}">
          <customer_gateway_id>{{ vpn_connection.customer_gateway_id }}</customer_gateway_id>
          <vpn_gateway_id>{{ vpn_connection.vpn_gateway_id }}</vpn_gateway_id>
          <vpn_connection_type>ipsec.1</vpn_connection_type>
          <ipsec_tunnel>
            <customer_gateway>
            <tunnel_outside_address>
              <ip_address>12.1.2.3</ip_address>
            </tunnel_outside_address>
            <tunnel_inside_address>
              <ip_address>169.254.44.42</ip_address>
              <network_mask>255.255.255.252</network_mask>
              <network_cidr>30</network_cidr>
            </tunnel_inside_address>
            <bgp>
              <asn>65000</asn>
              <hold_time>30</hold_time>
            </bgp>
            </customer_gateway>
            <vpn_gateway>
            <tunnel_outside_address>
              <ip_address>52.2.144.13</ip_address>
            </tunnel_outside_address>
            <tunnel_inside_address>
              <ip_address>169.254.44.41</ip_address>
              <network_mask>255.255.255.252</network_mask>
              <network_cidr>30</network_cidr>
            </tunnel_inside_address>
            <bgp>
              <asn>7224</asn>
              <hold_time>30</hold_time>
            </bgp>
            </vpn_gateway>
            <ike>
            <authentication_protocol>sha1</authentication_protocol>
            <encryption_protocol>aes-128-cbc</encryption_protocol>
            <lifetime>28800</lifetime>
            <perfect_forward_secrecy>group2</perfect_forward_secrecy>
            <mode>main</mode>
            <pre_shared_key>Iw2IAN9XUsQeYUrkMGP3kP59ugFDkfHg</pre_shared_key>
            </ike>
            <ipsec>
            <protocol>esp</protocol>
            <authentication_protocol>hmac-sha1-96</authentication_protocol>
            <encryption_protocol>aes-128-cbc</encryption_protocol>
            <lifetime>3600</lifetime>
            <perfect_forward_secrecy>group2</perfect_forward_secrecy>
            <mode>tunnel</mode>
            <clear_df_bit>true</clear_df_bit>
            <fragmentation_before_encryption>true</fragmentation_before_encryption>
            <tcp_mss_adjustment>1387</tcp_mss_adjustment>
            <dead_peer_detection>
              <interval>10</interval>
              <retries>3</retries>
            </dead_peer_detection>
            </ipsec>
          </ipsec_tunnel>
          <ipsec_tunnel>
            <customer_gateway>
            <tunnel_outside_address>
              <ip_address>12.1.2.3</ip_address>
            </tunnel_outside_address>
            <tunnel_inside_address>
              <ip_address>169.254.44.42</ip_address>
              <network_mask>255.255.255.252</network_mask>
              <network_cidr>30</network_cidr>
            </tunnel_inside_address>
            <bgp>
              <asn>65000</asn>
              <hold_time>30</hold_time>
            </bgp>
            </customer_gateway>
            <vpn_gateway>
            <tunnel_outside_address>
              <ip_address>52.2.144.13</ip_address>
            </tunnel_outside_address>
            <tunnel_inside_address>
              <ip_address>169.254.44.41</ip_address>
              <network_mask>255.255.255.252</network_mask>
              <network_cidr>30</network_cidr>
            </tunnel_inside_address>
            <bgp>
              <asn>7224</asn>
              <hold_time>30</hold_time>
            </bgp>
            </vpn_gateway>
            <ike>
            <authentication_protocol>sha1</authentication_protocol>
            <encryption_protocol>aes-128-cbc</encryption_protocol>
            <lifetime>28800</lifetime>
            <perfect_forward_secrecy>group2</perfect_forward_secrecy>
            <mode>main</mode>
            <pre_shared_key>Iw2IAN9XUsQeYUrkMGP3kP59ugFDkfHg</pre_shared_key>
            </ike>
            <ipsec>
            <protocol>esp</protocol>
            <authentication_protocol>hmac-sha1-96</authentication_protocol>
            <encryption_protocol>aes-128-cbc</encryption_protocol>
            <lifetime>3600</lifetime>
            <perfect_forward_secrecy>group2</perfect_forward_secrecy>
            <mode>tunnel</mode>
            <clear_df_bit>true</clear_df_bit>
            <fragmentation_before_encryption>true</fragmentation_before_encryption>
            <tcp_mss_adjustment>1387</tcp_mss_adjustment>
            <dead_peer_detection>
              <interval>10</interval>
              <retries>3</retries>
            </dead_peer_detection>
            </ipsec>
          </ipsec_tunnel>
        </vpn_connection>
      </customerGatewayConfiguration>
    <type>ipsec.1</type>
    <customerGatewayId>{{ vpn_connection.customer_gateway_id }}</customerGatewayId>
    <vpnGatewayId>{{ vpn_connection.vpn_gateway_id }}</vpnGatewayId>
    <tagSet>
    {% for tag in vpn_connection.get_tags() %}
      <item>
        <resourceId>{{ tag.resource_id }}</resourceId>
        <resourceType>{{ tag.resource_type }}</resourceType>
        <key>{{ tag.key }}</key>
        <value>{{ tag.value }}</value>
      </item>
    {% endfor %}
    </tagSet>
  </vpnConnection>
</CreateVpnConnectionResponse>"""

CREATE_VPN_CONNECTION_ROUTE_RESPONSE = """
<CreateVpnConnectionRouteResponse xmlns="http://ec2.amazonaws.com/doc/2013-10- 15/">
    <requestId>4f35a1b2-c2c3-4093-b51f-abb9d7311990</requestId>
    <return>true</return>
</CreateVpnConnectionRouteResponse>"""

DELETE_VPN_CONNECTION_RESPONSE = """
<DeleteVpnConnectionResponse xmlns="http://ec2.amazonaws.com/doc/2013-10-15/">
   <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
   <return>true</return>
</DeleteVpnConnectionResponse>"""

DELETE_VPN_CONNECTION_ROUTE_RESPONSE = """
<DeleteVpnConnectionRouteResponse xmlns="http://ec2.amazonaws.com/doc/2013-10- 15/">
    <requestId>4f35a1b2-c2c3-4093-b51f-abb9d7311990</requestId>
    <return>true</return>
</DeleteVpnConnectionRouteResponse>"""

DESCRIBE_VPN_CONNECTION_RESPONSE = """
<DescribeVpnConnectionsResponse xmlns="http://ec2.amazonaws.com/doc/2013-10-15/">
  <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
  <vpnConnectionSet>
    {% for vpn_connection in vpn_connections %}
    <item>
      <vpnConnectionId>{{ vpn_connection.id }}</vpnConnectionId>
      <state>available</state>
      <customerGatewayConfiguration>
        <vpn_connection id="{{ vpn_connection.id }}">
          <customer_gateway_id>{{ vpn_connection.customer_gateway_id }}</customer_gateway_id>
          <vpn_gateway_id>{{ vpn_connection.vpn_gateway_id }}</vpn_gateway_id>
          <vpn_connection_type>ipsec.1</vpn_connection_type>
          <ipsec_tunnel>
            <customer_gateway>
            <tunnel_outside_address>
              <ip_address>12.1.2.3</ip_address>
            </tunnel_outside_address>
            <tunnel_inside_address>
              <ip_address>169.254.44.42</ip_address>
              <network_mask>255.255.255.252</network_mask>
              <network_cidr>30</network_cidr>
            </tunnel_inside_address>
            <bgp>
              <asn>65000</asn>
              <hold_time>30</hold_time>
            </bgp>
            </customer_gateway>
            <vpn_gateway>
            <tunnel_outside_address>
              <ip_address>52.2.144.13</ip_address>
            </tunnel_outside_address>
            <tunnel_inside_address>
              <ip_address>169.254.44.41</ip_address>
              <network_mask>255.255.255.252</network_mask>
              <network_cidr>30</network_cidr>
            </tunnel_inside_address>
            <bgp>
              <asn>7224</asn>
              <hold_time>30</hold_time>
            </bgp>
            </vpn_gateway>
            <ike>
            <authentication_protocol>sha1</authentication_protocol>
            <encryption_protocol>aes-128-cbc</encryption_protocol>
            <lifetime>28800</lifetime>
            <perfect_forward_secrecy>group2</perfect_forward_secrecy>
            <mode>main</mode>
            <pre_shared_key>Iw2IAN9XUsQeYUrkMGP3kP59ugFDkfHg</pre_shared_key>
            </ike>
            <ipsec>
            <protocol>esp</protocol>
            <authentication_protocol>hmac-sha1-96</authentication_protocol>
            <encryption_protocol>aes-128-cbc</encryption_protocol>
            <lifetime>3600</lifetime>
            <perfect_forward_secrecy>group2</perfect_forward_secrecy>
            <mode>tunnel</mode>
            <clear_df_bit>true</clear_df_bit>
            <fragmentation_before_encryption>true</fragmentation_before_encryption>
            <tcp_mss_adjustment>1387</tcp_mss_adjustment>
            <dead_peer_detection>
              <interval>10</interval>
              <retries>3</retries>
            </dead_peer_detection>
            </ipsec>
          </ipsec_tunnel>
          <ipsec_tunnel>
            <customer_gateway>
            <tunnel_outside_address>
              <ip_address>12.1.2.3</ip_address>
            </tunnel_outside_address>
            <tunnel_inside_address>
              <ip_address>169.254.44.42</ip_address>
              <network_mask>255.255.255.252</network_mask>
              <network_cidr>30</network_cidr>
            </tunnel_inside_address>
            <bgp>
              <asn>65000</asn>
              <hold_time>30</hold_time>
            </bgp>
            </customer_gateway>
            <vpn_gateway>
            <tunnel_outside_address>
              <ip_address>52.2.144.13</ip_address>
            </tunnel_outside_address>
            <tunnel_inside_address>
              <ip_address>169.254.44.41</ip_address>
              <network_mask>255.255.255.252</network_mask>
              <network_cidr>30</network_cidr>
            </tunnel_inside_address>
            <bgp>
              <asn>7224</asn>
              <hold_time>30</hold_time>
            </bgp>
            </vpn_gateway>
            <ike>
            <authentication_protocol>sha1</authentication_protocol>
            <encryption_protocol>aes-128-cbc</encryption_protocol>
            <lifetime>28800</lifetime>
            <perfect_forward_secrecy>group2</perfect_forward_secrecy>
            <mode>main</mode>
            <pre_shared_key>Iw2IAN9XUsQeYUrkMGP3kP59ugFDkfHg</pre_shared_key>
            </ike>
            <ipsec>
            <protocol>esp</protocol>
            <authentication_protocol>hmac-sha1-96</authentication_protocol>
            <encryption_protocol>aes-128-cbc</encryption_protocol>
            <lifetime>3600</lifetime>
            <perfect_forward_secrecy>group2</perfect_forward_secrecy>
            <mode>tunnel</mode>
            <clear_df_bit>true</clear_df_bit>
            <fragmentation_before_encryption>true</fragmentation_before_encryption>
            <tcp_mss_adjustment>1387</tcp_mss_adjustment>
            <dead_peer_detection>
              <interval>10</interval>
              <retries>3</retries>
            </dead_peer_detection>
            </ipsec>
          </ipsec_tunnel>
        </vpn_connection>
      </customerGatewayConfiguration>
      <type>ipsec.1</type>
      <customerGatewayId>{{ vpn_connection.customer_gateway_id }}</customerGatewayId>
      <vpnGatewayId>{{ vpn_connection.vpn_gateway_id }}</vpnGatewayId>
      <tagSet>
      {% for tag in vpn_connection.get_tags() %}
        <item>
          <resourceId>{{ tag.resource_id }}</resourceId>
          <resourceType>{{ tag.resource_type }}</resourceType>
          <key>{{ tag.key }}</key>
          <value>{{ tag.value }}</value>
        </item>
      {% endfor %}
      </tagSet>
    </item>
    {% endfor %}
  </vpnConnectionSet>
</DescribeVpnConnectionsResponse>"""
