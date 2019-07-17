![](https://raw.githubusercontent.com/s0lst1c3/readme-images/master/silent-bridge-logo.png)

# silentbridge
by Gabriel Ryan ([@s0lst1c3](https://twitter.com/s0lst1c3)) @ SpecterOps (gryan@specterops.io)

## Overview

Silentbridge is a toolkit for quickly bypassing 802.1x port security first presented at DEF CON 26. It provides the first documented means of bypassing 802.1x-2010 via its authentication process, as well as improvements to existing techniques for bypassing 802.1x-2004.

You can check out the accompanying whitepaper at [https://www.researchgate.net/publication/327402715_Bypassing_Port_Security_In_2018_-_Defeating_MACsec_and_8021x-2010](https://www.researchgate.net/publication/327402715_Bypassing_Port_Security_In_2018_-_Defeating_MACsec_and_8021x-2010). 

## Getting Started
For usage and setup instructions, please refer to the project's wiki page:

- [https://github.com/s0lst1c3/silentbridge/wiki](https://github.com/s0lst1c3/silentbridge/wiki)


These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Contributing

Contributions are encouraged and more than welcome. Guidelines for creating pull requests and reporting issues can be found in  [CONTRIBUTING.md](CONTRIBUTING.md).

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see  [https://github.com/s0lst1c3/silentbridge/tags](https://github.com/s0lst1c3/silentbridge/tags). 

## License

This project is licensed under the GNU Public License 3.0 - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments
This tool either builds upon, is inspired by, or directly incorporates over ten years of prior research and development from the following awesome people:

- [Steve Riley - Hub-based 802.1x-2004 bypass](https://blogs.technet.microsoft.com/steriley/2005/08/11/august-article-802-1x-on-wired-networks-considered-harmful/)
- [Alva Duckwall - Bridge-based 802.1x-2004 bypass](https://www.defcon.org/images/defcon-19/dc-19-presentations/Duckwall/DEFCON-19-Duckwall-Bridge-Too-Far.pdf)
- [Abb - Tap-based 802.1x-2004 bypass](https://www.gremwell.com/marvin-mitm-tapping-dot1x-links)
- [Valerian Legrand - Injection-based 802.1x-2004 bypass](https://hackinparis.com/data/slides/2017/2017_Legrand_Valerian_802.1x_Network_Access_Control_and_Bypass_Techniques.pdf)
- [Josh Wright and Brad Antoniewicz - Attacks Against Weak EAP Methods](http://www.willhackforsushi.com/presentations/PEAP_Shmoocon2008_Wright_Antoniewicz.pdf)
- [Dom White and Ian de Villier - More Attacks Against Weak EAP Methods](https://sensepost.com/blog/2015/improvements-in-rogue-ap-attacks-mana-1%2F2/)
- [Moxie Marlinspike and David Hulton - Attacks Against MS-CHAPv2](http://web.archive.org/web/20160203043946/https:/www.cloudcracker.com/blog/2012/07/29/cracking-ms-chap-v2/)

Additional thanks to [@LargeCardinal](https://twitter.com/LargeCardinal) for convincing me to actually follow through with this idea. 
