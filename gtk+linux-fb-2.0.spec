%define archname gtk+
%define major 0
%define libname %mklibname gtk-linux-fb-2.0_ %{major}

Summary: gtk+ linux-fb libraries
Name: gtk-linux-fb-2.0
Version: 2.4.14
Release: %mkrel 7
Source0: %{archname}-%{version}.tar.bz2
License: GPL
Group: System/Configuration/Theme
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires:	libglib2-devel libatk-devel libpango-devel
BuildRequires:	libtiff-devel libpng-devel
BuildRequires:	libgdk_pixbuf2.0-devel
Prefix: %{_prefix}

%description

gtk+ linux-fb libraries

%package -n %{libname}
Summary: gtk+ linux-fb library
Group: System/Libraries

%description -n %{libname}

gtk+ linux-fb library

%package -n %{libname}-devel
Summary:  Development library for gtk+-linux-fb-2.0
Group: 	  Development/C
Requires: %{libname} = %{version}
Provides: gtk-linux-fb-2.0-devel = %{version}-%{release} libgtk-linux-fb-2.0-devel = %{version}-%{release} gdk-linux-fb-2.0-devel = %{version}-%{release} libgdk-linux-fb-2.0-devel = %{version}-%{release}

%description -n %{libname}-devel

Development library for gtk+-linux-fb-2.0

%prep
%setup -q -n %{archname}-%{version}

%build
libtoolize --copy --force
%configure2_5x --with-gdktarget=linux-fb --enable-gtk-doc=no
%make

%install
rm -rf $RPM_BUILD_ROOT

# install shared libs only
make install-libLTLIBRARIES DESTDIR=$RPM_BUILD_ROOT -C gdk
make install-libLTLIBRARIES DESTDIR=$RPM_BUILD_ROOT -C gtk
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{libname}
%defattr(755,root,root)
%{_libdir}/libgtk-*.so.*
%{_libdir}/libgdk-*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/libgdk-*.so
%{_libdir}/libgtk-*.so

