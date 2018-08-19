Name:           clipgrab
Version:        3.6.8
Release:        3%{?dist}

License:        GPLv3 and Non-Commercial Use Only (Artwork and Trademark)
Group:          Applications/Internet
Summary:        A free video downloader and converter
URL:            http://clipgrab.de/en
Source0:        https://download.clipgrab.org/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop

BuildRequires:  qt-devel
BuildRequires:  qt-webkit-devel
BuildRequires:  desktop-file-utils
Requires:       ffmpeg

%description
ClipGrab is a free downloader and converter for YouTube, Vimeo, Dailymotion
and many other online video sites.

%prep
%setup -q
chmod 0644 *.cpp *.h icon.png COPYING README license.odt

%build
%{qmake_qt4} %{name}.pro
%make_build 

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_datadir}/applications
install -Dm 644 icon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

%files
%license COPYING
%doc README
%{_bindir}/%{name}
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/clipgrab.desktop

%changelog
* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.6.8-3
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 3.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 23 2018 Martin Gansser <martinkg@fedoraproject.org> - 3.6.8-1
- Update to 3.6.8
- Remove scriptlets

* Wed Feb 14 2018 Sérgio Basto <sergio@serjux.com> - 3.6.7-1
- Update to 3.6.7

* Sat Oct 14 2017 Sérgio Basto <sergio@serjux.com> - 3.6.6-1
- Update clipgrab to 3.6.6

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 3.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat May 13 2017 Martin Gansser <martinkg@fedoraproject.org> - 3.6.5-1
- Update to 3.6.5

* Sun Mar 26 2017 Martin Gansser <martinkg@fedoraproject.org> - 3.6.4-1
- Update to 3.6.4

* Sat Mar 25 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 3.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Martin Gansser <martinkg@fedoraproject.org> - 3.6.3-1
- Update to 3.6.3

* Fri Dec 09 2016 Martin Gansser <martinkg@fedoraproject.org> - 3.6.2-1
- Update to 3.6.2

* Wed Aug 17 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.6.1-2
- Use fedora build flags so package complies with packaging guidelines

* Fri Jul 01 2016 Martin Gansser <martinkg@fedoraproject.org> - 3.6.1-1
- Update to 3.6.1

* Thu Dec 24 2015 Martin Gansser <martinkg@fedoraproject.org> - 3.5.6-1
- Update to 3.5.6

* Tue Dec 01 2015 Martin Gansser <martinkg@fedoraproject.org> - 3.5.5-1
- Update to 3.5.5

* Fri Aug 07 2015 Martin Gansser <martinkg@fedoraproject.org> - 3.5.1-1
- Update to 3.5.1

* Fri May 22 2015 Martin Gansser <martinkg@fedoraproject.org> - 3.4.11-1
- Update to 3.4.11

* Tue Feb 03 2015 Martin Gansser <martinkg@fedoraproject.org> - 3.4.9-1
- Update to 3.4.9
- Mark license files as %%license where available

* Sun Dec 07 2014 Martin Gansser <martinkg@fedoraproject.org> - 3.4.8-3
- correct license field

* Sat Dec 06 2014 Martin Gansser <martinkg@fedoraproject.org> - 3.4.8-2
- added  parallel make %%{?_smp_mflags} macro
- correct icon path in desktop file

* Sat Dec 06 2014 Martin Gansser <martinkg@fedoraproject.org> - 3.4.8-1
- rebuild for new version
