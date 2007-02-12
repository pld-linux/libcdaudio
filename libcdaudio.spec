# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	A library of functions for controlling audio CD-ROM players
Summary(fr.UTF-8):   Une bibliothèque pour le contrôle des lecteurs de CD-ROMS audio
Summary(it.UTF-8):   Una libreria di funzioni per controllare i lettori di CD-AUDIO
Summary(pl.UTF-8):   Biblioteka funkcji sterujących odtwarzaniem muzycznych płyt CD
Summary(sk.UTF-8):   Knižnica funkcií pre ovládanie prehrávačov zvukových CD-ROM
Name:		libcdaudio
Version:	0.99.12p2
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libcdaudio/%{name}-%{version}.tar.gz
# Source0-md5:	15de3830b751818a54a42899bd3ae72c
URL:		http://libcdaudio.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fomit-frame-pointer

%description
libcdaudio is a library designed to provide functions to control
operation of a CD-ROM when playing audio CDs. It also contains
functions for CDDB and CD Index lookup.

%description -l fr.UTF-8
libcdaudio est une bibliothèque pour développer des lecteurs de CDs.
Elle comprend le jeu de commandes de base pour contrôler la lecture
des CDs ainsi que des fonctions d'accès à CDDB, à CD index et Cover
Art Index.

%description -l it.UTF-8
libcdaudio e' un librerie per lo sviluppo di lettori di CD audio che
include un set base di comandi per controllare le operazioni del
lettore CD-ROM cosi' come funzioni per accedere ai CDDB, i CD indice,
i cd di cover art.

%description -l pl.UTF-8
libcdaudio jest biblioteką zapewniającą funkcje kontrolujące działanie
CD-ROMu podczas odtwarzania płyt muzycznych. Wspiera również zapytania
CDDB i CD Index.

%description -l sk.UTF-8
libcdaudio je knižnica pre vývoj CD prehrávačov, obsahujúca základnú
sadu príkazov pre ovládanie CD-ROM jednotky, ako aj funkcie pre
prístup k CDDB, CD indexu a indexu obalov.

%package devel
Summary:	Header files and libraries for libcdaudio development
Summary(cs.UTF-8):   Knihovny a hlavičkové soubory pro vývoj s libcdaudio
Summary(fr.UTF-8):   Fichiers en-tête et bibliothèques de développement pour libcdaudio
Summary(it.UTF-8):   File header e librerie per lo sviluppo con libcdaudio
Summary(pl.UTF-8):   Biblioteki i pliki nagłówkowe libcdaudio
Summary(sk.UTF-8):   Hlavičkové súbory a knižnice pre vývoj s libcdaudio
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The libcdaudio-devel package provides the header files and libraries
needed for libcdaudio development.

%description devel -l fr.UTF-8
Le paquetage libcdaudio-devel fournit les ent^etes pour utiliser cette
bibliothèque.

%description devel -l it.UTF-8
Il pacchetto libcdaudio-devel contiene i file header e le librerie
necessarie lo sviluppo con libcdaudio.

%description devel -l pl.UTF-8
Biblioteki i pliki nagłówkowe libcdaudio.

%description devel -l sk.UTF-8
Balík libcdaudio-devel poskytuje hlavičkové súbory a knižnice potrebné
pre vývoj s použitím libcdaudio.

%package static
Summary:	libcdaudio static library
Summary(cs.UTF-8):   Statické knihovny pro vývoj s libcdaudio
Summary(fr.UTF-8):   Bibliothèques statiques de développement pour libcdaudio
Summary(it.UTF-8):   Librerie statiche per lo sviluppo con libcdaudio
Summary(pl.UTF-8):   Biblioteka statyczna libcdaudio
Summary(sk.UTF-8):   Statické knižnice pre vývoj s libcdaudio
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
The libcdaudio-static package provides static library needed for
libcdaudio development.

%description static -l it.UTF-8
Il pacchetto libcdaudio-static contiene le librerie statiche
necessarie lo sviluppo con libcdaudio.

%description static -l pl.UTF-8
Biblioteka statyczna libcdaudio.

%description static -l sk.UTF-8
Balík libcdaudio-static poskytuje statické knižnice potrebné pre vývoj
s použitím libcdaudio.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
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
%{_pkgconfigdir}/*.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
