import argparse

def options():

    parser = argparse.ArgumentParser()

    modes_group = parser.add_argument_group('Modes')
    modes_group_ = modes_group.add_mutually_exclusive_group()

    modes_group_.add_argument('--create-bridge',
                        dest='create_bridge',
                        action='store_true',
                        help='Create transparant bridge with phy and upstream ifaces as slaves.')

    modes_group_.add_argument('--destroy-bridge',
                        dest='destroy_bridge',
                        action='store_true',
                        help='Destroy transparant bridge and release all ifaces.')

    modes_group_.add_argument('--ifaces-down',
                        dest='ifaces_down',
                        action='store_true',
                        help='Bring all ifaces that are slaves to bridge down.')

    modes_group_.add_argument('--ifaces-up',
                        dest='ifaces_up',
                        action='store_true',
                        help='Bring all ifaces that are slaves to bridge up.')

    modes_group_.add_argument('--bridge-up',
                        dest='bridge_up',
                        action='store_true',
                        help='Bring bridge and all ifaces that are slaves to bridge up.')

    modes_group_.add_argument('--bridge-down',
                        dest='bridge_down',
                        action='store_true',
                        help='Bring bridge and all ifaces that are slaves to bridge down.')

    modes_group_.add_argument('--rogue-gateway',
                        dest='rogue_gateway',
                        action='store_true',
                        help='Perform Rogue Gateway attack.')

    modes_group_.add_argument('--add-interaction',
                        dest='add_interaction',
                        action='store_true',
                        help='Add interaction to bridge-based bypass.')

    modes_group_.add_argument('--cert-wizard',
                        dest='cert_wizard',
                        action='store_true',
                        help='Perform Bait and Switch attack.')

    modes_group_.add_argument('--bait-n-switch',
                        dest='bait_n_switch',
                        action='store_true',
                        help='Perform Bait and Switch attack.')

    modes_group_.add_argument('--analyze-auth-active',
                        dest='analyze_auth_active',
                        action='store_true',
                        help='Enter active analyze mode to determine EAP type and steal EAP-MD5 credentials. Uses bridge instead of passive LAN tap. Forces supplicant to reauthenticate.')

    modes_group_.add_argument('--discovery',
                        dest='discovery',
                        action='store_true',
                        help='Sniff traffic flowing across bridge to identify important data points such as MAC and IP address. Note that this mode is a wrapper for a hardcoded tcpdump command... you may have better results just using tcpdump for this purpose. Also, if your rogue device supports hardware bypass (see docs for more details), consider sniffing traffic from the passive LAN tap instead.')

    modes_group_.add_argument('--splitterctl',
                        dest='splitterctl',
                        action='store_true',
                        help='Manually control mechanical splitters if hardware bypass is supported (use in conjunction with --upstream-splitter and --phy-splitter flags).')

# ------------------------------------------------------------------

    spoofing_params = parser.add_argument_group('Spoofing Params')
    spoofing_params.add_argument('--client-mac',
                        dest='client_mac',
                        type=str,
                        help='MAC address for client device.')

    spoofing_params.add_argument('--switch-mac',
                        dest='switch_mac',
                        type=str,
                        help='MAC address of switch.')

    spoofing_params.add_argument('--gw-mac',
                        dest='gw_mac',
                        type=str,
                        help='MAC address of gateway.')

    spoofing_params.add_argument('--client-ip',
                        dest='client_ip',
                        type=str,
                        help='IP address of client device.')

    spoofing_params.add_argument('--switch-ip',
                        dest='switch_ip',
                        type=str,
                        help='IP address of upstream switch.')

    spoofing_params.add_argument('--gw-ip',
                        dest='gw_ip',
                        type=str,
                        help='IP address of the upstream gateway.')

    spoofing_params.add_argument('--netmask',
                        dest='netmask',
                        required=False,
                        default='255.255.255.0',
                        help='Netmask of client device.')

# ------------------------------------------------------------------

    interfaces_group = parser.add_argument_group('Interfaces')

    interfaces_group.add_argument('--bridge',
                        dest='bridge',
                        type=str,
                        default='br0',
                        help='Specify bridge iface (default: br0).')

    interfaces_group.add_argument('--sidechannel',
                        dest='sidechannel',
                        type=str,
                        help='Specify sidechannel interface (wifi, LTE, etc).')

    interfaces_group.add_argument('--upstream',
                        dest='upstream',
                        type=str,
                        help='Upstream network interface.')

    interfaces_group.add_argument('--phy',
                        dest='phy',
                        type=str,
                        help='Downstream network interface.')

# ------------------------------------------------------------------

    bait_n_switch_group = parser.add_argument_group('Bait n Switch')

    bait_n_switch_group.add_argument('--wired-conf',
                        dest='wired_conf',
                        type=str,
                        help='WPA supplicant conf file for Bait n Switch')

# ------------------------------------------------------------------

    splitterctl_group = parser.add_argument_group('Splitter Control Group')

    splitterctl_group.add_argument('--upstream-splitter',
                        dest='upstream_splitter',
                        type=str,
                        choices=['connect', 'bypass'],
                        help='Set upstream splitter to connect or bypass.')

    splitterctl_group.add_argument('--phy-splitter',
                        dest='phy_splitter',
                        type=str,
                        choices=['connect', 'bypass'],
                        help='Set PHY splitter to connect or bypass.')

# ------------------------------------------------------------------

    discovery_group = parser.add_argument_group('Discovery')

    discovery_group.add_argument('--client-only',
                        dest='client_only',
                        action='store_true',
                        help='Only perform discovery by sniffing client-side interface (PHY). Keep all other interfaces down.')

# ------------------------------------------------------------------

    parser.add_argument('--egress-port',
                        dest='egress_port',
                        type=int,
                        default=22,
                        help='Allow outbound connections to PORT from --sidechannel interface. (default: 22)')

    parser.add_argument('--use-splitters',
                        dest='use_splitters',
                        action='store_true',
                        help='Use mechanical splitters for Rogue Gateway and Bait n Switch.')

    parser.add_argument('--debug',
                        dest='debug',
                        action='store_true',
                        help='start in debug mode')

    args = parser.parse_args()

    missing_nec_params = any([
        args.phy is None,
        args.upstream is None,
        args.sidechannel is None,
    ])
    if args.create_bridge and missing_nec_params:
        parser.error("--create-bridge requires the --phy, --sidechannel, and --upstream flags")

    missing_nec_params = any([
        args.phy is None,
        args.upstream is None,
        args.sidechannel is None,
        args.client_mac is None,
        args.client_ip is None,
        args.gw_mac is None,
    ])
    if args.add_interaction and missing_nec_params:
        parser.error("--add-interaction requires the --phy, --sidechannel, --upstream, --client-mac, --client-ip, and --gw-mac flags")

    missing_nec_params = any([
        args.upstream is None,
        args.client_mac is None,
    ])
    if args.analyze_auth_active and  missing_nec_params:
        parser.error("--analyze-auth-active requires --client-mac and --upstream")

    missing_nec_params = any([
        args.switch_mac is None,
        args.phy is None,
        args.client_mac is None,
    ])
    if args.rogue_gateway and missing_nec_params:
        parser.error("--rogue-gateway requires --client-mac, --switch-mac, --phy, --netmask, --switch-ip")

    missing_nec_params = any([
        args.client_mac is None,
        args.upstream is None,
        args.netmask is None,
        args.client_ip is None,
        args.wired_conf is None,
        args.gw_ip is None,
    ])
    if args.bait_n_switch and missing_nec_params:
        parser.error("--bait-n-switch requires --client-mac, --upstream, --client-ip, --netmask --wired-conf")

    missing_nec_params = any([
        args.upstream is None,
        args.phy is None,
    ])
    if args.discovery and missing_nec_params:
        parser.error("--discovery flag requires the --phy and --upstream flags")

    missing_nec_params = any([
        args.upstream_splitter is None,
        args.phy_splitter is None,
    ])
    if args.splitterctl and missing_nec_params:
        parser.error("--splitterctl requires the --upstream-splitter and --phy-splitter flags")

    no_mode_selected = not any([
        args.analyze_auth_active,
        args.bait_n_switch,
        args.cert_wizard,
        args.rogue_gateway,
        args.create_bridge,
        args.destroy_bridge,
        args.ifaces_up,
        args.ifaces_down,
        args.bridge_up,
        args.bridge_down,
        args.discovery,
        args.splitterctl,
        args.add_interaction,
    ])
    if no_mode_selected:
        parser.error('You must select a valid mode.')

    return args.__dict__

