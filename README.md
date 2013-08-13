netboot-plus
============

To Do:

1. Add automatic nfs configuration (must be manually added right now to /etc/exports) 
2. Add automatic http configuration
3. Add support for UEFI 
4. Create amahi boot splash
5. Customize menus for amahi 
6. Check modules libcom32.c32, ldllinux.c32, libutil.c32
7. Test plugins

Changes
- Existing erpxe syslinux 4.05 modules & bootloaders upgraded to syslinux 6.01
- New syslinux 6.01 modules & libraries added 
	1. cptime.c32
	2. hexdump.c32
	3. ifmemdsk.c32
	4. kontron_wdt.c32
	5. ldlinux.c32
	6. libcom32.c32
	7. libgpl.c32
	8. liblua.c32
	9. libmenu.c32
	10.libutil.c32
	11. poweroff.c32
	12. prdhcp.c32
	13. pxechn.c32


- Updated amahi-pxe.conf   added lines: enable-tftp  tftp-root=/tftpboot
- Updated amahi-pxe.conf   removed ip 192.168.32.10 entry
- Updated amahi-netboot.spec: changed default install directory from /var/lib/tftpboot/ to /tftpboot for erpxe plugin compatibility
- Updated amahi-netboot.spec: added "%define _binaries_in_noarch_packages_terminate_build 0" entry to resolve build error "Arch dependent binaries in noarch package"
- Replaced tftp dir contents with erpxe base install package
- Replaced syslinux 4.05 bootloaders & modules from erpxe with sylinux 6.01 bootloaders & modules for http & ftp support pxe-boot support introduced in syslinux 5.10
- Added powerdown option to erpxe Main Menu utilizing syslinux powerdown.c32, added powerdown.module to shared directory
- Updated undionly.kpxe  , see "http://ipxe.org/howto/chainloading"
- Added compiled ipxelinux.0 bootloader , see "https://coderwall.com/p/0sq9gg"
- Added lpxelinux.0 bootloader from syslinux 6.01

