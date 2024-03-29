%define		_doc_version	5.2.2
Summary:	Software package for booting x86 PCs over a network
Summary(pl.UTF-8):	Oprogramowanie do startowania komputerów PC poprzez sieć
Name:		etherboot
Version:	5.4.3
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/etherboot/%{name}-%{version}.tar.bz2
# Source0-md5:	813a9e1d5dec57dd1b9ddc106585acbe
Source1:	http://dl.sourceforge.net/etherboot/%{name}-doc-%{_doc_version}.tar.bz2
# Source1-md5:	1531d654a9534361c5339d931d5f92f4
URL:		http://etherboot.sourceforge.net/
BuildRequires:	cdrtools-mkisofs
BuildRequires:	mtools >= 3.9.10-1.20070411.1 
BuildRequires:	perl-base
BuildRequires:	syslinux
BuildRequires:	syslinux
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _noautostrip    .*

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

%description -l pl.UTF-8
Etherboot to "wolne" oprogramowanie służące do startowania komputerów
PC x86 poprzez sieć (dowolną sieć TCP/IP wspierającą rozgłaszanie
adresów (broadcasting)). W praktyce wymagania co do przepustowości
łącz ograniczają zastosowanie tego pakietu w sieciach LAN i niektórych
WAN. Etherboot jest użyteczny do startowania bezdyskowych PC.

%prep
%setup -q -a1

%build
# we don't use custom optimalizations here because it can cause problems
%{__make} -j1 \
	allcoms allelfs allisos allroms	\
	allzdsks allzhds allzlilos allzpxes allzroms	\
	-C src CC="%{__cc}"
# alllisos // Removed from make because It doesn't compile with proper mtools (don't know why)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/%{name}/{com,elf,iso,liso,rom,zdsk,zhd,zlilo,zpxe,zrom},%{_bindir}}

install src/bin/*.com $RPM_BUILD_ROOT%{_libdir}/%{name}/com
install src/bin/*.elf $RPM_BUILD_ROOT%{_libdir}/%{name}/elf
install src/bin/*.iso $RPM_BUILD_ROOT%{_libdir}/%{name}/iso
#install src/bin/*.liso $RPM_BUILD_ROOT%{_libdir}/%{name}/liso
install src/bin/*.rom $RPM_BUILD_ROOT%{_libdir}/%{name}/rom
install src/bin/*.zdsk $RPM_BUILD_ROOT%{_libdir}/%{name}/zdsk
install src/bin/*.zhd $RPM_BUILD_ROOT%{_libdir}/%{name}/zhd
install src/bin/*.zlilo $RPM_BUILD_ROOT%{_libdir}/%{name}/zlilo
install src/bin/*.zpxe $RPM_BUILD_ROOT%{_libdir}/%{name}/zpxe
install src/bin/*.zrom $RPM_BUILD_ROOT%{_libdir}/%{name}/zrom
install src/util/makerom.pl $RPM_BUILD_ROOT%{_bindir}/makerom.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc index.html contrib INSTALL RELNOTES doc/text/*txt src/bin/NIC
%{_libdir}/%{name}
%attr(755,root,root) %{_bindir}/*
