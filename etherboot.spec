Name:		etherboot
Version:	4.2.6
Release:	1
Summary:	software package for booting x86 PCs over a network
Summary(pl):	oprogramowanie do startowania komputerów PC poprzez sieæ
Source:		http://www.slug.org.au/etherboot/%{name}-%{version}.tar.bz2
Patch:		etherboot-fixes.patch
Group:		Utilities/System
Group(pl):	Narzêdzia/System
BuildRequires:	bin86
Copyright:	GPL
URL:		http://www.slug.org.au/etherboot/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
#ExcludeArch:	i386

%description
Etherboot is a free software package for booting x86 PCs over a network.
In principle this could be any network technology that TCP/IP runs on
that supports broadcasting. In practice, the bandwidth required means
it's only practical over LANs and some WANs. Etherboot is useful for
booting PCs diskless. This is desirable in various situations, for
example:
  * Maintaining software for a cluster of equally configured workstations
    centrally.
  * A low-cost X-terminal.
  * A low cost user platform where remote partitions are mounted by NFS
    and you are willing to accept the slowness of data transfers that
    results from NFS, compared to a local disk.
  * Various kinds of remote servers, e.g. a tape drive server that
    can be accessed with the RMT protocol.
  * Routers.
  * Machines doing tasks in environments unfriendly to disks.

%description -l pl
Etherboot to "wolne" oprogramowanie s³u¿±ce do startowania komputerów PC x86
poprzez sieæ (dowoln± sieæ TCP/IP wspieraj±c± rozg³aszanie adresów (broadcasting)).
W praktyce wymagania co do przepustowo¶ci ³±cz ograniczaj± zastosowanie
tego pakietu w sieciach LAN i niektórych WAN. Etherboot jest u¿yteczny
do startowania bezdyskowych PC.

%prep
%setup -q -n %{name}-4.2
%patch -p1

%build
cd netboot-* && %configure && make && cd ..
cd src-32 && make && cd ..

%install
rm -rf $RPM_BUILD_ROOT

install -d				 $RPM_BUILD_ROOT%{_sbindir}
install -d				 $RPM_BUILD_ROOT%{_datadir}/%{name}/{bin,lzrom,rom}
install -d				 $RPM_BUILD_ROOT%{_mandir}/man8

install src-32/*.bin			 $RPM_BUILD_ROOT%{_datadir}/%{name}/bin
install src-32/*.rom			 $RPM_BUILD_ROOT%{_datadir}/%{name}/rom
install src-32/*.lzrom			 $RPM_BUILD_ROOT%{_datadir}/%{name}/lzrom

install -s netboot-*/mknbi-blkdev/makec	 $RPM_BUILD_ROOT%{_sbindir}/makec-blkdev
install -s netboot-*/mknbi-blkdev/mknbi	 $RPM_BUILD_ROOT%{_sbindir}/mknbi-blkdev
install netboot-*/mknbi-blkdev/mknbi.man $RPM_BUILD_ROOT%{_mandir}/man8/mknbi-blkdev.8
install -s netboot-*/mknbi-dos/mknbi	 $RPM_BUILD_ROOT%{_sbindir}/mknbi-dos
install netboot-*/mknbi-dos/mknbi.man	 $RPM_BUILD_ROOT%{_mandir}/man8/mknbi-dos.8
install -s netboot-*/mknbi-linux/mknbi	 $RPM_BUILD_ROOT%{_sbindir}/mknbi-linux
install netboot-*/mknbi-linux/mknbi.man  $RPM_BUILD_ROOT%{_mandir}/man8/mknbi-linux.8

gzip -9nf INSTALL RELNOTES index.html doc/html/* $RPM_BUILD_ROOT%{_mandir}/man8/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {INSTALL,RELNOTES,index.html}.gz
%doc doc/html/* contrib
%attr(755,root,root) %{_sbindir}/*
%attr(644,root,root) %{_mandir}/man8/*
%attr(644,root,root) %{_datadir}/%{name}/*/*
%attr(755,root,root) %dir %{_datadir}/%{name}
%attr(755,root,root) %dir %{_datadir}/%{name}/bin
%attr(755,root,root) %dir %{_datadir}/%{name}/rom
%attr(755,root,root) %dir %{_datadir}/%{name}/lzrom
