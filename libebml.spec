Summary:	Extensible Binary Meta Language access library
Summary(pl):	Biblioteka dost�pu rozszerzalnego metaj�zyka binarnego
Name:		libebml
Version:	0.6.4
Release:	1
License:	GPL v2 or QPL
Group:		Libraries
Source0:	http://matroska.free.fr/downloads/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	7ac6fb3f4bcadcd845f0e9446ff446b7
Patch0:		%{name}-makefile.patch
URL:		http://www.matroska.org/
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Extensible Binary Meta Language access library is a library for
reading and writing files with the Extensible Binary Meta Language, a
binary pendant to XML.

%description -l pl
Biblioteka rozszerzalnego metaj�zyka binarnego (Extensible Binary Meta
Language, w skr�cie EBML) umo�liwia czytanie i zapisywanie plik�w w
tym metaj�zyku, b�d�cym binarnym uzupe�nieniem XML-a.

%package devel
Summary:	Header files for Extensible Binary Meta Language library
Summary(pl):	Nag��wki biblioteki rozszerzalnego metaj�zyka binarnego
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	libstdc++-devel

%description devel
Header files for Extensible Binary Meta Language library.

%description devel -l pl
Nag��wki biblioteki rozszerzalnego metaj�zyka binarnego.

%package static
Summary:	Static version of Extensible Binary Meta Language library
Summary(pl):	Statyczna wersja biblioteki rozszerzalnego metaj�zyka binarnego
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of Extensible Binary Meta Language library.

%description static -l pl
Statyczna wersja biblioteki rozszerzalnego metaj�zyka binarnego.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -C make/linux \
	prefix=%{_prefix} \
	libdir=%{_libdir} \
	CXX="%{__cxx}" \
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

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libebml.so
%{_libdir}/libebml.la
%{_includedir}/ebml

%files static
%defattr(644,root,root,755)
%{_libdir}/libebml.a