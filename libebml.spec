Summary:	Extensible Binary Meta Language access library
Summary(pl.UTF-8):	Biblioteka dostępu rozszerzalnego metajęzyka binarnego
Name:		libebml
Version:	1.3.3
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://dl.matroska.org/downloads/libebml/%{name}-%{version}.tar.bz2
# Source0-md5:	a8b270482620970d9891958618b54d77
URL:		http://www.matroska.org/
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Extensible Binary Meta Language access library is a library for
reading and writing files with the Extensible Binary Meta Language, a
binary pendant to XML.

%description -l pl.UTF-8
Biblioteka rozszerzalnego metajęzyka binarnego (Extensible Binary Meta
Language, w skrócie EBML) umożliwia czytanie i zapisywanie plików w
tym metajęzyku, będącym binarnym uzupełnieniem XML-a.

%package devel
Summary:	Header files for Extensible Binary Meta Language library
Summary(pl.UTF-8):	Nagłówki biblioteki rozszerzalnego metajęzyka binarnego
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for Extensible Binary Meta Language library.

%description devel -l pl.UTF-8
Nagłówki biblioteki rozszerzalnego metajęzyka binarnego.

%package static
Summary:	Static version of Extensible Binary Meta Language library
Summary(pl.UTF-8):	Statyczna wersja biblioteki rozszerzalnego metajęzyka binarnego
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of Extensible Binary Meta Language library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki rozszerzalnego metajęzyka binarnego.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libebml.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libebml.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libebml.so
%{_libdir}/libebml.la
%{_includedir}/ebml
%{_pkgconfigdir}/libebml.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libebml.a
