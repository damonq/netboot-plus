Name:           amahi-netboot
Version: 0.2
Release:       1

Summary:        Amahi Netboot - Boot over the network

Group:          System Environment/Daemons
License:        GPL
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires: tftp-server

%define debug_package %{nil}
%define _binaries_in_noarch_packages_terminate_build 0

%description
Amahi Netboot - Boot over the network from your HDA

%prep
%setup -q

%build


%install
%{__mkdir} -p %{buildroot}/tftpboot/
%{__cp} -a tftp/* %{buildroot}/tftpboot/
%{__mkdir} -p %{buildroot}%{_sysconfdir}/dnsmasq.d/
%{__cp} -a amahi-pxe.conf %{buildroot}%{_sysconfdir}/dnsmasq.d/

%clean
rm -rf %{buildroot}

%post

# restart dns
if [[ -a /etc/xinetd.d/tftp ]] ; then
	sed -i -e 's|disabled.*=.*$|disabled = no|' /etc/xinetd.d/tftp
	/bin/systemctl enable xinetd.service &> /dev/null
	/bin/systemctl restart dnsmasq.service &> /dev/null
fi

%preun

%files
%defattr(-,root,root,-)
/tftpboot/*
%{_sysconfdir}/dnsmasq.d/amahi-pxe.conf

%changelog
* Mon Aug 12 2013 damonq 
- updated amahi-pxe.conf   added lines: enable-tftp  tftp-root=/tftpboot
- updated amahi-pxe.conf   removed ip 192.168.32.10 entry
- updated amahi-netboot.spec: changed default install directory from /var/lib/tftpboot/ to /tftpboot for erpxe plugin compatibility
- updated amahi-netboot.spec: added "%define" entry to resolve build error "Arch dependent binaries in noarch package"
- replaced tftp dir contents with erpxe base install package
- replaced syslinux 4.05 bootloaders & modules from erpxe with sylinux 6.01 bootloaders & modules for http & ftp support pxe-boot support introduced in syslinux 5.10
- added powerdown option to Main Menu utilizing syslinux powerdown.c32 module
- added compiled ipxelinux.0 bootloader & lpxelinux.0
* Wed Jul 17 2013 Carlos Puchol <cpg+git@amahi.org>
- updated for fedora 19
* Sun Aug  2 2009 Carlos Puchol <cpg+git@amahi.org>
- initial version
