Summary:	X Miscellaneous Utilities library
Name:		xorg-libXmu
Version:	1.1.2
Release:	3
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXmu-%{version}.tar.bz2
# Source0-md5:	41d92ab627dfa06568076043f3e089e4
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-libXt-devel
BuildRequires:	xorg-xtrans-devel
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Miscellaneous Utilities library.

%package devel
Summary:	Header files for libXmu and libXmuu libraries
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
X Miscellaneous Utilities library.

This package contains the header files needed to develop programs that
use libXmu or libXmuu.

%prep
%setup -qn libXmu-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %ghost %{_libdir}/libXmu.so.?
%attr(755,root,root) %ghost %{_libdir}/libXmuu.so.?
%attr(755,root,root) %{_libdir}/libXmu.so.*.*.*
%attr(755,root,root) %{_libdir}/libXmuu.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXmu.so
%attr(755,root,root) %{_libdir}/libXmuu.so
%dir %{_includedir}/X11/Xmu
%{_includedir}/X11/Xmu/*.h
%{_pkgconfigdir}/xm*.pc

