Summary:	software package for booting x86 PCs over a network
Summary(pl):	oprogramowanie do startowania komputerów PC poprzez sieæ
Name:		etherboot
Version:	4.7.18
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	http://etherboot.sourceforge.net/%{name}-%{version}.tar.bz2
URL:		http://etherboot.sourceforge.net/
Exclusivearch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Etherboot is a free software package for booting x86 PCs over a
network. In principle this could be any network technology that TCP/IP
runs on that supports broadcasting. In practice, the bandwidth
required means it's only practical over LANs and some WANs. Etherboot
is useful for booting PCs diskless. This is desirable in various
situations, for example:
  - Maintaining software for a cluster of equally configured
    workstations centrally.
  - A low-cost X-terminal.
  - A low cost user platform where remote partitions are mounted by NFS
    and you are willing to accept the slowness of data transfers that
    results from NFS, compared to a local disk.
  - Various kinds of remote servers, e.g. a tape drive server that can
    be accessed with the RMT protocol.
  - Routers.
  - Machines doing tasks in environments unfriendly to disks.

%description -l pl
Etherboot to "wolne" oprogramowanie s³u¿±ce do startowania komputerów
PC x86 poprzez sieæ (dowoln± sieæ TCP/IP wspieraj±c± rozg³aszanie
adresów (broadcasting)). W praktyce wymagania co do przepustowo¶ci
³±cz ograniczaj± zastosowanie tego pakietu w sieciach LAN i niektórych
WAN. Etherboot jest u¿yteczny do startowania bezdyskowych PC.

%prep
%setup -q

%build
%{__make} -C src
%{__make} -C mknbi-1.1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_libdir}/%{name}/{lzrom,rom}} \
	$RPM_BUILD_ROOT%{_mandir}/man1

install src/bin32/*.rom $RPM_BUILD_ROOT%{_libdir}/%{name}/rom
install src/bin32/*.lzrom $RPM_BUILD_ROOT%{_libdir}/%{name}/lzrom

install mknbi-*/{dismbr,disnbi,mklnim,mknbi} $RPM_BUILD_ROOT%{_sbindir}
install mknbi-*/*.1 $RPM_BUILD_ROOT%{_mandir}/man1/
install mknbi-*/*.pl $RPM_BUILD_ROOT%{_libdir}/%{name}

gzip -9nf INSTALL RELNOTES doc/text/*txt src/NIC

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz index.html doc/text/*.gz contrib src/*.gz
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/%{name}/*.pl
%{_libdir}/%{name}/rom
%{_libdir}/%{name}/lzrom
%attr(644,root,root) %{_mandir}/man1/*
%attr(755,root,root) %dir %{_libdir}/%{name}
