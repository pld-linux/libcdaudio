Summary:	cdaudio library
Summary(pl):	Biblioteka cdaudio
Name:		libcdaudio
Version:	0.99.4
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.linuxberg.ps.pl/files/console/dev/%{name}-%{version}.tar.gz
URL:		http://cdcd.undergrid.net/libcdaudio/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libcdaudio is a library designed to provide functions to control
operation of a CD-ROM when playing audio CDs. It also contains
functions for CDDB and CD Index lookup.

%description -l pl
libcdaudio jest biblioteką zapewniającą funkcje kontrolujące działanie
CD-ROMu podczas odtwarzania płyt muzycznych. Wspiera również zapytania
CDDB i CD Index.

%package devel
Summary:	libcdaudio development
Summary(pl):	Biblioteki i pliki nagłówkowe libcdaudio
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
libcdaudio development.

%description devel -l pl
Biblioteki i pliki nagłówkowe libcdaudio.

%package static
Summary:	cdaudio static library
Summary(pl):	Biblioteka statyczna libcdaudio
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
cdaudio static library.

%description static -l pl
Biblioteka statyczna libcdaudio.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_includedir}/*
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
