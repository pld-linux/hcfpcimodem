
Summary:	Conexant HCF controllerless modem driver
Summary(pl):	Strownik do winmodemów HCF firmy Conexant
Name:		hcfpcimodem
Version:	0.98mbsibeta02110301
Release:	1
License:	Freely redistributable and some GPL
Group:		Base/Kernel
Source0:	http://www.mbsi.ca/cnxtlindrv/hcf/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
URL:		http://www.mbsi.ca/
Requires:	pciutils
Conflicts:	hcflinmodem
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Conexant HCF controllerless modem driver for Linux.

%description -l pl
Strownik do winmodemów HCF firmy Conexant dla Linuxa.

%prep
%setup -q

%build
%{__make} all
    
%install
rm -rf $RPM_BUILD_ROOT

%{__make} install ROOT=$RPM_BUILD_ROOT

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
%dir %{_libdir}/hcfpci/modules
%{_libdir}/hcfpci/imported
%{_libdir}/hcfpci/modules/[!k]*
%attr(755,root,root) %{_libdir}/hcfpci/modules/*.sh
