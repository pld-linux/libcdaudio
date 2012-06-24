%bcond_without	static	# don't build static library
Summary:	A library of functions for controlling audio CD-ROM players
Summary(fr):	Une biblioth�que pour le contr�le des lecteurs de CD-ROMS audio
Summary(it):	Una libreria di funzioni per controllare i lettori di CD-AUDIO
Summary(pl):	Biblioteka funkcji steruj�cych odtwarzaniem muzycznych p�yt CD
Summary(sk):	Kni�nica funkci� pre ovl�danie prehr�va�ov zvukov�ch CD-ROM
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
libcdaudio est une biblioth�que pour d�velopper des lecteurs de CDs.
Elle comprend le jeu de commandes de base pour contr�ler la lecture
des CDs ainsi que des fonctions d'acc�s � CDDB, � CD index et Cover
Art Index.

%description -l it
libcdaudio e' un librerie per lo sviluppo di lettori di CD audio che
include un set base di comandi per controllare le operazioni del
lettore CD-ROM cosi' come funzioni per accedere ai CDDB, i CD indice,
i cd di cover art.

%description -l pl
libcdaudio jest bibliotek� zapewniaj�c� funkcje kontroluj�ce dzia�anie
CD-ROMu podczas odtwarzania p�yt muzycznych. Wspiera r�wnie� zapytania
CDDB i CD Index.

%description -l sk
libcdaudio je kni�nica pre v�voj CD prehr�va�ov, obsahuj�ca z�kladn�
sadu pr�kazov pre ovl�danie CD-ROM jednotky, ako aj funkcie pre
pr�stup k CDDB, CD indexu a indexu obalov.

%package devel
Summary:	Header files and libraries for libcdaudio development
Summary(cs):	Knihovny a hlavi�kov� soubory pro v�voj s libcdaudio
Summary(fr):	Fichiers en-t�te et biblioth�ques de d�veloppement pour libcdaudio
Summary(it):	File header e librerie per lo sviluppo con libcdaudio
Summary(pl):	Biblioteki i pliki nag��wkowe libcdaudio
Summary(sk):	Hlavi�kov� s�bory a kni�nice pre v�voj s libcdaudio
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The libcdaudio-devel package provides the header files and libraries
needed for libcdaudio development.

%description devel -l fr
Le paquetage libcdaudio-devel fournit les ent^etes pour utiliser cette
biblioth�que.

%description devel -l it
Il pacchetto libcdaudio-devel contiene i file header e le librerie
necessarie lo sviluppo con libcdaudio.

%description devel -l pl
Biblioteki i pliki nag��wkowe libcdaudio.

%description devel -l sk
Bal�k libcdaudio-devel poskytuje hlavi�kov� s�bory a kni�nice potrebn�
pre v�voj s pou�it�m libcdaudio.

%package static
Summary:	libcdaudio static library
Summary(cs):	Statick� knihovny pro v�voj s libcdaudio
Summary(fr):	Biblioth�ques statiques de d�veloppement pour libcdaudio
Summary(it):	Librerie statiche per lo sviluppo con libcdaudio
Summary(pl):	Biblioteka statyczna libcdaudio
Summary(sk):	Statick� kni�nice pre v�voj s libcdaudio
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
Bal�k libcdaudio-static poskytuje statick� kni�nice potrebn� pre v�voj
s pou�it�m libcdaudio.

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
