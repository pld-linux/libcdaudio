%bcond_without	static	# don't build static library
Summary:	A library of functions for controlling audio CD-ROM players
Summary(fr):	Une bibliothèque pour le contrôle des lecteurs de CD-ROMS audio
Summary(it):	Una libreria di funzioni per controllare i lettori di CD-AUDIO
Summary(pl):	Biblioteka funkcji steruj±cych odtwarzaniem muzycznych p³yt CD
Summary(sk):	Kni¾nica funkcií pre ovládanie prehrávaèov zvukových CD-ROM
Name:		libcdaudio
Version:	0.99.4
Release:	4
License:	GPL
Group:		Libraries
Source0:	http://www.linuxberg.ps.pl/files/console/dev/%{name}-%{version}.tar.gz
# Source0-md5:	a6a2939cb762e930ba8971f8539f76da
Patch0:		%{name}-am18.patch
URL:		http://cdcd.undergrid.net/libcdaudio/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fomit-frame-pointer

%description
libcdaudio is a library designed to provide functions to control
operation of a CD-ROM when playing audio CDs. It also contains
functions for CDDB and CD Index lookup.

%description -l fr
libcdaudio est une bibliothèque pour développer des lecteurs de CDs.
Elle comprend le jeu de commandes de base pour contrôler la lecture
des CDs ainsi que des fonctions d'accès à CDDB, à CD index et Cover
Art Index.

%description -l it
libcdaudio e' un librerie per lo sviluppo di lettori di CD audio che
include un set base di comandi per controllare le operazioni del
lettore CD-ROM cosi' come funzioni per accedere ai CDDB, i CD indice,
i cd di cover art.

%description -l pl
libcdaudio jest bibliotek± zapewniaj±c± funkcje kontroluj±ce dzia³anie
CD-ROMu podczas odtwarzania p³yt muzycznych. Wspiera równie¿ zapytania
CDDB i CD Index.

%description -l sk
libcdaudio je kni¾nica pre vývoj CD prehrávaèov, obsahujúca základnú
sadu príkazov pre ovládanie CD-ROM jednotky, ako aj funkcie pre
prístup k CDDB, CD indexu a indexu obalov.

%package devel
Summary:	Header files and libraries for libcdaudio development
Summary(cs):	Knihovny a hlavièkové soubory pro vývoj s libcdaudio
Summary(fr):	Fichiers en-tête et bibliothèques de développement pour libcdaudio
Summary(it):	File header e librerie per lo sviluppo con libcdaudio
Summary(pl):	Biblioteki i pliki nag³ówkowe libcdaudio
Summary(sk):	Hlavièkové súbory a kni¾nice pre vývoj s libcdaudio
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The libcdaudio-devel package provides the header files and libraries
needed for libcdaudio development.

%description devel -l fr
Le paquetage libcdaudio-devel fournit les ent^etes pour utiliser cette
bibliothèque.

%description devel -l it
Il pacchetto libcdaudio-devel contiene i file header e le librerie
necessarie lo sviluppo con libcdaudio.

%description devel -l pl
Biblioteki i pliki nag³ówkowe libcdaudio.

%description devel -l sk
Balík libcdaudio-devel poskytuje hlavièkové súbory a kni¾nice potrebné
pre vývoj s pou¾itím libcdaudio.

%package static
Summary:	libcdaudio static library
Summary(cs):	Statické knihovny pro vývoj s libcdaudio
Summary(fr):	Bibliothèques statiques de développement pour libcdaudio
Summary(it):	Librerie statiche per lo sviluppo con libcdaudio
Summary(pl):	Biblioteka statyczna libcdaudio
Summary(sk):	Statické kni¾nice pre vývoj s libcdaudio
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
The libcdaudio-static package provides static library needed for
libcdaudio development.

%description static -l it
Il pacchetto libcdaudio-static contiene le librerie statiche
necessarie lo sviluppo con libcdaudio.

%description static -l pl
Biblioteka statyczna libcdaudio.

%description static -l sk
Balík libcdaudio-static poskytuje statické kni¾nice potrebné pre vývoj
s pou¾itím libcdaudio.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libcdaudio-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_aclocaldir}/libcdaudio.m4

%if %{with static}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
