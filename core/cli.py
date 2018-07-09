import argparse

def options():

    parser = argparse.ArgumentParser()

    modes_group = parser.add_argument_group('Modes')
    modes_group_ = modes_group.add_mutually_exclusive_group()

    modes_group_.add_argument('--create-bridge',
                        dest='create_bridge',
                        action='store_true',
                        help='create transparant bridge with phy and upstream ifaces as slaves')

    modes_group_.add_argument('--destroy-bridge',
                        dest='destroy_bridge',
                        action='store_true',
                        help='destroy transparant bridge and release all ifaces')

    modes_group_.add_argument('--ifaces-down',
                        dest='ifaces_down',
                        action='store_true',
                        help='bring all ifaces that are slaves to bridge down')

    modes_group_.add_argument('--ifaces-up',
                        dest='ifaces_up',
                        action='store_true',
                        help='bring all ifaces that are slaves to bridge up')

    modes_group_.add_argument('--bridge-up',
                        dest='bridge_up',
                        action='store_true',
                        help='bring bridge and all ifaces that are slaves to bridge up')

    modes_group_.add_argument('--bridge-down',
                        dest='bridge_down',
                        action='store_true',
                        help='bring bridge and all ifaces that are slaves to bridge down')

    modes_group_.add_argument('--rogue-gateway',
                        dest='rogue_gateway',
                        action='store_true',
                        help='perform rogue gateway attack')

    modes_group_.add_argument('--cert-wizard',
                        dest='cert_wizard',
                        action='store_true',
                        help='perform bate and switch attack')

    modes_group_.add_argument('--bate-n-switch',
                        dest='bate_n_switch',
                        action='store_true',
                        help='perform bate and switch attack')

    modes_group_.add_argument('--analyze_auth',
                        dest='analyze_auth',
                        action='store_true',
                        help='Enter analyze mode to determine EAP type and steal EAP-MD5 credentials.')

    modes_group_.add_argument('--discovery',
                        dest='discovery',
                        action='store_true',
                        help='Enter discovery mode to identify important data points such as MAC and IP addresses.')


# ------------------------------------------------------------------

    spoofing_params = parser.add_argument_group('Spoofing Params:')
    spoofing_params.add_argument('--client-mac',
                        dest='client_mac',
                        type=str,
                        help='MAC address for client device')

    spoofing_params.add_argument('--switch-mac',
                        dest='switch_mac',
                        type=str,
                        help='MAC address of switch')

    spoofing_params.add_argument('--gw-mac',
                        dest='gw_mac',
                        type=str,
                        help='MAC address of gateway')

    spoofing_params.add_argument('--client-ip',
                        dest='client_ip',
                        type=str,
                        help='IP address of client device')

    spoofing_params.add_argument('--switch-ip',
                        dest='switch_ip',
                        type=str,
                        help='IP address of upstream switch')

    spoofing_params.add_argument('--netmask',
                        dest='netmask',
                        required=False,
                        default='255.255.255.0',
                        help='Netmask of client device')

# ------------------------------------------------------------------

    interfaces_group = parser.add_argument_group('Interfaces:')

    interfaces_group.add_argument('--bridge',
                        dest='bridge',
                        type=str,
                        default='br0',
                        help='specify bridge iface (default: br0)')

    interfaces_group.add_argument('--sidechannel',
                        dest='sidechannel',
                        type=str,
                        help='Specify sidechannel interface (wifi, LTE, etc)')

    interfaces_group.add_argument('--upstream',
                        dest='upstream',
                        type=str,
                        help='Upstream network interface')

    interfaces_group.add_argument('--phy',
                        dest='phy',
                        type=str,
                        help='Downstream network interface')

# ------------------------------------------------------------------
    bate_n_switch_group = parser.add_argument_group('Bate n Switch')

    bate_n_switch_group.add_argument('--wired-conf',
                        dest='wired_conf',
                        type=str,
                        help='WPA supplicant conf file for Bate n Switch')

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

    parser.add_argument('--debug',
                        dest='debug',
                        action='store_true',
                        help='start in debug mode')

    args = parser.parse_args()

    missing_nec_params = any([
        args.phy is None,
        args.upstream is None,
        args.client_mac is None,
        args.switch_mac is None,
        args.sidechannel is None,
    ])
    if args.create_bridge and missing_nec_params:
        parser.error("--create-bridge requires the --phy, --sidechannel, --upstream, --client-mac, and --switch-mac flags")

    if args.analyze_auth and args.client_mac is None:
        parser.error("--analyze-auth requires --client-mac")

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
    ])
    if args.bate_n_switch and missing_nec_params:
        parser.error("--bate-n-switch requires --client-mac, --upstream, --client-ip, --netmask --wired-conf")

    missing_nec_params = any([
        args.upstream is None,
        args.phy is None,
    ])
    if args.discovery and missing_nec_params:
        parser.error("--discovery flag requires the --phy and --upstream flags")

    no_mode_selected = not any([
        args.analyze_auth,
        args.bate_n_switch,
        args.cert_wizard,
        args.rogue_gateway,
        args.create_bridge,
        args.destroy_bridge,
        args.ifaces_up,
        args.ifaces_down,
        args.bridge_up,
        args.bridge_down,
        args.discovery,
    ])
    if no_mode_selected:
        parser.error('You must select a valid mode.')

    return args.__dict__

