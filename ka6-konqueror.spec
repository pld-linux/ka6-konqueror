#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.08.1
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		konqueror
Summary:	konqueror
Name:		ka6-%{kaname}
Version:	24.08.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	9b062ba13ffccd71e5f1d38b067aa4a1
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel
BuildRequires:	Qt6Gui-devel >= 5.11.1
BuildRequires:	Qt6Network-devel >= 5.11.1
BuildRequires:	Qt6Positioning-devel >= 5.11.1
BuildRequires:	Qt6PrintSupport-devel >= 5.11.1
BuildRequires:	Qt6Qml-devel >= 5.11.1
BuildRequires:	Qt6Quick-devel >= 5.11.1
BuildRequires:	Qt6Test-devel
BuildRequires:	Qt6WebChannel-devel >= 5.11.1
BuildRequires:	Qt6WebEngine-devel >= 5.11.1
BuildRequires:	Qt6Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-karchive-devel >= %{kframever}
BuildRequires:	kf6-kbookmarks-devel >= %{kframever}
BuildRequires:	kf6-kcmutils-devel >= %{kframever}
BuildRequires:	kf6-kcrash-devel >= %{kframever}
BuildRequires:	kf6-kparts-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	tidy-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	%{name}-data = %{version}-%{release}
Obsoletes:	ka5-%{kaname} < %{version}
ExcludeArch:	x32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Konqueror is KDE's Webbrowser and swiss-army-knife for any kind of
file-management and file previewing.. Features. Webbrowsing using
KHTML or KDEWebKit as rendering engines; File management using most of
Dolphin's features (including version-control, service menus and the
basic UI)

%description -l pl.UTF-8
Konqueror jest przeglądarką www KDE i szwajcarskim scyzorykiem do
każdego rodzaju zarządzania plikami i ich podglądem. Cechy:
przeglądanie www przy użyciu KHTML lub KDEWebKit jako silników
renderowania; zarządzanie plikami używając większości możliwości
Dolphina (łącznie z kontrolą wersji, menu i podstawowym UI).

%package data
Summary:	Data files for %{kaname}
Summary(pl.UTF-8):	Dane dla %{kaname}
Group:		X11/Applications
Obsoletes:	ka5-%{kaname}-data < %{version}
BuildArch:	noarch

%description data
Data files for %{kaname}.

%description data -l pl.UTF-8
Dane dla %{kaname}.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	ka5-%{kaname}-devel < %{version}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DQT_MAJOR_VERSION=6
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/{el,ko,sr,zh_CN}
%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
/etc/xdg/autostart/konqy_preload.desktop
/etc/xdg/konqsidebartngrc
/etc/xdg/translaterc
/etc/xdg/useragenttemplatesrc
%attr(755,root,root) %{_bindir}/fsview
%attr(755,root,root) %{_bindir}/kcreatewebarchive
%attr(755,root,root) %{_bindir}/kfmclient
%attr(755,root,root) %{_bindir}/konqueror
%attr(755,root,root) %{_libdir}/libKF6Konq.so.*.*
%{_libdir}/libKF6Konq.so.7
%attr(755,root,root) %{_libdir}/libkonqsidebarplugin.so.*.*
%{_libdir}/libkonqsidebarplugin.so.6
%attr(755,root,root) %{_libdir}/libkonquerorprivate.so.*.*
%{_libdir}/libkonquerorprivate.so.5
%attr(755,root,root) %{_libdir}/qt6/plugins/akregatorkonqfeedicon.so
%attr(755,root,root) %{_libdir}/qt6/plugins/autorefresh.so
%attr(755,root,root) %{_libdir}/qt6/plugins/babelfishplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/dolphinpart/kpartplugins/dirfilterplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/dolphinpart/kpartplugins/kimgallery.so
%attr(755,root,root) %{_libdir}/qt6/plugins/dolphinpart/kpartplugins/konq_shellcmdplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kfileitemaction/akregatorplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kio/bookmarks.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/parts/fsviewpart.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/parts/konq_sidebar.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/parts/webenginepart.so
%attr(755,root,root) %{_libdir}/qt6/plugins/khtml/kpartplugins/akregatorkonqfeediconkhtml_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt6/plugins/khtml/kpartplugins/autorefreshkhtml_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt6/plugins/khtml/kpartplugins/babelfishpluginkhtml_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt6/plugins/khtml/kpartplugins/khtmlsettingspluginkhtml_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt6/plugins/khtml/kpartplugins/konqueror_kget_browser_integrationkhtml_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt6/plugins/khtml/kpartplugins/uachangerpluginkhtml_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt6/plugins/khtml/kpartplugins/webarchiverpluginkhtml_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt6/plugins/khtmlsettingsplugin.so
%dir %{_libdir}/qt6/plugins/konqueror
%dir %{_libdir}/qt6/plugins/konqueror/kpartplugins
%dir %{_libdir}/qt6/plugins/konqueror/sidebar
%attr(755,root,root) %{_libdir}/qt6/plugins/konqueror/kpartplugins/searchbarplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/konqueror/sidebar/konqsidebar_bookmarks.so
%attr(755,root,root) %{_libdir}/qt6/plugins/konqueror/sidebar/konqsidebar_history.so
%attr(755,root,root) %{_libdir}/qt6/plugins/konqueror/sidebar/konqsidebar_places.so
%attr(755,root,root) %{_libdir}/qt6/plugins/konqueror/sidebar/konqsidebar_tree.so
%dir %{_libdir}/qt6/plugins/konqueror_kcms
%attr(755,root,root) %{_libdir}/qt6/plugins/konqueror_kcms/kcm_bookmarks.so
%attr(755,root,root) %{_libdir}/qt6/plugins/konqueror_kcms/kcm_history.so
%attr(755,root,root) %{_libdir}/qt6/plugins/konqueror_kcms/kcm_konq.so
%attr(755,root,root) %{_libdir}/qt6/plugins/konqueror_kcms/kcm_performance.so
%attr(755,root,root) %{_libdir}/qt6/plugins/konqueror_kcms/khtml_appearance.so
%attr(755,root,root) %{_libdir}/qt6/plugins/konqueror_kcms/khtml_behavior.so
%attr(755,root,root) %{_libdir}/qt6/plugins/konqueror_kcms/khtml_cache.so
%attr(755,root,root) %{_libdir}/qt6/plugins/konqueror_kcms/khtml_cookies.so
%attr(755,root,root) %{_libdir}/qt6/plugins/konqueror_kcms/khtml_filter.so
%attr(755,root,root) %{_libdir}/qt6/plugins/konqueror_kcms/khtml_general.so
%attr(755,root,root) %{_libdir}/qt6/plugins/konqueror_kcms/khtml_java_js.so
%attr(755,root,root) %{_libdir}/qt6/plugins/konqueror_kcms/khtml_tabs.so
%attr(755,root,root) %{_libdir}/qt6/plugins/konqueror_kcms/khtml_useragent.so
%attr(755,root,root) %{_libdir}/qt6/plugins/konqueror_kget_browser_integration.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kwebkitpart/kpartplugins/akregatorkonqfeediconkwebkitpart_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kwebkitpart/kpartplugins/autorefreshkwebkitpart_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kwebkitpart/kpartplugins/babelfishpluginkwebkitpart_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kwebkitpart/kpartplugins/khtmlsettingspluginkwebkitpart_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kwebkitpart/kpartplugins/konqueror_kget_browser_integrationkwebkitpart_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kwebkitpart/kpartplugins/uachangerpluginkwebkitpart_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kwebkitpart/kpartplugins/webarchiverpluginkwebkitpart_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt6/plugins/uachangerplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/webarchiverplugin.so
%attr(755,root,root) %{_libdir}/qt6/plugins/webenginepart/kpartplugins/akregatorkonqfeediconwebenginepart_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt6/plugins/webenginepart/kpartplugins/autorefreshwebenginepart_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt6/plugins/webenginepart/kpartplugins/babelfishpluginwebenginepart_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt6/plugins/webenginepart/kpartplugins/khtmlsettingspluginwebenginepart_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt6/plugins/webenginepart/kpartplugins/konqueror_kget_browser_integrationwebenginepart_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt6/plugins/webenginepart/kpartplugins/uachangerpluginwebenginepart_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt6/plugins/webenginepart/kpartplugins/webarchiverpluginwebenginepart_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/thumbcreator/webarchivethumbnail.so
%attr(755,root,root) %{_libdir}/libKF6KonqSettings.so.*.*
%ghost %{_libdir}/libKF6KonqSettings.so.?

%files data -f %{kaname}.lang
%defattr(644,root,root,755)
%{_datadir}/akregator/pics/feed.png
%{_desktopdir}/bookmarks.desktop
%{_desktopdir}/kcm_bookmarks.desktop
%{_desktopdir}/kfmclient.desktop
%{_desktopdir}/kfmclient_dir.desktop
%{_desktopdir}/kfmclient_html.desktop
%{_desktopdir}/kfmclient_war.desktop
%{_desktopdir}/konqbrowser.desktop
%{_desktopdir}/org.kde.konqueror.desktop
%{_datadir}/config.kcfg/kcreatewebarchive.kcfg
%{_datadir}/config.kcfg/konqueror.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.Konqueror.Main.xml
%{_datadir}/dbus-1/interfaces/org.kde.Konqueror.MainWindow.xml
%{_iconsdir}/hicolor/*x*/apps/*.png
%{_iconsdir}/hicolor/*x*/actions/*.png
%{_datadir}/kcmcss/template.css
%{_datadir}/kconf_update/webenginepart.upd
%{_datadir}/kcontrol/pics/onlyone.png
%{_datadir}/kcontrol/pics/overlapping.png
%{_datadir}/kf6/kbookmark/directory_bookmarkbar.desktop
%{_datadir}/kio_bookmarks/kio_bookmarks.css
%{_datadir}/konqsidebartng
%{_datadir}/konqueror
%{_datadir}/metainfo/org.kde.konqueror.appdata.xml
%{_datadir}/qlogging-categories6/akregatorplugin.categories
%{_datadir}/qlogging-categories6/fsview.categories
%{_datadir}/qlogging-categories6/konqueror.categories
%{_datadir}/webenginepart/error.html

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF6/konq_events.h
%{_includedir}/KF6/konq_historyentry.h
%{_includedir}/KF6/konq_historyprovider.h
%{_includedir}/KF6/konq_kpart_plugin.h
%{_includedir}/KF6/konq_popupmenu.h
%{_includedir}/KF6/konq_version.h
%{_includedir}/KF6/konqsidebarplugin.h
%{_includedir}/KF6/libkonq_export.h
%{_includedir}/KF6/konqsettings.h
%{_includedir}/KF6/konqsettings_version.h
%{_includedir}/KF6/libkonqsettings_export.h
%{_includedir}/KF6/selectorinterface.h
%{_libdir}/cmake/KF6Konq
%{_libdir}/libKF6Konq.so
%{_libdir}/libkonqsidebarplugin.so
%{_libdir}/libkwebenginepart.so
%{_libdir}/libKF6KonqSettings.so
