Summary:	software package for booting x86 PCs over a network
Summary(pl):	oprogramowanie do startowania komputer�w PC poprzez sie�
Name:		etherboot
Version:	5.0.0
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	http://prdownloads.sourceforge.net/etherboot/%{name}-%{version}.tar.bz2     
Patch0:		%{name}-oformat.patch
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
Etherboot to "wolne" oprogramowanie s�u��ce do startowania komputer�w
PC x86 poprzez sie� (dowoln� sie� TCP/IP wspieraj�c� rozg�aszanie
adres�w (broadcasting)). W praktyce wymagania co do przepustowo�ci
��cz ograniczaj� zastosowanie tego pakietu w sieciach LAN i niekt�rych
WAN. Etherboot jest u�yteczny do startowania bezdyskowych PC.

%prep
%setup -q
%patch0 -p1

%build
# we don't use custom optimalizations here because it can cause problems
%{__make} -C src

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/{lzrom,rom}

install src/bin32/*.rom		$RPM_BUILD_ROOT%{_libdir}/%{name}/rom
install src/bin32/*.lzrom	$RPM_BUILD_ROOT%{_libdir}/%{name}/lzrom

gzip -9nf INSTALL RELNOTES doc/text/*txt src/NIC

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz index.html doc/text/*.gz contrib src/*.gz
%{_libdir}/%{name}
