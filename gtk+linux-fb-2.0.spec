%define archname gtk+
%define major 0
%define libname %mklibname gtk-linux-fb-2.0_ %{major}

Summary:	gtk+ linux-fb libraries
Name:		gtk-linux-fb-2.0
Version:	2.4.14
Release:	%mkrel 9
License:	GPL
Group:		System/Configuration/Other
Source0:	%{archname}-%{version}.tar.bz2
Patch0:		gtk+-2.4.14-no_DISABLE_DEPRECATED_fix.diff
Patch1:		gtk+-2.4.14-linkage_fix.diff
Patch2:		gtk+-2.4.14-g_hash_table_get_keys_fix.diff
BuildRequires:	automake1.7
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	libglib2-devel libatk-devel libpango-devel
BuildRequires:	libtiff-devel libpng-devel
BuildRequires:	libtool gtk-doc
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%patch0 -p1 -b .no_DISABLE_DEPRECATED_fix
%patch1 -p0 -b .linkage_fix
%patch2 -p1 -b .g_hash_table_get_keys_fix

#needed by all patches
autoreconf

%build
%configure2_5x --with-gdktarget=linux-fb --enable-gtk-doc=no

%make

%install
rm -rf %{buildroot}

# install shared libs only
make install-libLTLIBRARIES DESTDIR=%{buildroot} -C gdk
make install-libLTLIBRARIES DESTDIR=%{buildroot} -C gtk
rm -f %{buildroot}%{_libdir}/*.la

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
 
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(755,root,root)
%{_libdir}/libgtk-*.so.*
%{_libdir}/libgdk-*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/libgdk-*.so
%{_libdir}/libgtk-*.so
