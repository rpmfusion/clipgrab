Name:           clipgrab
Version:        3.9.6
Release:        1%{?dist}

License:        GPLv3 and Non-Commercial Use Only (Artwork and Trademark)
Summary:        A free video downloader and converter
URL:            http://clipgrab.de/en
Source0:        https://download.clipgrab.org/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop

ExcludeArch:    ppc64le ppc64

BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5WebEngineWidgets)
BuildRequires:  pkgconfig(Qt5Xml)
# Work around https://bugzilla.redhat.com/show_bug.cgi?id=1909195
BuildRequires: nss nspr

Requires:       hicolor-icon-theme
Requires:       ffmpeg

%description
ClipGrab is a free downloader and converter for YouTube, Vimeo, Dailymotion
and many other online video sites.

%prep
#setup -q
%autosetup -p 1 -n %{name}-%{version}
chmod 0644 *.cpp *.h icon.png COPYING README license.odt
# Fix build with Qt 5.12: https://aur.archlinux.org/packages/clipgrab-qt5/
sed -i 's|QtWebKit/QWebView|QtWebKitWidgets/QWebView|' mainwindow.ui

%build
%{qmake_qt5} clipgrab.pro QMAKE_CXXFLAGS="%{optflags}"
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
* Thu Dec 17 2020 Martin Gansser <martinkg@fedoraproject.org> - 3.9.6-1
- Update to 3.9.6
- BR nss nspr

* Sat Nov 28 2020 Martin Gansser <martinkg@fedoraproject.org> - 3.9.5-1
- Update to 3.9.5

* Tue Nov 24 2020 Martin Gansser <martinkg@fedoraproject.org> - 3.9.4-1
- Update to 3.9.4

* Fri Nov 20 2020 Martin Gansser <martinkg@fedoraproject.org> - 3.9.2-1
- Update to 3.9.2

* Thu Oct 29 2020 Martin Gansser <martinkg@fedoraproject.org> - 3.8.15-1
- Update to 3.8.15

* Sun Aug 30 2020 Martin Gansser <martinkg@fedoraproject.org> - 3.8.14-1
- Update to 3.8.14

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.8.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 12 2020 Martin Gansser <martinkg@fedoraproject.org> - 3.8.13-1
- Update to 3.8.13

* Wed Jun 03 2020 Martin Gansser <martinkg@fedoraproject.org> - 3.8.12-1
- Update to 3.8.12

* Wed Mar 18 2020 Martin Gansser <martinkg@fedoraproject.org> - 3.8.11-1
- Update to 3.8.11

* Sun Jan 26 2020 Sérgio Basto <sergio@serjux.com> - 3.8.10-2
- Add aarch64 arch

* Sun Jan 26 2020 Sérgio Basto <sergio@serjux.com> - 3.8.10-1
- Update to 3.8.10

* Sun Jan 26 2020 Sérgio Basto <sergio@serjux.com> - 3.8.9-2
- Update to 3.8.10

* Sat Jan 04 2020 Martin Gansser <martinkg@fedoraproject.org> - 3.8.9-1
- Update to 3.8.9

* Wed Jan 01 2020 Martin Gansser <martinkg@fedoraproject.org> - 3.8.8-1
- Update to 3.8.8

* Tue Nov 26 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.8.7-1
- Update to 3.8.7

* Wed Sep 18 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.8.5-1
- Update to 3.8.5

* Mon Aug 26 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.8.4-1
- Update to 3.8.4
- Drop clipgrab-qt5-3.7.2.patch

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 13 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.8.3-1
- Update to 3.8.3

* Mon Mar 11 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.8.2-1
- Update to 3.8.2

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Feb 24 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.8.1-1
- Update to 3.8.1

* Thu Jan 24 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.8.0-1
- Update to 3.8.0
- Use %%{qmake_qt5}

* Mon Nov 19 2018 Martin Gansser <martinkg@fedoraproject.org> - 3.7.1-2
- Update to 3.7.2

* Fri Oct 05 2018 Martin Gansser <martinkg@fedoraproject.org> - 3.7.1-1
- Update to 3.7.1

* Fri Sep 28 2018 Martin Gansser <martinkg@fedoraproject.org> - 3.7.0-1
- Update to 3.7.0

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
