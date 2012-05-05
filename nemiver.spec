Name: 	 	nemiver
Summary: 	Graphical debugger intended for GNOME
Version: 	0.9.2
Release: 	1
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/nemiver/%{name}-%{version}.tar.xz
URL:		http://projects.gnome.org/nemiver/
License:	GPLv2+
Group:		Development/Other
BuildRequires: pkgconfig(gdlmm-3.0) >= 3.0
BuildRequires: pkgconfig(giomm-2.4) >= 2.15.2
BuildRequires: pkgconfig(glibmm-2.4) >= 2.14
BuildRequires: pkgconfig(gmodule-2.0) >= 2.14
BuildRequires: pkgconfig(gsettings-desktop-schemas) >= 0.0.1
BuildRequires: pkgconfig(gthread-2.0) >= 2.14
BuildRequires: pkgconfig(gtk+-3.0) >= 2.22
BuildRequires: pkgconfig(gtkhex-3) >= 2.90
BuildRequires: pkgconfig(gtkmm-3.0) >= 3.0
BuildRequires: pkgconfig(libgtop-2.0) >= 2.14
BuildRequires: pkgconfig(libxml-2.0) >= 2.6.22
BuildRequires: pkgconfig(sqlite3) >= 3.0
BuildRequires: pkgconfig(vte-2.90) >= 0.28
BuildRequires: pkgconfig(gtksourceviewmm-3.0)
BuildRequires: intltool
BuildRequires: gdb
BuildRequires: gnome-doc-utils >= 0.3.2
BuildRequires: boost-devel
BuildRequires: dconf
Requires:	gdb
Obsoletes:	%{_lib}nemiver0
Obsoletes:	%{_lib}nemiver0-devel

%description
Nemiver is a graphical debugger that integrates well in the GNOME
desktop environment. It currently features a backend which uses the
well known GNU Debugger gdb to debug C / C++ programs.

%prep
%setup -q 

%build
%configure2_5x --enable-gsettings=yes --disable-scrollkeeper --disable-schemas-compile --disable-schemas-install --disable-static
%make

%install
%makeinstall_std

#remove unpackaged files
rm -rf %{buildroot}%{_includedir}/* %{buildroot}%{_libdir}/pkgconfig
find %{buildroot} -name *.la -delete

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS TODO* README
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/icons/hicolor/*/apps/nemiver*
%{_libdir}/%{name}
%{_mandir}/man1/*
%dir %{_datadir}/omf/nemiver
%{_datadir}/omf/nemiver/*-C.omf
%lang(sv) %{_datadir}/omf/nemiver/*-sv.omf
%lang(es) %{_datadir}/omf/nemiver/*-es.omf
%lang(oc) %{_datadir}/omf/nemiver/*-oc.omf
%lang(cs) %{_datadir}/omf/nemiver/*-cs.omf
%lang(de) %{_datadir}/omf/nemiver/*-de.omf
%lang(fr) %{_datadir}/omf/nemiver/*-fr.omf
%lang(gl) %{_datadir}/omf/nemiver/*-gl.omf
%lang(sl) %{_datadir}/omf/nemiver/*-sl.omf
%lang(zh_CN) %{_datadir}/omf/nemiver/*-zh_CN.omf

