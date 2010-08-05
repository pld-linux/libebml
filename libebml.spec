Summary:	Extensible Binary Meta Language access library
Summary(pl.UTF-8):	Biblioteka dostępu rozszerzalnego metajęzyka binarnego
Name:		libebml
Version:	0.7.8
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://dl.matroska.org/downloads/libebml/%{name}-%{version}.tar.bz2
# Source0-md5:	6278109f52e4f9d2c8a8dfc0d668b587
Patch0:		%{name}-makefile.patch
Patch1:		libtool-tag.patch
URL:		http://www.matroska.org/
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
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
%patch0 -p1
%patch1 -p1

%build
%{__make} -C make/linux \
	prefix=%{_prefix} \
	libdir=%{_libdir} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags}" \
	LD="%{__cxx}" \
	LDFLAGS="%{rpmldflags}"\
	DEBUGFLAGS="%{rpmcflags} %{?debug:-DDEBUG}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C make/linux install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	libdir=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libebml.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libebml.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libebml.so
%{_libdir}/libebml.la
%{_includedir}/ebml

%files static
%defattr(644,root,root,755)
%{_libdir}/libebml.a
