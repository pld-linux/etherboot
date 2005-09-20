%define		_doc_version	5.2.2
Summary:	Software package for booting x86 PCs over a network
Summary(pl):	Oprogramowanie do startowania komputer�w PC poprzez sie�
Name:		etherboot
Version:	5.4.1
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/etherboot/%{name}-%{version}.tar.bz2
# Source0-md5:	9d8666f32ca259a045130487e382f88b
Source1:	http://dl.sourceforge.net/etherboot/%{name}-doc-%{_doc_version}.tar.bz2
# Source1-md5:	1531d654a9534361c5339d931d5f92f4
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
Etherboot to "wolne" oprogramowanie s�u��ce do startowania komputer�w
PC x86 poprzez sie� (dowoln� sie� TCP/IP wspieraj�c� rozg�aszanie
adres�w (broadcasting)). W praktyce wymagania co do przepustowo�ci
��cz ograniczaj� zastosowanie tego pakietu w sieciach LAN i niekt�rych
WAN. Etherboot jest u�yteczny do startowania bezdyskowych PC.

%prep
%setup -q -a1

%build
# we don't use custom optimalizations here because it can cause problems
%{__make} allzroms alllisos -C src \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/%{name}/{zrom,liso},%{_bindir}}

install src/bin/*.zrom $RPM_BUILD_ROOT%{_libdir}/%{name}/zrom
install src/bin/*.liso $RPM_BUILD_ROOT%{_libdir}/%{name}/liso
install src/util/makerom.pl $RPM_BUILD_ROOT%{_bindir}/makerom.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc index.html contrib INSTALL RELNOTES doc/text/*txt src/bin/NIC
%{_libdir}/%{name}
%attr(755,root,root) %{_bindir}/*
