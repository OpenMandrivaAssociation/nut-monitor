Summary:	NUT (Network UPS Tools) GUI Client
Name:		nut-monitor
Version:	1.1
Release:	3
Group:		Monitoring
License:	GPLv3+
URL:		http://www.lestat.st/informatique/projets/nut-monitor-en
Source0:	http://www.lestat.st/_media/informatique/projets/nut-monitor/%{name}-%{version}.tar.gz
Requires:	pygtk2.0
Requires:	pygtk2.0-libglade
Requires:	python
Requires:	python-pynut
BuildRequires:	imagemagick
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
NUT-Monitor is a graphical application to monitor and manage UPSes connected to
a NUT server. This application is written in Python and PyGTK and uses the
PyNUT class.

%prep

%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/%{name}
install -d %{buildroot}%{_bindir}

install -m0755 NUT-Monitor %{buildroot}%{_bindir}/%{name}
install -m0644 gui.glade %{buildroot}%{_datadir}/%{name}/

# install icons
install -d %{buildroot}%{_miconsdir}
install -d %{buildroot}%{_iconsdir}
install -d %{buildroot}%{_liconsdir}

convert -scale 16x16 %{name}.png %{buildroot}%{_miconsdir}/%{name}.png
convert -scale 32x32 %{name}.png %{buildroot}%{_iconsdir}/%{name}.png
install -m0644 %{name}.png %{buildroot}%{_liconsdir}/%{name}.png

# menu
install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=NUT Monitor
Comment=Network UPS Tools GUI client
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=GTK;Settings;System;X-MandrivaLinux-CrossDesktop;
EOF

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README copyright
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png


%changelog
* Mon Sep 14 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.1-2mdv2010.0
+ Revision: 440354
- rebuild

* Wed Mar 11 2009 Oden Eriksson <oeriksson@mandriva.com> 1.1-1mdv2009.1
+ Revision: 353748
- 1.1

* Tue Sep 30 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdv2009.1
+ Revision: 290080
- import nut-monitor


* Tue Sep 30 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdv2009.0
- initial Mandriva package
