#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	Extensible Binary Meta Language access library
Summary(pl.UTF-8):	Biblioteka dostępu rozszerzalnego metajęzyka binarnego
Name:		libebml
Version:	1.3.10
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://dl.matroska.org/downloads/libebml/%{name}-%{version}.tar.xz
# Source0-md5:	71edd78f05a7136c9bbed89f010bbef0
URL:		https://www.matroska.org/
BuildRequires:	cmake >= 3.1.2
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	xz
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
# .pc file generation expects relative CMAKE_INSTALL_{INCLUDE,LIB}DIR
%if %{with static_libs}
install -d build-static
cd build-static
%cmake .. \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-DCMAKE_INSTALL_INCLUDEDIR=include \
	-DCMAKE_INSTALL_LIBDIR=%{_lib}

%{__make}
cd ..
%endif

install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_INCLUDEDIR=include \
	-DCMAKE_INSTALL_LIBDIR=%{_lib}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%if %{with static_libs}
%{__make} -C build-static install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README.md
%attr(755,root,root) %{_libdir}/libebml.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libebml.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libebml.so
%{_includedir}/ebml
%{_pkgconfigdir}/libebml.pc
%{_libdir}/cmake/EBML

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libebml.a
%endif
