%define		_doc_version	5.0.11
Summary:	Software package for booting x86 PCs over a network
Summary(pl):	Oprogramowanie do startowania komputerów PC poprzez sieæ
Name:		etherboot
Version:	5.0.11
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/etherboot/%{name}-%{version}.tar.bz2
# Source0-md5:	f23e90c9e33916fb1f0298ef67810b05
Source1:	http://dl.sourceforge.net/etherboot/%{name}-doc-%{_doc_version}.tar.bz2
# Source1-md5:	f178fd5324f7860d1cdd8372e286a334
URL:		http://etherboot.sourceforge.net/
ExclusiveArch:	%{ix86}
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
%setup -q -a1

%build
# we don't use custom optimalizations here because it can cause problems
%{__make} -C src
%{__make} bin/boot1a.bin -C src

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/%{name}/{lzrom,rom},%{_bindir}}

install src/bin32/*.rom $RPM_BUILD_ROOT%{_libdir}/%{name}/rom
install src/bin32/*.lzrom $RPM_BUILD_ROOT%{_libdir}/%{name}/lzrom
install src/bin/*.bin $RPM_BUILD_ROOT%{_libdir}/%{name}
install src/bin/makerom	$RPM_BUILD_ROOT%{_bindir}/makerom

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc index.html contrib INSTALL RELNOTES doc/text/*txt src/NIC
%{_libdir}/%{name}
%attr(755,root,root) %{_bindir}/*
