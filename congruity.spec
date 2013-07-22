Summary:	Logitech Harmony remote programmer GUI
Name:		congruity
Version:	16
Release:	1
License:	GPLv3+
URL:		http://congruity.sourceforge.net/
Source:		https://sourceforge.net/projects/congruity/files/congruity/16/%{name}-%{version}.tar.bz2
Group:		System/Configuration/Hardware
Requires:	python-libconcord
Requires:	wxPythonGTK
BuildArch:	noarch

%description
This software allows you to program your Logitech Harmony universal
remote.

%prep
%setup -q

%install
%makeinstall_std RUN_UPDATE_DESKTOP_DB=0 PREFIX=%{_prefix}

install -d -m755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-harmony-www.desktop <<EOF
[Desktop Entry]
Name=Logitech Harmony configuration
Comment=Configure a Harmony remote
Exec=www-browser http://members.harmonyremote.com/
Type=Application
Icon=web_browser_section
Categories=Utility;Electronics;
StartupNotify=false
EOF

%files
%doc Changelog README.txt LICENSE.txt
%{_bindir}/congruity
%{_bindir}/mhgui
%{_datadir}/congruity
%{_datadir}/applications/congruity.desktop
%{_datadir}/applications/mandriva-harmony-www.desktop
%{_mandir}/man1/congruity*


%changelog
* Sat Sep 04 2010 Anssi Hannula <anssi@mandriva.org> 15-1mdv2011.0
+ Revision: 575837
- new version
- update license tag
- disable non-working startup notification for the WWW configurator
  menu entry

* Fri Dec 25 2009 Ahmad Samir <ahmadsamir@mandriva.org> 14-1mdv2010.1
+ Revision: 482192
- Add missing Requires (bug #56650)
- Update to new version 14

* Thu Oct 01 2009 Anssi Hannula <anssi@mandriva.org> 13-1mdv2010.0
+ Revision: 452156
- new version
- drop desktop.patch, applied upstream

* Sun Jul 12 2009 Anssi Hannula <anssi@mandriva.org> 12-1mdv2010.0
+ Revision: 395312
- new version
- use included desktop file with changes (desktop.patch)

* Sun Nov 02 2008 Anssi Hannula <anssi@mandriva.org> 9-1mdv2009.1
+ Revision: 299208
- initial Mandriva release


