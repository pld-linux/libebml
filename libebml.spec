Summary:	Extensible Binary Meta Language access library
Summary(pl):	Biblioteka dostêpu rozszerzalnego metajêzyka binarnego
Name:		libebml
Version:	0.4.4
Release:	1
License:	GPL/QPL
Group:		Libraries
Source0:	http://matroska.free.fr/downloads/libebml/%{name}-%{version}.tar.bz2
# Source0-md5:	0b0cea70bbe04ecdbb3a0e2a603515b8
Patch0:		%{name}-makefile.patch
URL:		http://www.matroska.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Extensible Binary Meta Language access library
A library for reading and writing files with the Extensible Binary
Meta Language, a binary pendant to XML.
   
%description -l pl
Biblioteki rozszerzalnego metajêzyka binarnego umo¿liwiaj±ce czytanie
i zapisywanie plików w tym metajêzyku, dzia³aj±ca w oparciu o xml.

%package devel
Summary:	Developmment files and headers for Extensible Binary Meta Language.
Summary(pl):	Nag³ówki dla rozszerzalnego metajêzyka binarnego.
Group:		Development/Libraries
Requires:       %{name} >= %{version}

%description devel
Developmment files and headers for Extensible Binary Meta Language.

%description devel -l pl
Nag³ówki dla rozszerzalnego metajêzyka binarnego.

%package static
Summary:        Static libraries for Extensible Binary Meta Language.
Summary(pl):   	Biblioteki statyczne dla rozszerzalnego metajêzyka binarnego.
Group:          Libraries

%description static
Static libraries for Extensible Binary Meta Language.

%description static -l pl
Biblioteki statyczne dla rozszerzalnego metajêzyka binarnego.

%prep
%setup -q 
%patch0 -p1

%build
cd make/linux
%{__make} clean
%{__make} \
	prefix=%{_prefix} \
	CXX=%{__cxx} \
	LD=%{__cxx} \
	AR="%{__ar} rcvu"  \
	RANLIB=%{__ranlib} \
	INSTALL=%{__install} \
	%{?debug:DEBUG=yes} \
	INSTALL_OPTS="" \
	INSTALL_OPTS_LIB="" \
	INSTALL_DIR_OPTS="" \
	LDFLAGS="-shared"\
	CXXFLAGS="%{rpmcflags}"  \
	SRC_DIR=%{_builddir}/%{name}-%{version}/src/

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} -f make/linux/Makefile install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	CXX=%{__cxx} \
	LD=%{__cxx} \
	AR="%{__ar} rcvu"  \
	RANLIB=%{__ranlib} \
	INSTALL=%{__install} \
	%{?debug:DEBUG=yes} \
	INSTALL_OPTS="" \
	INSTALL_OPTS_LIB="" \
	INSTALL_DIR_OPTS="" \
	SRC_DIR=%{_builddir}/%{name}-%{version}/src/\
	LDFLAGS="-shared" \
        CXXFLAGS="%{rpmcflags}"

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files 
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libebml.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/ebml

%files static
%defattr(644,root,root,755)
%{_libdir}/libebml.a
