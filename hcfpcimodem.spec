Summary:	Conexant HCF controllerless modem driver
Summary(pl.UTF-8):	Sterownik do winmodemów HCF firmy Conexant
Name:		hcfpcimodem
Version:	0.99lnxtbeta03042700
%define	_rel	0.1
Release:	%{_rel}@%{_kernel_ver_str}
License:	Freely redistributable and some GPL
Group:		Base/Kernel
Source0:	http://www.linuxant.com/drivers/hcf/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f3fc1cb0b35e7cbd54132aeac66667ab
URL:		http://www.linuxant.com/
%{!?_without_dist_kernel:BuildRequires:	kernel-source }
BuildRequires:	%{kgcc_package}
%{!?_without_dist_kernel:%requires_releq_kernel_up}
Requires:	pciutils
Conflicts:	hcflinmodem
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Conexant HCF controllerless modem driver for Linux.

%description -l pl.UTF-8
Sterownik do winmodemów HCF firmy Conexant dla Linuksa.

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
