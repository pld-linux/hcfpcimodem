Summary:	Conexant HCF controllerless modem driver
Summary(pl):	Sterownik do winmodemów HCF firmy Conexant
Name:		hcfpcimodem
Version:	0.99mbsibeta02123100
%define	_rel	0.1
Release:	%{_rel}@%{_kernel_ver_str}
License:	Freely redistributable and some GPL
Group:		Base/Kernel
Source0:	http://www.mbsi.ca/cnxtlindrv/hcf/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
# Source0-md5: 3fa155c87fc30cd3b03835d0c3c76c7d
URL:		http://www.mbsi.ca/cnxtlindrv/
%{!?_without_dist_kernel:BuildRequires:	kernel-source }
BuildRequires:	%{kgcc_package}
%{!?_without_dist_kernel:%requires_releq_kernel_up}
Requires:	pciutils
Conflicts:	hcflinmodem
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Conexant HCF controllerless modem driver for Linux.

%description -l pl
Sterownik do winmodemów HCF firmy Conexant dla Linuxa.

%prep
%setup -q

%build
%{__make} all KERNELSRC=%{_kernelsrcdir} 
    
%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	ROOT=$RPM_BUILD_ROOT \
	KERNELSRC=%{_kernelsrcdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/hcfpciconfig --auto

%preun
%{_sbindir}/hcfpciconfig --remove

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES CREDITS FAQ INSTALL LICENSE README modules/COPYING
%attr(0755,root,root) %{_sbindir}/*
%dir /etc/hcfpci
%dir /etc/hcfpci/inf
%config /etc/hcfpci/inf/*
%dir %{_libdir}/hcfpci
%config %{_libdir}/hcfpci/config.mak
%{_libdir}/hcfpci/imported
%dir %{_libdir}/hcfpci/modules
%{_libdir}/hcfpci/modules/[!k]*
%attr(755,root,root) %{_libdir}/hcfpci/modules/*.sh
